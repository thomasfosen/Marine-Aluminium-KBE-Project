# NX 12.0.2.9
# Journal created by tuanat on Thu Feb 20 13:05:10 2020 W. Europe Standard Time
#
import math
def main() :

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display

    blockFeatureBuilder1 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    blockFeatureBuilder1.BooleanOption.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create

    targetBodies1 = [NXOpen.Body.Null] * 1
    targetBodies1[0] = NXOpen.Body.Null
    blockFeatureBuilder1.BooleanOption.SetTargetBodies(targetBodies1)

    coordinates1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point1 = workPart.Points.CreatePoint(coordinates1)

    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)

    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Block")

    theSession.DeleteUndoMark(markId2, None)

    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Block")

    blockFeatureBuilder1.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths

    blockFeatureBuilder1.OriginPoint = point1

    originPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    blockFeatureBuilder1.SetOriginAndLengths(originPoint1, "100", "100", "100")

    blockFeatureBuilder1.SetBooleanOperationAndTarget(NXOpen.Features.Feature.BooleanType.Create, NXOpen.Body.Null)

    feature1 = blockFeatureBuilder1.CommitFeature()

    theSession.DeleteUndoMark(markId3, None)

    theSession.SetUndoMarkName(markId1, "Block")

    blockFeatureBuilder1.Destroy()

    workPart.Expressions.Delete(expression1)
