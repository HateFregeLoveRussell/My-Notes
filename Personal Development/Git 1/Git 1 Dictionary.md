---
type: Academic
tags: [Dict, RepoNote]
alias: Gi-Dict
class: {"class-name":"The Git and Github Bootcamp","instructor":"Colt Steele","medium":"Online Course","start-date":"2023-04-25","online-platform":"Udemy","length":"17 hours","class-alias":"Gi-1","template":{"name":"class-online-course-obj","version":1}}
relationship: 
status: {state: In Progress, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-dict-temnplate, version: 1}
---

### Version Control Software 
##### Description:
A piece of software used in tracking and managing changes made to files over time
- Source Alias: Sec2-Gi-1

##### Referenced In:
- [[What is Git]]

### Working Directory
##### Description
The location in the system file directory that the terminal is currently viewing
- Source Alias: Sec3-Gi-1

##### Referenced In
- [[Unix Type Commands]]
- [[Git Configuration Commands]]

### Commit
##### Description
A Commit in git is a snapshot of a repo which has been saved and can be visited. Every Commit in a repository has a string parameter summarizing the changes made in it.

##### Referenced In
- [[Git Snapshot Commands]]

##### See Also 
- [[Git 1 Dictionary#Staging Area|Staging Area]]

### Staging Area
##### Description
The Staging Area in Git is a sort of middle ground between repository data and the [[Git 1 Dictionary#Working Directory|Working Directory]]. Any change that you wish to be saved as repository data must pass through the Staging Area before being saved through a [[Git 1 Dictionary#Commit|Commit]]. 

##### Referenced In
- [[Git Snapshot Commands]]

##### See Also
- [[Git 1 Dictionary#Commit|Commit]]

### Atomic Commits 
##### Description
Atomic Commits is a heuristic approach to version control where each [[Git 1 Dictionary#Commit|Commit]] is focused around changes around the same subject.

### Branches
##### Description
A Branch is a work context in which git can operate in. Git can support multiple branches and switch between them while preserving content. 

##### Referenced In
- [[Git Branches]]

##### See Also
- [[Git 1 Dictionary#Master Branch|Master Branch]]

### Master Branch
##### Description
The Master Branch is a [[Git 1 Dictionary#Branches|Branch]] in which git commits to by default. In GitHub, has renamed this branch to "Main".

##### Referenced In
- [[Git Branches]]

##### See Also
- [[Git 1 Dictionary#Branches|Branches]]

### Branch Tip
##### Description
The Branch Tip refers to the most recent commit in a given [[Git 1 Dictionary#Branches|Branch]].

##### Referenced In
- [[Git Branches]]

##### See Also
- [[Git 1 Dictionary#Branch Pointer|Branch Pointer]]

### Branch Pointer
##### Description
The Branch Pointer is a pointer present in every [[Git 1 Dictionary#Branches|Branch]] which points to the current [[Git 1 Dictionary#Branch Tip|Branch Tip]].

##### Referenced In
- [[Git Branches]]

##### See Also
- [[Git 1 Dictionary#Branch Tip|Branch Tip]]
- [[Git 1 Dictionary#HEAD Pointer|HEAD Pointer]]

### HEAD Pointer
##### Description
The HEAD Pointer is a pointer which is used to describe the current branch occupied. It will point to the [[Git 1 Dictionary#Branch Tip|Branch Tip]] of the branch being worked on.

##### Referenced In
- [[Git Branches]]

##### See Also
- [[Git 1 Dictionary#Branch Pointer|Branch Pointer]]
- [[Git 1 Dictionary#Branch Tip|Branch Tip]]