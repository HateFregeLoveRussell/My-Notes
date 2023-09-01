---
type: Academic
tags:
alias: Math-An-1-ParityOfLUBPandGLBP
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
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Bounds and Bounded Sets]]"
status: {
  state: "In Progress",
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
#### Introduction:
The following proof will illustrate the relationship between [[Bounds and Bounded Sets#Definition 1.8|least upper bounds]] and [[Bounds and Bounded Sets#Definition 1.8|greatest lower bounds]]. It will show that any set that has the [[Bounds and Bounded Sets#Definition 1.10|least-upper-bound property]] also must necessarily have the [[Bounds and Bounded Sets#Definition 1.10|greatest-lower-bound property]]

#### Theorem 1.11: 
Suppose there is a set $\large S$ with the [[Bounds and Bounded Sets#Definition 1.10|least-upper-bound property]]. Consider a set $\large B$ which is $\large {B \subset S}$, is [[Basic Set Notation#Definition 1.3|non-empty]], and is [[Bounds and Bounded Sets#Definition 1.7|bounded below]]. Let $\large L$ be the set of all lower bounds of $\large B$. 
Then $\large{\alpha = \operatorname{sup} B}$ must exist in $\large S$ and $\large{\alpha = \operatorname{inf} B}$.
In particular, we know that $\large{\operatorname{inf} B}$ must also exist in $\large S$ 

##### Proof:
Note that by definition of a [[Bounds and Bounded Sets#Definition 1.7|lower bound]] every element of $\large L$ is necessarily an element of $\large S$, therefore $\large{L \subset S}$. Furthermore, note that since $\large B$ is [[Bounds and Bounded Sets#Definition 1.7|bounded below]],$\large L$ is also [[Basic Set Notation#Definition 1.3|non-empty]].

Elaborating the definition of $\large L$ we know that $\large L$ is composed of exactly the elements of $\large {y\in S}$ for which $\large {\forall x \in B (y \le x)}$ so it stands to say that every element of $\large B$ are an [[Bounds and Bounded Sets#Definition 1.7|upper bound]] of $\large L$. Which means that $\large L$ is [[Bounds and Bounded Sets#Definition 1.7|bounded above]]. 

Since $\large{L \subset S}$, $\large L$ is non-empty, and $\large L$ is bounded-above by the definition of the [[Bounds and Bounded Sets#Definition 1.10|least-upper-bound property]] we know that the [[Bounds and Bounded Sets#Definition 1.8|Supremum]] of $\large L$ exists and is a member of $\large S$. We will call this Supremum $\large \alpha$.

Suppose we have some upper bound of $\large L$ called $\large {\gamma \in B}$, If $\large {\gamma \lt \alpha}$ then $\large \alpha$ would not be the Supremum of $\large L$ hence, $\large {\gamma \ge \alpha}$. It stands to say that $\large {\forall x \in B(\alpha \le x)}$ which by definition means that $\large {\alpha \in L}$, or in other words, that $\large \alpha$ is a lower bound for $\large B$.

$\large \alpha$ is an upper-bound of $\large L$ by virtue of it being the Supremum of $\large L$ so it stands to say that if $\large {\beta \gt \alpha}$ then $\large{\beta \notin L}$.

We have established that $\large {\alpha \in L}$,and that if $\large {\beta \gt \alpha}$ then $\large{\beta \notin L}$. In other words, $\large \alpha$ is greatest possible lower bound of $\large B$, which by [[Bounds and Bounded Sets#Definition 1.8|the definition of the Infimum]] means that $\large {\alpha = \operatorname{inf} B}$.
 