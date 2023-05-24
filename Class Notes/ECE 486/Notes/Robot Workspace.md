---
type: Academic
tags:
alias: ECE-486-WorkSpace
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
source: {link: "[[ECE 486 Textbook Chapter 2 Bibliography#Textbook Chapter 2.5]]", alias: tbch2s5-ECE-486, template: {name: bib-source-obj , version: 1}}
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Robot Configuration]]"
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Overview
The Workspace of a robot is a specification of the configurations that can be reached by the robot's [[ECE 486 Component Dictionary#End Effector|End Effector]]. It is important to note that the Work Space is generally distinct form the robot's C-Space. One point in the Work Space can be reached by more than one point in the C-Space meaning that the Work Space gives an incomplete specification of the C-Space. By definition, all points in the Work Space is reachable by at least one point in the C-Space.

Mechanisms with different C-Spaces can have the same Work Space, consider a planar 2R and 3R mechanical arm. However mechanisms with the same C-Space can have different Work Spaces. 