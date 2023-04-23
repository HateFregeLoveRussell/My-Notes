---
type: Academic
tags:
alias: P-DS-1-NumpyBroadcasting
class: {"class-name":"Python for Data Science","instructor":"Maxwell Armi","medium":"Online Course","start-date":"2023-04-01","online-platform":"FreeCodeCamp-Youtube","length":"12hr20min","class-alias":"P-DS-1","template":{"name":"class-online-course-obj","version":1}}
source: {link: "[[Python Data Science 1 Bibliography#The NumPy Python Data Science Library]]", alias: numpy-P-DS-1, template: {name: bib-source-obj , version: 1}}
relationship: {name: standard-relationship-obj, version: 1}
friends: ["[[Numpy Arrays]]"]
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description 

"Broadcasting" in Numpy refers to a feature used to abbreviate operations which are preformed on every element in a [[Numpy Arrays|Numpy Array]]. Broadcasting allows us to forgo creating arrays of a specified size and shape in order to apply operations such as addition to every entry of a target matrix. 

As an example, Say we have a matrix `A` and we wish to add the number `5` to each entry in `A`. Normally we would need to construct a matrix of equivalent shape to `A` with `5` being every element. With Broadcasting we could simply write `A = A + 5` and have the compiler automatically create the matrix of appropriate shape. 

Broadcasting applies to objects other than constants such as `5`. Broadcasting can act on both Rows and Columns provided they are not too big, and even other matrices. Broadcasting will only throw an error when the supplied object cannot be expanded to be the same shape as the target matrix.
