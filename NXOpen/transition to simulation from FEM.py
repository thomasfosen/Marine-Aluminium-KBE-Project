# NX 12.0.2.9
# Journal created by tuanat on Mon Feb 24 09:33:09 2020 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.CAE
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workFemPart = theSession.Parts.BaseWork
    displayFemPart = theSession.Parts.BaseDisplay
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    fileNew1 = theSession.Parts.FileNew()
    
    theSession.SetUndoMarkName(markId1, "New Part File Dialog")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New Part File")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New Part File")
    
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
    
    fileNew1.NewFileName = "C:\\Users\\tuanat\\Desktop\\test\\model1_fem1_sim1.sim"
    
    fileNew1.MasterFileName = ""
    
    fileNew1.MakeDisplayedPart = True
    
    fileNew1.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    theSession.DeleteUndoMark(markId3, None)
    
    theSession.SetUndoMarkName(markId1, "New Part File")
    
    baseTemplateManager1 = theSession.XYPlotManager.TemplateManager
    
    nXObject1 = fileNew1.Commit()
    
    workSimPart = theSession.Parts.BaseWork
    displaySimPart = theSession.Parts.BaseDisplay
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId4, "New Simulation Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin New Simulation
    # ----------------------------------------------
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New Simulation")
    
    theSession.DeleteUndoMark(markId5, None)
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New Simulation")
    
    simPart1 = workSimPart
    femPart1 = theSession.Parts.FindObject("model1_fem1")
    description1 = []
    simPart1.FinalizeCreation(femPart1, 0, description1)
    
    theSession.DeleteUndoMark(markId6, None)
    
    fileNew1.Destroy()
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    simPart2 = workSimPart
    simSimulation1 = simPart2.Simulation
    
    simSolution1 = simSimulation1.CreateSolution("NX NASTRAN", "Structural", "SESTATIC 101 - Single Constraint", "Solution 1", NXOpen.CAE.SimSimulation.AxisymAbstractionType.NotSet)
    
    propertyTable1 = simSolution1.PropertyTable
    
    caePart1 = workSimPart
    modelingObjectPropertyTable1 = caePart1.ModelingObjectPropertyTables.CreateModelingObjectPropertyTable("Bulk Data Echo Request", "NX NASTRAN - Structural", "NX NASTRAN", "Bulk Data Echo Request1", 1)
    
    caePart2 = workSimPart
    modelingObjectPropertyTable2 = caePart2.ModelingObjectPropertyTables.CreateModelingObjectPropertyTable("Structural Output Requests", "NX NASTRAN - Structural", "NX NASTRAN", "Structural Output Requests1", 2)
    
    theSession.SetUndoMarkName(markId7, "Solution Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Solution
    # ----------------------------------------------
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Solution")
    
    theSession.DeleteUndoMark(markId8, None)
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Solution")
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    simSolution1.Rename("Solution 1", False)
    
    propertyTable2 = simSolution1.PropertyTable
    
    propertyTable2.SetNamedPropertyTablePropertyValue("Bulk Data Echo Request", modelingObjectPropertyTable1)
    
    propertyTable2.SetNamedPropertyTablePropertyValue("Output Requests", modelingObjectPropertyTable2)
    
    id1 = theSession.NewestVisibleUndoMark
    
    nErrs1 = theSession.UpdateManager.DoUpdate(id1)
    
    simSolutionStep1 = simSolution1.CreateStep(0, True, "Subcase - Static Loads 1")
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId10)
    
    theSession.DeleteUndoMark(markId10, None)
    
    theSession.DeleteUndoMark(markId9, None)
    
    theSession.SetUndoMarkName(id1, "Solution")
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()