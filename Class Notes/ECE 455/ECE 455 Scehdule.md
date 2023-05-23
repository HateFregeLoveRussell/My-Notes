---
type: Academic
tags: [Querynote, Reponote]
alias: ECE-455-Sched
class: {
  class-name: "Embedded Software",
  instructor: "Murray Dunne",
  medium: "In Person",
  start-date: "2023-05-08",
  university: "University of Waterloo",
  class-alias: "ECE-455",
  template: {
    name: "class-uni-obj",
    version: 1
  }
}
relationship: 
status: {state: In Progress, template: {name: status-obj, version: 1}}
validity: {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-sched-template, version: 1} 
---
### Upcoming Content:
##### Deliverables
```dataview
TABLE deliverable.due AS "Due Date", deliverable.weight + "%" AS "Weight", status.state AS "State"
FROM "Class Notes/ECE 455/Deliverables"
WHERE date(deliverable.due) - date(today) < dur("3 weeks")  AND typeof(deliverable.due) != "obj" AND deliverable.due != "EOT"
SORT deliverable.due ASC
```


### Class Deliverables:
##### Class Labs
```dataview 
TABLE deliverable.due AS "Due Date", deliverable.weight + "%" AS "Weight", status.state AS "State"
FROM "Class Notes/ECE 455/Deliverables/Labs"
WHERE deliverable.type = "Lab"
SORT deliverable.due ASC
```

##### Class Quizzes
```dataview 
TABLE deliverable.due AS "Due Date", deliverable.weight + "%" AS "Weight", status.state AS "State"
FROM "Class Notes/ECE 455/Deliverables/Quizzes"
WHERE deliverable.type = "Quiz"
SORT deliverable.due ASC
```

##### Class Exams
```dataview 
TABLE deliverable.due AS "Due Date", deliverable.weight + "%" AS "Weight", status.state AS "State"
FROM "Class Notes/ECE 455/Deliverables"
WHERE deliverable.type = "Exam"
SORT deliverable.due ASC
```
