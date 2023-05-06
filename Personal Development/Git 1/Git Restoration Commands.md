---
type: Academic
tags:
alias: Gi-1-Restoration
class: {"class-name":"The Git and Github Bootcamp","instructor":"Colt Steele","medium":"Online Course","start-date":"2023-04-25","online-platform":"Udemy","length":"17 hours","class-alias":"Gi-1","template":{"name":"class-online-course-obj","version":1}}
source: [{link: "[[Git 1 Bibliography#Section 10: Undoing Changes and Time Traveling]]", alias: Sec10-Gi-1, template: {name: bib-source-obj , version: 1}}]
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Git Branching Commands]]"
status: {state: Completed, template: {name: status-obj, version: 1}}
validity: {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description:
The following are a list of git commands that aid in restoring or moving file content between commits.

#### git restore
This command when provided with an argument corresponding to a file name in the repository will revert the file back to it's state at the commit which the [[Git 1 Dictionary#HEAD Pointer|HEAD Pointer]] is pointing. This command works identically to `git checkout HEAD <filename>`. It similarly can be used to revert multiple files simultaneously by providing multiple space-separated arguments. 

The command `git restore --source <commit hash> <file name>` will preform [[Git Branching Commands#git checkout|git checkout]]'s other functionality of moving the HEAD pointer to a commit pointed to by a commit hash.

The command `git restore --staged <filename>` will move the file mentioned by `filename` out of the [[Git 1 Dictionary#Staging Area|Staging Area]].

#### git reset
This command when provided with an argument corresponding to a commit hash will remove all commits between the [[Git 1 Dictionary#HEAD Pointer|HEAD Pointer]] and the commit hash and then will move the pointer to the commit hash. It is important to note that the [[Git 1 Dictionary#Working Directory|Working Directory]] is preserved in this process.

When this command is used in conjunction with the flag `--hard` it will preform its regular function however it will not preserve the Working Directory.

#### git revert
This command when provided an argument in the form of a commit hash will create a new commit in which the state of the project is the same as the one in the commit pointed to by the commit hash. This method proves especially useful in collaborative workflows.