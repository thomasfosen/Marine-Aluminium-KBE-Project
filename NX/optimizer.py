import NXOpen
import NXOpen.CAE

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

    def get_result(self):
        theSession  = NXOpen.Session.GetSession()
        workSimPart = theSession.Parts.BaseWork

        simSimulation1 = workSimPart.FindObject("Simulation")
        objects1 = [NXOpen.CAE.ResultMeasure.Null] * 1
        resultMeasure1 = simSimulation1.ResultMeasures.Find("NXOpen.CAE.ResultMeasure[max_von_mises]")
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
        # going from low stress to the limit. it's possible to do it from either direction
        # and with a decreasing change in diameter to get a more accurate result
        stress_result = 0
        optimize = True
        change_in_diameter = -10
        while optimize == True:
            result = self.perform_loop_iteration(change_in_diameter)

            if result > target_stress:
                optimize = False
                final_diameter = current_node_diameter = self.dfa_manager.get_node_diameter()
                self.print('Optimization has finished. Final stress:' + str(result) + '\n final diameter:' + str(final_diameter))

if __name__ == '__main__':
    AA5086_yield = 215 #MPa
    safety_factor = 1.4

    target_stress = AA5086_yield / safety_factor

    optimizer = Optimizer('model1', 'C:/Users/tuanat/Desktop/The loop')
    optimizer.optimize(target_stress)
