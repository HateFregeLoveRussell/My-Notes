---
type: Academic
tags:
alias: Math-An-1-Orders
class: {
  class-name: "Mathematical Analysis 1",
  author: "Walter Rudin",
  medium: "Textbook",
  class-alias: "Math-An-1",
  title: "Principles Of Mathematical Analysis",
  edition: "Third",
  publisher: "McGraw-Hill Book Company",
  ISBN: "978-0-07-054235-8",
  length: 334,
  template: {
    name: "class-textbook-obj",
    version: 1,
    type: "object"
  }
}
source: {
  type: "tbsection",
  section-name: "The Real and Complex Number Systems: Ordered Sets",
  ISBN: "978-0-07-054235-8",
  book-title: "Principles of Mathematical Analysis",
  class-alias: Math-An-1,
  source-alias: Math-An-1-TheRealAndComplexNumberSystems-OrderedSets,
  start-page: 3,
  end-page: 5,
  template: {
    name: "source-tbsection-obj",
    version: 1,
    type: "object"
  }
}
status: {
  state: "Completed",
  template: {
    name: "status-obj",
    version: 1,
    type: "object"
  }
}
validity:  {
  state: true,
  template: {
    name: "validity-obj",
    version: 1,
    type: "object"
  }
}
template: {name: class-note-template, version: 1}
---
#### Definition 1.5:
- let $\large{S}$ be a set. An **==order==** on $\large{S}$ is a relation denoted with $\large\lt$ which has the following properties:
	- I) If $\large{x \in S}$ and $\large{y \in S}$ then one and only one of the following properties is true:
		- $\large{x \lt y}$
		- $\large{x = y}$
		- $\large{y \lt x}$ 
	- II) if $\large{x,y,z \in S}$ if $\large{x \lt y}$ and $\large{y \lt z}$ then $\large{x \lt z}$ (transitivity)
- A common writing convention is to use $\large{y \gt x}$ in place of $\large{x \lt y}$ 
- $\large{x \lt y}$ is read as **==x is less than y==**, **==x is smaller than y==**, **==x precedes y==**
- The notation $\large{x \le y}$ indicates that $\large{x \lt y}$ or $\large{x = y}$ 
	- It is important to note that $\large{x \le y}$ is the formal negation of $\large{x \gt y}$ 

#### Definition 1.6:
An **==ordered set==** is a set $\large S$ in which an [[Orders and Ordered Sets#Definition 1.5|order]] is defined on.

##### Example: 
$\large\Bbb Q$ is an ordered set if $\large{r \lt s}$ is defined to mean that $\large{s - r}$ is a positive rational number