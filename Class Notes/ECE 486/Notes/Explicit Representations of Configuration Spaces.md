---
type: Academic
tags:
alias: ECE-486-ExplictReps
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
An Explicit Representation of Parametrization of the space refers to a representation of a space in which $\large{n}$ co-ordinates are used to represent an $\large{n}$ dimensional space. Explicit parametrizations are often only valid within a certain range, for example, an explicit parametrization of the surface of a sphere would have co-ordinates $\large{\theta_1\in[-180^\circ,180^\circ]}$ and $\large{\theta_2\in[-90^\circ,90^\circ]}$  representing the longitude and latitude. 

### Shortcomings of Explicit Representations
Explicit parametrizations are often unsatisfactory, due to the presence of "singularities", points on the parametrization space where taking a small step in parameter-space would result in ever larger steps in the C-space(in the sphere example the singularities manifest at the poles). The presence of singularities can make velocity calculations extremely difficult. 

### Solutions to the shortcomings of Explicit Representations
One way to use a Explicit parametrization without suffering the presence of singularities, is to use multiple "co-ordinate charts", the location of singulatives is independent to the space's topology and instead relies on the choice of parametrized variables (sphere looks the same at all perspectives but still has two singularities), whenever we would approach a singularity we would switch to a co-ordinate plane where the singularity is in a different place. The co-ordinate charts that are needed to avoid any singularity in the space are called the "atlas" of the space. The downside of this approach is the laborious calculations involved in switching between charts and the increased memory requirements.