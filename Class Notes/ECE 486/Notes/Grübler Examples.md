---
type: Academic
tags:
alias: ECE-486-GrublerEx
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
source: {link: [[ECE 486 Textbook Chapter 2 Bibliography#Textbook Chapter 2.2]], alias: tbch2s2-ECE-486, template: {name: bib-source-obj , version: 1}}
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Grübler's Formula]]"
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Overview
The following are some applications of Grübler's formula to a variety of different two-dimensional example mechanisms. 

### Examples
#### Example 1: A K-Link Planar Serial Chain of Revolute Joints
##### Reference Figure
![[Grubler Example 1.png]]
##### Solution
This form of mechanism is often called a "kR robot", in this case $\large{k=4}$.
Generally speaking $\large{N = k + 1}\text{ and }\large{J=k}$
Therefore,
$$
\large
\begin{align}
DOF &= 3(N-1-J)+\sum_{i=1}^Jf_i \\
&= 3(k-k) + \sum_{i=1}^k1 \\
&= k \\
&= 4
\end{align}
$$
So an kR Robot has k degrees of freedom
#### Example 2: 
##### Reference Figure:
![[Grubler Example 2.png]]
##### Solution
From the figure above... 
$\large{N=4,\space J=5,\space m=3,\space f_i=1 \forall{i \in \{1,2,3,4,5\}}}$
$\large{DOF = 3(5-1-5) + 5 = 2}$ 

#### Example 3: Stephenson Six-bar Linkage
##### Reference Figure: 
![[Grubler Example 3.png]]
##### Solution: 
From the figure above...
$\large{N=6,\space J=7,\space m=3,\space f_i=1 \forall{i \in \{1,2,3,4,5,6,7\}}}$
$\large{DOF = 3(6-1-7) + 7 = 1}$

#### Example 4:
##### Reference Figure:
![[Grubler Example 4.png]]
##### Solution
From the figure above... 
$\large{N=6,\space J=7,\space m=3,\space f_i=1 \forall{i \in \{1,2,3,4,5,6,7\}}}$
$\large{DOF = 3(6-1-7) + 7 = 1}$

#### Example 5:
##### Reference Figure:
![[Grubler Example 5.png]]
##### Solution
Note that the non-revolute joint is a symbol for a [[Types of Joints#Prismatic (P) Joint|P-Joint]], and that the R-joint joining both arms on the right hand side is actually two separate R-joints per our definition of [[ECE 486 Component Dictionary#Joints|Joints]].
$\large{N=8,\space J=9,\space m=3}$
$$\large
\begin{align}
DOF &=m(N -1 -J) + \text{freedoms from R-Joint} + \text{freedom from P-Joint} \\ 
&= 3(8-1-9) + 8  + 1\\
&= 3
\end{align}$$

#### Example 6:
##### Reference Figure:
![[Grubler Example 6.png]]
##### Solution
From the figure... 
$\large{N=5,\space J=6,\space m=3,\space f_i=1 \forall{i \in \{1,2,3,4,5,6\}}}$
$\large{DOF = 3(5-1-6) + 6 = 0}$
However this doesn't seem to be correct. A body with $\large{DOF = 0}$ is rigid but we can tell from inspection that this body can move. By inspection we can see that the middle arm does not contribute to the dimensionality of the motion of the mechanism, so it does not provide independent constraints. Removing this arm gives us... 
$\large{N=5,\space J=4,\space m=3,\space f_i=1 \forall{i \in \{1,2,3,4\}}}$
$\large{DOF = 3(4-1-4) + 4 = 1}$
which is the correct answer. 
