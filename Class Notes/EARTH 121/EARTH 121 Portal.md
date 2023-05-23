---
type: Academic
tags: [Entrynote]
alias: EARTH-121-Portal
class: {class-name: "Intoduction to Earth Sciences", instructor: "John Johnson", medium: "In Person", start-date: 2023-05-21, university: "University of Waterloo", class-alias: EARTH-121, template: {name: class-uni-obj, version: 1}}
relationship: 
parent: ["[[Class-Sched]]","[[Class-Display-Portal]]","[[Class-Bibliography]]"]
class-status: {state: In Progress, template: {name: status-obj, version: 1}}
status: {state: In Progress, template: {name: status-obj, version: 1}}
valitiy: {state: true, template: {name: validity-obj, version: 1}}
template: {name: Class-Portal, version: 2} 
---
### Class Description:
##### Overview
Introductory class to the Earth Science. Containing Systematic breakdown of the study of rocks, geological time, natural resources, and natural hazards.

##### Mark Breakdown
- Discussions (weight:: 15%)
- Field Note Journals (weight:: 20%)
- Study Site Assessments (weight:: 25%)
- Quizzes (weight:: 40%)


### Class Content:
- Introduction and Four Ways of Thinking
- Introduction to Rocks
- Introduction to the Rock Cycle
- Introduction to the Rock Classification
- Geologic Time and Geologic Time Scale
- Constructing the Geologic Time Scale
- Natural, Nonrenewable and Mineral Resources
- Categories of Mineral Resources and Renewable Resources
- Natural Hazards–Volcanoes, Earthquakes, and Mass Wasting
- The Role of Geoscientists: Temporal and System Thinking, Field Thinking, and Mitigation and Natural Service Function
- The Why of Water and Where is Water Found?
- Waterloo: The Importance of Water

### Class Progress: 
##### In Progress Notes
```dataview
TABLE status.state AS "State"
FROM "Class Notes/EARTH 121/Notes" AND -"Class Notes/EARTH 121/Figures"
WHERE status.state != "Completed" AND deliverable = null
```
##### Completed Notes
```dataview
TABLE status.state AS "State"
FROM "Class Notes/EARTH 121/Notes" AND -"Class Notes/EARTH 121/Figures"
WHERE status.state = "Completed" AND deliverable = null
```
##### Incomplete Deliverables
```dataview
TABLE status.state AS "State"
FROM "Class Notes/EARTH 121"
WHERE status.state != "Completed" AND deliverable != null
```
##### Completed Deliverables
```dataview
TABLE status.state AS "State"
FROM "Class Notes/EARTH 121"
WHERE status.state = "Completed" AND deliverable != null
```
