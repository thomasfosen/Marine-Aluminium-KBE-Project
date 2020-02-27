


import math
import NXOpen
import NXOpen.CAE
import time

def main():


    theSession  = NXOpen.Session.GetSession()
    workSimPart = theSession.Parts.BaseWork
    displaySimPart = theSession.Parts.BaseDisplay

    theSimSolveManager = NXOpen.CAE.SimSolveManager.GetSimSolveManager(theSession)

    simSimulation1 = workSimPart.FindObject("Simulation")
    simSolution1 = simSimulation1.FindObject("Solution[Solution 1]")
    psolutions1 = [NXOpen.CAE.SimSolution.Null] * 1
    psolutions1[0] = simSolution1
    numsolutionssolved1, numsolutionsfailed1, numsolutionsskipped1 = theSimSolveManager.SolveChainOfSolutions(psolutions1, NXOpen.CAE.SimSolution.SolveOption.Solve, NXOpen.CAE.SimSolution.SetupCheckOption.CompleteCheckAndOutputErrors, NXOpen.CAE.SimSolution.SolveMode.Background)

    #to give results some buffer time
    time.sleep(10)

    simResultReference1 = simSolution1.Find("Structural")
    solutionResult1 = theSession.ResultManager.CreateReferenceResult(simResultReference1)

    postviewId1 = theSession.Post.CreateNewPostview(0, solutionResult1, False, NXOpen.CAE.Post.DisplayColorSchemeType.Fringe)


if __name__ == '__main__':
    main()
