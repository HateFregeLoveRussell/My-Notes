---
type: Academic
tags:
alias: Gi-1-GitIgnore
class: {"class-name":"The Git and Github Bootcamp","instructor":"Colt Steele","medium":"Online Course","start-date":"2023-04-25","online-platform":"Udemy","length":"17 hours","class-alias":"Gi-1","template":{"name":"class-online-course-obj","version":1}}
source: {link: "[[Git 1 Bibliography#Section 5: Commits in Detail (And Related Topics)]]", alias: Sec5-Gi-1, template: {name: bib-source-obj , version: 1}}
relationship: 
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description: 
Git can be made to exclude files from it's tracking using the `.gitignore` file. By convention this file is put at the root of the directory where the repository has been initialized. This file can contain entries including but not limited to the following forms: `.DS_Store` will ignore a file called `.DS_Store` Entries of the form `folderName/` will ignore all files under the directory `folderName`. Entries of the form `*.log` will ignore any file with a `.log` extension. 
