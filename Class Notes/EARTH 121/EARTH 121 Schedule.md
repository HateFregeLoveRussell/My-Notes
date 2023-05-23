---
type: Academic
tags: [Querynote, Reponote]
alias: EARTH-121-Sched
class: {
  class-name: "Intoduction to Earth Sciences",
  instructor: "John Johnson",
  medium: "In Person",
  start-date: "2023-05-21",
  university: "University of Waterloo",
  class-alias: "EARTH-121",
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

```dataview
TABLE deliverable.due AS "Due Date",deliverable.indRespDue as "Post Due", deliverable.constrFeedbackDue as "Reply Due", delivarable.respFeedbackDue AS "Response Due", deliverable.weight + "%" AS "Weight", status.state AS "State", date(deliverable.due) - date(today) AS "Time Left"
FROM "Class Notes/EARTH 121/Deliverables"
WHERE date(deliverable.due) - date(today) < dur("3 weeks") AND date(deliverable.due) > date(today) AND typeof(deliverable.due) != "obj" AND deliverable.due != "EOT"
SORT deliverable.due ASC
```

### Class Deliverables:
##### Class Discussions:
```dataview
TABLE deliverable.indRespDue as "Post Due", deliverable.constrFeedbackDue as "Reply Due", deliverable.respFeedbackDue as "Response Due", deliverable.weight + "%" AS "Weight", status.state AS "State"
FROM "Class Notes/EARTH 121/Deliverables/Discussions"
WHERE deliverable.type = "Assignment"
SORT deliverable.due ASC
```


##### Class Quizzes:
```dataview
TABLE deliverable.due AS "Due Date", deliverable.weight + "%" AS "Weight", status.state AS "State"
FROM "Class Notes/EARTH 121/Deliverables/Quizzes"
WHERE deliverable.type = "Quiz"
SORT deliverable.due ASC
```

##### Field Journal Notes:
```dataview
TABLE deliverable.due AS "Due Date", deliverable.weight + "%" AS "Weight", status.state AS "State"
FROM "Class Notes/EARTH 121/Deliverables/Field Journal Notes"
WHERE deliverable.type = "Assignment"
SORT deliverable.due ASC
```

##### Study Site Assessments
```dataview
TABLE deliverable.due AS "Due Date", deliverable.weight + "%" AS "Weight", status.state AS "State"
FROM "Class Notes/EARTH 121/Deliverables/Study Site Assessments"
WHERE deliverable.type = "Assignment"
SORT deliverable.due ASC
```
