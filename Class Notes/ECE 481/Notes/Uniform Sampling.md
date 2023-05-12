---
type: Academic
tags:
alias: ECE-481-UniformSampling
class: {"class-name":"Digital Control Systems","instructor":"Dr. Yash Vardhan Pant","medium":"In Person","start-date":"2023-05-08","university":"University of Waterloo","class-alias":"ECE-481","template":{"name":"class-uni-obj","version":1}}
source: {link: "[[ECE 481 Bibliography#Lecture 1]]", alias: Lec1-ECE-481, template: {name: bib-source-obj , version: 1}}
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Sampled Data Control Systems]]"
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description
Uniform Sampling is a type of sampling(transforming a CT signal to a DT one) where the sampling period is constant, often denoted $\large{T}$. As demonstrated in the figure below the process creates a discrete sequence(or vector) from a continuous signal. 
![[Uniform Sampling Demonstration Figure.excalidraw|500]]

### Process Equation
The Process can be represented mathematically through the following equation.
$$\large{y[k] = y(kT)\space k\in\Bbb{Z_{\ge0}}}$$
