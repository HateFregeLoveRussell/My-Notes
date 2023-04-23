---
type: Academic
tags:
alias: P-DS-1-NumpyArrays
class: {"class-name":"Python for Data Science","instructor":"Maxwell Armi","medium":"Online Course","start-date":"2023-04-01","online-platform":"FreeCodeCamp-Youtube","length":"12hr20min","class-alias":"P-DS-1","template":{"name":"class-online-course-obj","version":1}}
source: {link: "[[Python Data Science 1 Bibliography#The NumPy Python Data Science Library]]", alias: numpy-P-DS-1, template: {name: bib-source-obj , version: 1}}
relationship: 
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description 

Numpy arrays are a much faster, more optimized version of Python Lists. All elements in a Numpy array are of the same type, and the Numpy Module provides us with a series of functions that work very quickly with Numpy Arrays. 

### Construction

Numpy arrays can be created through the method `np.array()`. You can pass any Array-like object, such as Lists or Tuples into this method to create a NumPy Array with the same content as it's argument. This constructor also possesses an option type field which specifies the type all members of the array should be, if a member is not of the type specified it will be cast to that type. 

> [!example]- Ex. 
> ```python
> import numpy as np
> a = np.array((1,2,3,4))  
> b = np.array([1,2,3], str)  
> c = np.array([13.2,12.9],dtype='i')
> print(a)  
> print(b)  
> print(c)  
> print(type(a))
>```
>produces:
> ```
>[1 2 3 4]
>['1' '2' '3']
>[13 12]
><class 'numpy.ndarray'>
>```

### Dimensionality 

All Numpy arrays possess the field `.ndim` which is an integer corresponding to the dimensionality of the array. Two dimensional arrays would have an `.ndim` of 2, lone variables would have a `.ndim` of 0, etc.

In multidimensional Numpy arrays specific members can be addressed through the following notation: `arr[<root array select>,<root child array select>,...,<element select>]`. So in the case of `A = np.array([[1,2,3],[4,5,6]])` `A[1,0]` would equal 1. ^eea67c

Multidimensional arrays in Numpy must satisfy homogeneity in order to be initialized without error. This means arrays at the same level must be the same length. Initialization of `A = np.array([[1],[2,3]])` would yield an error. 

The `.shape` property belongs to all Numpy arrays and is a tuple of equal elements to `.ndim` which gives information about array length at different levels of nesting. For example, `A.shape = (2,3,3)` would mean that `A` contains two two-dimensional arrays each of which hold 3 one-dimensional arrays which each hold 3 elements. ^b84506

The `.size` property of Numpy arrays tells us the total number of zero-dimensional elements in the array. Note that this value is equal to the product of every member of `.shape`