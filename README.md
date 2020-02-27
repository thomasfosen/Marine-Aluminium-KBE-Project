# Marine-Aluminium-KBE-Project

## Introduction
This page is the culmination of work conducted under the KBE project course taught by Andrei Lobov. The report is written in iterative processes, updating new information as new goals and requirements are added. The work presented in this part involves the automated generation of a gusset node based on varying load parameters formulated by customer demands and engineer interpretation. The system architecture uses knowledge-based engineering (KBE) to capture engineering intent through parameterization to quickly automate generation of new product models based on customer and engineering demands.

The gusset nodes are intended for use in Marine Aluminium's helidecks, and should be automatically provided by the system based on input parameters such as directional forces and torques. The provided solution should adhere to standards involving structural integrity while remaining as cost-effective as possible.

High level primitives (HLP) can be what the customer sees

## Method
### Architecture

### Gusset node
Initial focus was directed towards system functionality and expandability, instead of the complexity of the node. Therefore, a simplistic shape was selected for the node this time. This allowed us to develop a system to generate the geometry while keeping track of relevant faces and bodies. Because of this functionality, changes to the node should be automatically incorporated by the system, allowing for changes and more complex nodes to be developed.
