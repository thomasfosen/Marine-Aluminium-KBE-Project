# NX 12.0.2.9
# Journal created by tuanat on Mon Feb 24 09:29:41 2020 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.CAE
def main() :

    theSession  = NXOpen.Session.GetSession()
    workFemPart = theSession.Parts.BaseWork
    displayFemPart = theSession.Parts.BaseDisplay

    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")

    fEModel1 = workFemPart.FindObject("FEModel")
    meshManager1 = fEModel1.Find("MeshManager")

    mesh3dHexBuilder1 = meshManager1.CreateMesh3dHexBuilder(NXOpen.CAE.SweptMesh.Null)
    mesh3dHexBuilder1.ElementType.DestinationCollector.ElementContainer = NXOpen.CAE.MeshCollector.Null
    mesh3dHexBuilder1.ElementType.ElementTypeName = "CHEXA(20)"

    unit1 = workFemPart.UnitCollection.FindObject("MilliMeter")
    mesh3dHexBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("source element size", "31.6", unit1)

    theSession.SetUndoMarkName(markId1, "3D Swept Mesh Dialog")

    mesh3dHexBuilder1.CreationType = NXOpen.CAE.Mesh3dHexBuilder.Type.Automatic

    objects1 = [NXOpen.DisplayableObject.Null] * 1
    cAEBody1 = workFemPart.FindObject("CAE_Body(1)")
    cAEFace1 = cAEBody1.FindObject("CAE_Face(3)")
    objects1[0] = cAEFace1
    added1 = mesh3dHexBuilder1.SourceFaceList.Add(objects1)


    mesh3dHexBuilder1.ElementType.ElementDimension = NXOpen.CAE.ElementTypeBuilder.ElementType.SweepSolid
    mesh3dHexBuilder1.ElementType.ElementTypeName = "CHEXA(20)"

    destinationCollectorBuilder1 = mesh3dHexBuilder1.ElementType.DestinationCollector
    destinationCollectorBuilder1.ElementContainer = NXOpen.CAE.MeshCollector.Null
    destinationCollectorBuilder1.AutomaticMode = True

    #mesh settings
    mesh3dHexBuilder1.PropertyTable.SetIntegerPropertyValue("mesh time stamp", 0)
    mesh3dHexBuilder1.PropertyTable.SetIntegerPropertyValue("mesh edit allowed", 0)
    mesh3dHexBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("quad mesh overall edge size", "1", unit1)
    mesh3dHexBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("source element size", "31.6", unit1)
    mesh3dHexBuilder1.PropertyTable.SetBooleanPropertyValue("mapped mesh option bool", False)
    mesh3dHexBuilder1.PropertyTable.SetIntegerPropertyValue("quad only option", 0)
    mesh3dHexBuilder1.PropertyTable.SetBooleanPropertyValue("make mesh manual bool", False)
    mesh3dHexBuilder1.PropertyTable.SetBooleanPropertyValue("create cohesive element type", False)
    mesh3dHexBuilder1.PropertyTable.SetBooleanPropertyValue("reverse elements orientation", False)
    mesh3dHexBuilder1.PropertyTable.SetBooleanPropertyValue("Number of Layers bool", False)
    mesh3dHexBuilder1.PropertyTable.SetIntegerPropertyValue("number of layers", 1)
    mesh3dHexBuilder1.PropertyTable.SetBooleanPropertyValue("project vertices option", False)
    mesh3dHexBuilder1.PropertyTable.SetBooleanPropertyValue("target face smoothing option", False)

    meshes1 = mesh3dHexBuilder1.CommitMesh()


if __name__ == '__main__':
    main()
