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
* Put a figure of the full architecture
* Put a figure of the optimizer loop architecture
### Gusset node
Initial focus was directed towards system functionality and expandability, instead of the complexity of the node. Therefore, a simplistic shape was selected for the node this time. This allowed us to develop a system to generate the geometry while keeping track of relevant faces and bodies. Because of this functionality, changes to the node should be automatically incorporated by the system, allowing for changes and more complex nodes to be developed.

### Meshing
The mesh type chosen for this demonstration was TET10 for the simple reason that it's the most easy and flexible mesh yet capable to apply. A method for determining an appropriate mesh size was not developed. Instead a very simple algorithm based on the size of the node was used. The "lightning bolt" automatic mesh size function in NX was not available in the journal files.  

### Simulation environment
To keep things simple, the load cases for the node was reduced to only one force and one torque acting on a single beam similarly to what can be seen in figure 1.

### Result extraction
To extract the results, the "result measures" function in NX was used. This function was available through the NXOpen class "ResultMeasures" and allowed max values of any kind to be accessed through python code. Initially, the plan was to use either the OP2, or other result files to read through simulation results. However, after much digging it was suspected that NX is applying a form of post-processing in order to convert stress into for example von mises and max principal stresssed, which makes sense.
