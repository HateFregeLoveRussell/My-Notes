---
type: Academic
tags:
alias: Gi-1-Stashing
class: {"class-name":"The Git and Github Bootcamp","instructor":"Colt Steele","medium":"Online Course","start-date":"2023-04-25","online-platform":"Udemy","length":"17 hours","class-alias":"Gi-1","template":{"name":"class-online-course-obj","version":1}}
source: [{link: "[[Git 1 Bibliography#Section 9: The Ins and Outs of Stashing]]", alias: Sec9-Gi-1, template: {name: bib-source-obj , version: 1}}]
relationship: 
status: {state: Completed, template: {name: status-obj, version: 1}}
validity: {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description
This page is dedicated to describing the behaviour of the `git stash` command used in [[Git 1 Dictionary#Stashing|Stashing]].

#### git stash
This command when used in it's native form will move all changes in the [[Git 1 Dictionary#Working Directory|Working Directory]] to the Stash.
The stash is itself a LIFO stack so it can be added to and removed from multiple times. In order to view the full stack of the stash use the command `git stash list`
The two stash commands below can be applied to particular members of the stack by passing the stash id of the entry as an argument, these ids can be found through `git stash list`
The command `git stash pop` will remove the most recent changes that have been moved to the stash. This command will also move these changes to the Working Directory Prior to deleting.
The Command `git stash apply` will move the most recent changes in the stash to the working directory, but does not delete the changes from the stash. 
The Command `git stash drop <stashId>` will remove the entry in the stash stack corresponding to the `stashId`.
The Command `git stash clear` can be used to clear the stash stack all together.
