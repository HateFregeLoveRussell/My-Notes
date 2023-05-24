---
type: Academic
tags:
alias: ECE-486-DecompTopologicalSpaces
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
source: {link: "[[ECE 486 Textbook Chapter 2 Bibliography#Textbook Chapter 2.3]]", alias: tbch2s3-ECE-486, template: {name: bib-source-obj , version: 1}}
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Configuration Space Topology]]"
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Overview
Some topological spaces can be expressed as a cartesian product of lower-dimensional topological spaces. This means that we can represent the points of a given C-Space with a union of lower-dimensional points. 


### Examples
#### Example 1:
The C-Space of a rigid body in the plane can be written as $\large{\mathbb{R}^2\times\mathcal{S}^1}$  where the first term is indicative of position on the plane and the second term represents orientation.

#### Example 2:
The C-Space of a PR-Robot arm can be written as $\large{\mathbb{R}^1\times\mathcal{S}^1}$ where the Euclidean component comes from the prismatic joint and the spherical component from the rotary joint

#### Example 3:
The C-Space of a 2R-Robot arm can be written as $\large{\mathcal{S}^1\times \mathcal{S}^1 = \mathcal{T}^2}$ since the two rotational components in series trace out a torus. In general: $\large{\mathcal{S}^1\times\mathcal{S}^1\times ... \times \mathcal{S}^1\times = \mathcal{T}^n \neq \mathcal{S}^n}$ 

#### Example 4:
The C-Space of a freely moving planar rigid body attached to a 2R arm in the third dimension can be written as: $\large{\mathbb{R}^2\times\mathcal{S}^1\times\mathcal{T}^2=\mathbb{R}^2 \times\mathcal{T}^3}$ where the first half of the right hand side was derived in example 1 and the second in example 3.

#### Example 5:
The C-Space of a freely moving spatial rigid body is represented by:  $\large{\mathbb{R}^3\times\mathcal{S}^2\times\mathcal{S}^1}$. Referring back to our [[Determining the DOF of a Spatial Rigid Body|proof]], the first term can be seen as the representation of the first point the second, the representation of the second point and the third the representation of the third point. 