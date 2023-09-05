---
type: Academic
tags:
alias: Math-An-1-ExtendedRealNumberSystem
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
  start-page: 11,
  end-page: 12,
  type: "tbsection",
  class-alias: "Math-An-1",
  book-title: "Principles of Mathematical Analysis",
  source-alias: "Math-An-1-TheRealAndComplexNumberSystems-TheExtendedRealNumberSystem",
  ISBN: "978-0-07-054235-8",
  template: {
    name: "source-tbsection-obj",
    type: "object",
    version: 1
  },
  section-name: "The Real and Complex Number Systems: The Extended Real Number System"
}
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[The Real Field]]"
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

#### Definition 1.24:
The **==extended real number system==** consists of the [[The Real Field|Real Field]] $\large \Bbb R$, alongside two additional symbols denoted $\large{+\infty}$ and $\large {-\infty}$. These symbols preserve the [[Orders and Ordered Sets#Definition 1.5|Order]] of $\large \Bbb R$ through the property $\large{\forall x \in \Bbb R-\infty< x  < +\infty}$. Numbers in the extended real number system which are not $\large{+\infty}$ or $\large{-\infty}$ are called **==finite==**.

##### Note 1: 
With the inclusion of the symbol $\large +\infty$ it is clear that any nonempty subset of $\large \Bbb R$ has a [[Bounds and Bounded Sets#Definition 1.8|least-upper-bound]]. If $\large E \subset \Bbb R$ is nonempty and is [[Bounds and Bounded Sets#Definition 1.7|Bounded Above]] than by [[The Real Field#Theorem 1.19(The Existence Theorem)|Theorem 1.19]] we know $\large E$ has a [[Bounds and Bounded Sets#Definition 1.8|Supremum]] in $\large \Bbb R$. If $\large{E \subset \Bbb R}$ is nonempty and is not [[Bounds and Bounded Sets#Definition 1.7|Bounded Above]] then $\large{\operatorname{sup} E = +\infty}$. The exact same reasoning follows with the [[Bounds and Bounded Sets#Definition 1.8|greatest-lower-bound]] and $\large{- \infty}$.

##### Note 2:
The extended real number system does not constitute a [[Fields and Ordered Fields#Definition 1.12|Field]] but regardless, the following conventions are defined:
- a) If $\large{x \in \Bbb R}$ then $\large{x+\infty=+\infty, \quad x-\infty=-\infty, \quad \frac{x}{+\infty} = \frac{x}{-\infty}= 0}$ 
- b) If $\large{x > 0}$ then $\large{x(+\infty)=\infty, \quad x(-\infty) = -\infty}$
- c) If $\large{x<0}$ then $\large{x(+\infty) = -\infty, \quad x(-\infty) = +\infty}$ 