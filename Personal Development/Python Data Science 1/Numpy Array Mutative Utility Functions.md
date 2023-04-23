---
type: Academic
tags:
alias: P-DS-1-NumpyArrayMutativeUtility
class: {"class-name":"Python for Data Science","instructor":"Maxwell Armi","medium":"Online Course","start-date":"2023-04-01","online-platform":"FreeCodeCamp-Youtube","length":"12hr20min","class-alias":"P-DS-1","template":{"name":"class-online-course-obj","version":1}}
source: [{link: "[[Python Data Science 1 Bibliography#The NumPy Python Data Science Library]]", alias: numpy-P-DS-1, template: {name: bib-source-obj , version: 1}}, {link: "[[Python Data Science 1 Bibliography#Python Help()]]", alias: numpy-help, template: {name: bib-source-obj , version: 1}}]
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Numpy Arrays]]"
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
This note contains some useful functions for mutating [[Numpy Arrays]] It is not exhaustive or all-inclusive. 

### arr.reshape(newshape, order = 'C')

This method can be called on any Numpy Array, in order to mutate it to have the [[Numpy Arrays#^b84506|shape]] property that is desired which is specified by `newshape`. The `order` parameter determines the indexing scheme used in achieving this, refer to documentation for more information. 

### arr.sort(axis)

This method is used to sort the Numpy Array `arr`. When `arr` is a one-dimensional array then the argument `axis` is to be omitted. When `arr` is of higher dimension then `axis` is used to determine the depth at which the sort method is called. When `axis = 0` in a two-dimensional array for example, the array is sorted on it's columns, when `axis = 1` it is sorted on it's rows, and so on. All sorting is done in ascending order, to achieve sorting on a descending order, simply reverse the array with the method covered [[Numpy Array Slicing|here]].

### arr.T

This attribute retrieves the transpose of the array `arr`.
More linear algebra tools can be found in `numpy.linalg`

### np.hstack(T)

This method is used to concatenate the entries of the tuple `T` horizontally, or row-wise. 

### np.vstack(T)

This method works very similarly to np.hstack() but instead of concatenating the entries of tuple `T` horizontally, it is done vertically or column-wise. 