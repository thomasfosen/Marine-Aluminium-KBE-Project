# NX 12.0.2.9
# Journal created by tuanat on Mon Mar  2 13:41:07 2020 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.CAE
def main() :

    theSession  = NXOpen.Session.GetSession()
    workSimPart = theSession.Parts.BaseWork
    displaySimPart = theSession.Parts.BaseDisplay



    simSimulation1 = workSimPart.FindObject("Simulation")
    simSolution1 = simSimulation1.FindObject("Solution[Solution 1]")
    simResultReference1 = simSolution1.Find("Structural")
    resultManager1 = theSession.ResultManager
    solutionResult1 = resultManager1.FindObject("SolutionResult[model1_fem1_sim1.sim_Solution 1]")
    loadcase1 = solutionResult1.Find("Loadcase[1]")
    iteration1 = loadcase1.Find("Iteration[1]")
    ptype1 = NXOpen.CAE.Result.Type(NXOpen.CAE.Result.Quantity.Stress, NXOpen.CAE.Result.Location.ElementNodal, NXOpen.CAE.Result.Section.NotApplicable)
    resultMeasureResultOptions1 = simSimulation1.ResultMeasures.CreateNewResultOptions(simSolution1, simResultReference1, loadcase1, iteration1, False, NXOpen.CAE.Iteration.Null, ptype1, NXOpen.CAE.Result.Component.VonMises)
    unit1 = workSimPart.UnitCollection.FindObject("StressNewtonPerSquareMilliMeter")
    resultMeasureResultOptions1.SetUnit(unit1)
    resultMeasureResultOptions1.SetPlynum(0)
    resultMeasureResultOptions1.SetOperation(NXOpen.CAE.ResultMeasure.Operation.Maximum)
    resultMeasure1 = simSimulation1.ResultMeasures.CreateResultMeasureNew(resultMeasureResultOptions1, None, "as1newre234sultmeasure")




if __name__ == '__main__':
    main()
