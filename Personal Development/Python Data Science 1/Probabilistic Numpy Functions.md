---
type: Academic
tags:
alias: P-DS-1-probabilisticNumpyFunc
class: {"class-name":"Python for Data Science","instructor":"Maxwell Armi","medium":"Online Course","start-date":"2023-04-01","online-platform":"FreeCodeCamp-Youtube","length":"12hr20min","class-alias":"P-DS-1","template":{"name":"class-online-course-obj","version":1}}
source: [{link: "[[Python Data Science 1 Bibliography#The NumPy Python Data Science Library]]", alias: numpy-P-DS-1, template: {name: bib-source-obj , version: 1}}, {link: "[[Python Data Science 1 Bibliography#Python Help()]]", alias: numpy-help, template: {name: bib-source-obj , version: 1}}]
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Numpy Arrays]]"
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---

The following are some NumPy functions that are probabilistic in nature, this list is not exhaustive as some methods are better characterized by other attributes. 


### np.random.randint(lowerbound, upperbound)

This method creates a random integer with the lower bound of `lowerbound` and the upper bound of `upperbound`, the upper bound is not inclusive. The integers are generated using a discrete uniform distributions.

### np.random.permutation(x)

If `x` is an integer, then this method generates a [[Numpy Arrays|Numpy Array]] using [[Numpy Array Generation Functions#np.arange(x, y=0, z=1)|np.arange(x)]] and then shuffles the entries randomly.

If `x` itself is a Numpy Array though it will just shuffle the entries in the array randomly. 

### np.random.rand(d0, d1, d2, …, dn)

Produces a [[Numpy Arrays|Numpy Array]] with the [[Numpy Arrays#^b84506|shape]] of `(d0,d1,d2,...,dn)` with each entry being a random float between `0` and `1` (not including `1`). The distribution used in generating the entries is the standard uniform distribution.

### np.random.randn(d0, d1, d2, …, dn)

Works very similarly to np.random.rand(), it produces a [[Numpy Arrays|Numpy Array]] with the shape `(d0,d1,d2,...,dn)` with each entry being a random number. The distribution used in generating the random entries however, is the standard normal distribution. 
