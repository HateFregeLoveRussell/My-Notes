---
type: Academic
tags:
alias: P-DS-1-PandasIndexing
class: {"class-name":"Python for Data Science","instructor":"Maxwell Armi","medium":"Online Course","start-date":"2023-04-01","online-platform":"FreeCodeCamp-Youtube","length":"12hr20min","class-alias":"P-DS-1","template":{"name":"class-online-course-obj","version":1}}
source: {link: "[[Python Data Science 1 Bibliography#The Pandas Python Data Science Library]]", alias: pandas-P-DS-1, template: {name: bib-source-obj , version: 1}}
relationship: {name: standard-relationship-obj, version: 1}
friends: ["[[Pandas Data Frame]]","[[Pandas Series]]","[[Numpy Array Indexing Functions]]"]
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---

### Description

Indexing Pandas [[Pandas Series|Series]] and [[Pandas Data Frame|Data Frame]] objects when done through implicit indices is more or less the same as [[Numpy Array Indexing Functions|Indexing Numpy Arrays]]. Regardless of the form of the object slicing is always done through the same notation as Numpy Arrays. However, when indexed through explicit indices an important thing to note would be that the end-index of the slice is included. This is contrary to Numpy Indexing where the last index is always excluded. 

### Explicit-Implicit Slicing Problem

When Indexing Pandas Data Frames and Series objects, you can find yourself in a situation where the objects are explicitly indexed but the explicit indices are numeric. In such a case it becomes ambiguous whether slicing would be done through the explicit or implicit indices. In such a case, addressing values with notation such as `data[1]` uses the explicit indices by default and slicing an object through notation such as `data[1:3]` uses implicit indices by default. You can force the program to use the opposite indices through the `.iloc` and `.loc` methods. To demonstrate, the expression `data.iloc[2,3]` would address the value using implicit indices despite the explicit default, and the expression `data.loc[1:3]` would use explicit indices despite the implicit default.

Keep in mind, that the slices `data.loc[1:3]` and `data.iloc[1:3]` are never equal, as explicit slicing always includes the last index of the slice.