# NX 12.0.2.9
# Journal created by tuanat on Thu Feb 27 14:51:19 2020 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.CAE
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workFemPart = theSession.Parts.BaseWork
    displayFemPart = theSession.Parts.BaseDisplay
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()