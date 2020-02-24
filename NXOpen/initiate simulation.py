# NX 12.0.2.9
# Journal created by tuanat on Mon Feb 24 09:35:47 2020 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.CAE
def main() :

    theSession  = NXOpen.Session.GetSession()
    workSimPart = theSession.Parts.BaseWork
    displaySimPart = theSession.Parts.BaseDisplay

    theSimSolveManager = NXOpen.CAE.SimSolveManager.GetSimSolveManager(theSession)

    psolutions1 = [NXOpen.CAE.SimSolution.Null] * 1
    simSimulation1 = workSimPart.FindObject("Simulation")
    simSolution1 = simSimulation1.FindObject("Solution[Solution 1]")
    psolutions1[0] = simSolution1
    numsolutionssolved1, numsolutionsfailed1, numsolutionsskipped1 = theSimSolveManager.SolveChainOfSolutions(psolutions1, NXOpen.CAE.SimSolution.SolveOption.Solve, NXOpen.CAE.SimSolution.SetupCheckOption.CompleteCheckAndOutputErrors, NXOpen.CAE.SimSolution.SolveMode.Background)

if __name__ == '__main__':
    main()
