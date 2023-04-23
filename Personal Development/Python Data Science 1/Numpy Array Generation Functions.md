---
type: Academic
tags:
alias: P-DS-1-ArrayGenerationFunctions
class: {"class-name":"Python for Data Science","instructor":"Maxwell Armi","medium":"Online Course","start-date":"2023-04-01","online-platform":"FreeCodeCamp-Youtube","length":"12hr20min","class-alias":"P-DS-1","template":{"name":"class-online-course-obj","version":1}}
source: [{link: "[[Python Data Science 1 Bibliography#The NumPy Python Data Science Library]]", alias: numpy-P-DS-1, template: {name: bib-source-obj , version: 1}}, {link: "[[Python Data Science 1 Bibliography#Python Help()]]", alias: numpy-help, template: {name: bib-source-obj , version: 1}}]
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Numpy Arrays]]"
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
Below are a list of functions generating [[Numpy Arrays|Numpy Arrays]]. Note that this list is not exhaustive, functions that are purely generative may exist in other notes and not in this note because they are better classified by some other quality. 

### np.arange(x, y=0, z=1)

This method creates a Numpy Array object including all integer elements that start from `y` and go to (but do not include) `x`. `y` is an optional argument, when excluded it is presumed to be `0`. `z` as an argument determines the step size between each element in the array, it is `1` by default.


### np.zeros(shape, dtype = float, order = 'C')

This method creates a Numpy Array Object of [[Numpy Arrays#Dimensionality|shape]] `shape`, and data type `dtype`, with all entries equalling to `0`. the `order` parameter determines how the array object is stored in memory, refer to documentation for more information. 

### np.ones(shape, dtype = float, order = 'C')

This method works very similarly to np.zeros(), it generates a Numpy Array Object of shape `shpae`, data type `dtype`, and memory representation of `order`. But instead of populating each entry with `0` the method populates each entry in the array with `1`.

### np.linspace( start, stop, entries)

This method will create a Numpy Array object spanning from numeric point `start` to `stop` with `entries` number of elements equally spaced along the span. This method is particularly useful in graphing applications.