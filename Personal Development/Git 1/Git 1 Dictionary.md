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
- Source Alias: Sec4-Gi-1

##### Referenced In
- [[Git Snapshot Commands]]

##### See Also 
- [[Git 1 Dictionary#Staging Area|Staging Area]]

### Staging Area
##### Description
The Staging Area in Git is a sort of middle ground between repository data and the [[Git 1 Dictionary#Working Directory|Working Directory]]. Any change that you wish to be saved as repository data must pass through the Staging Area before being saved through a [[Git 1 Dictionary#Commit|Commit]]. 
- Source Alias: Sec4-Gi-1

##### Referenced In
- [[Git Snapshot Commands]]

##### See Also
- [[Git 1 Dictionary#Commit|Commit]]

### Atomic Commits 
##### Description
Atomic Commits is a heuristic approach to version control where each [[Git 1 Dictionary#Commit|Commit]] is focused around changes around the same subject.
- Source Alias: Sec5-Gi-1

### Branches
##### Description
A Branch is a work context in which git can operate in. Git can support multiple branches and switch between them while preserving content. 
- Source Alias: Sec6-Gi-1

##### Referenced In
- [[Git Branches]]

##### See Also
- [[Git 1 Dictionary#Master Branch|Master Branch]]

### Master Branch
##### Description
The Master Branch is a [[Git 1 Dictionary#Branches|Branch]] in which git commits to by default. In GitHub, has renamed this branch to "Main".
- Source Alias: Sec6-Gi-1

##### Referenced In
- [[Git Branches]]

##### See Also
- [[Git 1 Dictionary#Branches|Branches]]

### Branch Tip
##### Description
The Branch Tip refers to the most recent commit in a given [[Git 1 Dictionary#Branches|Branch]].
- Source Alias: Sec6-Gi-1

##### Referenced In
- [[Git Branches]]

##### See Also
- [[Git 1 Dictionary#Branch Pointer|Branch Pointer]]

### Branch Pointer
##### Description
The Branch Pointer is a pointer present in every [[Git 1 Dictionary#Branches|Branch]] which points to the current [[Git 1 Dictionary#Branch Tip|Branch Tip]].
- Source Alias: Sec6-Gi-1

##### Referenced In
- [[Git Branches]]

##### See Also
- [[Git 1 Dictionary#Branch Tip|Branch Tip]]
- [[Git 1 Dictionary#HEAD Pointer|HEAD Pointer]]

### HEAD Pointer
##### Description
The HEAD Pointer is a pointer which is used to describe the current branch occupied. It will point to the [[Git 1 Dictionary#Branch Tip|Branch Tip]] of the branch being worked on.
- Source Alias: Sec6-Gi-1

##### Referenced In
- [[Git Branches]]

##### See Also
- [[Git 1 Dictionary#Branch Pointer|Branch Pointer]]
- [[Git 1 Dictionary#Branch Tip|Branch Tip]]

#todo
### Fast-Forward Merge
##### Description
A Fast Forward Merge is a type of automatic, non-conflicting merge preformed by git when there is no conflicting content between two [[Git 1 Dictionary#Branches|Branches]] and the path from one to the other is linear.
- Source Alias: Sec7-Gi-1

##### Referenced In
- [[Git Fast Forward Merges]]
- [[Non-FFM Non-Conflicting Merges Figure 1]]
- [[Git Merge Conflicts]]

##### See Also
- [[Git 1 Dictionary#Merge Conflict|Merge Conflict]]

### Merge Conflict
##### Description
A Merge Conflict is an event that arises when two branches are merged that have conflicting contents. This event must be resolved before the two branches can be merged through the use of a [[Git 1 Dictionary#Merge Commit|Merge Commit]].
- Source Alias: Sec7-Gi-1

##### Referenced In
- [[Git Merge Conflicts]]

##### See Also
- [[Git Merge Conflicts]]
- [[Git Non-Conflicting Non-Linear Merges]]]
- [[Git Fast Forward Merges]]

### Merge Commit
##### Description
A Merge Commit is a type of [[Git 1 Dictionary#Commit|Commit]] that is required for two branches with non-linear paths between them to be merged.
- Source Alias: Sec7-Gi-1

##### Referenced In
- [[Git Merge Conflicts]]
- [[Git Non-Conflicting Non-Linear Merges]]

##### See Also
- [[Git 1 Dictionary#Merge Conflict|Merge Conflict]]

### Conflict Markers
##### Description
A Conflict Marker are a series of markers that are edited into conflicting file content during a [[Git 1 Dictionary#Merge Conflict|Merge Conflict]] There Markers must be removed during the process of resolving a merge conflict.
- Source Alias: Sec7-Gi-1

##### Referenced In
- [[Git Merge Conflicts]]

#### See Also
- [[Git 1 Dictionary#Merge Conflict|Merge Conflict]]


### Stashing
##### Description
Stashing refers to a feature in git where changes can be saved without needing a [[Git 1 Dictionary#Commit|Commit]]. This feature exists so that a user is not forced to commit unnecessarily when switching [[Git 1 Dictionary#Branches|Branches]].

##### Referenced In
- [[Git Stashing]]