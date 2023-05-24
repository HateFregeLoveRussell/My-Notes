---
type: Academic
tags: [Dict, RepoNote]
alias: ECE-486-CompDict
class: {
  class-name: "Robot Dynamics And Control",
  instructor: "Brandon J. DeHart",
  medium: "In-Person",
  start-date: "2023-05-08",
  university: "University of Waterloo",
  class-alias: "ECE-486",
  template: {
    name: "class-uni-obj",
    version: 1
  }
}
relationship: {name: standard-relationship-obj, version: 1}
child: "[[ECE 486 Dictionary]]"
status: {state: In Progress, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-dict-temnplate, version: 1}
---
## Description
The following is a list of definitions for the class ECE 486 which relates to the various physical components relevant to the field of Robotics. 

### Link

#### Description
Links are rigid bodies that connect [[ECE 486 Component Dictionary#Joints|Joints]]. Typically links are rigid.

#### Referenced In
- [[Robot Components]]

#### See Also
- [[ECE 486 Component Dictionary#Joints|Joints]]

### Joints

#### Description
A Joint is an object that connect exactly two [[ECE 486 Component Dictionary#Link|Links]] together and allows for some form of relative motion between the two links. It is important to note that in this class joints that connect more than two links together are treated as two or more separate joints which each connect two links.

#### Referenced In
- [[Robot Components]]

#### See Also
- [[ECE 486 Component Dictionary#Link|Links]]

### End Effector

#### Description
The End Effector is a type of actuator that a robot uses to manipulate the environment around it. End effectors are typically found at the end of a [[ECE 486 Component Dictionary#Link|Link]] - [[ECE 486 Component Dictionary#Joints|Joint]] chain. 

#### Referenced In
- [[Robot Components]]

#### See Also
- [[ECE 486 Component Dictionary#Link|Links]]
- [[ECE 486 Component Dictionary#Joints|Joints]]

### Soft-Bodied Robots

#### Description
A Soft bodied robot is a type of robot in which one or more [[ECE 486 Component Dictionary#Link|link]] is not rigid. The analysis of the motion of these robots are often very complicated.

#### Referenced In
- [[Robot Components]]

#### See Also
- [[ECE 486 Component Dictionary#Link|Links]]

### Open-Chain Mechanisms

#### Description
Open-Chain or Serial Mechanisms are robotic mechanisms that do not have any closed loops. An example of a open-chain mechanism would be a robotic arm.

#### Referenced In
- [[Grübler's Formula]]

#### See Also
- [[ECE 486 Component Dictionary#Closed-Chain Mechanisms|Closed-Chain Mechanisms]] 

### Closed-Chain Mechanisms

#### Description
Closed-Chain Mechanisms are robotic mechanisms that contain closed loops. An example of a closed-chain mechanism would be someone standing on the ground, the loop present goes from one leg, to the other, to the ground, and back to the first leg.

#### See Also
 - [[ECE 486 Component Dictionary#Open-Chain Mechanisms|Open-Chain Mechanisms]]
