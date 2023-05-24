---
type: Academic
tags:
alias: ECE-486-planarm
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
The following would be a derivation of the DOF of a planar rigid body with no constraints put on it's configurations. 

### Proof
Consider an arbitrary two dimensional rigid object. Now consider a single point on this object called $\large{A}$ , $\large{A}$  will need two-coordinates for it's position on the plane to be specified $\large{(x_A,y_A)}$. Now   consider a second point on this object $\large{B}$, $\large{B}$ must lie some distance away from $\large{A}$, this means our choice of $\large{B}$ is restricted by the property $\large{d(A,B) = d_{AB}}$, or in other words $\large{B}$  must lie somewhere on a circle centered around $\large{A}$  with a radius $\large{d_{AB}}$. This means that we now only need one co-ordinate to specify $\large{B}$ 's location, the angle from the x-axis: $\large{\phi_{AB}}$. Considering an arbitrary third point $\large{C}$ we can see that the position of $\large{C}$  must now adhere to the constraints:   $\large{d(C,B) = d_{CB}}$  and  $\large{d(C,A) = d_{CA}}$, or in other words $\large{C}$ must lie on the intersection of a circle centered at $\large{A}$ with radius $\large{d_{AC}}$ and a circle centered at $\large{B}$ with radius $\large{d_{BC}}$, since such an intersection can only result in a discrete number of possible locations we can conclude that no new coordinates will be needed to specify the locations of any other points in the object. Hence, we can conclude that the DOF of a planar rigid body is $\Large{m = 3}$. 