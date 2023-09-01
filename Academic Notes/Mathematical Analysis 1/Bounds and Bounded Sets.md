---
type: Academic
tags:
alias: Math-An-1-Bounds
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
friends: "[[Orders and Ordered Sets]]"
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
#### Definition 1.7:
Suppose that $\large S$ is an [[Orders and Ordered Sets#Definition 1.6|Ordered Set]] and $\large{ E \subset S}$. If there exists $\large{\beta \in S}$ such that $\large{x \le \beta}$ for every $\large{x \in E}$, we say that $\large E$ is **==bounded above==** and call $\large \beta$ the **==upper bound==** of $\large E$ 

- The **==lower bound==** of a set/ a **==bounded below==** set are defined similarly, replacing $\large \le$ with $\large \ge$ 
- It is important to note that the upper bound of a set does not necessarily need to belong to the set

#### Definition 1.8:
Suppose that $\large S$ is an [[Orders and Ordered Sets#Definition 1.6|Ordered Set]], and $\large {E \subset S}$, and $\large E$ is [[Bounds and Bounded Sets#Definition 1.7|bounded above]]. Suppose there exists an $\large{\alpha \in S}$ with the following properties: 
- I) $\large \alpha$ is an [[Bounds and Bounded Sets#Definition 1.7|upper bound]] of $\large E$
- II) If $\large{\gamma}$ is an [[Bounds and Bounded Sets#Definition 1.7|upper bound]] of $\large E$ then $\large{\gamma \ge \alpha}$ 
Then $\large \alpha$ is called the **==least upper bound==** of $\large E$ or the **==Supremum==** of $\large E$ which we denote with: $\large {\alpha = \operatorname{sup} E}$.

- The **==greatest lower bound==** or **==Infimum==** of a set $\large E$ which is [[Bounds and Bounded Sets#Definition 1.7|bounded below]] is defined similarly, where if $\large \beta$ is a [[Bounds and Bounded Sets#Definition 1.7|lower bound]] of $\large E$ then $\large {\beta \le \alpha}$. This relationship is similarly denoted with: $\large{\alpha = \operatorname{inf} E}$ 
- That there is at most one Supremum or Infimum is clear from looking at property II 

#### Examples: 

##### Example A:
Consider the sets $\large A$ and $\large B$ of [[Holes in the Rationals#Insightful Proof About the Gaps in the Rationals|the following proof]], as subsets of the ordered set $\large \Bbb Q$. The set $\large A$ is bounded above, in fact, the upper bounds of $\large A$ are exactly all members of $\large B$. Since $\large B$ contains no smallest member, we can conclude that $\large A$ has no [[Bounds and Bounded Sets#Definition 1.8|least upper bound]] in $\large \Bbb Q$.

##### Example B:
Note that If $\large {\alpha = \operatorname{sup} E}$ exists, then $\large{\alpha}$ may or may not be a member of $\large E$.
As an example let $\large{E_1}$ be the set of all $\large{r \in \Bbb Q}$ such that $\large {r \lt 0}$. Let $\large E_2$ be the set of all $\large r \in \Bbb Q$ such that $\large{r \le 0}$.

Clearly: $\large{\operatorname{sup} E_1 = \operatorname{sup} E_2 = 0}$ 

but $\large{0 \notin E_1}$ and $\large{0 \in E_2}$ 

#### Definition 1.10:
An ordered set $\large S$ is said to have the **==least-upper-bound property==** if $\large {E \subset S}$, $\large E$ is nonempty, $\large E$ is [[Bounds and Bounded Sets#Definition 1.7|bounded above]] and the [[Bounds and Bounded Sets#Definition 1.8|Supremum]] of $\large E$ exists in $\large S$.
- [[Bounds and Bounded Sets#Example A|Example A]] shows that $\large \Bbb Q$ does not have the least-upper-bound property