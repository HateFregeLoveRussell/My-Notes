---
type: Academic
tags:
alias: ECE-486-TypesOfJoints
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
source: {link: "[[ECE 486 Textbook Chapter 2 Bibliography#Textbook Chapter 2.2]]", alias: tbch2s2-ECE-486, template: {name: bib-source-obj , version: 1}}
relationship: {name: standard-relationship-obj, version: 1}
friends: ["[[Robot Components]]", "[[Determining the DOF of a Planar Rigid Body]]", "[[Determining the DOF of a Spatial Rigid Body]]"]
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Overview
The following is a list of the types of joints used in the analysis preformed in this class. Often the restrictions which define the DOF of a link is imparted by the joint preceding it, so the information presented here will prove especially useful in DOF calculations. 

### Reference Figure
![[Types of Joints.png]]
### Joints
#### Revolute (R) Joint
The Revolute or Hinge joint allows for rotational motion about it's joint axis. So it imparts 2 restrictions and 1 freedom in two-dimensional space and 5 restrictions and 1 freedom in three-dimensional space. DOF =1

#### Prismatic (P) Joint
The Prismatic or Sliding joint allows for translational/rectilinear motion along the direction of the joint axis. Similarly to the Revolute Joint, it provides us with 2 restrictions and 1 freedom in two-dimensional space and 5 restrictions and 1 freedom in three-dimensional space. DOF =1

#### Helical (H) Joint
The Helical or Screw joint allows for simultaneous rotation and translation about a single fixed axis. This joint gives us 5 constraints and 1 freedom in three-dimensional space. It is not realizable in two-dimensional space. DOF = 1 

#### Cylindrical (C) Joint
The Cylindrical joint allows independent translation and rotation about the joint axis. It provides us with 4 constraints and 2 freedoms in three-dimensional space. It is not realisable in two-dimensional space. DOF = 2

#### Universal (U) Joint
The Universal joint consists of two Revolute joints aligned orthogonally, it allows for two independent axis of rotation. It provides us with 4 constraints and 2 freedoms in three-dimensional space and is not realizable in two-dimensional space. DOF = 2

### Spherical (S) Joint
The Spherical or Ball and Socket Joint gives us 3 constraints in three-dimensional space. It is not realizable in two-dimensional space. DOF = 3