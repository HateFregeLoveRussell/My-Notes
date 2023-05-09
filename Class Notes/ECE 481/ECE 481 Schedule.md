---
type: Academic
tags: [Querynote, Reponote]
alias: ECE-481-Sched
class: {"class-name":"Digital Control Systems","instructor":"Dr. Yash Vardhan Pant","medium":"In Person","start-date":"2023-05-08","university":"University of Waterloo","class-alias":"ECE-481","template":{"name":"class-uni-obj","version":1}}
relationship: 
status: {state: In Progress, template: {name: status-obj, version: 1}}
validity: {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-sched-template, version: 1} 
---

### Upcoming Content:
##### Deliverables
```dataview
TABLE deliverable.due AS "Due Date", deliverable.weight + "%" AS "Weight", status.state AS "State"
FROM "Class Notes/ECE 481/Deliverables"
WHERE date(deliverable.due) - date(today) < dur("3 weeks")  AND typeof(deliverable.due) != "obj" AND deliverable.due != "EOT"
SORT deliverable.due ASC
```


### Class Deliverables:
##### Class Labs
```dataview 
TABLE deliverable.due AS "Due Date", deliverable.weight + "%" AS "Weight", status.state AS "State"
FROM "Class Notes/ECE 481/Deliverables/Labs"
WHERE deliverable.type = "Lab"
SORT deliverable.due ASC
```

##### Class Assignments
```dataview 
TABLE deliverable.due AS "Due Date", deliverable.weight + "%" AS "Weight", status.state AS "State"
FROM "Class Notes/ECE 481/Deliverables/Assignments"
WHERE deliverable.type = "Assignment"
SORT deliverable.due ASC
```

##### Class Exams
```dataview 
TABLE deliverable.due AS "Due Date", deliverable.weight + "%" AS "Weight", status.state AS "State"
FROM "Class Notes/ECE 481/Deliverables"
WHERE deliverable.type = "Exam"
SORT deliverable.due ASC
```

