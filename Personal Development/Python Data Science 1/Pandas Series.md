---
type: Academic
tags:
alias: P-DS-1-PandasSeries
class: {"class-name":"Python for Data Science","instructor":"Maxwell Armi","medium":"Online Course","start-date":"2023-04-01","online-platform":"FreeCodeCamp-Youtube","length":"12hr20min","class-alias":"P-DS-1","template":{"name":"class-online-course-obj","version":1}}
source: {link: "[[Python Data Science 1 Bibliography#The Pandas Python Data Science Library]]", alias: pandas-P-DS-1, template: {name: bib-source-obj , version: 1}}
relationship: {name: standard-relationship-obj, version: 1}
friends: ["[[Pandas Indexing]]","[[Numpy Arrays]]"]
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description

The Series object is a data structure present in the [[The Pandas Library|Pandas]] Library, used in representing one-dimensional data. For information on Indexing/Slicing of Pandas Series Objects refer to [[Pandas Indexing]]

### Construction 

Series Objects can be constructed through the use of the `pd.Series()` method. Providing this method with an array will produce a Series object indexed by the natural numbers, for most purposes identical to [[Numpy Arrays|Numpy Arrays]]. In such a case you can specify the optional parameter `index` with another array of equal length to the first argument, this second argument will act as the index array of the Series. We refer to the entries of this index array as "explicit indices", It is important to note that in such a case the Series object is still addressable through the natural number or the "implicit indices". 

Series Objects could also be constructed by passing a dictionary as the only argument. The keys of the dictionary will act as the index array and the values will act as the values array.

The value array can be accessed with `data.values` which is of type [[Numpy Arrays|Numpy Array]] and the Index Array can be accessed with `data.index` which is of type Index object.

> [!example]- Ex.
> The Code  
> ```python
> import pandas as pd  
> data_a = pd.Series([1,3,3.12], index=["a","b","c"])  
> data_c = pd.Series([1,2,3,4])  
> data_b = pd.Series({"d" : 12,"e" :2, "f" : 0}) 
> print(data_a)  
> print(data_b)  
> print(data_c)  
> print(data_a.values)  
> print(data_a.index)
> ```
> Will Produce: 
> ```
> a    1.00
> b    3.00
> c    3.12
> dtype: float64
> d    12
> e     2
> f     0
> dtype: int64
> 0    1
> 1    2
> 2    3
> 3    4
> dtype: int64
> [1.   3.   3.12]
> Index(['a', 'b', 'c'], dtype='object')
>```
