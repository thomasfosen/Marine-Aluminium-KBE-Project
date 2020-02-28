# NX 12.0.2.9
# Journal created by tuanat on Thu Feb 27 14:28:55 2020 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.CAE
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    femPart1 = theSession.Parts.FindObject("cake_fem")
    status1, partLoadStatus1 = theSession.Parts.SetDisplay(femPart1, False, True)
    
    workPart = NXOpen.Part.Null
    workFemPart = theSession.Parts.BaseWork
    displayPart = NXOpen.Part.Null
    displayFemPart = theSession.Parts.BaseDisplay
    femPart2 = workFemPart
    theSession.Parts.SetWork(femPart2)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()