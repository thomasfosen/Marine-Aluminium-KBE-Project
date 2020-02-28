# NX 12.0.2.9
# Journal created by tuanat on Thu Feb 27 14:53:44 2020 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.CAE
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workFemPart = theSession.Parts.BaseWork
    displayFemPart = theSession.Parts.BaseDisplay
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Make Displayed Part")
    
    simPart1 = theSession.Parts.FindObject("cake_fem_sim1")
    status1, partLoadStatus1 = theSession.Parts.SetActiveDisplay(simPart1, NXOpen.DisplayPartOption.AllowAdditional, NXOpen.PartDisplayPartWorkPartOption.SameAsDisplay)
    
    workSimPart = theSession.Parts.BaseWork
    displaySimPart = theSession.Parts.BaseDisplay
    partLoadStatus1.Dispose()
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()