# Marine-Aluminium-KBE-Project

## Introduction
This page is the culmination of work conducted under the KBE project course taught by Andrei Lobov. The report is written in iterative processes, updating new information as new goals and requirements are added. The work presented in this part involves the automated generation of a gusset node based on varying load parameters formulated by customer demands and engineer interpretation. The system architecture uses knowledge-based engineering (KBE) to capture engineering intent through parameterization to quickly automate generation of new product models based on customer and engineering demands.

The gusset nodes are intended for use in Marine Aluminium's helidecks, and should be automatically provided by the system based on input parameters such as directional forces and torques. The provided solution should adhere to standards involving structural integrity while remaining as cost-effective as possible. An example of such a node can be observed in figure 1.

<p align="center">
<img src="https://github.com/thomasfosen/Marine-Aluminium-KBE-Project/blob/master/figures/Duralok-6.png" width="600"><br>
Figure 1: Example node <a href="https://www.scafom-rux.com/products/scaffolding/duralok">[Source]</a>
</p>

High level primitives (HLP) can be what the customer sees

## Method
### Architecture



Our attention was directed towards having a functional loop. Instead of having a complex geometry we decided to start the simulation with a simple sphere(dfa template) with 6 surfaces. Although these steps are not in the loop, they are all made into functions and could be automated as well.

<p align="center">
<img src="https://github.com/thomasfosen/Marine-Aluminium-KBE-Project/blob/master/figures/system_loop.PNG" width="600"><br>
Figure 2: System loop achitecture
</p>



We use websockets for the NX server to listen and communicate with the web server. When the customer has inputted the force and torque the node, with default diameter, goes through FEA generating a result which either meets the requirements and results in finished geometry, or gets sent back to the loop for further iteration in order to get a optimal geometry. As with the assignment of constraints, forces and torques, the geometry optimization is a simplified solution in that it is just a reduction of the sphere's diameter.

When the results don't match up with the requirements, the loop sends us back to the part in NX, and then to modelling, where the Knowledge Fusion child rule is refreshed and the diameter is reduced with 10mm. The next part of the loop is to go to fem and update the mesh geometry and solve the simulation with the new geometry. Then the result are checked. If requirements are met the finished geometry is sent to the web server. If the requirements are not met the iteration continues.

<p align="center">
<img src="https://github.com/thomasfosen/Marine-Aluminium-KBE-Project/blob/master/figures/system_architecture.PNG" width="900"><br>
Figure 3: System loop achitecture
</p>



### NX Server

To set up the NX server, we decided to use python websockets module. This module is however not commonly available in the default NX python 3.6 library. To overcome this, we had to manually locate and edit the library. For us, the library was located at C:\Program Files\Siemens\NX 12.0\NXBIN\python as a Python36.zip file. The websocket module, among other modules were added for experimentation. The edited version of the zip can be found [here](https://drive.google.com/open?id=1WgCf_HSY4ERatKjxpM7Fh7ePXeKPpVZC).

To run the server from NX, the following code was added to the server script:
```python
import asyncio
import websockets

async def response(websocket, path):
    message = await websocket.recv()

if __name__ == '__main__':
  start_server = websockets.serve(response, 'localhost', 1234)
  asyncio.get_event_loop().run_until_complete(start_server)
  asyncio.get_event_loop().run_forever()
```

Different NX functions could then be called depending on what kind of message was received. To send messages to the server, a separate script with the following code was added to the client side:

```python
import asyncio
import websockets

async def message():
	async with websockets.connect("ws://localhost:1234") as socket:
		await socket.send('refresh')


asyncio.get_event_loop().run_until_complete(message())

```

### Gusset node
Initial focus was directed towards system functionality and expandability, instead of the complexity of the node. Therefore, a simplistic shape was selected for the node this time. This allowed us to develop a system to generate the geometry while keeping track of relevant faces and bodies. Because of this functionality, changes to the node should be automatically incorporated by the system, allowing for changes and more complex nodes to be developed.


### Meshing
The mesh type chosen for this demonstration was TET10 for the simple reason that it's the most easy and flexible mesh yet capable to apply. A method for determining an appropriate mesh size was not developed. Instead a very simple algorithm based on the size of the node was used. The "lightning bolt" automatic mesh size function in NX was not available in the journal files.  

### Simulation environment
The geometry is simplified by using a sphere with six surfaces. To keep things simple, the load cases for the node was reduced to only one force and one torque acting on the node. We put a fixed constraint on the bottom surface, a vertical surface is exposed to a force and the top surface is exposed to a torque.

### Result extraction
To extract the results, the "result measures" function in NX was used. This function was available through the NXOpen class "ResultMeasures" and allowed max values of any kind to be accessed through python code. Initially, the plan was to use either the OP2, or other result files to read through simulation results. However, after much digging it was suspected that NX is applying a form of post-processing in order to convert stress into for example von mises and max principal stresses, which would make sense.


### Optimization/Results


The following is a visualization of the optimization process. The loop has been initiated with a given value from the customer/engineer, and is now iterating through analyses, as can be seen in figure 3.
<p align="center">
<img src="https://github.com/thomasfosen/Marine-Aluminium-KBE-Project/blob/master/figures/Recording-2.gif" width="600"><br>
Figure 3: Optimizer loop architecture
</p>

The final result is given as shown in figure 4, showing the final stress and diameter of the node.


<p align="center">
<img src="https://github.com/thomasfosen/Marine-Aluminium-KBE-Project/blob/master/figures/optimize.png" width="600"><br>
Figure 4: Optimizer loop results
</p>

## Discussion
The main requirements for the system to be functional are met, although there is room for improvement in most components. The main focus in our system is the optimization loop, which means the node model and the user interface are simplified designs. These components in particular could, and should, be further improved.  

As mentioned before, the geometry changes being made are reductions of the sphere diameter by 10mm. This constant reduction could possibly be time inefficient. To make it more time efficient we could look at the difference between the resulted stress and the yield strength, and also how much impact the 10mm reduction has on the resulted stress, and calculate a more accurate reduction of the diameter. A more complex solution could be to use topology optimization combined with artificial neural networks(ANN) or a genetic algorithm(GA).

Furthermore, it's important to note that the simulation environment for the node is very unrealistic. With our simplifications, the diameter of the entire node is reduced in each iteration. This also affects the diameter, thus, surface area of the beam connections. Because the force and torque objects are constrained to these surfaces, the main factor affecting the stress values is the surface area of the beam connection. In reality, the geometry of the truss beams would probably remain constant.

## Conclusion

The system is considered functional with regard to the problem statement, although there are many improvements to be made. As mentioned earlier, the main effort has been to design a fully functioning optimization loop, as this was regarded as the main objective of the project, thus affecting the effort put into design and minor components.
