---
type: Academic
tags:
alias: P-DS-1-DocStrings
class: {"class-name":"Python for Data Science","instructor":"Maxwell Armi","medium":"Online Course","start-date":"2023-04-01","online-platform":"FreeCodeCamp-Youtube","length":"12hr20min","class-alias":"P-DS-1","template":{"name":"class-online-course-obj","version":1}}
source: [{link: "[[Python Data Science 1 Bibliography#Functions in Python]]", alias: PyFuncs-P-DS-1, template: {name: bib-source-obj , version: 1}},{link: "[[Python Data Science 1 Bibliography#Python DocStrings]]", alias: DocStrings-P-DS-1, template: {name: bib-source-obj , version: 1}}]
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Some Useful Functions in Python]]"
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description

DocStrings are objects in Python used to provide documentation for user-written functions, modules, and classes similar to comments. This string will occupy the `__doc__` field in the function/module/class it is placed in and can be accessed directly or through the [[Some Useful Functions in Python#help(obj)|help() method]]. 

### Syntax

Doc Strings are enclosed in triple double quotes: `"""<your text here>"""` and must be placed in the starting line of the object they document, immediately below the `def` statement

> [!example]- Ex.
> ```python
> def hello_world()
> 	"""This Method Prints Hello World"""
> 	print("Hello World")
> ```
> Calling `help(hello_world)` produces the following console output: 
>
>```python
> hello_world()
>     This Method Prints Hello World
> ```
>
> Similarly `print(hello_world.__doc__)` produces `This Method Prints Hello World`
