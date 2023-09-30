---
type: Academic
tags: [practice]
alias: Math-Am-1-Ch1PP-Q18
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
relationship: {name: standard-relationship-obj, version: 1}
child: "[[Chapter 1 Practice Problems]]"
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
template: {name: class-textbook-practice-problem, version: 1}
---
#### Theorem 1.Q18:
If $\large{k \ge 2}$ and $\large{\textbf x \in \Bbb R^k}$ then there exists some $\large{\textbf y \in \Bbb R^k}$ such that $\large{\textbf y \ne \textbf 0}$ but $\large{\textbf x . \textbf y = 0}$.

##### Proof:
Consider the [[Euclidean Spaces#Definition 1.36|vector]] $\large{\textbf y \in \Bbb R ^k }$ where $\large{y_1 = x_2}$, $\large{y_2 = -x_1}$ and $\large{y_i = 0}$ for all $\large{3 \le i \le k}$ then $\large{\textbf x . \textbf y = \sum_{i =1}^k{x_iy_i} = x_1y_1 + x_2y_2 + \sum_{i =3}^k{x_iy_i} = x_1x_2 - x_2x_1 + \sum_{i = 3}^k {0} = x_1x_2 - x_2x_1 = 0}$. Note that if $\large{k = 1}$ then $\large{\textbf x . \textbf y = x_1y_1 }$ which can only equal $\large{0}$ if $\large{\textbf y = \textbf 0}$.