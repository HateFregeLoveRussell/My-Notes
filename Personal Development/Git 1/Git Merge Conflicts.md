---
type: Academic
tags:
alias: Gi-1-MergeConflicts
class: {"class-name":"The Git and Github Bootcamp","instructor":"Colt Steele","medium":"Online Course","start-date":"2023-04-25","online-platform":"Udemy","length":"17 hours","class-alias":"Gi-1","template":{"name":"class-online-course-obj","version":1}}
source: {link: "[[Git 1 Bibliography#Section 7: Merging Branches, Oh Boy!]]", alias: Sec7-Gi-1, template: {name: bib-source-obj , version: 1}}
relationship: {name: standard-relationship-obj, version: 1}
friends: ["[[Git Non-Conflicting Non-Linear Merges]]", "[[Git Fast Forward Merges]]"]
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description
In the case where neither a [[Git Fast Forward Merges|Fast Forward Merge]] nor a [[Git Non-Conflicting Non-Linear Merges|Non-Conflicting Merge]] can be preformed a Merge Conflict is raised. In such a case git will notify the user which files contain conflicts and the responsibility of resolving them is left to the user. The files containing conflicts are decorated with [[Git 1 Dictionary#Conflict Markers|Conflict Markers]] which are illustrated in the example below: 
```
<<<<<<<<<<<<<<<< HEAD
I have two cats
=======================
I have one dog
>>>>>>>>>>>>>>>> BugFix
```
The chunk separated by the "<" and "=" belong to the  [[Git 1 Dictionary#HEAD Pointer|HEAD Branch]], while the chunk separated by "=" and ">" belongs to the branch being merged in ("BugFix" in this case). To resolve merge conflicts:
1. Open Files With Merge Conflicts
2. Resolve Conflicts in Each File (Either keep Branch A, Branch B or both)
3. Remove Conflict Markers
4. Add these changes and commit
Once the Merge conflict is dealt with the branches will be merged through a [[Git 1 Dictionary#Merge Commit|Merge Commit]] as in the case of Non-Linear Non-Conflicting Merges.