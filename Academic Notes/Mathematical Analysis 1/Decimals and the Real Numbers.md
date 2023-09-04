---
type: Academic
tags:
alias: Math-An-1-DecimalsAndRealNumbers
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
  section-name: "The Real and Complex Number Systems: The Real Field",
  ISBN: "978-0-07-054235-8",
  book-title: "Principles of Mathematical Analysis",
  class-alias: Math-An-1,
  source-alias: Math-An-1-TheRealAndComplexNumberSystems-TheRealField,
  start-page: 8,
  end-page: 11,
  template: {
    name: "source-tbsection-obj",
    version: 1,
    type: "object"
  }
}
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[The Real Field]]"
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
#### The Decimals
Let $\large{x > 0}$ be a real number. Let $\large{n_0}$ be the largest integer such that $\large{n_0 \le x}$( The existence of $\large{n_0}$ depends on the [[Properties of the Real Field#Theorem 1.20|The Archimedean Property]]). Having chosen $\large{n_0, n_1, \ldots, n_{k-1}}$, let $\large n_k$ be the largest integer such that $\large{n_0+ \frac{n_1}{10} + \ldots + \frac{n_k}{10^k} \le x}$.
Let $\large{E}$ be the set of these numbers $\large{n_0+ \frac{n_1}{10} + \ldots + \frac{n_k}{10^k}}$ then $\large {x = \operatorname{sup} E}$. The **==decimal expansion==** of $\large x$ is $\large{n_0.n_1n_2n_3\ldots}$. 
Conversely, for any infinite decimal expansion, the set $\large E$ is [[Bounds and Bounded Sets#Definition 1.7|Bounded Above]] and the decimal expansion is the [[Bounds and Bounded Sets#Definition 1.8|Supremum]] of $\large {E}$