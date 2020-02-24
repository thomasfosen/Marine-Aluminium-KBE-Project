# NX 12.0.2.9
# Journal created by tuanat on Mon Feb 24 09:34:12 2020 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.Assemblies
import NXOpen.CAE
import NXOpen.Fields
def main() :

    theSession  = NXOpen.Session.GetSession()
    workSimPart = theSession.Parts.BaseWork

    simPart1 = workSimPart
    simSimulation1 = simPart1.Simulation

    #Applying the constraint
    simBCBuilder1 = simSimulation1.CreateBcBuilderForConstraintDescriptor("fixedConstraint", "Fixed(1)", 1)
    propertyTable1 = simBCBuilder1.PropertyTable
    setManager1 = simBCBuilder1.TargetSetManager

    objects1 = [None] * 1
    objects1[0] = NXOpen.CAE.SetObject()
    component1 = workSimPart.ComponentAssembly.RootComponent.FindObject("COMPONENT model1_fem1 1")
    cAEFace1 = component1.FindObject("PROTO#CAE_Body(1)|CAE_Face(3)")
    objects1[0].Obj = cAEFace1
    objects1[0].SubType = NXOpen.CAE.CaeSetObjectSubType.NotSet
    objects1[0].SubId = 0
    setManager1.SetTargetSetMembers(0, NXOpen.CAE.CaeSetGroupFilterType.GeomFace, objects1)

    #translational motion constraint
    unit_tran = workSimPart.UnitCollection.FindObject("MilliMeter")
    indepVarArray1 = []
    fieldExpression1 = propertyTable1.GetScalarFieldPropertyValue("DOF1")
    fieldExpression1.EditFieldExpression("0", unit_tran, indepVarArray1, False)
    propertyTable1.SetScalarFieldPropertyValue("DOF1", fieldExpression1)

    indepVarArray2 = []
    fieldExpression2 = propertyTable1.GetScalarFieldPropertyValue("DOF2")
    fieldExpression2.EditFieldExpression("0", unit_tran, indepVarArray2, False)
    propertyTable1.SetScalarFieldPropertyValue("DOF2", fieldExpression2)

    indepVarArray3 = []
    fieldExpression3 = propertyTable1.GetScalarFieldPropertyValue("DOF3")
    fieldExpression3.EditFieldExpression("0", unit_tran, indepVarArray3, False)
    propertyTable1.SetScalarFieldPropertyValue("DOF3", fieldExpression3)

    #rotational motion constraint
    unit_deg = workSimPart.UnitCollection.FindObject("Degrees")
    indepVarArray4 = []
    fieldExpression4 = propertyTable1.GetScalarFieldPropertyValue("DOF4")
    fieldExpression4.EditFieldExpression("0", unit_deg, indepVarArray4, False)
    propertyTable1.SetScalarFieldPropertyValue("DOF4", fieldExpression4)

    indepVarArray5 = []
    fieldExpression5 = propertyTable1.GetScalarFieldPropertyValue("DOF5")
    fieldExpression5.EditFieldExpression("0", unit_deg, indepVarArray5, False)
    propertyTable1.SetScalarFieldPropertyValue("DOF5", fieldExpression5)

    indepVarArray6 = []
    fieldExpression6 = propertyTable1.GetScalarFieldPropertyValue("DOF6")
    fieldExpression6.EditFieldExpression("0", unit_deg, indepVarArray6, False)
    propertyTable1.SetScalarFieldPropertyValue("DOF6", fieldExpression6)

    simBC1 = simBCBuilder1.CommitAddBc()


    #Applying the force
    simBCBuilder2 = simSimulation1.CreateBcBuilderForLoadDescriptor("magnitudeDirectionForce", "Force(1)", 1)

    propertyTable2 = simBCBuilder2.PropertyTable

    setManager2 = simBCBuilder2.TargetSetManager

    objects2 = [None] * 1
    objects2[0] = NXOpen.CAE.SetObject()
    cAEFace2 = component1.FindObject("PROTO#CAE_Body(1)|CAE_Face(6)")
    objects2[0].Obj = cAEFace2
    objects2[0].SubType = NXOpen.CAE.CaeSetObjectSubType.NotSet
    objects2[0].SubId = 0
    setManager2.SetTargetSetMembers(0, NXOpen.CAE.CaeSetGroupFilterType.GeomFace, objects2)

    unit_force = workSimPart.UnitCollection.FindObject("Newton")
    expression2 = workSimPart.Expressions.CreateSystemExpressionWithUnits("1000", unit_force)

    fieldManager1 = workSimPart.FindObject("FieldManager")
    scalarFieldWrapper1 = fieldManager1.CreateScalarFieldWrapperWithExpression(expression2)
    scalarFieldWrapper2 = propertyTable2.GetScalarFieldWrapperPropertyValue("TotalForce")
    scalarFieldWrapper3 = fieldManager1.CreateScalarFieldWrapperWithExpression(expression2)


    origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    vector1 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction1 = workSimPart.Directions.CreateDirection(origin1, vector1, NXOpen.SmartObject.UpdateOption.AfterModeling)

    #success1 = direction1.ReverseDirection()

    propertyTable2.SetScalarFieldWrapperPropertyValue("TotalForce", scalarFieldWrapper3)
    propertyTable2.SetVectorPropertyValue("Local Axis", direction1)


    simBC2 = simBCBuilder2.CommitAddBc()


if __name__ == '__main__':
    main()
