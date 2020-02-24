# NX 12.0.2.9
# Journal created by tuanat on Mon Feb 24 10:25:54 2020 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.CAE
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: Application->Design->Modeling
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Modeling")
    
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Play...
    # ----------------------------------------------
    part1 = theSession.Parts.Work
    
    part2 = theSession.Parts.Display
    
    theSession.ApplicationSwitchImmediate("UG_APP_SFEM")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Pre/Post")
    
    # ----------------------------------------------
    #   Menu: Application->Design->Modeling
    # ----------------------------------------------
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Modeling")
    
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Play...
    # ----------------------------------------------
    part3 = theSession.Parts.Work
    
    part4 = theSession.Parts.Display
    
    theSession.ApplicationSwitchImmediate("UG_APP_SFEM")
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Pre/Post")
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Play...
    # ----------------------------------------------
    part5 = theSession.Parts.Work
    
    part6 = theSession.Parts.Display
    
    theSession.ApplicationSwitchImmediate("UG_APP_SFEM")
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Pre/Post")
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Play...
    # ----------------------------------------------
    part7 = theSession.Parts.Work
    
    part8 = theSession.Parts.Display
    
    theSession.ApplicationSwitchImmediate("UG_APP_SFEM")
    
    fileNew1 = theSession.Parts.FileNew()
    
    fileNew1.TemplateFileName = "FemNxNastranMetric.fem"
    
    fileNew1.UseBlankTemplate = False
    
    fileNew1.ApplicationName = "CaeFemTemplate"
    
    fileNew1.Units = NXOpen.Part.Units.Millimeters
    
    fileNew1.RelationType = ""
    
    fileNew1.UsesMasterModel = "No"
    
    fileNew1.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew1.TemplatePresentationName = "NX Nastran"
    
    fileNew1.ItemType = ""
    
    fileNew1.Specialization = ""
    
    fileNew1.SetCanCreateAltrep(False)
    
    fileNew1.NewFileName = "C:\\Users\\tuanat\\Desktop\\test\\model1_fem11.fem"
    
    fileNew1.MasterFileName = ""
    
    fileNew1.MakeDisplayedPart = True
    
    fileNew1.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    baseTemplateManager1 = theSession.XYPlotManager.TemplateManager
    
    baseTemplateManager2 = theSession.XYPlotManager.TemplateManager
    
    nXObject1 = fileNew1.Commit()
    
    workPart = NXOpen.Part.Null
    workFemPart = theSession.Parts.BaseWork
    displayPart = NXOpen.Part.Null
    displayFemPart = theSession.Parts.BaseDisplay
    basePart1 = theSession.Parts.BaseWork
    
    basePart2 = theSession.Parts.BaseDisplay
    
    femPart1 = workFemPart
    femPart1.PolygonGeometryMgr.SetPolygonBodyResolutionOnFemBodies(NXOpen.CAE.PolygonGeometryManager.PolygonBodyResolutionType.Standard)
    
    femPart2 = workFemPart
    femCreationOptions1 = femPart2.NewFemCreationOptions()
    
    femPart3 = workFemPart
    femSynchronizeOptions1 = femPart3.NewFemSynchronizeOptions()
    
    femSynchronizeOptions1.SynchronizePointsFlag = False
    
    femSynchronizeOptions1.SynchronizeCoordinateSystemFlag = False
    
    femSynchronizeOptions1.SynchronizeLinesFlag = False
    
    femSynchronizeOptions1.SynchronizeArcsFlag = False
    
    femSynchronizeOptions1.SynchronizeSplinesFlag = False
    
    femSynchronizeOptions1.SynchronizeConicsFlag = False
    
    femSynchronizeOptions1.SynchronizeSketchCurvesFlag = False
    
    basePart3 = theSession.Parts.FindObject("model1")
    
    part9 = basePart3
    femCreationOptions1.SetCadData(part9, "C:\\Users\\tuanat\\Desktop\\test\\model1.prt")
    
    body1 = part9.Bodies.FindObject("BLOCK(4)")
    
    bodies1 = [NXOpen.Body.Null] * 1 
    bodies1[0] = body1
    femCreationOptions1.SetGeometryOptions(NXOpen.CAE.FemCreationOptions.UseBodiesOption.VisibleBodies, bodies1, femSynchronizeOptions1)
    
    femCreationOptions1.SetSolverOptions("NX NASTRAN", "Structural", NXOpen.CAE.BaseFemPart.AxisymAbstractionType.NotSet)
    
    description1 = []
    femCreationOptions1.SetDescription(description1)
    
    femCreationOptions1.SetMorphingFlag(False)
    
    femCreationOptions1.SetCyclicSymmetryData(False, NXOpen.CoordinateSystem.Null)
    
    femPart4 = workFemPart
    femPart4.FinalizeCreation(femCreationOptions1)
    
    femSynchronizeOptions1.Dispose()
    femCreationOptions1.Dispose()
    fileNew1.Destroy()
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Pre/Post")
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Play...
    # ----------------------------------------------
    basePart4 = theSession.Parts.BaseWork
    
    femPart5 = workFemPart
    iNXObject1 = femPart5.FindObject("FEModel")
    
    fEModel1 = iNXObject1
    taggedObject1 = fEModel1.Find("MeshManager")
    
    meshManager1 = taggedObject1
    mesh3dHexBuilder1 = meshManager1.CreateMesh3dHexBuilder(NXOpen.CAE.SweptMesh.Null)
    
    elementTypeBuilder1 = mesh3dHexBuilder1.ElementType
    
    destinationCollectorBuilder1 = elementTypeBuilder1.DestinationCollector
    
    destinationCollectorBuilder1.ElementContainer = NXOpen.CAE.MeshCollector.Null
    
    elementTypeBuilder2 = mesh3dHexBuilder1.ElementType
    
    elementTypeBuilder2.ElementTypeName = "CHEXA(20)"
    
    unit1 = workFemPart.UnitCollection.FindObject("MilliMeter")
    
    propertyTable1 = mesh3dHexBuilder1.PropertyTable
    
    propertyTable1.SetBaseScalarWithDataPropertyValue("source element size", "31.6", unit1)
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId7, "3D Swept Mesh Dialog")
    
    mesh3dHexBuilder1.CreationType = NXOpen.CAE.Mesh3dHexBuilder.Type.Automatic
    
    femPart6 = workFemPart
    iNXObject2 = femPart6.FindObject("CAE_Body(1)")
    
    cAEBody1 = iNXObject2
    iNXObject3 = cAEBody1.FindObject("CAE_Face(3)")
    
    selectDisplayableObjectList1 = mesh3dHexBuilder1.SourceFaceList
    
    objects1 = [NXOpen.DisplayableObject.Null] * 1 
    cAEFace1 = iNXObject3
    objects1[0] = cAEFace1
    added1 = selectDisplayableObjectList1.Add(objects1)
    
    elementTypeBuilder3 = mesh3dHexBuilder1.ElementType
    
    elementTypeBuilder3.ElementDimension = NXOpen.CAE.ElementTypeBuilder.ElementType.SweepSolid
    
    elementTypeBuilder4 = mesh3dHexBuilder1.ElementType
    
    elementTypeBuilder4.ElementTypeName = "CHEXA(20)"
    
    elementTypeBuilder5 = mesh3dHexBuilder1.ElementType
    
    destinationCollectorBuilder2 = elementTypeBuilder5.DestinationCollector
    
    destinationCollectorBuilder2.ElementContainer = NXOpen.CAE.MeshCollector.Null
    
    destinationCollectorBuilder2.AutomaticMode = True
    
    propertyTable2 = mesh3dHexBuilder1.PropertyTable
    
    propertyTable2.SetIntegerPropertyValue("mesh time stamp", 0)
    
    propertyTable3 = mesh3dHexBuilder1.PropertyTable
    
    propertyTable3.SetIntegerPropertyValue("mesh edit allowed", 0)
    
    propertyTable4 = mesh3dHexBuilder1.PropertyTable
    
    propertyTable4.SetBaseScalarWithDataPropertyValue("quad mesh overall edge size", "1", unit1)
    
    propertyTable5 = mesh3dHexBuilder1.PropertyTable
    
    propertyTable5.SetBaseScalarWithDataPropertyValue("source element size", "31.6", unit1)
    
    propertyTable6 = mesh3dHexBuilder1.PropertyTable
    
    propertyTable6.SetBooleanPropertyValue("mapped mesh option bool", False)
    
    propertyTable7 = mesh3dHexBuilder1.PropertyTable
    
    propertyTable7.SetIntegerPropertyValue("quad only option", 0)
    
    propertyTable8 = mesh3dHexBuilder1.PropertyTable
    
    propertyTable8.SetBooleanPropertyValue("make mesh manual bool", False)
    
    propertyTable9 = mesh3dHexBuilder1.PropertyTable
    
    propertyTable9.SetBooleanPropertyValue("create cohesive element type", False)
    
    propertyTable10 = mesh3dHexBuilder1.PropertyTable
    
    propertyTable10.SetBooleanPropertyValue("reverse elements orientation", False)
    
    propertyTable11 = mesh3dHexBuilder1.PropertyTable
    
    propertyTable11.SetBooleanPropertyValue("Number of Layers bool", False)
    
    propertyTable12 = mesh3dHexBuilder1.PropertyTable
    
    propertyTable12.SetIntegerPropertyValue("number of layers", 1)
    
    propertyTable13 = mesh3dHexBuilder1.PropertyTable
    
    propertyTable13.SetBooleanPropertyValue("project vertices option", False)
    
    propertyTable14 = mesh3dHexBuilder1.PropertyTable
    
    propertyTable14.SetBooleanPropertyValue("target face smoothing option", False)
    
    id1 = theSession.NewestVisibleUndoMark
    
    nErrs1 = theSession.UpdateManager.DoUpdate(id1)
    
    meshes1 = mesh3dHexBuilder1.CommitMesh()
    
    # ----------------------------------------------
    #   Menu: Edit->Undo
    # ----------------------------------------------
    marksRecycled1, undoUnavailable1 = theSession.UndoLastNVisibleMarks(1)
    
    femPart7 = workFemPart
    femPart7.Close(NXOpen.BasePart.CloseWholeTree.FalseValue, NXOpen.BasePart.CloseModified.UseResponses, None)
    
    workFemPart = NXOpen.BasePart.Null
    displayFemPart = NXOpen.BasePart.Null
    theSession.ApplicationSwitchImmediate("UG_APP_NOPART")
    
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Change Displayed Part")
    
    status1, partLoadStatus1 = theSession.Parts.SetActiveDisplay(part9, NXOpen.DisplayPartOption.AllowAdditional, NXOpen.PartDisplayPartWorkPartOption.UseLast)
    
    workPart = theSession.Parts.Work # model1
    displayPart = theSession.Parts.Display # model1
    partLoadStatus1.Dispose()
    theSession.ApplicationSwitchImmediate("UG_APP_SFEM")
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Pre/Post")
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Play...
    # ----------------------------------------------
    part10 = theSession.Parts.Work
    
    part11 = theSession.Parts.Display
    
    theSession.ApplicationSwitchImmediate("UG_APP_SFEM")
    
    fileNew2 = theSession.Parts.FileNew()
    
    fileNew2.TemplateFileName = "FemNxNastranMetric.fem"
    
    fileNew2.UseBlankTemplate = False
    
    fileNew2.ApplicationName = "CaeFemTemplate"
    
    fileNew2.Units = NXOpen.Part.Units.Millimeters
    
    fileNew2.RelationType = ""
    
    fileNew2.UsesMasterModel = "No"
    
    fileNew2.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew2.TemplatePresentationName = "NX Nastran"
    
    fileNew2.ItemType = ""
    
    fileNew2.Specialization = ""
    
    fileNew2.SetCanCreateAltrep(False)
    
    fileNew2.NewFileName = "C:\\Users\\tuanat\\Desktop\\test\\model1_fem11.fem"
    
    fileNew2.MasterFileName = ""
    
    fileNew2.MakeDisplayedPart = True
    
    fileNew2.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    baseTemplateManager3 = theSession.XYPlotManager.TemplateManager
    
    baseTemplateManager4 = theSession.XYPlotManager.TemplateManager
    
    nXObject2 = fileNew2.Commit()
    
    workPart = NXOpen.Part.Null
    workFemPart = theSession.Parts.BaseWork # model1_fem11
    displayPart = NXOpen.Part.Null
    displayFemPart = theSession.Parts.BaseDisplay # model1_fem11
    basePart5 = theSession.Parts.BaseWork
    
    basePart6 = theSession.Parts.BaseDisplay
    
    femPart8 = workFemPart
    femPart8.PolygonGeometryMgr.SetPolygonBodyResolutionOnFemBodies(NXOpen.CAE.PolygonGeometryManager.PolygonBodyResolutionType.Standard)
    
    femPart9 = workFemPart
    femCreationOptions2 = femPart9.NewFemCreationOptions()
    
    femPart10 = workFemPart
    femSynchronizeOptions2 = femPart10.NewFemSynchronizeOptions()
    
    femSynchronizeOptions2.SynchronizePointsFlag = False
    
    femSynchronizeOptions2.SynchronizeCoordinateSystemFlag = False
    
    femSynchronizeOptions2.SynchronizeLinesFlag = False
    
    femSynchronizeOptions2.SynchronizeArcsFlag = False
    
    femSynchronizeOptions2.SynchronizeSplinesFlag = False
    
    femSynchronizeOptions2.SynchronizeConicsFlag = False
    
    femSynchronizeOptions2.SynchronizeSketchCurvesFlag = False
    
    basePart7 = theSession.Parts.FindObject("model1")
    
    part12 = basePart7
    femCreationOptions2.SetCadData(part12, "C:\\Users\\tuanat\\Desktop\\test\\model1.prt")
    
    body2 = part12.Bodies.FindObject("BLOCK(4)")
    
    bodies2 = [NXOpen.Body.Null] * 1 
    bodies2[0] = body2
    femCreationOptions2.SetGeometryOptions(NXOpen.CAE.FemCreationOptions.UseBodiesOption.VisibleBodies, bodies2, femSynchronizeOptions2)
    
    femCreationOptions2.SetSolverOptions("NX NASTRAN", "Structural", NXOpen.CAE.BaseFemPart.AxisymAbstractionType.NotSet)
    
    description2 = []
    femCreationOptions2.SetDescription(description2)
    
    femCreationOptions2.SetMorphingFlag(False)
    
    femCreationOptions2.SetCyclicSymmetryData(False, NXOpen.CoordinateSystem.Null)
    
    femPart11 = workFemPart
    femPart11.FinalizeCreation(femCreationOptions2)
    
    femSynchronizeOptions2.Dispose()
    femCreationOptions2.Dispose()
    fileNew2.Destroy()
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Pre/Post")
    
    femPart12 = workFemPart
    femPart12.Close(NXOpen.BasePart.CloseWholeTree.FalseValue, NXOpen.BasePart.CloseModified.UseResponses, None)
    
    workFemPart = NXOpen.BasePart.Null
    displayFemPart = NXOpen.BasePart.Null
    theSession.ApplicationSwitchImmediate("UG_APP_NOPART")
    
    # ----------------------------------------------
    #   Menu: File->New...
    # ----------------------------------------------
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    fileNew3 = theSession.Parts.FileNew()
    
    theSession.SetUndoMarkName(markId11, "New Dialog")
    
    fileNew3.Destroy()
    
    theSession.UndoToMark(markId11, None)
    
    theSession.DeleteUndoMark(markId11, None)
    
    # ----------------------------------------------
    #   Menu: File->New...
    # ----------------------------------------------
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    fileNew4 = theSession.Parts.FileNew()
    
    theSession.SetUndoMarkName(markId12, "New Dialog")
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New")
    
    theSession.DeleteUndoMark(markId13, None)
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New")
    
    fileNew4.TemplateFileName = "model-plain-1-mm-template.prt"
    
    fileNew4.UseBlankTemplate = False
    
    fileNew4.ApplicationName = "ModelTemplate"
    
    fileNew4.Units = NXOpen.Part.Units.Millimeters
    
    fileNew4.RelationType = ""
    
    fileNew4.UsesMasterModel = "No"
    
    fileNew4.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew4.TemplatePresentationName = "Model"
    
    fileNew4.ItemType = ""
    
    fileNew4.Specialization = ""
    
    fileNew4.SetCanCreateAltrep(False)
    
    fileNew4.NewFileName = "C:\\Users\\tuanat\\Desktop\\test\\test\\model1.prt"
    
    fileNew4.MasterFileName = ""
    
    fileNew4.MakeDisplayedPart = True
    
    fileNew4.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    try:
        # File already exists
        nXObject3 = fileNew4.Commit()
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1020004)
        
    theSession.UndoToMarkWithStatus(markId14, None)
    
    theSession.DeleteUndoMark(markId14, None)
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New")
    
    theSession.DeleteUndoMark(markId15, None)
    
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New")
    
    fileNew4.TemplateFileName = "model-plain-1-mm-template.prt"
    
    fileNew4.UseBlankTemplate = False
    
    fileNew4.ApplicationName = "ModelTemplate"
    
    fileNew4.Units = NXOpen.Part.Units.Millimeters
    
    fileNew4.RelationType = ""
    
    fileNew4.UsesMasterModel = "No"
    
    fileNew4.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew4.TemplatePresentationName = "Model"
    
    fileNew4.ItemType = ""
    
    fileNew4.Specialization = ""
    
    fileNew4.SetCanCreateAltrep(False)
    
    fileNew4.NewFileName = "C:\\Users\\tuanat\\Desktop\\test\\test\\model1.prt"
    
    fileNew4.MasterFileName = ""
    
    fileNew4.MakeDisplayedPart = True
    
    fileNew4.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    try:
        # File already exists
        nXObject4 = fileNew4.Commit()
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1020004)
        
    theSession.UndoToMarkWithStatus(markId16, None)
    
    theSession.DeleteUndoMark(markId16, None)
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New")
    
    theSession.DeleteUndoMark(markId17, None)
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New")
    
    fileNew4.TemplateFileName = "model-plain-1-mm-template.prt"
    
    fileNew4.UseBlankTemplate = False
    
    fileNew4.ApplicationName = "ModelTemplate"
    
    fileNew4.Units = NXOpen.Part.Units.Millimeters
    
    fileNew4.RelationType = ""
    
    fileNew4.UsesMasterModel = "No"
    
    fileNew4.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew4.TemplatePresentationName = "Model"
    
    fileNew4.ItemType = ""
    
    fileNew4.Specialization = ""
    
    fileNew4.SetCanCreateAltrep(False)
    
    fileNew4.NewFileName = "C:\\Users\\tuanat\\Desktop\\test\\cake\\model1.prt"
    
    fileNew4.MasterFileName = ""
    
    fileNew4.MakeDisplayedPart = True
    
    fileNew4.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    try:
        # File already exists
        nXObject5 = fileNew4.Commit()
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1020004)
        
    theSession.UndoToMarkWithStatus(markId18, None)
    
    theSession.DeleteUndoMark(markId18, None)
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New")
    
    theSession.DeleteUndoMark(markId19, None)
    
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New")
    
    fileNew4.TemplateFileName = "model-plain-1-mm-template.prt"
    
    fileNew4.UseBlankTemplate = False
    
    fileNew4.ApplicationName = "ModelTemplate"
    
    fileNew4.Units = NXOpen.Part.Units.Millimeters
    
    fileNew4.RelationType = ""
    
    fileNew4.UsesMasterModel = "No"
    
    fileNew4.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew4.TemplatePresentationName = "Model"
    
    fileNew4.ItemType = ""
    
    fileNew4.Specialization = ""
    
    fileNew4.SetCanCreateAltrep(False)
    
    fileNew4.NewFileName = "C:\\Users\\tuanat\\Desktop\\test\\cake\\cake.prt"
    
    fileNew4.MasterFileName = ""
    
    fileNew4.MakeDisplayedPart = True
    
    fileNew4.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    baseTemplateManager5 = theSession.XYPlotManager.TemplateManager
    
    nXObject6 = fileNew4.Commit()
    
    workPart = theSession.Parts.Work # cake
    displayPart = theSession.Parts.Display # cake
    theSession.DeleteUndoMark(markId20, None)
    
    fileNew4.Destroy()
    
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    # ----------------------------------------------
    #   Menu: File->Save
    # ----------------------------------------------
    partSaveStatus1 = workPart.Save(NXOpen.BasePart.SaveComponents.TrueValue, NXOpen.BasePart.CloseAfterSave.FalseValue)
    
    partSaveStatus1.Dispose()
    # ----------------------------------------------
    #   Menu: Tools->Journal->Play...
    # ----------------------------------------------
    part13 = theSession.Parts.Work
    
    part14 = theSession.Parts.Display
    
    part15 = theSession.Parts.Work
    
    part16 = theSession.Parts.Display
    
    part17 = theSession.Parts.Work
    
    part18 = theSession.Parts.Display
    
    blockFeatureBuilder1 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    
    originPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    blockFeatureBuilder1.SetOriginAndLengths(originPoint1, "100", "100", "300")
    
    feature1 = blockFeatureBuilder1.CommitFeature()
    
    scaleAboutPoint1 = NXOpen.Point3d(-92.137806489825039, -3.2632139798479658, 0.0)
    viewCenter1 = NXOpen.Point3d(92.137806489825039, 3.2632139798479658, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(-115.65214252108242, -4.0790174748099561, 0.0)
    viewCenter2 = NXOpen.Point3d(115.65214252108242, 4.0790174748099561, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint2, viewCenter2)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete1 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects2 = [NXOpen.TaggedObject.Null] * 1 
    block1 = feature1
    objects2[0] = block1
    nErrs2 = theSession.UpdateManager.AddObjectsToDeleteList(objects2)
    
    notifyOnDelete2 = theSession.Preferences.Modeling.NotifyOnDelete
    
    nErrs3 = theSession.UpdateManager.DoUpdate(markId22)
    
    theSession.DeleteUndoMark(markId21, None)
    
    part19 = theSession.Parts.Work
    
    part20 = theSession.Parts.Display
    
    blockFeatureBuilder2 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    
    originPoint2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    blockFeatureBuilder2.SetOriginAndLengths(originPoint2, "100", "100", "300")
    
    feature2 = blockFeatureBuilder2.CommitFeature()
    
    theSession.ApplicationSwitchImmediate("UG_APP_SFEM")
    
    fileNew5 = theSession.Parts.FileNew()
    
    fileNew5.TemplateFileName = "FemNxNastranMetric.fem"
    
    fileNew5.UseBlankTemplate = False
    
    fileNew5.ApplicationName = "CaeFemTemplate"
    
    fileNew5.Units = NXOpen.Part.Units.Millimeters
    
    fileNew5.RelationType = ""
    
    fileNew5.UsesMasterModel = "No"
    
    fileNew5.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew5.TemplatePresentationName = "NX Nastran"
    
    fileNew5.ItemType = ""
    
    fileNew5.Specialization = ""
    
    fileNew5.SetCanCreateAltrep(False)
    
    fileNew5.NewFileName = "model1_fem11_test.fem"
    
    fileNew5.MasterFileName = ""
    
    fileNew5.MakeDisplayedPart = True
    
    fileNew5.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    baseTemplateManager6 = theSession.XYPlotManager.TemplateManager
    
    baseTemplateManager7 = theSession.XYPlotManager.TemplateManager
    
    nXObject7 = fileNew5.Commit()
    
    workPart = NXOpen.Part.Null
    workFemPart = theSession.Parts.BaseWork # model1_fem11_test
    displayPart = NXOpen.Part.Null
    displayFemPart = theSession.Parts.BaseDisplay # model1_fem11_test
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Pre/Post")
    
    scaleAboutPoint3 = NXOpen.Point3d(-66.46978159252096, 21.071606020309485, 0.0)
    viewCenter3 = NXOpen.Point3d(66.46978159252096, -21.071606020309407, 0.0)
    workFemPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint3, viewCenter3)
    
    scaleAboutPoint4 = NXOpen.Point3d(-83.087226990651175, 26.33950752538685, 0.0)
    viewCenter4 = NXOpen.Point3d(83.087226990651217, -26.33950752538675, 0.0)
    workFemPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint4, viewCenter4)
    
    scaleAboutPoint5 = NXOpen.Point3d(-101.18225451825428, 30.782961030685797, 0.0)
    viewCenter5 = NXOpen.Point3d(101.18225451825434, -30.782961030685797, 0.0)
    workFemPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint5, viewCenter5)
    
    scaleAboutPoint6 = NXOpen.Point3d(-126.47781814781783, 38.47870128835725, 0.0)
    viewCenter6 = NXOpen.Point3d(126.47781814781791, -38.47870128835725, 0.0)
    workFemPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint6, viewCenter6)
    
    scaleAboutPoint7 = NXOpen.Point3d(-158.09727268477229, 48.098376610446564, 0.0)
    viewCenter7 = NXOpen.Point3d(158.09727268477235, -48.098376610446564, 0.0)
    workFemPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint7, viewCenter7)
    
    scaleAboutPoint8 = NXOpen.Point3d(-197.62159085596537, 60.122970763058206, 0.0)
    viewCenter8 = NXOpen.Point3d(197.62159085596537, -60.122970763058206, 0.0)
    workFemPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint8, viewCenter8)
    
    scaleAboutPoint9 = NXOpen.Point3d(-247.02698856995673, 77.767755660912442, 0.0)
    viewCenter9 = NXOpen.Point3d(247.02698856995673, -77.767755660912741, 0.0)
    workFemPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint9, viewCenter9)
    
    scaleAboutPoint10 = NXOpen.Point3d(-197.62159085596537, 63.259821411565724, 0.0)
    viewCenter10 = NXOpen.Point3d(197.62159085596537, -63.259821411565724, 0.0)
    workFemPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint10, viewCenter10)
    
    scaleAboutPoint11 = NXOpen.Point3d(-158.09727268477226, 50.607857129252572, 0.0)
    viewCenter11 = NXOpen.Point3d(158.09727268477238, -50.607857129252572, 0.0)
    workFemPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint11, viewCenter11)
    
    scaleAboutPoint12 = NXOpen.Point3d(-127.81620775784768, 41.824675313431833, 0.0)
    viewCenter12 = NXOpen.Point3d(127.81620775784776, -41.824675313431833, 0.0)
    workFemPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint12, viewCenter12)
    
    scaleAboutPoint13 = NXOpen.Point3d(-103.32367789430201, 34.530451938769282, 0.0)
    viewCenter13 = NXOpen.Point3d(103.32367789430201, -34.530451938769282, 0.0)
    workFemPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint13, viewCenter13)
    
    scaleAboutPoint14 = NXOpen.Point3d(-83.087226990651217, 28.05264622622505, 0.0)
    viewCenter14 = NXOpen.Point3d(83.087226990651118, -28.05264622622505, 0.0)
    workFemPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint14, viewCenter14)
    
    scaleAboutPoint15 = NXOpen.Point3d(-86.342190522243669, -13.533795736621565, 0.0)
    viewCenter15 = NXOpen.Point3d(86.342190522243669, 13.533795736621565, 0.0)
    workFemPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint15, viewCenter15)
    
    scaleAboutPoint16 = NXOpen.Point3d(-107.92773815280459, -16.917244670776956, 0.0)
    viewCenter16 = NXOpen.Point3d(107.92773815280459, 16.917244670776956, 0.0)
    workFemPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint16, viewCenter16)
    
    scaleAboutPoint17 = NXOpen.Point3d(-134.90967269100574, -21.146555838471194, 0.0)
    viewCenter17 = NXOpen.Point3d(134.90967269100574, 21.146555838471194, 0.0)
    workFemPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint17, viewCenter17)
    
    scaleAboutPoint18 = NXOpen.Point3d(-107.92773815280459, -16.917244670776956, 0.0)
    viewCenter18 = NXOpen.Point3d(107.92773815280459, 16.917244670776956, 0.0)
    workFemPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint18, viewCenter18)
    
    femPart13 = workFemPart
    femPart13.Close(NXOpen.BasePart.CloseWholeTree.FalseValue, NXOpen.BasePart.CloseModified.UseResponses, None)
    
    workFemPart = NXOpen.BasePart.Null
    displayFemPart = NXOpen.BasePart.Null
    theSession.ApplicationSwitchImmediate("UG_APP_NOPART")
    
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Change Displayed Part")
    
    status2, partLoadStatus2 = theSession.Parts.SetActiveDisplay(part20, NXOpen.DisplayPartOption.AllowAdditional, NXOpen.PartDisplayPartWorkPartOption.UseLast)
    
    workPart = theSession.Parts.Work # cake
    displayPart = theSession.Parts.Display # cake
    partLoadStatus2.Dispose()
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Play...
    # ----------------------------------------------
    part21 = theSession.Parts.Work
    
    part22 = theSession.Parts.Display
    
    theSession.ApplicationSwitchImmediate("UG_APP_SFEM")
    
    fileNew6 = theSession.Parts.FileNew()
    
    fileNew6.TemplateFileName = "FemNxNastranMetric.fem"
    
    fileNew6.UseBlankTemplate = False
    
    fileNew6.ApplicationName = "CaeFemTemplate"
    
    fileNew6.Units = NXOpen.Part.Units.Millimeters
    
    fileNew6.RelationType = ""
    
    fileNew6.UsesMasterModel = "No"
    
    fileNew6.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew6.TemplatePresentationName = "NX Nastran"
    
    fileNew6.ItemType = ""
    
    fileNew6.Specialization = ""
    
    fileNew6.SetCanCreateAltrep(False)
    
    fileNew6.NewFileName = "C:\\Users\\tuanat\\Desktop\\test\\model1_fem11.fem"
    
    fileNew6.MasterFileName = ""
    
    fileNew6.MakeDisplayedPart = True
    
    fileNew6.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    baseTemplateManager8 = theSession.XYPlotManager.TemplateManager
    
    baseTemplateManager9 = theSession.XYPlotManager.TemplateManager
    
    nXObject8 = fileNew6.Commit()
    
    workPart = NXOpen.Part.Null
    workFemPart = theSession.Parts.BaseWork # model1_fem11
    displayPart = NXOpen.Part.Null
    displayFemPart = theSession.Parts.BaseDisplay # model1_fem11
    basePart8 = theSession.Parts.BaseWork
    
    basePart9 = theSession.Parts.BaseDisplay
    
    femPart14 = workFemPart
    femPart14.PolygonGeometryMgr.SetPolygonBodyResolutionOnFemBodies(NXOpen.CAE.PolygonGeometryManager.PolygonBodyResolutionType.Standard)
    
    femPart15 = workFemPart
    femCreationOptions3 = femPart15.NewFemCreationOptions()
    
    femPart16 = workFemPart
    femSynchronizeOptions3 = femPart16.NewFemSynchronizeOptions()
    
    femSynchronizeOptions3.SynchronizePointsFlag = False
    
    femSynchronizeOptions3.SynchronizeCoordinateSystemFlag = False
    
    femSynchronizeOptions3.SynchronizeLinesFlag = False
    
    femSynchronizeOptions3.SynchronizeArcsFlag = False
    
    femSynchronizeOptions3.SynchronizeSplinesFlag = False
    
    femSynchronizeOptions3.SynchronizeConicsFlag = False
    
    femSynchronizeOptions3.SynchronizeSketchCurvesFlag = False
    
    basePart10 = theSession.Parts.FindObject("model1")
    
    part23 = basePart10
    femCreationOptions3.SetCadData(part23, "C:\\Users\\tuanat\\Desktop\\test\\model1.prt")
    
    body3 = part23.Bodies.FindObject("BLOCK(4)")
    
    bodies3 = [NXOpen.Body.Null] * 1 
    bodies3[0] = body3
    femCreationOptions3.SetGeometryOptions(NXOpen.CAE.FemCreationOptions.UseBodiesOption.VisibleBodies, bodies3, femSynchronizeOptions3)
    
    femCreationOptions3.SetSolverOptions("NX NASTRAN", "Structural", NXOpen.CAE.BaseFemPart.AxisymAbstractionType.NotSet)
    
    description3 = []
    femCreationOptions3.SetDescription(description3)
    
    femCreationOptions3.SetMorphingFlag(False)
    
    femCreationOptions3.SetCyclicSymmetryData(False, NXOpen.CoordinateSystem.Null)
    
    femPart17 = workFemPart
    femPart17.FinalizeCreation(femCreationOptions3)
    
    femSynchronizeOptions3.Dispose()
    femCreationOptions3.Dispose()
    fileNew6.Destroy()
    
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Pre/Post")
    
    femPart18 = workFemPart
    femPart18.Close(NXOpen.BasePart.CloseWholeTree.FalseValue, NXOpen.BasePart.CloseModified.UseResponses, None)
    
    workFemPart = NXOpen.BasePart.Null
    displayFemPart = NXOpen.BasePart.Null
    theSession.ApplicationSwitchImmediate("UG_APP_NOPART")
    
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Change Displayed Part")
    
    status3, partLoadStatus3 = theSession.Parts.SetActiveDisplay(part22, NXOpen.DisplayPartOption.AllowAdditional, NXOpen.PartDisplayPartWorkPartOption.UseLast)
    
    workPart = theSession.Parts.Work # cake
    displayPart = theSession.Parts.Display # cake
    partLoadStatus3.Dispose()
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    # ----------------------------------------------
    #   Menu: File->Save
    # ----------------------------------------------
    partSaveStatus2 = workPart.Save(NXOpen.BasePart.SaveComponents.TrueValue, NXOpen.BasePart.CloseAfterSave.FalseValue)
    
    partSaveStatus2.Dispose()
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete3 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects3 = [NXOpen.TaggedObject.Null] * 1 
    block2 = feature2
    objects3[0] = block2
    nErrs4 = theSession.UpdateManager.AddObjectsToDeleteList(objects3)
    
    notifyOnDelete4 = theSession.Preferences.Modeling.NotifyOnDelete
    
    nErrs5 = theSession.UpdateManager.DoUpdate(markId28)
    
    theSession.DeleteUndoMark(markId27, None)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Play...
    # ----------------------------------------------
    part24 = theSession.Parts.Work
    
    part25 = theSession.Parts.Display
    
    blockFeatureBuilder3 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    
    originPoint3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    blockFeatureBuilder3.SetOriginAndLengths(originPoint3, "100", "100", "300")
    
    feature3 = blockFeatureBuilder3.CommitFeature()
    
    theSession.ApplicationSwitchImmediate("UG_APP_SFEM")
    
    fileNew7 = theSession.Parts.FileNew()
    
    fileNew7.TemplateFileName = "FemNxNastranMetric.fem"
    
    fileNew7.UseBlankTemplate = False
    
    fileNew7.ApplicationName = "CaeFemTemplate"
    
    fileNew7.Units = NXOpen.Part.Units.Millimeters
    
    fileNew7.RelationType = ""
    
    fileNew7.UsesMasterModel = "No"
    
    fileNew7.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew7.TemplatePresentationName = "NX Nastran"
    
    fileNew7.ItemType = ""
    
    fileNew7.Specialization = ""
    
    fileNew7.SetCanCreateAltrep(False)
    
    fileNew7.NewFileName = "model1_fem11_test.fem"
    
    fileNew7.MasterFileName = ""
    
    fileNew7.MakeDisplayedPart = True
    
    fileNew7.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    baseTemplateManager10 = theSession.XYPlotManager.TemplateManager
    
    baseTemplateManager11 = theSession.XYPlotManager.TemplateManager
    
    nXObject9 = fileNew7.Commit()
    
    workPart = NXOpen.Part.Null
    workFemPart = theSession.Parts.BaseWork # model1_fem11_test
    displayPart = NXOpen.Part.Null
    displayFemPart = theSession.Parts.BaseDisplay # model1_fem11_test
    markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Pre/Post")
    
    femPart19 = workFemPart
    femPart19.Close(NXOpen.BasePart.CloseWholeTree.FalseValue, NXOpen.BasePart.CloseModified.UseResponses, None)
    
    workFemPart = NXOpen.BasePart.Null
    displayFemPart = NXOpen.BasePart.Null
    theSession.ApplicationSwitchImmediate("UG_APP_NOPART")
    
    markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Change Displayed Part")
    
    status4, partLoadStatus4 = theSession.Parts.SetActiveDisplay(part25, NXOpen.DisplayPartOption.AllowAdditional, NXOpen.PartDisplayPartWorkPartOption.UseLast)
    
    workPart = theSession.Parts.Work # cake
    displayPart = theSession.Parts.Display # cake
    partLoadStatus4.Dispose()
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Play...
    # ----------------------------------------------
    part26 = theSession.Parts.Work
    
    part27 = theSession.Parts.Display
    
    blockFeatureBuilder4 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    
    originPoint4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    blockFeatureBuilder4.SetOriginAndLengths(originPoint4, "100", "100", "300")
    
    feature4 = blockFeatureBuilder4.CommitFeature()
    
    theSession.ApplicationSwitchImmediate("UG_APP_SFEM")
    
    fileNew8 = theSession.Parts.FileNew()
    
    fileNew8.TemplateFileName = "FemNxNastranMetric.fem"
    
    fileNew8.UseBlankTemplate = False
    
    fileNew8.ApplicationName = "CaeFemTemplate"
    
    fileNew8.Units = NXOpen.Part.Units.Millimeters
    
    fileNew8.RelationType = ""
    
    fileNew8.UsesMasterModel = "No"
    
    fileNew8.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew8.TemplatePresentationName = "NX Nastran"
    
    fileNew8.ItemType = ""
    
    fileNew8.Specialization = ""
    
    fileNew8.SetCanCreateAltrep(False)
    
    fileNew8.NewFileName = "model1_fem11_test.fem"
    
    fileNew8.MasterFileName = ""
    
    fileNew8.MakeDisplayedPart = True
    
    fileNew8.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    baseTemplateManager12 = theSession.XYPlotManager.TemplateManager
    
    baseTemplateManager13 = theSession.XYPlotManager.TemplateManager
    
    nXObject10 = fileNew8.Commit()
    
    workPart = NXOpen.Part.Null
    workFemPart = theSession.Parts.BaseWork # model1_fem11_test
    displayPart = NXOpen.Part.Null
    displayFemPart = theSession.Parts.BaseDisplay # model1_fem11_test
    markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Pre/Post")
    
    femPart20 = workFemPart
    femPart20.Close(NXOpen.BasePart.CloseWholeTree.FalseValue, NXOpen.BasePart.CloseModified.UseResponses, None)
    
    workFemPart = NXOpen.BasePart.Null
    displayFemPart = NXOpen.BasePart.Null
    theSession.ApplicationSwitchImmediate("UG_APP_NOPART")
    
    markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Change Displayed Part")
    
    status5, partLoadStatus5 = theSession.Parts.SetActiveDisplay(part27, NXOpen.DisplayPartOption.AllowAdditional, NXOpen.PartDisplayPartWorkPartOption.UseLast)
    
    workPart = theSession.Parts.Work # cake
    displayPart = theSession.Parts.Display # cake
    partLoadStatus5.Dispose()
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete5 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects4 = [NXOpen.TaggedObject.Null] * 1 
    block3 = feature4
    objects4[0] = block3
    nErrs6 = theSession.UpdateManager.AddObjectsToDeleteList(objects4)
    
    notifyOnDelete6 = theSession.Preferences.Modeling.NotifyOnDelete
    
    nErrs7 = theSession.UpdateManager.DoUpdate(markId34)
    
    theSession.DeleteUndoMark(markId33, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete7 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects5 = [NXOpen.TaggedObject.Null] * 1 
    block4 = feature3
    objects5[0] = block4
    nErrs8 = theSession.UpdateManager.AddObjectsToDeleteList(objects5)
    
    notifyOnDelete8 = theSession.Preferences.Modeling.NotifyOnDelete
    
    nErrs9 = theSession.UpdateManager.DoUpdate(markId36)
    
    theSession.DeleteUndoMark(markId35, None)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Play...
    # ----------------------------------------------
    part28 = theSession.Parts.Work
    
    part29 = theSession.Parts.Display
    
    blockFeatureBuilder5 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    
    originPoint5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    blockFeatureBuilder5.SetOriginAndLengths(originPoint5, "100", "100", "300")
    
    feature5 = blockFeatureBuilder5.CommitFeature()
    
    theSession.ApplicationSwitchImmediate("UG_APP_SFEM")
    
    fileNew9 = theSession.Parts.FileNew()
    
    fileNew9.TemplateFileName = "FemNxNastranMetric.fem"
    
    fileNew9.UseBlankTemplate = False
    
    fileNew9.ApplicationName = "CaeFemTemplate"
    
    fileNew9.Units = NXOpen.Part.Units.Millimeters
    
    fileNew9.RelationType = ""
    
    fileNew9.UsesMasterModel = "No"
    
    fileNew9.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew9.TemplatePresentationName = "NX Nastran"
    
    fileNew9.ItemType = ""
    
    fileNew9.Specialization = ""
    
    fileNew9.SetCanCreateAltrep(False)
    
    fileNew9.NewFileName = "cake.fem"
    
    fileNew9.MasterFileName = ""
    
    fileNew9.MakeDisplayedPart = True
    
    fileNew9.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    baseTemplateManager14 = theSession.XYPlotManager.TemplateManager
    
    try:
        # A part file with the same base name already exists.
        nXObject11 = fileNew9.Commit()
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(3815011)
        
    markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Pre/Post")
    
    # ----------------------------------------------
    #   Menu: Application->Design->Modeling
    # ----------------------------------------------
    markId38 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Modeling")
    
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId39 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete9 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId40 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects6 = [NXOpen.TaggedObject.Null] * 1 
    block5 = feature5
    objects6[0] = block5
    nErrs10 = theSession.UpdateManager.AddObjectsToDeleteList(objects6)
    
    notifyOnDelete10 = theSession.Preferences.Modeling.NotifyOnDelete
    
    nErrs11 = theSession.UpdateManager.DoUpdate(markId40)
    
    theSession.DeleteUndoMark(markId39, None)
    
    part30 = theSession.Parts.Work
    
    part31 = theSession.Parts.Display
    
    blockFeatureBuilder6 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    
    originPoint6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    blockFeatureBuilder6.SetOriginAndLengths(originPoint6, "100", "100", "300")
    
    feature6 = blockFeatureBuilder6.CommitFeature()
    
    theSession.ApplicationSwitchImmediate("UG_APP_SFEM")
    
    fileNew10 = theSession.Parts.FileNew()
    
    fileNew10.TemplateFileName = "FemNxNastranMetric.fem"
    
    fileNew10.UseBlankTemplate = False
    
    fileNew10.ApplicationName = "CaeFemTemplate"
    
    fileNew10.Units = NXOpen.Part.Units.Millimeters
    
    fileNew10.RelationType = ""
    
    fileNew10.UsesMasterModel = "No"
    
    fileNew10.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew10.TemplatePresentationName = "NX Nastran"
    
    fileNew10.ItemType = ""
    
    fileNew10.Specialization = ""
    
    fileNew10.SetCanCreateAltrep(False)
    
    fileNew10.NewFileName = "model1_fem11.fem"
    
    fileNew10.MasterFileName = ""
    
    fileNew10.MakeDisplayedPart = True
    
    fileNew10.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    baseTemplateManager15 = theSession.XYPlotManager.TemplateManager
    
    baseTemplateManager16 = theSession.XYPlotManager.TemplateManager
    
    nXObject12 = fileNew10.Commit()
    
    workPart = NXOpen.Part.Null
    workFemPart = theSession.Parts.BaseWork # model1_fem11
    displayPart = NXOpen.Part.Null
    displayFemPart = theSession.Parts.BaseDisplay # model1_fem11
    basePart11 = theSession.Parts.BaseWork
    
    markId41 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Pre/Post")
    
    femPart21 = workFemPart
    femPart21.Close(NXOpen.BasePart.CloseWholeTree.FalseValue, NXOpen.BasePart.CloseModified.UseResponses, None)
    
    workFemPart = NXOpen.BasePart.Null
    displayFemPart = NXOpen.BasePart.Null
    theSession.ApplicationSwitchImmediate("UG_APP_NOPART")
    
    markId42 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Change Displayed Part")
    
    status6, partLoadStatus6 = theSession.Parts.SetActiveDisplay(part31, NXOpen.DisplayPartOption.AllowAdditional, NXOpen.PartDisplayPartWorkPartOption.UseLast)
    
    workPart = theSession.Parts.Work # cake
    displayPart = theSession.Parts.Display # cake
    partLoadStatus6.Dispose()
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId43 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete11 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId44 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects7 = [NXOpen.TaggedObject.Null] * 1 
    block6 = feature6
    objects7[0] = block6
    nErrs12 = theSession.UpdateManager.AddObjectsToDeleteList(objects7)
    
    notifyOnDelete12 = theSession.Preferences.Modeling.NotifyOnDelete
    
    nErrs13 = theSession.UpdateManager.DoUpdate(markId44)
    
    theSession.DeleteUndoMark(markId43, None)
    
    # ----------------------------------------------
    #   Menu: Application->Design->Modeling
    # ----------------------------------------------
    markId45 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Modeling")
    
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()