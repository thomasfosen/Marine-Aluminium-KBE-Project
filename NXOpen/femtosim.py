# NX 12.0.2.9
# Journal created by tuanat on Mon Feb 24 18:40:14 2020 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.CAE
def main() :
    filename = 'dfgdfg'

    theSession  = NXOpen.Session.GetSession()
    workFemPart = theSession.Parts.BaseWork
    displayFemPart = theSession.Parts.BaseDisplay

    fileNew1 = theSession.Parts.FileNew()
    fileNew1.TemplateFileName = "SimNxNastranMetric.sim"
    fileNew1.UseBlankTemplate = False
    fileNew1.ApplicationName = "CaeSimTemplate"
    fileNew1.Units = NXOpen.Part.Units.Millimeters
    fileNew1.RelationType = ""
    fileNew1.UsesMasterModel = "No"
    fileNew1.TemplateType = NXOpen.FileNewTemplateType.Item
    fileNew1.TemplatePresentationName = "NX Nastran"
    fileNew1.ItemType = ""
    fileNew1.Specialization = ""
    fileNew1.SetCanCreateAltrep(False)

    fileNew1.NewFileName = filename + "_sim1.sim"
    fileNew1.MasterFileName = ""
    fileNew1.MakeDisplayedPart = True
    fileNew1.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional


    baseTemplateManager1 = theSession.XYPlotManager.TemplateManager
    nXObject1 = fileNew1.Commit()
    workSimPart = theSession.Parts.BaseWork
    displaySimPart = theSession.Parts.BaseDisplay


    simPart1 = workSimPart
    femPart1 = theSession.Parts.FindObject(filename)
    description1 = []
    simPart1.FinalizeCreation(femPart1, 0, description1)
    fileNew1.Destroy()
    simPart2 = workSimPart
    simSimulation1 = simPart2.Simulation
    simSolution1 = simSimulation1.CreateSolution("NX NASTRAN", "Structural", "SESTATIC 101 - Single Constraint", "Solution 1", NXOpen.CAE.SimSimulation.AxisymAbstractionType.NotSet)
    propertyTable1 = simSolution1.PropertyTable
    caePart1 = workSimPart
    modelingObjectPropertyTable1 = caePart1.ModelingObjectPropertyTables.CreateModelingObjectPropertyTable("Bulk Data Echo Request", "NX NASTRAN - Structural", "NX NASTRAN", "Bulk Data Echo Request1", 1)
    caePart2 = workSimPart
    modelingObjectPropertyTable2 = caePart2.ModelingObjectPropertyTables.CreateModelingObjectPropertyTable("Structural Output Requests", "NX NASTRAN - Structural", "NX NASTRAN", "Structural Output Requests1", 2)
    simSolution1.Rename("Solution 1", False)
    propertyTable2 = simSolution1.PropertyTable
    propertyTable2.SetNamedPropertyTablePropertyValue("Bulk Data Echo Request", modelingObjectPropertyTable1)
    propertyTable2.SetNamedPropertyTablePropertyValue("Output Requests", modelingObjectPropertyTable2)
    simSolutionStep1 = simSolution1.CreateStep(0, True, "Subcase - Static Loads 1")



if __name__ == '__main__':
    main()
