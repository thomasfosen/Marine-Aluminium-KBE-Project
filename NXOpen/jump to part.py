# NX 12.0.2.9
# Journal created by tuanat on Thu Mar  5 18:53:27 2020 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.CAE
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workFemPart = theSession.Parts.BaseWork
    displayFemPart = theSession.Parts.BaseDisplay
    part1 = theSession.Parts.FindObject("model1")
    status1, partLoadStatus1 = theSession.Parts.SetDisplay(part1, False, True)
    
    workFemPart = NXOpen.BasePart.Null
    workPart = theSession.Parts.Work
    displayFemPart = NXOpen.BasePart.Null
    displayPart = theSession.Parts.Display
    theSession.Parts.SetWork(workPart)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()