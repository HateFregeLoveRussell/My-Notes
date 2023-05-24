---
type: Academic
tags:
alias: ECE-486-DOF
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
source: [{link: "[[ECE 486 Textbook Chapter 2 Bibliography#Textbook Chapter 2.0]]", alias: tbch2-ECE-486, template: {name: bib-source-obj , version: 1}}, {link: "[[ECE 486 Textbook Chapter 2 Bibliography#Textbook Chapter 2.1]]", alias: tbch2s1-ECE-486, template: {name: bib-source-obj , version: 1}}, {link: "[[ECE 486 Class Videos Bibliography#Video Set 1]]", alias: VidCh2-ECE-486, template: {name: bib-source-obj , version: 1}}]
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Robot Configuration]]"
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Overview
The [[ECE 486 Formal Dictionaries#Configuration and Degrees Of Freedom|Degrees of Freedom(DOF)]] of a robot refers to the smallest number of real-valued co-ordinates needed to represent it's [[Robot Configuration|Configuration]]. In other words, the DOF of a robot is the dimensionality of it's C-Space. 

### Example
As an example, the DOF of a coin facing down on a table would be 3. Two co-ordinates are needed to specify the position of the coin, and one co-ordinate is needed to specify the angle of the coin. Note that the co-ordinate specifying which face of the coin is facing away from the table does not contribute to it's DOF as such a co-ordinate is a discrete variable and co-ordinates that can contribute to something's DOF must be real-valued.