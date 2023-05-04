---
type: Academic
tags:
alias: Gi-1-FFMerge
class: {"class-name":"The Git and Github Bootcamp","instructor":"Colt Steele","medium":"Online Course","start-date":"2023-04-25","online-platform":"Udemy","length":"17 hours","class-alias":"Gi-1","template":{"name":"class-online-course-obj","version":1}}
source: [{link: "[[Git 1 Bibliography#Section 7: Merging Branches, Oh Boy!]]", alias: Sec7-Gi-1, template: {name: bib-source-obj , version: 1}}]
relationship: 
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description:
A Fast-Forward Merge to a type of merge between git [[Git 1 Dictionary#Branches|Branches]] where neither branch contradicts the other's content, and there is a linear path from one branch to the other. Fast-Forward Branches occur automatically in git and do not cause a [[Git 1 Dictionary#Merge Conflict|Merge Conflict]].

![[Fast Forward Merge Figure 1]]

In order to preform a FFW, Navigate to the smaller branch and call `git merge <larger_branch>`
