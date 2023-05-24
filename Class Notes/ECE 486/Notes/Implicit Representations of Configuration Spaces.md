---
type: Academic
tags:
alias: ECE-486-ImplicitReps
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
child: "[[Representation of Configuration Space]]"
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Overview
An Implicit Representation of a space is a parametrization which views the space as embedded in a higher dimensional Euclidean space subject to some constraints. As an example an implicit parametrization of the surface of a unit sphere would be $\large{(x,y,z)}$ subject to $\large{x^2 + y ^ 2+ z^2 = 1}$. An obvious disadvantage of this approach is the increased number of co-ordinates, but an advantage would be the absence of singularities. 