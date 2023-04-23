---
type: Academic
tags:
alias: P-DS-1-UsefulFunctionsPythonStandardLib
class: {"class-name":"Python for Data Science","instructor":"Maxwell Armi","medium":"Online Course","start-date":"2023-04-01","online-platform":"FreeCodeCamp-Youtube","length":"12hr20min","class-alias":"P-DS-1","template":{"name":"class-online-course-obj","version":1}}
source: {link: "[[Python Data Science 1 Bibliography#Other Useful Python Functions]]", alias: OtherPyFuncs-P-DS-1, template: {name: bib-source-obj , version: 1}}
relationship: 
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---

### divmod(x, y)

The `divmod()` method computes the quotient and remainder of inputs `x` and `y` and returns these computed values as a tuple 

> [!example]- Ex.
> `divmod(19,4)` => `(4,3)`
> `19//4` => `4`
> `19%4` => `3`

### isinstance(obj, class)

The `isinstance()` is a method returning a Boolean which takes any object as its first argument and a class type or tuple of class types as its second argument.
The method returns `true` if `obj` is a member of the class `class` or in the case where `class` is a tuple, the method returns `true` if `obj` belongs to any member of the array `class`. Otherwise the method returns `false`

> [!example]- Ex. 
> `isinstance(3,int)` => `true`
> `isinstance(3.4,int)` => `false`
> `isinstance(3.4,(int,float))` => `true`

### pow(base, exp, mod=None)

When the first two arguments are provided output is identical to `base**exp`.
When three arguments are provided output is identical to `base**exp%mod`

### help(obj)

When no arguments given starts interactive help session.
When argument in the form of function literal given, prints information about function.