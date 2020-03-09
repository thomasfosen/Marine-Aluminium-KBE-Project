# NX 12.0.2.9
# Journal created by tuanat on Mon Mar  9 10:01:05 2020 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.Assemblies
import NXOpen.CAE
import NXOpen.Fields
def main() :

    theSession  = NXOpen.Session.GetSession()
    workSimPart = theSession.Parts.BaseWork

    simSimulation1 = workSimPart.Simulation

    simLoad1 = simSimulation1.Loads.FindObject("Load[Force(1)]")
    simBCBuilder1 = simSimulation1.CreateBcBuilderForBc(simLoad1)

    propertyTable1 = simBCBuilder1.PropertyTable
    setManager1 = simBCBuilder1.TargetSetManager
    simBCBuilder1.BcName = "Force(1)"
    simBCBuilder1.BcLabel = 1

    setManager2 = propertyTable1.GetSetManagerPropertyValue("DirectionNode1")
    setManager3 = propertyTable1.GetSetManagerPropertyValue("DirectionNode2")
    setManager4 = propertyTable1.GetSetManagerPropertyValue("DirectionNode3")
    setManager5 = propertyTable1.GetSetManagerPropertyValue("DirectionNode4")

    objects1 = [None] * 1
    objects1[0] = NXOpen.CAE.SetObject()
    component1 = workSimPart.ComponentAssembly.RootComponent.FindObject("COMPONENT model1_fem1 1")
    cAEFace1 = component1.FindObject("PROTO#CAE_Body(78)|CAE_Face(774)")
    objects1[0].Obj = cAEFace1
    objects1[0].SubType = NXOpen.CAE.CaeSetObjectSubType.NotSet
    objects1[0].SubId = 0
    setManager1.SetTargetSetMembers(0, NXOpen.CAE.CaeSetGroupFilterType.GeomFace, objects1)

    scalarFieldWrapper1 = propertyTable1.GetScalarFieldWrapperPropertyValue("TotalForce")

    expression1 = scalarFieldWrapper1.GetExpression()

    unit1 = workSimPart.UnitCollection.FindObject("Newton")
    workSimPart.Expressions.EditWithUnits(expression1, unit1, "800000")

    scalarFieldWrapper1.SetExpression(expression1)

    propertyTable1.SetScalarFieldWrapperPropertyValue("TotalForce", scalarFieldWrapper1)

    setManager6 = propertyTable1.GetSetManagerPropertyValue("DirectionNode1")
    setManager7 = propertyTable1.GetSetManagerPropertyValue("DirectionNode2")
    setManager8 = propertyTable1.GetSetManagerPropertyValue("DirectionNode3")
    setManager9 = propertyTable1.GetSetManagerPropertyValue("DirectionNode4")

    propertyTable1.SetTablePropertyWithoutValue("DistributionField")
    propertyTable1.SetScalarFieldWrapperPropertyValue("DistributionField", NXOpen.Fields.ScalarFieldWrapper.Null)

    propertyValue1 = []
    propertyTable1.SetTextPropertyValue("description", propertyValue1)
    simBC1 = simBCBuilder1.CommitAddBc()
    simBCBuilder1.Destroy()


    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------

if __name__ == '__main__':
    main()
