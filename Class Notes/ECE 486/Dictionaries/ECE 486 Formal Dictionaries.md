---
type: Academic
tags: [Dict, RepoNote]
alias: ECE-486-FormalDict
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
relationship: {name: standard-relationship-obj, version: 1}
child: "[[ECE 486 Dictionary]]"
status: {state: In Progress, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-dict-temnplate, version: 1}
---

### Configuration and Degrees Of Freedom 

#### Description
**Definition 2.1:** The _Configuration_ of a robot is a complete specification of the position of every point of the robot. The minimum number of real-valued co-ordinates $\large{n}$ needed to represent the configuration of a robot is called it's _Degrees of Freedom_ (often abbreviated as DOF). The $\large{n}$-dimensional space containing all possible configurations of a robot is called it's _C-Space_. The Configuration of a robot is a point in it's C-Space.

#### Referenced In
- [[Robot Configuration]]


### Topological Equivalence

#### Description
Two shapes are said to be topologically equivalent in this class if one can be smoothly deformed into the other without cutting or gluing.
