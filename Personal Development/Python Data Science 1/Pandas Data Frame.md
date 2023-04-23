---
type: Academic
tags:
alias: P-DS-1-DataFrame
class: {"class-name":"Python for Data Science","instructor":"Maxwell Armi","medium":"Online Course","start-date":"2023-04-01","online-platform":"FreeCodeCamp-Youtube","length":"12hr20min","class-alias":"P-DS-1","template":{"name":"class-online-course-obj","version":1}}
source: {link: "[[Python Data Science 1 Bibliography#The Pandas Python Data Science Library]]", alias: pandas-P-DS-1, template: {name: bib-source-obj , version: 1}}
relationship: {name: standard-relationship-obj, version: 1}
friends: ["[[Pandas Series]]","[[Pandas NaN Methods]]","[[Pandas Indexing]]"]
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---

### Description

The Data Frame Object is a data structure belonging to the [[The Pandas Library|Pandas Library]]. It is used to represent higher-dimensional Data in the case that the [[Pandas Series|Series Object]] cannot be used. Most data will in practicality be represented by a Data Frame. 

### Construction

Data Frames can be created through the `pd.DataFrame()` method passing an array of [[Pandas Series|Series]] Objects . If for a particular index a data point is not specified in the Data Frame `NaN` will be placed in it's spot. Refer to [[Pandas NaN Methods|NaN Methods]] for more information. Similar to Series Objects the indices of each series (in this case referred to as the columns) can be made explicit by passing a Dictionary of Series objects as the argument of the function. Additionally a Data Frame can also be initialized by passing an array of Dictionaries, each dictionary will be cast to a Series object and each Series Object will be added to the data frame. The peculiarities of slicing Data Frames will be covered in [[Pandas Indexing]].

> [!example]- Ex.
> The Program:
> ```python
>  import pandas as pd  
> data_a = pd.Series([1,2,3,4,5])  
> data_b = pd.Series([7,8,9,10])  
> data_1 = pd.DataFrame([data_a,data_b])  
> data_2 = pd.DataFrame({"first":data_a, "second":data_b})  
> data_3 = pd.DataFrame([{"a": 1,"b":2,"c":3},{"a":4,"c":12}])  
> print (data_1)  
> print (data_2)  
> print (data_3)
> ```
> Produces the output:
> ```
>            0    1    2     3    4
>      0  1.0  2.0  3.0   4.0  5.0
>      1  7.0  8.0  9.0  10.0  NaN
>         first  second
>      0      1     7.0
>      1      2     8.0
>      2      3     9.0
>      3      4    10.0
>      4      5     NaN
>         a    b   c
>      0  1  2.0   3
>      1  4  NaN  12
>``` 

Similarly to the Series Object, the value-matrix of a Data Frame can be accessed through `data.values`. And its columns can be accessed through `data.columns` as a Index type object.

> [!example]- Ex. 
> The Code: 
> ```python
> import pandas as pd  
> data = pd.DataFrame([{"a": 1,"b":2,"c":3},{"a":4,"c":12}])  
> print (data.values)  
> print (data.columns)
> ```
>Produces the Output: 
>```
> [[ 1.  2.  3.]
> [ 4. nan 12.]]
> Index(['a', 'b', 'c'], dtype='object')
>```

