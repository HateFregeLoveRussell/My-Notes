---
type: Academic
tags:
alias: Gi-1-DiffCommand
class: {"class-name":"The Git and Github Bootcamp","instructor":"Colt Steele","medium":"Online Course","start-date":"2023-04-25","online-platform":"Udemy","length":"17 hours","class-alias":"Gi-1","template":{"name":"class-online-course-obj","version":1}}
source: {link: "[[Git 1 Bibliography#Section 8: Comparing Changes With Git Diff]]", alias: Sec8-Gi-1, template: {name: bib-source-obj , version: 1}}
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Reading Git Diff Output]]"
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description
The following note is dedicated to describing the behaviour of the `git diff` command. For information on how to read the output of this command, visit [[Reading Git Diff Output]].

#### git diff
This command is used to compare files, when used in it's native form it will print the difference between the [[Git 1 Dictionary#Staging Area|Staging Area]] and the [[Git 1 Dictionary#Working Directory|Working Directory]].

`git diff HEAD` will then compare The Working Directory with the commit which the [[Git 1 Dictionary#HEAD Pointer|HEAD Pointer]] is pointing to. Another argument, `filename` can be given in order to compare specific files in the Working Directory with it's counter part at the HEAD pointer.

The flags `--cached` and `--staged` will compare the Staging Area with the last Commit. Similarly this command can be used in conjunction with an argument `filename` in order to compare particular files.

This command can also be used in conjunction with two arguments corresponding to branch names in the following form `git diff <branch1>..<branch2>`. In such a case the command will print the difference between the latest commits in both branches. In such a case `branch1` will correspond to `file a` and `branch2` to `file b` in the output.

Similarly, the command can be used with two space-separated arguments corresponding to Commit Hashes, in such a case the command will print the difference between these two commits. 