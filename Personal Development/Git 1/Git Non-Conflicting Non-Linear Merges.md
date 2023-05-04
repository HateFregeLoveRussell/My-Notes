---
type: Academic
tags:
alias: Gi-1-NonConflictingNonFFMerges
class: {"class-name":"The Git and Github Bootcamp","instructor":"Colt Steele","medium":"Online Course","start-date":"2023-04-25","online-platform":"Udemy","length":"17 hours","class-alias":"Gi-1","template":{"name":"class-online-course-obj","version":1}}
source: [{link: "[[Git 1 Bibliography#Section 7: Merging Branches, Oh Boy!]]", alias: Sec7-Gi-1, template: {name: bib-source-obj , version: 1}}]
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Fast Forward Merge Figure 1]]"
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description:
This type of merge refers to merge types where there is still no conflict in the branch contents but there is no linear path from the first branch to the second branch. In such a case merging is still done without raising a [[Git 1 Dictionary#Merge Conflict|Merge Conflict]] and the procedure for preforming it is the same as [[Git Fast Forward Merges|Fast Forward Merges]]. However, this type of merge will result in a [[Git 1 Dictionary#Merge Commit|Merge Commit]].

![[Non-FFM Non-Conflicting Merges Figure 1]]
