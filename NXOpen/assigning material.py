﻿# NX 12.0.2.9
# Journal created by tuanat on Mon Feb 24 09:31:44 2020 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.CAE
import NXOpen.PhysMat
def main() :

    theSession  = NXOpen.Session.GetSession()
    workFemPart = theSession.Parts.BaseWork

    fEModel1 = workFemPart.FindObject("FEModel")
    meshManager1 = fEModel1.Find("MeshManager")
    meshCollector1 = meshManager1.FindObject("MeshCollector[Solid(1)]")
    meshCollectorBuilder1 = meshManager1.CreateCollectorBuilder(meshCollector1, "Solid")


    physicalPropertyTable1 = workFemPart.PhysicalPropertyTables.FindObject("PhysPropTable[PSOLID1]")
    propertyTable1 = physicalPropertyTable1.PropertyTable
    physicalMaterialListBuilder1 = workFemPart.MaterialManager.PhysicalMaterials.CreateListBlockBuilder()
    physicalMaterial1 = workFemPart.MaterialManager.PhysicalMaterials.LoadFromNxmatmllibrary("Aluminum_6061")
    physicalMaterialListBuilder1.Destroy()
    propertyTable1.SetMaterialPropertyValue("material", False, physicalMaterial1)
    nXObject1 = meshCollectorBuilder1.Commit()

    meshCollectorBuilder1.Destroy()


    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------

if __name__ == '__main__':
    main()
