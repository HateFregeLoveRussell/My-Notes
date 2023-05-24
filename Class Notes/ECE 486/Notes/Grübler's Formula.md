---
type: Academic
tags:
alias: ECE-486-GrublerFormula
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
source: {link: "[[ECE 486 Textbook Chapter 2 Bibliography#Textbook Chapter 2.2]]", alias: tbch2s1-ECE-486, template: {name: bib-source-obj , version: 1}}
relationship: {name: standard-relationship-obj, version: 1}
friends: ["[[Robot Degrees of Freedom]]", "[[Types of Joints]]"]
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Overview
Joints can be viewed to be providing either freedoms or constraints to their corresponding link. Sometimes the [[ECE 486 Formal Dictionaries#Configuration and Degrees Of Freedom|DOF]] of a mechanism comprised of links and joints can be found by looking at these constraints/freedoms. What captures this relationship between the mechanism's DOF and the freedoms/constraints provided by each of it's joints is known as Grübler's formula.

### Grübler's Formula
**Proposition 2.2:** Consider a mechanism consisting of $\large{N}$ links where the ground is also regarded as a link. Let $\large{J}$ be the number of joints, and $\large{m}$ the DOF of a rigid body in the space ($\large{m = 3}$ in a planar space as derived [[Determining the DOF of a Planar Rigid Body|here]], and $\large{m=6}$  in a spatial body as derived [[Determining the DOF of a Spatial Rigid Body|here]]), additionally let $\large{f_i}$ represent the number of freedoms provided by joint $\large{i}$ and $\large{c_i}$ be the number of constraints provided by joint $\large{i}$, where $\large{f_i + c_i = m\space\space \forall i\in J}$. Then:
$$
\large
\begin{align}
\\
DOF &= \text{Rigid Body Freedoms} - \text{Joint Constraints}\\ 
DOF &= m(N-1) - \sum_{i=1}^J{c_i} \\
DOF &= m(N-1) - \sum_{i=1}^J(m-f_i) \\
DOF &= m(N-1-J) + \sum_{i=1}^Jf_i
\end{align}
$$
This formula works for "generic cases" but fails with certain configurations of joints and links, such as when the constraints provided by two links are not independent(In such a case Grübler's Formula calculates a lower bound for the DOF). In general checking for independence between joints is very costly. Typically the joints of a [[ECE 486 Component Dictionary#Open-Chain Mechanisms|Open-Chain Mechanism]] provide independent constraints. 