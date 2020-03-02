# NX 12.0.2.9
# Journal created by tuanat on Mon Mar  2 12:39:43 2020 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.CAE
def main() :

    theSession  = NXOpen.Session.GetSession()
    workSimPart = theSession.Parts.BaseWork

    simSimulation1 = workSimPart.FindObject("Simulation")
    objects1 = [NXOpen.CAE.ResultMeasure.Null] * 1
    resultMeasure1 = simSimulation1.ResultMeasures.Find("NXOpen.CAE.ResultMeasure[newresultmeasure]")
    objects1[0] = resultMeasure1

    simSimulation1.ResultMeasures.UpdateMeasures(objects1)

    theNxMessageBox = NXOpen.UI.GetUI().NXMessageBox
    theNxMessageBox.Show("Bodies",NXOpen.NXMessageBoxDialogType.Information, str(resultMeasure1.Result))

if __name__ == '__main__':
    main()
