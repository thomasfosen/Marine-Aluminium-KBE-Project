# NX 12.0.2.9
# Journal created by tuanat on Tue Feb 25 11:22:49 2020 W. Europe Standard Time
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
    meshCollector1 = meshManager1.FindObject("MeshCollector[cake]")
    meshCollectorBuilder1 = meshManager1.CreateCollectorBuilder(meshCollector1, "Solid")
    physicalPropertyTable1 = workFemPart.PhysicalPropertyTables.FindObject("PhysPropTable[PSOLID1]")
    meshCollectorBuilder1.PropertyTable.SetNamedPropertyTablePropertyValue("Solid Property", physicalPropertyTable1)

    nXObject1 = meshCollectorBuilder1.Commit()
    meshCollectorBuilder1.Destroy()


if __name__ == '__main__':
    main()
