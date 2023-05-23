---
type: Academic
tags: [Querynote, Reponote]
alias: ECE-486-Sched
class: 
relationship: 
status: {state: Completed, template: {name: status-obj, version: 1}}
validity: {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-sched-template, version: 1} 
---
### Upcoming Content:
##### Deliverables
```dataview
TABLE deliverable.due AS "Due Date",deliverable.Report-Due as "Report Due", deliverable.weight + "%" AS "Weight", status.state AS "State", date(deliverable.due) - date(today) AS "Time Left"
FROM "Class Notes/ECE 486/Deliverables"
WHERE date(deliverable.due) - date(today) < dur("3 weeks") AND date(deliverable.due) > date(today) AND typeof(deliverable.due) != "obj" AND deliverable.due != "EOT"
SORT deliverable.due ASC
```

### Class Deliverables:
##### Class Project
```dataview
TABLE deliverable.Report-Due AS "Report Due", deliverable.Grading-Starts AS "Grading Starts", deliverable.weight + "%" AS "Weight", status.state AS "State"
FROM "Class Notes/ECE 486/Deliverables/Course Project"
WHERE deliverable.type = "Project"
SORT deliverable.due.Report-Due ASC
```

##### Class Quizzes
```dataview
TABLE deliverable.due AS "Due Date", deliverable.weight + "%" AS "Weight", status.state AS "State"
FROM "Class Notes/ECE 486/Deliverables/Quizzes"
WHERE deliverable.type = "Quiz"
SORT deliverable.due ASC
```

##### Class Labs
```dataview 
TABLE deliverable.due AS "Due Date", deliverable.weight + "%" AS "Weight", status.state AS "State"
FROM "Class Notes/ECE 486/Deliverables/Labs"
WHERE deliverable.type = "Lab"
SORT deliverable.due ASC
```












