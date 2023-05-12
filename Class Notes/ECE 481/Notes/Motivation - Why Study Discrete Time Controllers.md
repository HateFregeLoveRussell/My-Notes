---
type: Academic
tags:
alias: ECE-481-WhyDTSyatem
class: {"class-name":"Digital Control Systems","instructor":"Dr. Yash Vardhan Pant","medium":"In Person","start-date":"2023-05-08","university":"University of Waterloo","class-alias":"ECE-481","template":{"name":"class-uni-obj","version":1}}
source: {link: "[[ECE 481 Bibliography#Lecture 1]]", alias: Lec1-ECE-481, template: {name: bib-source-obj , version: 1}}
relationship: 
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description 
The following is an explanation of the motivations behind the study of Discrete-Time Control Systems.

### The Short Comings of Analog Controllers
When implementing Analog Controllers we often suffer from a myriad of problems that can be either eliminated or mitigated through the use of a digital control system. 
These problems can include the following. 

##### Inflexibility
Analog Control Systems are often implemented using circuitry, or some other physically elaborate component. This means that changing the controller can involve great difficulties as it often involves hardware changes.

##### Adaptivity
Creating an Adaptive Controller is very difficult with an Analog Controller this is both in a theoretical sense and in terms of components used in Analog Control. 

##### Cost
The components of Analog Controllers are often much more expensive than their digital counterparts, this has led to more sophisticated controllers using Digital Controllers.

### Conclusion
Because of the short comings listed above most Control Systems in practice are [[Sampled Data Control Systems|Sampled-Data(SD) Control Systems]].