﻿# NX 12.0.2.9
# Journal created by tuanat on Tue Feb 25 11:08:52 2020 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.CAE
def main() :

    theSession  = NXOpen.Session.GetSession()
    workFemPart = theSession.Parts.BaseWork
    displayFemPart = theSession.Parts.BaseDisplay

    fEModel1 = workFemPart.FindObject("FEModel")
    meshManager1 = fEModel1.Find("MeshManager")
    meshCollectorBuilder1 = meshManager1.CreateCollectorBuilder(NXOpen.CAE.MeshCollector.Null, "Solid")
    meshCollectorBuilder1.CollectorName = "cake"
    nXObject1 = meshCollectorBuilder1.Commit()
    meshCollectorBuilder1.Destroy()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          # ----------------------------------------------
    #   Menu: Tools->Journal->Play...
    # ----------------------------------------------
    basePart1 = theSession.Parts.BaseWork
    
    unit1 = workFemPart.UnitCollection.FindObject("MilliMeter")
    
    unit2 = workFemPart.UnitCollection.FindObject("Degrees")
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()