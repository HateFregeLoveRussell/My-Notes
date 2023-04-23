---
type: Academic
tags:
alias: P-DS-1-AddingPythonModules
class: {"class-name":"Python for Data Science","instructor":"Maxwell Armi","medium":"Online Course","start-date":"2023-04-01","online-platform":"FreeCodeCamp-Youtube","length":"12hr20min","class-alias":"P-DS-1","template":{"name":"class-online-course-obj","version":1}}
source: [{link: "[[Python Data Science 1 Bibliography#Modules In Python]]", alias: PyModu-P-DS-1, template: {name: bib-source-obj , version: 1}},{link: "[[Python Data Science 1 Bibliography#Sys.path.append() in Python]]", alias: SysAppend-P-DS-1, template: {name: bib-source-obj , version: 1}}]
relationship: 
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---

### Description

By default user defined modules are accessible provided they are present in the same directory as the calling file. If the targeted module is not present the targeted module path must be added to the list of recognized paths. Such paths are kept in a system variable called `sys.path` as an array. Note that for this variable to be accessible the `system` module must be imported. 

You can add to this array during an execution session using: `sys.path.append(<path>)`
In order to add to this variable permanently you must modify the PYTHONPATH variable through the command line.