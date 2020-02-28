import math
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.CAE

#just a simplified wrapper for "normal" use
class NX_wrapper():
    def __init__(self):
        #session and workparts should be redefined in each function
        #this is because the state changes, which doesn't get updated within the objects.
        self.theSession  = NXOpen.Session.GetSession()
        #self.workPart = self.theSession.Parts.Work
        #self.displayPart = self.theSession.Parts.Display
        self.workSimPart = self.theSession.Parts.BaseWork
        self.workFemPart = self.workSimPart
        #UNITS
        self.unit_translation = self.workSimPart.UnitCollection.FindObject("MilliMeter")
        self.unit_rotation = self.workSimPart.UnitCollection.FindObject("Degrees")
        #SHOULD WORK IF A PROPER DIRECTORY PATH IS SPECIFIED
        #All nx open files are ran from program files/Siemens/NX12/UGII/ apparently
        #Should be the same as the part file name
        self.filename = 'cake'

        #IMPORTANT: Specify path to directory
        self.path = 'C:/Users/tuanat/Desktop/test/cake/'

        self.body_objects = []

    def create_block(self, coords, dims):
        theSession  = NXOpen.Session.GetSession()
        try:
            workPart = theSession.Parts.Work

        #just a check to see if parts can be created in FEM mode. It's possible, but they need to be loaded into the correct environment
        except Exception as e:
            workPart = theSession.Parts.BaseWork


        blockFeatureBuilder1 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
        coordinates1 = NXOpen.Point3d(float(coords[0]), float(coords[1]), float(coords[2]))
        blockFeatureBuilder1.SetOriginAndLengths(coordinates1, str(dims[0]), str(dims[1]), str(dims[2]))
        feature1 = blockFeatureBuilder1.CommitFeature()

    def go_to_prepost(self):
        self.theSession.ApplicationSwitchImmediate("UG_APP_SFEM")

    def go_to_modeling(self):
        self.theSession.ApplicationSwitchImmediate("UG_APP_MODELING")

    def create_FEM_part(self):
        theSession  = NXOpen.Session.GetSession()
        workPart = self.theSession.Parts.Work
        displayPart = self.theSession.Parts.Display

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
        fileNew1.NewFileName = self.path + self.filename + "_fem.fem"
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

        part1 = theSession.Parts.FindObject(self.filename)
        femCreationOptions1.SetCadData(part1, self.filename + ".prt")

        bodies1 = [NXOpen.Body.Null] * 1
        #should be replaced by a function to find all relevant bodies?
        #objects = workPart.Layers.GetAllObjectsOnLayer(1)
        body1 = part1.Bodies.FindObject("BLOCK(2)")
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

    def create_collector(self, name):
        theSession  = NXOpen.Session.GetSession()
        workFemPart = theSession.Parts.BaseWork
        displayFemPart = theSession.Parts.BaseDisplay

        fEModel1 = workFemPart.FindObject("FEModel")
        meshManager1 = fEModel1.Find("MeshManager")
        meshCollectorBuilder1 = meshManager1.CreateCollectorBuilder(NXOpen.CAE.MeshCollector.Null, "Solid")
        meshCollectorBuilder1.CollectorName = name
        nXObject1 = meshCollectorBuilder1.Commit()
        meshCollectorBuilder1.Destroy()

    def apply_swept_mesh(self, body, face):
        theSession  = NXOpen.Session.GetSession()
        workFemPart = theSession.Parts.BaseWork

        fEModel1 = workFemPart.FindObject("FEModel")
        meshManager1 = fEModel1.Find("MeshManager")

        mesh3dHexBuilder1 = meshManager1.CreateMesh3dHexBuilder(NXOpen.CAE.SweptMesh.Null)
        mesh3dHexBuilder1.ElementType.DestinationCollector.ElementContainer = NXOpen.CAE.MeshCollector.Null
        mesh3dHexBuilder1.ElementType.ElementTypeName = "CHEXA(20)"

        unit_tran = workFemPart.UnitCollection.FindObject("MilliMeter")
        mesh3dHexBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("source element size", "31.6", unit_tran)

        mesh3dHexBuilder1.CreationType = NXOpen.CAE.Mesh3dHexBuilder.Type.Automatic

        objects1 = [NXOpen.DisplayableObject.Null] * 1

        #Should be replaced by get all solid body objects / faces function
        cAEBody1 = workFemPart.FindObject("CAE_Body(" + str(body) + ")")
        cAEFace1 = cAEBody1.FindObject("CAE_Face(" + str(face) + ")")
        objects1[0] = cAEFace1
        added1 = mesh3dHexBuilder1.SourceFaceList.Add(objects1)

        mesh3dHexBuilder1.ElementType.ElementDimension = NXOpen.CAE.ElementTypeBuilder.ElementType.SweepSolid

        destinationCollectorBuilder1 = mesh3dHexBuilder1.ElementType.DestinationCollector
        destinationCollectorBuilder1.ElementContainer = NXOpen.CAE.MeshCollector.Null
        destinationCollectorBuilder1.AutomaticMode = True


        meshes1 = mesh3dHexBuilder1.CommitMesh()


    def apply_tet_mesh(self, body, mesh_size, collector = 'Solid(1)'):
        theSession  = NXOpen.Session.GetSession()
        workFemPart = theSession.Parts.BaseWork
        displayFemPart = theSession.Parts.BaseDisplay

        fEModel1 = workFemPart.FindObject("FEModel")
        meshManager1 = fEModel1.Find("MeshManager")
        mesh3dTetBuilder1 = meshManager1.CreateMesh3dTetBuilder(NXOpen.CAE.Mesh3d.Null)

        meshCollector1 = meshManager1.FindObject("MeshCollector[" + collector + "]")
        mesh3dTetBuilder1.ElementType.DestinationCollector.ElementContainer = meshCollector1

        mesh3dTetBuilder1.ElementType.ElementTypeName = "CTETRA(10)"

        unit1 = workFemPart.UnitCollection.FindObject("MilliMeter")

        cAEBody1 = workFemPart.FindObject("CAE_Body(" + str(body) + ")")
        added1 = mesh3dTetBuilder1.SelectionList.Add(cAEBody1)

        mesh3dTetBuilder1.ElementType.DestinationCollector.AutomaticMode = False
        mesh3dTetBuilder1.AutoResetOption = False
        mesh3dTetBuilder1.ElementType.ElementDimension = NXOpen.CAE.ElementTypeBuilder.ElementType.FreeSolid
        mesh3dTetBuilder1.ElementType.ElementTypeName = "CTETRA(10)"
        destinationCollectorBuilder1 = mesh3dTetBuilder1.ElementType.DestinationCollector
        destinationCollectorBuilder1.ElementContainer = meshCollector1
        destinationCollectorBuilder1.AutomaticMode = False

        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("quad mesh overall edge size", str(float(mesh_size)), unit1)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("small feature value", "4.83", NXOpen.Unit.Null)
        mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("mapped mesh option bool", True)
        mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("multiblock cylinder option bool", False)
        mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("fillet num elements", 3)
        mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("num elements on cylinder circumference", 6)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("element size on cylinder height", "1", unit1)
        mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("create pyramids bool", False)
        mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("midnodes", 0)
        mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("geometry tolerance option bool", False)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("geometry tolerance", "0", unit1)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("max jacobian", "10", NXOpen.Unit.Null)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("surface mesh size variation", "50", NXOpen.Unit.Null)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("volume mesh size variation", "50", NXOpen.Unit.Null)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("internal mesh gradation", "1.05", NXOpen.Unit.Null)
        mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("internal max edge option bool", False)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("internal max edge length value", "0", unit1)
        mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("two elements through thickness bool", False)
        mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("mesh transition bool", False)
        mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("remesh on bad quality bool", False)
        mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("maximum edge length bool", False)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("maximum edge length", "1", unit1)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("small feature tolerance", "10", NXOpen.Unit.Null)
        mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("boundary layer element type", 3)
        mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("insert blend elements", True)

        unit2 = workFemPart.UnitCollection.FindObject("Degrees")
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("blending angle", "90", unit2)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("sweep angle", "45", unit2)
        mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("control aspect ratio", False)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("maximum exposed aspect ratio", "1000", NXOpen.Unit.Null)
        mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("control slender", False)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("minimum aspect ratio", "0.01", NXOpen.Unit.Null)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("maximum imprint dihedral angle", "120", unit2)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("gradation rate", "10", NXOpen.Unit.Null)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("smoothing distance factor", "3", NXOpen.Unit.Null)
        mesh3dTetBuilder1.PropertyTable.SetBooleanPropertyValue("all-tet boundary layer", False)
        mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("dont format mesh to solver", 0)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("quad mesh edge match tolerance", "0.02", NXOpen.Unit.Null)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("quad mesh smoothness tolerance", "0.01", unit1)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("min face angle", "20", unit2)
        mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("mesh time stamp", 0)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("quad mesh node coincidence tolerance", "0.0001", unit1)
        mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("mesh edit allowed", 0)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("edge angle", "15", unit2)
        mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("merge edge toggle", 0)
        mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("auto constraining", 1)
        mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("curvature scaling", 1)
        mesh3dTetBuilder1.PropertyTable.SetBaseScalarWithDataPropertyValue("target angle", "45", unit2)
        mesh3dTetBuilder1.PropertyTable.SetIntegerPropertyValue("edge shape", 2)


        meshes1 = mesh3dTetBuilder1.CommitMesh()

        mesh3dTetBuilder1.Destroy()

    def assign_material(self, collector):
        #these sadly should be reassigned within the class functions. The reason being that "states" are obtained.
        #So if they're assigned early on, they will only save the state before FEM models and such have been generated
        theSession  = NXOpen.Session.GetSession()
        workFemPart = theSession.Parts.BaseWork

        fEModel1 = workFemPart.FindObject("FEModel")
        meshManager1 = fEModel1.Find("MeshManager")
        meshCollector1 = meshManager1.FindObject("MeshCollector[" + collector + "]")
        meshCollectorBuilder1 = meshManager1.CreateCollectorBuilder(meshCollector1, "Solid")



        physicalMaterialListBuilder1 = self.workFemPart.MaterialManager.PhysicalMaterials.CreateListBlockBuilder()
        physicalMaterial1 = self.workFemPart.MaterialManager.PhysicalMaterials.LoadFromNxmatmllibrary("Aluminum_6061")
        physicalMaterialListBuilder1.Destroy()
        physicalPropertyTable1 = workFemPart.PhysicalPropertyTables.FindObject("PhysPropTable[PSOLID1]")
        propertyTable1 = physicalPropertyTable1.PropertyTable
        propertyTable1.SetMaterialPropertyValue("material", False, physicalMaterial1)
        meshCollectorBuilder1.PropertyTable.SetNamedPropertyTablePropertyValue("Solid Property", physicalPropertyTable1)
        nXObject1 = meshCollectorBuilder1.Commit()

    def assign_material2(self, collector):
        theSession  = NXOpen.Session.GetSession()
        workFemPart = theSession.Parts.BaseWork
        displayFemPart = theSession.Parts.BaseDisplay

        fEModel1 = workFemPart.FindObject("FEModel")
        meshManager1 = fEModel1.Find("MeshManager")
        meshCollector1 = meshManager1.FindObject("MeshCollector[" + collector + "]")
        meshCollectorBuilder1 = meshManager1.CreateCollectorBuilder(meshCollector1, "Solid")

        caePart1 = workFemPart
        physicalPropertyTable1 = caePart1.PhysicalPropertyTables.CreatePhysicalPropertyTable("PSOLID", "NX NASTRAN - Structural", "NX NASTRAN", "PSOLID1", 1)
        propertyTable1 = physicalPropertyTable1.PropertyTable

        physicalMaterialListBuilder1 = workFemPart.MaterialManager.PhysicalMaterials.CreateListBlockBuilder()
        physicalMaterial1 = workFemPart.MaterialManager.PhysicalMaterials.LoadFromNxmatmllibrary("Aluminum_6061")
        physicalMaterialListBuilder1.Destroy()

        propertyTable1.SetMaterialPropertyValue("material", False, physicalMaterial1)
        meshCollectorBuilder1.PropertyTable.SetNamedPropertyTablePropertyValue("Solid Property", physicalPropertyTable1)

        nXObject1 = meshCollectorBuilder1.Commit()
        meshCollectorBuilder1.Destroy()


    def create_SIM_part(self):
        filename = self.filename

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

        fileNew1.NewFileName = self.path + self.filename + "_fem_sim1.sim"
        fileNew1.MasterFileName = ""
        fileNew1.MakeDisplayedPart = True
        fileNew1.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional


        baseTemplateManager1 = theSession.XYPlotManager.TemplateManager
        nXObject1 = fileNew1.Commit()
        workSimPart = theSession.Parts.BaseWork
        displaySimPart = theSession.Parts.BaseDisplay


        simPart1 = workSimPart
        femPart1 = theSession.Parts.FindObject(filename + '_fem')
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


    def apply_force(self, force, body, face, direction):
        theSession  = NXOpen.Session.GetSession()
        workSimPart = theSession.Parts.BaseWork
        simSimulation1 = workSimPart.Simulation

        simBCBuilder2 = simSimulation1.CreateBcBuilderForLoadDescriptor("magnitudeDirectionForce", "Force(1)", 1)

        propertyTable2 = simBCBuilder2.PropertyTable

        setManager2 = simBCBuilder2.TargetSetManager

        objects2 = [None] * 1
        objects2[0] = NXOpen.CAE.SetObject()
        component1 = workSimPart.ComponentAssembly.RootComponent.FindObject("COMPONENT " + self.filename + "_fem 1")

        #Can be used with the find all objects function
        #In theory, more faces could be added at once? For us it's probably easier to loop though this function though
        cAEFace2 = component1.FindObject("PROTO#CAE_Body(" + str(body) + ")|CAE_Face(" + str(face) + ")")
        objects2[0].Obj = cAEFace2
        objects2[0].SubType = NXOpen.CAE.CaeSetObjectSubType.NotSet
        objects2[0].SubId = 0
        setManager2.SetTargetSetMembers(0, NXOpen.CAE.CaeSetGroupFilterType.GeomFace, objects2)

        unit_force = workSimPart.UnitCollection.FindObject("Newton")
        expression2 = workSimPart.Expressions.CreateSystemExpressionWithUnits(str(force), unit_force)

        fieldManager1 = workSimPart.FindObject("FieldManager")
        scalarFieldWrapper1 = fieldManager1.CreateScalarFieldWrapperWithExpression(expression2)
        scalarFieldWrapper2 = propertyTable2.GetScalarFieldWrapperPropertyValue("TotalForce")
        scalarFieldWrapper3 = fieldManager1.CreateScalarFieldWrapperWithExpression(expression2)


        origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)
        vector1 = NXOpen.Vector3d(float(direction[0]), float(direction[1]), float(direction[2]))
        direction1 = workSimPart.Directions.CreateDirection(origin1, vector1, NXOpen.SmartObject.UpdateOption.AfterModeling)

        #success1 = direction1.ReverseDirection()

        propertyTable2.SetScalarFieldWrapperPropertyValue("TotalForce", scalarFieldWrapper3)
        propertyTable2.SetVectorPropertyValue("Local Axis", direction1)

        simBC2 = simBCBuilder2.CommitAddBc()

    #only fully fixed. check apply_constraint.py for full code
    def apply_constraint(self,body, face):
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
        component1 = workSimPart.ComponentAssembly.RootComponent.FindObject("COMPONENT " + self.filename + "_fem 1")
        cAEFace1 = component1.FindObject("PROTO#CAE_Body(" + str(body) + ")|CAE_Face(" + str(face) + ")")
        objects1[0].Obj = cAEFace1
        objects1[0].SubType = NXOpen.CAE.CaeSetObjectSubType.NotSet
        objects1[0].SubId = 0
        setManager1.SetTargetSetMembers(0, NXOpen.CAE.CaeSetGroupFilterType.GeomFace, objects1)

        #translational motion constraint
        unit_tran = workSimPart.UnitCollection.FindObject("MilliMeter")
        indepVarArray = []
        fieldExpression1 = propertyTable1.GetScalarFieldPropertyValue("DOF1")
        fieldExpression1.EditFieldExpression("0", unit_tran, indepVarArray, False)
        propertyTable1.SetScalarFieldPropertyValue("DOF1", fieldExpression1)
        propertyTable1.SetScalarFieldPropertyValue("DOF2", fieldExpression1)
        propertyTable1.SetScalarFieldPropertyValue("DOF3", fieldExpression1)

        #rotational motion constraint
        unit_deg = workSimPart.UnitCollection.FindObject("Degrees")
        fieldExpression4 = propertyTable1.GetScalarFieldPropertyValue("DOF4")
        fieldExpression4.EditFieldExpression("0", unit_deg, indepVarArray, False)
        propertyTable1.SetScalarFieldPropertyValue("DOF4", fieldExpression4)
        propertyTable1.SetScalarFieldPropertyValue("DOF5", fieldExpression4)
        propertyTable1.SetScalarFieldPropertyValue("DOF6", fieldExpression4)

        simBC1 = simBCBuilder1.CommitAddBc()

    def solve(self):
        theSession  = NXOpen.Session.GetSession()
        workSimPart = theSession.Parts.BaseWork
        displaySimPart = theSession.Parts.BaseDisplay

        theSimSolveManager = NXOpen.CAE.SimSolveManager.GetSimSolveManager(theSession)

        simSimulation1 = workSimPart.FindObject("Simulation")
        simSolution1 = simSimulation1.FindObject("Solution[Solution 1]")
        psolutions1 = [NXOpen.CAE.SimSolution.Null] * 1
        psolutions1[0] = simSolution1
        numsolutionssolved1, numsolutionsfailed1, numsolutionsskipped1 = theSimSolveManager.SolveChainOfSolutions(psolutions1, NXOpen.CAE.SimSolution.SolveOption.Solve, NXOpen.CAE.SimSolution.SetupCheckOption.CompleteCheckAndOutputErrors, NXOpen.CAE.SimSolution.SolveMode.Background)

    def refresh_KF_rule(self):
        theSession  = NXOpen.Session.GetSession()
        workPart = theSession.Parts.BaseWork
        workPart.RuleManager.Reload(True)
        workPart.RuleManager.RegenerateAll()

    def update_fem_geometry(self):
        theSession  = NXOpen.Session.GetSession()
        workFemPart = theSession.Parts.BaseWork

        fEModel1 = workFemPart.FindObject("FEModel")
        fEModel1.UpdateFemodel()

    def jump_to_prt(self):
        theSession  = NXOpen.Session.GetSession()
        workFemPart = theSession.Parts.BaseWork
        displayFemPart = theSession.Parts.BaseDisplay
        part1 = theSession.Parts.FindObject(self.filename)
        status1, partLoadStatus1 = theSession.Parts.SetDisplay(part1, False, False)

        workFemPart = NXOpen.BasePart.Null
        workPart = theSession.Parts.Work
        displayFemPart = NXOpen.BasePart.Null
        displayPart = theSession.Parts.Display
        theSession.Parts.SetWork(workPart)

    def jump_to_fem(self):
        theSession  = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work
        displayPart = theSession.Parts.Display
        femPart1 = theSession.Parts.FindObject(self.filename + "_fem")
        status1, partLoadStatus1 = theSession.Parts.SetDisplay(femPart1, False, False)

        workPart = NXOpen.Part.Null
        workFemPart = theSession.Parts.BaseWork
        displayPart = NXOpen.Part.Null
        displayFemPart = theSession.Parts.BaseDisplay
        femPart2 = workFemPart
        theSession.Parts.SetWork(femPart2)
    #these only work in the modeling environment

    def jump_to_sim(self):
        theSession  = NXOpen.Session.GetSession()
        workFemPart = theSession.Parts.BaseWork
        displayFemPart = theSession.Parts.BaseDisplay

        simPart1 = theSession.Parts.FindObject(self.filename + "_fem_sim1")
        status1, partLoadStatus1 = theSession.Parts.SetActiveDisplay(simPart1, NXOpen.DisplayPartOption.AllowAdditional, NXOpen.PartDisplayPartWorkPartOption.SameAsDisplay)

        workSimPart = theSession.Parts.BaseWork
        displaySimPart = theSession.Parts.BaseDisplay
        partLoadStatus1.Dispose()
    def get_solid_bodies(self):
        pass
    def find_solid_bodies(self):
        theSession  = NXOpen.Session.GetSession()
        theNxMessageBox = NXOpen.UI.GetUI().NXMessageBox
        try:
            workPart = theSession.Parts.Work

        #just a check to see if parts can be created in FEM mode. It's possible, but they need to be loaded into the correct environment
        except Exception as e:
            workPart = theSession.Parts.BaseWork
            theNxMessageBox.Show("test",NXOpen.NXMessageBoxDialogType.Information, str(1))
        #object for showing dialogue boxes


        #collect all objects on a particular layer (default is 1)
        objects = workPart.Layers.GetAllObjectsOnLayer(1)

        body_counter = 0
        face_counter = 0
        #Loops through all objects
        for object in objects:
            if object.Name != "":
                theNxMessageBox.Show("test",NXOpen.NXMessageBoxDialogType.Information, object.Name)
            try:
                #attempts to check if object is a body
                if object.IsSolidBody:

                    body_counter += 1

                    #if object is a body, collect all faces
                    faces = object.GetFaces()

                    face_counter += len(faces)
                    theNxMessageBox.Show("test",NXOpen.NXMessageBoxDialogType.Information, str(object.JournalIdentifier))


            #if error is met, do nothing
            except Exception as e:
                pass

        theNxMessageBox.Show("test",NXOpen.NXMessageBoxDialogType.Information, str(len(objects)))
        theNxMessageBox.Show("test",NXOpen.NXMessageBoxDialogType.Information, str(body_counter))
        theNxMessageBox.Show("test",NXOpen.NXMessageBoxDialogType.Information, str(face_counter))

    def update_geometry(self):
        self.jump_to_prt()
        self.refresh_KF_rule()
        self.jump_to_fem()
        self.update_fem_geometry()
        self.jump_to_sim()
