# NX 12.0.2.9
# Journal created by tuanat on Thu Feb 27 15:34:47 2020 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.CAE
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workFemPart = theSession.Parts.BaseWork
    displayFemPart = theSession.Parts.BaseDisplay
    # ----------------------------------------------
    #   Menu: Insert->Mesh->3D Tetrahedral Mesh...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    fEModel1 = workFemPart.FindObject("FEModel")
    meshManager1 = fEModel1.Find("MeshManager")
    mesh3dTetBuilder1 = meshManager1.CreateMesh3dTetBuilder(NXOpen.CAE.Mesh3d.Null)
    
    meshCollector1 = meshManager1.FindObject("MeshCollector[test]")
    mesh3dTetBuilder1.ElementType.DestinationCollector.ElementContainer = meshCollector1
    
    mesh3dTetBuilder1.ElementType.ElementTypeName = "CTETRA(10)"
    
    mesh3dTetBuilder1.ElementType.DestinationCollector.AutomaticMode = False
    
    unit1 = workFemPart.UnitCollection.FindObject("MilliMeter")
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("quad mesh overall edge size", "100", unit1)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("small feature value", "10", NXOpen.Unit.Null)
    
    theSession.SetUndoMarkName(markId1, "3D Tetrahedral Mesh Dialog")
    
    cAEBody1 = workFemPart.FindObject("CAE_Body(15)")
    added1 = mesh3dTetBuilder1.SelectionList.Add(cAEBody1)
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "3D Tetrahedral Mesh")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "3D Tetrahedral Mesh")
    
    mesh3dTetBuilder1.AutoResetOption = False
    
    mesh3dTetBuilder1.ElementType.ElementDimension = NXOpen.CAE.ElementTypeBuilder.ElementType.FreeSolid
    
    mesh3dTetBuilder1.ElementType.ElementTypeName = "CTETRA(10)"
    
    destinationCollectorBuilder1 = mesh3dTetBuilder1.ElementType.DestinationCollector
    
    destinationCollectorBuilder1.ElementContainer = meshCollector1
    
    destinationCollectorBuilder1.AutomaticMode = False
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("quad mesh overall edge size", "30.9", unit1)
    
    mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("mapped mesh option bool", True)
    
    mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("multiblock cylinder option bool", False)
    
    mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("fillet num elements", 3)
    
    mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("num elements on cylinder circumference", 6)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("element size on cylinder height", "1", unit1)
    
    mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("create pyramids bool", False)
    
    mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("midnodes", 0)
    
    mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("geometry tolerance option bool", False)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("geometry tolerance", "0", unit1)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("max jacobian", "10", NXOpen.Unit.Null)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("surface mesh size variation", "50", NXOpen.Unit.Null)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("volume mesh size variation", "50", NXOpen.Unit.Null)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("internal mesh gradation", "1.05", NXOpen.Unit.Null)
    
    mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("internal max edge option bool", False)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("internal max edge length value", "0", unit1)
    
    mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("two elements through thickness bool", False)
    
    mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("mesh transition bool", False)
    
    mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("remesh on bad quality bool", False)
    
    mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("maximum edge length bool", False)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("maximum edge length", "1", unit1)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("small feature tolerance", "10", NXOpen.Unit.Null)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("small feature value", "3.09", NXOpen.Unit.Null)
    
    mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("boundary layer element type", 3)
    
    mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("insert blend elements", True)
    
    unit2 = workFemPart.UnitCollection.FindObject("Degrees")
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("blending angle", "90", unit2)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("sweep angle", "45", unit2)
    
    mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("control aspect ratio", False)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("maximum exposed aspect ratio", "1000", NXOpen.Unit.Null)
    
    mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("control slender", False)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("minimum aspect ratio", "0.01", NXOpen.Unit.Null)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("maximum imprint dihedral angle", "120", unit2)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("gradation rate", "10", NXOpen.Unit.Null)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("smoothing distance factor", "3", NXOpen.Unit.Null)
    
    mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("all-tet boundary layer", False)
    
    mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("dont format mesh to solver", 0)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("quad mesh edge match tolerance", "0.02", NXOpen.Unit.Null)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("quad mesh smoothness tolerance", "0.01", unit1)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("min face angle", "20", unit2)
    
    mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("mesh time stamp", 0)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("quad mesh node coincidence tolerance", "0.0001", unit1)
    
    mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("mesh edit allowed", 0)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("edge angle", "15", unit2)
    
    mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("merge edge toggle", 0)
    
    mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("auto constraining", 1)
    
    mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("curvature scaling", 1)
    
    mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("target angle", "45", unit2)
    
    mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("edge shape", 2)
    
    id1 = theSession.NewestVisibleUndoMark
    
    nErrs1 = theSession.UpdateManager.DoUpdate(id1)
    
    meshes1 = mesh3dTetBuilder1.CommitMesh()
    
    theSession.DeleteUndoMark(markId3, None)
    
    theSession.SetUndoMarkName(id1, "3D Tetrahedral Mesh")
    
    mesh3dTetBuilder1.Destroy()
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()