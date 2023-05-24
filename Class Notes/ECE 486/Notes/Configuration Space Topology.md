---
type: Academic
tags:
alias: ECE-486-CSpaceTopology
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
friends: "[[Robot Configuration]]"
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Overview
The Topology of a C-Space is relevant to it's [[Representation of Configuration Space|Representation]], as an example think of how a Euclidean plane expands forever, while the surface of a sphere wraps around. Because of this it is important in general to analyse the topology of a given C-Space in the process of designing a Robot. It is important to note that joint limits are often ignored when talking about the topology of a given C-Space.