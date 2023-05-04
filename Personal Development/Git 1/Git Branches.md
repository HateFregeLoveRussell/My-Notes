---
type: Academic
tags:
alias: Gi-1-Branches
class: {"class-name":"The Git and Github Bootcamp","instructor":"Colt Steele","medium":"Online Course","start-date":"2023-04-25","online-platform":"Udemy","length":"17 hours","class-alias":"Gi-1","template":{"name":"class-online-course-obj","version":1}}
source: {link: "[[Git 1 Bibliography#Section 6: Working With Branches]]", alias: Sec6-Gi-1, template: {name: bib-source-obj , version: 1}}
relationship: 
status: {state: In Progress, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description: 
A Repository's history can essentially be viewed as a directed graph where the direction of each edge represents seniority. Git allows us to split our repository's history into multiple context's which can be worked on simultaneously. These context's are referred to as branches. Branches can be merged at later points into single contexts. 

![[Branch Figure 1]]

The Branch in which git commits to by default is known as the "Master Branch". GitHub has renamed this branch to "Main", Branches can be renamed so a repository can be made to conform to this standard fairly easily. 

Every Branch has a "tip" or the most recent commit that is part of that branch, every branch has a pointer field called the "Branch Pointer" which points to this commit. The "HEAD Pointer" is a pointer used to denote the current branch being worked on, it will point to the branch pointer of the branch which is currently occupied in a repository.

