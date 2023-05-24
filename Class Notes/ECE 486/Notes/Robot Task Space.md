---
type: Academic
tags:
alias: ECE-486-TaskSPace
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
source: {link: "[[ECE 486 Textbook Chapter 2 Bibliography#Textbook Chapter 2.5]]", alias: tbch2s5-ECE-486, template: {name: bib-source-obj , version: 1}}
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Robot Configuration]]"
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Overview: 
The Task Space of a robot is the space which the robot's task can be naturally expressed in. As an example the task space of a robot with a pen and a piece of paper would probably be $\large{\mathbb{R}^2}$. As another example, the task space of a robot made to manipulate a rigid body is the C-Space of that body. The Task Space of a robot relies entirely on the task it is designed to preform and is independent of the actual robot. It is important to note that the 

Task Space is often distinct from a robot's C-Space. A point in the Task Space can be reachable by multiple points in the C-Space meaning that a point in the Task Space gives us an incomplete configuration of the robot's C-Space.  Some points in the Task Space may not be reachable at all by the robot.