---
type: Academic
tags:
alias: ECE-481-ZeroOrderHoldInterpolation
class: {"class-name":"Digital Control Systems","instructor":"Dr. Yash Vardhan Pant","medium":"In Person","start-date":"2023-05-08","university":"University of Waterloo","class-alias":"ECE-481","template":{"name":"class-uni-obj","version":1}}
source: {link: "[[ECE 481 Bibliography#Lecture 1]]", alias: Lec1-ECE-481, template: {name: bib-source-obj , version: 1}}
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Sampled Data Control Systems]]"
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description
Zero-Order Hold Interpolation refers to a process of transferring a discrete-time signal to a continuous-time one by holding the value for the signal for the range of values between each discrete point and abruptly jumping to the next value when the next discrete point in time is reached. The process is illustrated below:
![[Zero-Order Hold Interpolation Demonstration Figure.excalidraw|500]]

### Process Equation
Mathematically, the process can be expressed as the equation:
$$\large{u(t)=u(kT)\space\forall t\in[kT,(k + 1)T)}$$
Where $\large{k\in\Bbb{Z_{\ge0}}}$ and $\large T$ is a constant representing the time between each sample