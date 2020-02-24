# NX 12.0.2.9
# Journal created by tuanat on Thu Feb 20 14:15:59 2020 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities

def block(coords, dims):
    workPart = NXOpen.Session.GetSession().Parts.Work

    blockFeatureBuilder1 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    coordinates1 = NXOpen.Point3d(float(coords[0]), float(coords[1]), float(coords[2]))
    blockFeatureBuilder1.SetOriginAndLengths(coordinates1, str(dims[0]), str(dims[1]), str(dims[2]))
    feature1 = blockFeatureBuilder1.CommitFeature()

def main() :
    block([0,0,0],[100,100,300])

if __name__ == '__main__':
    main()
