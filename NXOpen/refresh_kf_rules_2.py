# NX 12.0.2.9
# Journal created by tuanat on Tue Mar 10 10:23:27 2020 W. Europe Standard Time
#
import math
import NXOpen
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    workPart.RuleManager.Reload(True)
    
    workPart.RuleManager.RegenerateAll()
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()