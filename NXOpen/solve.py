


import math
import NXOpen
import NXOpen.CAE

def main():


    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display


    theSimSolveManager = NXOpen.CAE.SimsolveManager.GetSimSolveManager(theSession)


    psolutions1 = [NXOpen.CAE.SimSolution.Null] * 1
    psolutions1[0] = simSolution2
    numsolutionssolved1, numsolutionsfailed1, numsolutionsskipped1 = theSimSolveManager.SolveChainOfSolutions(psolutions1, NXOpen.CAE.SimSolution.SolveOption.Solve, NXOpen.CAE.SimSolution.SetupCheckOption.CompleteCheckAndOutputErrors, NXOpen.CAE.SimSolution.SolveMode.Background)


    simResultReference1 = simSolution2.Find("Structural")
    solutionResult1 = theSession.ResultManager.CreateReferenceResult(simResultReference1)

    postviewId1 = theSession.Post.CreateNewPostview(0, solutionResult1, False, NXOpen.CAE.Post.DisplayColorSchemeType.Fringe)


if __name__ == '__main__':
    main()
