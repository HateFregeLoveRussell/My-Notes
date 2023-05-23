---
type: Academic
tags: [Entrynote]
alias: ECE-455-Portal
class: {class-name: "Embedded Software", instructor: "Murray Dunne", medium: "In Person", start-date: 2023-05-08, university: "University of Waterloo", class-alias: ECE-455, template: {name: class-uni-obj, version: 1}}
relationship: 
parent: ["[[Class-Sched]]","[[Class-Display-Portal]]","[[Class-Bibliography]]", "[[ECE 455 Scehdule]]"]
class-status: {state: In Progress, template: {name: status-obj, version: 1}}
status: {state: In Progress, template: {name: status-obj, version: 1}}
valitiy: {state: true, template: {name: validity-obj, version: 1}}
template: {name: Class-Portal, version: 2} 
---
### Class Description:
##### Overview
This class puts a focus on the development of software used in safety-critical and real-time embedded systems.
This class has an in-person asynchronous lab segment. Additionally it has no textbook and all class content is dependent on lecture slides .
During any particular lecture module, lecture notes will successively be updated, this change will be reflected by other files with higher version numbers appearing on LEARN, when the module is finished all files will be concatenated into one.
Every lecture in this class will include an example of a catastrophic failure due to the failings of an embedded system as a case study.

##### Mark Breakdown
- Midterm Exam (weight:: 18%)
- Final Exam (weight:: 50%)
- In Class- Quizzes (weight:: 6%)
- Labs (weight:: 26%)

##### Labs
Labs are preformed asynchronously. Board access is on a drop-in or scheduled (if required) basis. Once the necessary code has been submitted the student is invited for a demo of the lab functionality with the Lab TAs. 
3 late days are allotted, they can only be used on Labs, and any number of the remaining late days can be used on any specific Lab. To use a lab, send an email after code submission to a TA detailing how many late days you'd like to use. The Email should include: student name, student number, quest ID.

##### Quizzes
There are 3 in-class quizzes this term. If proof of illness is provided to university the weight of the quiz will be distributed equally to other course components. Quizzes will be centered more around design questions (which technique should be used and why?).

##### Remarking
Remark request can be sent via email. They require specific information and justification for the element for which  a remark is requested. Student name, number, and Quest ID must be provided in this email.

### Class Content:
- Part 1: Review of Embedded Computing
- Part 2: Worst-case Execution Time Analysis (WCET)
- Part 3: Real-time Scheduling
- Part 4: Dependability
- Part 5: Security

### Class Progress: 
##### In Progress Notes
```dataview
TABLE status.state AS "State"
FROM "Class Notes/ECE 455/Notes" AND -"Class Notes/ECE 455/Figures"
WHERE status.state != "Completed" AND deliverable = null
```
##### Completed Notes
```dataview
TABLE status.state AS "State"
FROM "Class Notes/ECE 455/Notes" AND -"Class Notes/ECE 455/Figures"
WHERE status.state = "Completed" AND deliverable = null
```
##### Incomplete Deliverables
```dataview
TABLE status.state AS "State"
FROM "Class Notes/ECE 455"
WHERE status.state != "Completed" AND deliverable != null
```
##### Completed Deliverables
```dataview
TABLE status.state AS "State"
FROM "Class Notes/ECE 455"
WHERE status.state = "Completed" AND deliverable != null
```
