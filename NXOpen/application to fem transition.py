# NX 12.0.2.9
# Journal created by tuanat on Mon Feb 24 09:24:53 2020 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.CAE
def main() :

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display

    #switching to prepost mode
    theSession.ApplicationSwitchImmediate("UG_APP_SFEM")
    #switching to modeling
    #theSession.ApplicationSwitchImmediate("UG_APP_MODELING")

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

    baseTemplateManager2 = theSession.XYPlotManager.TemplateManager

    nXObject1 = fileNew1.Commit()

    workPart = NXOpen.Part.Null
    workFemPart = theSession.Parts.BaseWork
    displayPart = NXOpen.Part.Null
    displayFemPart = theSession.Parts.BaseDisplay

    femPart1 = workFemPart
    femPart1.PolygonGeometryMgr.SetPolygonBodyResolutionOnFemBodies(NXOpen.CAE.PolygonGeometryManager.PolygonBodyResolutionType.Standard)
    femCreationOptions1 = femPart1.NewFemCreationOptions()

    femSynchronizeOptions1 = femPart1.NewFemSynchronizeOptions()
    femSynchronizeOptions1.SynchronizePointsFlag = False
    femSynchronizeOptions1.SynchronizeCoordinateSystemFlag = False
    femSynchronizeOptions1.SynchronizeLinesFlag = False
    femSynchronizeOptions1.SynchronizeArcsFlag = False
    femSynchronizeOptions1.SynchronizeSplinesFlag = False
    femSynchronizeOptions1.SynchronizeConicsFlag = False
    femSynchronizeOptions1.SynchronizeSketchCurvesFlag = False

    part1 = theSession.Parts.FindObject("model1")
    femCreationOptions1.SetCadData(part1, "C:\\Users\\tuanat\\Desktop\\test\\model1.prt")

    bodies1 = [NXOpen.Body.Null] * 1
    body1 = part1.Bodies.FindObject("BLOCK(4)")
    bodies1[0] = body1
    femCreationOptions1.SetGeometryOptions(NXOpen.CAE.FemCreationOptions.UseBodiesOption.VisibleBodies, bodies1, femSynchronizeOptions1)
    femCreationOptions1.SetSolverOptions("NX NASTRAN", "Structural", NXOpen.CAE.BaseFemPart.AxisymAbstractionType.NotSet)
    femCreationOptions1.SetDescription([])
    femCreationOptions1.SetMorphingFlag(False)
    femCreationOptions1.SetCyclicSymmetryData(False, NXOpen.CoordinateSystem.Null)

    femPart1.FinalizeCreation(femCreationOptions1)
    femSynchronizeOptions1.Dispose()
    femCreationOptions1.Dispose()
    fileNew1.Destroy()

if __name__ == '__main__':
    main()
