---
type: Academic
tags:
alias: ECE-481-SDControlSystems
class: {"class-name":"Digital Control Systems","instructor":"Dr. Yash Vardhan Pant","medium":"In Person","start-date":"2023-05-08","university":"University of Waterloo","class-alias":"ECE-481","template":{"name":"class-uni-obj","version":1}}
source: {link: "[[ECE 481 Bibliography#Lecture 1]]", alias: Lec1-ECE-481, template: {name: bib-source-obj , version: 1}}
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Motivation - Why Study Discrete Time Controllers]]"
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description
A "Sampled Data Controller" or SD Controller for short is a type of control system which involves discretization of plant output in order to be controlled by a DT-Controller. Similarly, the Controller's  output is turned into a CT signal through interpolation. 

### The Typical SD Control System
The Typical SD Control System as shown in the figure below consists of a physical plant $\large P(s)$, and a Digital Controller $\large D[z]$. These two blocks are able to communicate with each other through a Digital to Analog Converter (DAC) and an Analog to Digital Converter (ADC). Typically the DAC will function through the use of [[Uniform Sampling|Uniform Sampling]] and the ADC will function through [[Zero-Order Hold Interpolation|Zero-Order Hold Interpolation]]. The signals $\large{y(t)}$ and $\large{y[k]}$ represent the CT and DT versions of of the Plant output respectively. $\large{u(t)}$ denotes the plant input. $\large{d(t)}$ is the disturbance signal the system experiences. $\large{e[k]}$ represents the "Tracking Error" of the system. And $\large{r[k]}$ represents the "reference signal" or input of the system, in essence, what output we desire.
![[Typical SD System Figure|700]]
It should go without saying that  $\Large{t\in\Bbb{R}}$  and $\Large{k\in\Bbb{Z}_{\ge0}}$ and that all signals save $\large{r[k]}$ and $\large{d(t)}$ are endogenous and dependent while the others are exogenous and independent. 

### Advantages 
This configuration essentially allows us to control a physical, continuous-time plant, with a digital, discrete-time controller.

### Disadvantages
Due to the challenges of realizing any DAC or ADC block all SD Systems will necessarily have to be time-varying. Additionally, this facet of the system will create additional challenges in maintaining the Linearity of a system through it's transformation to a SD-controlled system. Hardware improvements in practice however mitigate these limitations.