def main() :



    iz = NX_wrapper()
    #iz.create_block([200,200,0],[100,100,100])
    """
    mesh_collector = 'test'
    mesh_size = 20

    iz.go_to_prepost()
    iz.create_FEM_part()
    iz.create_collector(mesh_collector)
    #iz.apply_swept_mesh(1, 3)
    #iz.apply_swept_mesh(2, "(2)3")
    iz.apply_tet_mesh(1,mesh_size, mesh_collector)
    iz.apply_tet_mesh(2,mesh_size, mesh_collector)
    iz.apply_tet_mesh(3,mesh_size, mesh_collector)
    iz.apply_tet_mesh(4,mesh_size, mesh_collector)

    iz.assign_material2(mesh_collector)

    #
    #iz.apply_tet_mesh(3,mesh_size, mesh_collector)

    #iz.create_block([200,200,0],[100,100,300])
    iz.create_SIM_part()
    iz.apply_force(800000, 1, 1, [1,0,0])
    iz.apply_constraint(1, 3)

    iz.apply_force(800000, 2, 7, [1,0,0])
    iz.apply_constraint(2, 9)

    #for i in range(6):
    #    iz.apply_force(i+1, [1,1,1])
    iz.solve()"""
    mesh_collector = 'test'
    mesh_size = 20
    #iz.apply_tet_mesh(5,mesh_size, mesh_collector)
    #iz.find_solid_bodies()
    #iz.refresh_KF_rule()
    #iz.jump_to_fem()
    #iz.update_geometry()
    #iz.apply_force(800000, 5, 2, [1,0,0])
    #iz.apply_constraint(5, 1)
    #iz.solve()
    #iz.apply_tet_mesh(15,mesh_size, mesh_collector)
    theNxMessageBox = NXOpen.UI.GetUI().NXMessageBox
    #theNxMessageBox.Show("test",NXOpen.NXMessageBoxDialogType.Information, str(NXOpen.CAE.ResultComponent.MaximumShear))
    theNxMessageBox.Show("test",NXOpen.NXMessageBoxDialogType.Information, str(len(NXOpen.CAE.Result.AskElementNodes.elementIndex)))
    #for cake in NXOpen.CAE.Result.AskElementNodes:
    #    theNxMessageBox.Show("test",NXOpen.NXMessageBoxDialogType.Information, str(cake.elementIndex))
if __name__ == '__main__':
    main()
