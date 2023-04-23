---
type: Academic
tags:
alias: P-DS-1-NumpyArraySlicing
class: {"class-name":"Python for Data Science","instructor":"Maxwell Armi","medium":"Online Course","start-date":"2023-04-01","online-platform":"FreeCodeCamp-Youtube","length":"12hr20min","class-alias":"P-DS-1","template":{"name":"class-online-course-obj","version":1}}
source: {link: "[[Python Data Science 1 Bibliography#The NumPy Python Data Science Library]]", alias: numpy-P-DS-1, template: {name: bib-source-obj , version: 1}}
relationship: {name: standard-relationship-obj, version: 1}
friends: ["[[Numpy Arrays]]", "[[Numpy Broadcasting]]"]
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description

"Slicing" also known as "Indexing" refers to operations and methods used to obtain sub-arrays of declared [[Numpy Arrays]].

### Traditional Indexing

Traditional Indexing refers to methods that are similar to ones already present in the python standard library. Below is a summary of some of these operations.

```python
a[1:5] # index 1 - 4 including 4
a[:5] # index 0 - 4 including 4
a[2:] # index 2 until the end of the array (including last element)
a[::-1] # from tail to head of the array (the array in reverse order)
a[::2] # from start to end of the array including every other element
```
Keep in mind that contrary to the standard library, when slicing in this style in Numpy you are not creating a separate copy of the array, rather a reference. So manipulating the subarray obtained through slicing still manipulates the original. For example, 
`a = np.arange(12)`
`b = a[::-2]`
`b[0] = -2`
would mutate a.

To explicitly create a copy of a Numpy Array use `.copy()`

Some additional functionality can be found in how rows, columns, and sub matrices in general are addressed in Numpy. 
To address a row in a two dimensional array use `A[row_index,:]`
To address a column in a two dimensional array use `A[:,column_index]`
To address a sub-matrix of a two dimensional array use `A[start_row:end_row,start_column:end_column]`
so `A[1:3,2:4]` would retrieve the rows 1 and 2 alongside columns 2 and 3

### Fancy Indexing

The following are more advanced indexing techniques provided by Numpy. It is important to keep in mind that the methods below, unlike the methods of [[#Traditional Indexing]] don't yield references but copies of the passed Array.

#### Index Arrays

Index Arrays are a type of array where it's entries are indexes of some other array fulfilling some property. This indexing is done in convention with the [[Numpy Arrays#^eea67c|addressing]] already in Numpy, so Index arrays can be multi-dimensional. 

Overall a Numpy Array can be sliced by passing any valid index array to it's index argument `A[index_arr]`. For example, `A[[1,2,3]]` would retrieve a slice with elements at indices 1,2, and 3.

#### Masking

A "Mask" is a Boolean matrix matching in shape with the array it applies to. A mask can be passed as an array index the same way a [[#Index Arrays|Index Array]] would, yielding a slice containing all entries in which the mask is `true`. 

This can be combined with the principle of [[Numpy Broadcasting|Broadcasting]] to yield very easy, readable slicing notation. 
For example `A[A>8]` would yield a slice in which all elements of `A` which are greater than `8` are present. And `A[(A>9) & (A<12)]` would yield a slice of `A` only containing elements between `12` and `9`.
