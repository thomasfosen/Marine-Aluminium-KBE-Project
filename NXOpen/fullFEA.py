import math
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities

class NX_parser(object):
    """docstring for NX_parser."""

    def __init__(self):
        self.theSession  = NXOpen.Session.GetSession()
        self.workPart = self.theSession.Parts.Work
        self.displayPart = self.theSession.Parts.Display
        self.path = "C:\\Users\\tuanat\\Desktop\\test\\"

    def create_block(self, coords, dims):

        blockFeatureBuilder1 = self.workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
        coordinates1 = NXOpen.Point3d(float(coords[0]), float(coords[1]), float(coords[2]))
        blockFeatureBuilder1.SetOriginAndLengths(coordinates1, str(dims[0]), str(dims[1]), str(dims[2]))
        feature1 = blockFeatureBuilder1.CommitFeature()

    def go_to_prepost(self):
        self.theSession.ApplicationSwitchImmediate("UG_APP_SFEM")

    def go_to_modeling(self):
        self.theSession.ApplicationSwitchImmediate("UG_APP_MODELING")

    def create_FEM_part(self, filename):
        fileNew1 = self.theSession.Parts.FileNew()
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

        baseTemplateManager2 = self.theSession.XYPlotManager.TemplateManager

        nXObject1 = fileNew1.Commit()

        workPart = NXOpen.Part.Null
        workFemPart = self.theSession.Parts.BaseWork
        displayPart = NXOpen.Part.Null
        displayFemPart = self.theSession.Parts.BaseDisplay

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
        body1 = part1.Bodies.FindObject("BLOCK(11)")
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

def main() :
    iz = NX_parser()
    iz.create_block([0,0,0],[100,100,300])

    iz.go_to_prepost()
    iz.create_FEM_part('cake')

if __name__ == '__main__':
    main()
