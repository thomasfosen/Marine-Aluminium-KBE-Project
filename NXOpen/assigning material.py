# NX 12.0.2.9
# Journal created by tuanat on Mon Feb 24 09:31:44 2020 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.CAE
import NXOpen.PhysMat
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workFemPart = theSession.Parts.BaseWork
    displayFemPart = theSession.Parts.BaseDisplay
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    fEModel1 = workFemPart.FindObject("FEModel")
    meshManager1 = fEModel1.Find("MeshManager")
    meshCollector1 = meshManager1.FindObject("MeshCollector[Solid(1)]")
    meshCollectorBuilder1 = meshManager1.CreateCollectorBuilder(meshCollector1, "Solid")
    
    theSession.SetUndoMarkName(markId1, "Mesh Collector Dialog")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    physicalPropertyTable1 = workFemPart.PhysicalPropertyTables.FindObject("PhysPropTable[PSOLID1]")
    propertyTable1 = physicalPropertyTable1.PropertyTable
    
    theSession.SetUndoMarkName(markId2, "PSOLID Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin PSOLID
    # ----------------------------------------------
    physicalMaterialListBuilder1 = workFemPart.MaterialManager.PhysicalMaterials.CreateListBlockBuilder()
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    theSession.SetUndoMarkName(markId3, "Material List Dialog")
    
    id1 = theSession.GetNewestUndoMark(NXOpen.Session.MarkVisibility.AnyVisibility)
    
    theSession.DeleteUndoMark(id1, None)
    
    # ----------------------------------------------
    #   Dialog Begin Material List
    # ----------------------------------------------
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Material List")
    
    theSession.DeleteUndoMark(markId4, None)
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Material List")
    
    physicalMaterial1 = workFemPart.MaterialManager.PhysicalMaterials.LoadFromNxmatmllibrary("Aluminum_6061")
    
    theSession.DeleteUndoMark(markId5, None)
    
    theSession.DeleteUndoMark(id1, None)
    
    physicalMaterialListBuilder1.Destroy()
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "PSOLID")
    
    theSession.DeleteUndoMark(markId6, None)
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "PSOLID")
    
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    propertyTable1.SetMaterialPropertyValue("material", False, physicalMaterial1)
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId8)
    
    theSession.DeleteUndoMark(markId8, None)
    
    theSession.DeleteUndoMark(markId7, None)
    
    theSession.SetUndoMarkName(markId2, "PSOLID")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Mesh Collector")
    
    theSession.DeleteUndoMark(markId9, None)
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Mesh Collector")
    
    nXObject1 = meshCollectorBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId10, None)
    
    theSession.SetUndoMarkName(markId1, "Mesh Collector")
    
    meshCollectorBuilder1.Destroy()
    
    theSession.DeleteUndoMark(markId1, None)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()