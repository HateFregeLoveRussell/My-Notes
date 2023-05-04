---
type: Academic
tags:
alias: Gi-1-BranchCommands
class: {"class-name":"The Git and Github Bootcamp","instructor":"Colt Steele","medium":"Online Course","start-date":"2023-04-25","online-platform":"Udemy","length":"17 hours","class-alias":"Gi-1","template":{"name":"class-online-course-obj","version":1}}
source: {link: "[[Git 1 Bibliography#Section 6: Working With Branches]]", alias: Sec6-Gi-1, template: {name: bib-source-obj , version: 1}}
relationship: 
status: {state: In Progress, template: {name: status-obj, version: 1}}
validity: {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description 
The following is a list of commands that aid in [[Git Branches|Branching]] in Git. 

#### git branch
This command when used in it's native form will print a list of all available branches, marking the active branch with an asterisk. 
When provided a string as it's argument the command will instead create a new branch from the [[Git 1 Dictionary#HEAD Pointer|HEAD Pointer]] with the argument as it's name. It is important to note that when used in this context the branch name must not contain any spaces. It is also important to note that this command does not switch the user's active branch to this newly created branch. 
When provided with a String argument `branch_name` and in conjunction the command is used with the flag `-d` the branch with the name `branch_name` will be deleted only if it has been merged, `-D` flag does the same thing in the case that the branch has not been merged with it's remote counterpart.
When Provided the string argument `branch_name` in conjunction with the flag `-m` the branch currently occupied is renamed to `branch_name`

#### git switch
This command when provided with the String argument `branch_name` will switch the user's [[Git 1 Dictionary#HEAD Pointer|HEAD Pointer]] to the [[Git 1 Dictionary#Branch Pointer|Branch Pointer]] of the branch named `branch_name`.
When this command is used in conjunction with the `-C` flag the command will create a branch with name `branch_name` if a branch with that name is not found. 
before switching to a different branch all uncommitted changes must either be [[Git Stashing|Stashed]] or committed. If the changes made do not conflict with the branch you are switching to they will carry with you to the new branch but still need to be committed to show up in history.

#### git checkout
This command has the same functionality as [[Git Branching Commands#git switch|git switch]], it used to be the old git switch but had too many other functionalities so git switch was made. A subtle difference is that to create and switch to a branch using `git checkout` the `-b` flag is used. 

