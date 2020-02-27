# NX 12.0.2.9
# Journal created by tuanat on Tue Feb 25 12:21:35 2020 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.CAE
import NXOpen.PhysMat
def main() :

    theSession  = NXOpen.Session.GetSession()
    workFemPart = theSession.Parts.BaseWork
    displayFemPart = theSession.Parts.BaseDisplay

    fEModel1 = workFemPart.FindObject("FEModel")
    meshManager1 = fEModel1.Find("MeshManager")
    meshCollector1 = meshManager1.FindObject("MeshCollector[test]")
    meshCollectorBuilder1 = meshManager1.CreateCollectorBuilder(meshCollector1, "Solid")

    caePart1 = workFemPart
    physicalPropertyTable1 = caePart1.PhysicalPropertyTables.CreatePhysicalPropertyTable("PSOLID", "NX NASTRAN - Structural", "NX NASTRAN", "PSOLID1", 1)
    propertyTable1 = physicalPropertyTable1.PropertyTable

    physicalMaterialListBuilder1 = workFemPart.MaterialManager.PhysicalMaterials.CreateListBlockBuilder()
    physicalMaterial1 = workFemPart.MaterialManager.PhysicalMaterials.LoadFromNxmatmllibrary("Aluminum_6061")
    physicalMaterialListBuilder1.Destroy()

    propertyTable1.SetMaterialPropertyValue("material", False, physicalMaterial1)
    meshCollectorBuilder1.PropertyTable.SetNamedPropertyTablePropertyValue("Solid Property", physicalPropertyTable1)

    nXObject1 = meshCollectorBuilder1.Commit()
    meshCollectorBuilder1.Destroy()

if __name__ == '__main__':
    main()
