---
type: Academic
tags:
alias: ECE-481-SDDesignApproaches
class: {"class-name":"Digital Control Systems","instructor":"Dr. Yash Vardhan Pant","medium":"In Person","start-date":"2023-05-08","university":"University of Waterloo","class-alias":"ECE-481","template":{"name":"class-uni-obj","version":1}}
source: {link: "[[ECE 481 Bibliography#Lecture 1]]", alias: Lec1-ECE-481, template: {name: bib-source-obj , version: 1}}
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Sampled Data Control Systems]]"
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description
The following is a exposition of the various approaches we have to designing [[Sampled Data Control Systems|SD Control Systems]].

### Emulation
Emulation refers to an approach for designing SD Systems in which the controller is designed in Continuous-Time and then is discretized ($\large{C(s)\to D[z]}$).
MATLAB has a function used in the process of transforming CT systems to DT called "C2D"

##### Advantages of Emulation
- The Analysis of the system is straight-forward as the theoretical tools for it are identical to the ones used in Analog Control Theory.

##### Disadvantages of Emulation
- This approach puts a large amount of trust into the sampling rate of the SD system, without a high-enough sampling rate the model will become inaccurate. 

### Direct Design
Direct Design is an approach for designing SD Systems which involves discretizing the Plant ($\large{P(s)\to P[z]}$) and then designing the controller as if the system is purely a DT one. 

##### Advantages of Direct Design
- The Sampling of the Plant is part of our analysis and no assumptions about its frequency are made

##### Disadvantages of Direct Design
- The Discretized version of our Plant may not be accurate in comparison to the physical one
