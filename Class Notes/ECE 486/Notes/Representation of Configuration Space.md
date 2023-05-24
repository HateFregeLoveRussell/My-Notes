---
type: Academic
tags:
alias: ECE-486-CSpaceRep
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
friends: ["[[Configuration Space Topology]]", "[[Robot Configuration]]"]
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Overview
The representation of a C-Space is the parametrization used to represent a point in that space. Representations in general involve a choice by the designer and are not determined by the C-Space's [[Configuration Space Topology|Topology]]. The properties of a chosen representation however is effected by the Topology of the C-Space it parametrizes. 

There are two ways to represent a robot's C-Space, the first is known as [[Implicit Representations of Configuration Spaces|Implicit Representations]] while the other is known as [[Explicit Representations of Configuration Spaces|Explicit Representations]]. Due to the many challenges associated with Explicit representations we will use Implicit representations only in this class.