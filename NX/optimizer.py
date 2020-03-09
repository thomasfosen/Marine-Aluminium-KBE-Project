import NXOpen
import NXOpen.CAE
import NXOpen.Fields

import random
import time

from Generator import Generator

class Optimizer():

    def __init__(self, filename, filepath):
        self.filename = filename # To allow several sessions to run smoothly without collisions between "files"
        self.filepath = filepath
        # Bodies to analyze - to be updated via getSolidBodies method.
        self.bodies = []

        self.dfa_manager = Generator()
        self.dfa_template_location = 'C:/Users/tuanat/Meta/Marine-Aluminium-KBE-Project/NX/'

        # the amount of time to wait before extracting results
        # there might be a better way to do this, if NX can notify when the simulation is finished
        # current it seems like this is a parallell process running in NX
        self.simulation_wait_time = 4

        #setting default diameter
        self.default_node_diameter = 400

    def go_to_prepost(self):
        theSession = NXOpen.Session.GetSession()
        theSession.ApplicationSwitchImmediate("UG_APP_SFEM")

    def go_to_modeling(self):
        theSession = NXOpen.Session.GetSession()
        theSession.ApplicationSwitchImmediate("UG_APP_MODELING")

    # requires modelling environment in part
    def refresh_KF_rule(self):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.BaseWork
        workPart.RuleManager.Reload(True)
        workPart.RuleManager.RegenerateAll()

    def print(self, message):
        theNxMessageBox = NXOpen.UI.GetUI().NXMessageBox
        theNxMessageBox.Show("Print message",NXOpen.NXMessageBoxDialogType.Information, str(message))

    def go_to_prt(self):
        theSession  = NXOpen.Session.GetSession()
        workFemPart = theSession.Parts.BaseWork
        displayFemPart = theSession.Parts.BaseDisplay
        part1 = theSession.Parts.FindObject(self.filename)
        status1, partLoadStatus1 = theSession.Parts.SetDisplay(part1, False, False)

        workFemPart = NXOpen.BasePart.Null
        workPart = theSession.Parts.Work
        displayFemPart = NXOpen.BasePart.Null
        displayPart = theSession.Parts.Display
        theSession.Parts.SetWork(workPart)

    def go_to_fem(self):
        theSession  = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work
        displayPart = theSession.Parts.Display

        femPart1 = theSession.Parts.FindObject(self.filename + "_fem1")
        status1, partLoadStatus1 = theSession.Parts.SetDisplay(femPart1, False, False)

        workPart = NXOpen.Part.Null
        workFemPart = theSession.Parts.BaseWork
        displayPart = NXOpen.Part.Null
        displayFemPart = theSession.Parts.BaseDisplay
        femPart2 = workFemPart
        theSession.Parts.SetWork(femPart2)

    def update_fem_geometry(self):
        theSession  = NXOpen.Session.GetSession()
        workFemPart = theSession.Parts.BaseWork

        fEModel1 = workFemPart.FindObject("FEModel")
        fEModel1.UpdateFemodel()

    def go_to_sim(self):
        theSession  = NXOpen.Session.GetSession()
        workFemPart = theSession.Parts.BaseWork
        displayFemPart = theSession.Parts.BaseDisplay

        simPart1 = theSession.Parts.FindObject(self.filename + "_fem1_sim1")
        status1, partLoadStatus1 = theSession.Parts.SetActiveDisplay(simPart1, NXOpen.DisplayPartOption.AllowAdditional, NXOpen.PartDisplayPartWorkPartOption.SameAsDisplay)

        workSimPart = theSession.Parts.BaseWork
        displaySimPart = theSession.Parts.BaseDisplay
        partLoadStatus1.Dispose()

    def solve(self):
        theSession  = NXOpen.Session.GetSession()
        workSimPart = theSession.Parts.BaseWork
        displaySimPart = theSession.Parts.BaseDisplay

        theSimSolveManager = NXOpen.CAE.SimSolveManager.GetSimSolveManager(theSession)

        simSimulation1 = workSimPart.FindObject("Simulation")
        simSolution1 = simSimulation1.FindObject("Solution[Solution 1]")
        psolutions1 = [NXOpen.CAE.SimSolution.Null] * 1
        psolutions1[0] = simSolution1
        numsolutionssolved1, numsolutionsfailed1, numsolutionsskipped1 = theSimSolveManager.SolveChainOfSolutions(psolutions1, NXOpen.CAE.SimSolution.SolveOption.Solve, NXOpen.CAE.SimSolution.SetupCheckOption.CompleteCheckAndOutputErrors, NXOpen.CAE.SimSolution.SolveMode.Background)

    def get_result(self, name="max_von_mises"):
        theSession  = NXOpen.Session.GetSession()
        workSimPart = theSession.Parts.BaseWork

        simSimulation1 = workSimPart.FindObject("Simulation")
        objects1 = [NXOpen.CAE.ResultMeasure.Null] * 1
        resultMeasure1 = simSimulation1.ResultMeasures.Find("NXOpen.CAE.ResultMeasure[" + str(name) + "]")
        objects1[0] = resultMeasure1

        simSimulation1.ResultMeasures.UpdateMeasures(objects1)

        # return results (KPa to MPa)
        return resultMeasure1.Result/1000

    # currently node specific code
    def perform_loop_iteration(self, change_in_diameter):
        self.dfa_manager.dfa_template_location = self.dfa_template_location
        current_node_diameter = self.dfa_manager.get_node_diameter()

        # go to part in order to access update geometry functions
        self.go_to_prt()
        # update dfa file geometry
        self.dfa_manager.change_node_diameter(current_node_diameter + change_in_diameter)
        # udate geometry by reloading and regenerating knowledge fusion rules (dfa file)
        optimizer.refresh_KF_rule()

        # go to fem modelling to update fem geometry(mesh)
        self.go_to_fem()
        # update mesh geometry
        self.update_fem_geometry()

        # go to sim environment to run simulation
        self.go_to_sim()
        # initiate solve
        optimizer.solve()

        # extract results
        time.sleep(self.simulation_wait_time)
        result = self.get_result()

        return result

    def optimize(self, target_stress):

        # here we could implement fancy algorithms to speed up the process
        # an example would be to increase the value of change_of_diameter depending on the difference in value
        # between result and target

        # INITIAL STEPS: set force & set torque. Maybe reset geometry
        self.dfa_manager.dfa_template_location = self.dfa_template_location
        self.dfa_manager.change_node_diameter(self.default_node_diameter)

        # optimization loop
        # going from low stress (bigger diameter => bigger surface per force => low stress) to the limit. it's possible to do it from either direction
        # and with a decreasing change in diameter to get a more accurate result
        stress_result = 0
        optimize = True
        # how much the diameter will change in each iteration
        change_in_diameter = -10

        self.print(1)

        while optimize == True:
            self.print(5)
            # performs a single full iteration of updatating geometry, simulating and retrieving results
            result = self.perform_loop_iteration(change_in_diameter)
            self.print(2)

            # to detect when to stop the iteration. when target has been surpassed
            if result > target_stress:
                optimize = False
                self.print(3)

                # saving the last diameter. although, we should be getting the previous diameter
                # one solution is to store all the results in an array => easily get the previous result
                final_diameter = current_node_diameter = self.dfa_manager.get_node_diameter()

                #just a simple print for the user. This should be replaced with a message to the web server
                self.print('Optimization has finished. Final stress:' + str(result) + '\n final diameter:' + str(final_diameter))

    # These are very part specific
    def update_force(self, force, name='Force(1)'):
        theSession  = NXOpen.Session.GetSession()
        workSimPart = theSession.Parts.BaseWork

        simSimulation1 = workSimPart.Simulation

        simLoad1 = simSimulation1.Loads.FindObject("Load[Force(1)]")
        simBCBuilder1 = simSimulation1.CreateBcBuilderForBc(simLoad1)

        propertyTable1 = simBCBuilder1.PropertyTable
        setManager1 = simBCBuilder1.TargetSetManager
        simBCBuilder1.BcName = name
        simBCBuilder1.BcLabel = 1

        setManager2 = propertyTable1.GetSetManagerPropertyValue("DirectionNode1")
        setManager3 = propertyTable1.GetSetManagerPropertyValue("DirectionNode2")
        setManager4 = propertyTable1.GetSetManagerPropertyValue("DirectionNode3")
        setManager5 = propertyTable1.GetSetManagerPropertyValue("DirectionNode4")

        objects1 = [None] * 1
        objects1[0] = NXOpen.CAE.SetObject()
        component1 = workSimPart.ComponentAssembly.RootComponent.FindObject("COMPONENT model1_fem1 1")
        cAEFace1 = component1.FindObject("PROTO#CAE_Body(78)|CAE_Face(774)")
        objects1[0].Obj = cAEFace1
        objects1[0].SubType = NXOpen.CAE.CaeSetObjectSubType.NotSet
        objects1[0].SubId = 0
        setManager1.SetTargetSetMembers(0, NXOpen.CAE.CaeSetGroupFilterType.GeomFace, objects1)

        scalarFieldWrapper1 = propertyTable1.GetScalarFieldWrapperPropertyValue("TotalForce")

        expression1 = scalarFieldWrapper1.GetExpression()

        unit1 = workSimPart.UnitCollection.FindObject("Newton")
        workSimPart.Expressions.EditWithUnits(expression1, unit1, str(force))

        scalarFieldWrapper1.SetExpression(expression1)

        propertyTable1.SetScalarFieldWrapperPropertyValue("TotalForce", scalarFieldWrapper1)

        setManager6 = propertyTable1.GetSetManagerPropertyValue("DirectionNode1")
        setManager7 = propertyTable1.GetSetManagerPropertyValue("DirectionNode2")
        setManager8 = propertyTable1.GetSetManagerPropertyValue("DirectionNode3")
        setManager9 = propertyTable1.GetSetManagerPropertyValue("DirectionNode4")

        propertyTable1.SetTablePropertyWithoutValue("DistributionField")
        propertyTable1.SetScalarFieldWrapperPropertyValue("DistributionField", NXOpen.Fields.ScalarFieldWrapper.Null)

        propertyValue1 = []
        propertyTable1.SetTextPropertyValue("description", propertyValue1)
        simBC1 = simBCBuilder1.CommitAddBc()
        simBCBuilder1.Destroy()

    def update_torque(self, torque, name='Torque(1)'):
        theSession  = NXOpen.Session.GetSession()
        workSimPart = theSession.Parts.BaseWork
        displaySimPart = theSession.Parts.BaseDisplay

        simSimulation1 = workSimPart.Simulation

        simLoad1 = simSimulation1.Loads.FindObject("Load[Torque(1)]")
        simBCBuilder1 = simSimulation1.CreateBcBuilderForBc(simLoad1)

        propertyTable1 = simBCBuilder1.PropertyTable
        setManager1 = simBCBuilder1.TargetSetManager

        simBCBuilder1.BcName = "Torque(1)"
        simBCBuilder1.BcLabel = 1

        objects1 = [None] * 1
        objects1[0] = NXOpen.CAE.SetObject()
        component1 = workSimPart.ComponentAssembly.RootComponent.FindObject("COMPONENT model1_fem1 1")
        cAEEdge1 = component1.FindObject("PROTO#CAE_Body(78)|CAE_Edge(1007)")
        objects1[0].Obj = cAEEdge1
        objects1[0].SubType = NXOpen.CAE.CaeSetObjectSubType.NotSet
        objects1[0].SubId = 0
        setManager1.SetTargetSetMembers(0, NXOpen.CAE.CaeSetGroupFilterType.GeomCircularedge, objects1)

        scalarFieldWrapper1 = propertyTable1.GetScalarFieldWrapperPropertyValue("TotalForce")
        expression1 = scalarFieldWrapper1.GetExpression()
        unit1 = workSimPart.UnitCollection.FindObject("NewtonMilliMeter")
        workSimPart.Expressions.EditWithUnits(expression1, unit1, str(torque))

        scalarFieldWrapper1.SetExpression(expression1)
        propertyTable1.SetScalarFieldWrapperPropertyValue("TotalForce", scalarFieldWrapper1)

        propertyValue1 = []
        propertyTable1.SetTextPropertyValue("description", propertyValue1)

        simBC1 = simBCBuilder1.CommitAddBc()
        simBCBuilder1.Destroy()

if __name__ == '__main__':
    AA5086_yield = 215 #MPa
    safety_factor = 1.4

    target_stress = AA5086_yield / safety_factor

    optimizer = Optimizer('model1', 'C:/Users/tuanat/Desktop/The loop')

    optimizer.go_to_sim()
    # optimizer.update_force(30000)
    # optimizer.update_torque(50000)

    optimizer.optimize(target_stress)
