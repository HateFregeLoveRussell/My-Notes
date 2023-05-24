---
type: Academic
tags:
alias: ECE-486-Spatialm
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
source: {link: "[[ECE 486 Textbook Chapter 2 Bibliography#Textbook Chapter 2.1]]", alias: tbch2s1-ECE-486, template: {name: bib-source-obj , version: 1}}
relationship: {name: standard-relationship-obj, version: 1}
child: "[[Robot Degrees of Freedom]]"
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Overview
The following is a derivation of the DOF of a three-dimensional rigid body without any constraints on it's configuration.

### Proof
Consider an arbitrary rigid three-dimensional body. Now consider a point on that body called $\large{A}$, the location of this point will need to be specified using three co-ordinates $\large{(x_A,y_A,z_A)}$. Now consider a second point $\large{B}$, this point's location is constrained by it's distance to $\large{A}$: $\large{d(A,B) = d_{AB}}$. So $\large{B}$ must lie somewhere on the surface of a sphere centered at $\large{A}$ with radius $\large{d_{AB}}$ . The location of $\large{B}$ on this sphere can be specified by two co-ordinates $\large{(\alpha_B,\gamma_B)}$ representing the longitude and latitude of $\large{B}$. Now consider a third point $\large{C}$ the location of this point is now restricted by the constraints $\large{d(A,C) = d_{AC}}$ and $\large{d(B,C) = d_{BC}}$, meaning $\large{C}$ must lie somewhere in the intersection of two spheres, one centered around $\large{A}$ with radius $\large{d_{AC}}$ and another centered around $\large{B}$ with radius $\large{d_{BC}}$, since the intersection of two spheres in general is a circle, we can conclude that only one co-ordinate is needed to specify the location of $\large{C}$, $\large{\phi_C}$, corresponding to the angle of the point on said circle. Now Consider an additional point $\large{D}$, naturally, $\large{D}$ will have to lie on the intersection of three spheres, originating from $\large{A}$, $\large{B}$, and $\large{C}$ with radii $\large{d_{AD}}$, $\large{d_{BD}}$, and $\large{d_{CD}}$ respectively, such an intersection would only result in a discrete number of choices for the position of $\large{D}$, so we can conclude that no more co-ordinates are needed to specify the configuration of our object. Hence, the DOF of our object is $\large{m = 6}$. 

### Note
As a corollary it can be seen that our answer for the [[Determining the DOF of a Planar Rigid Body|DOF of a Planar Rigid Body]] can be derived by  adding 3 additional constraints to our spatial rigid body, namely $\large{(z_A=z_B=z_C=0)}$