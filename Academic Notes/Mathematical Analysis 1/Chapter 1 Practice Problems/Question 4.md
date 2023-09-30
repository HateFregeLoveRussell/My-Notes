---
type: Academic
tags: [practice]
alias: Math-An-1-Ch1PP-Q4
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

#### Theorem 1.Q4:
If $\large{E}$ be a nonempty subset of an [[Orders and Ordered Sets#Definition 1.6|Ordered Set]] with $\large{\alpha}$ as it's [[Bounds and Bounded Sets#Definition 1.7|Lower Bound]] and $\large{\beta}$ it's [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] then $\large{\alpha \le \beta}$.

##### Proof:
Suppose that $\large{\alpha}$ is a [[Bounds and Bounded Sets#Definition 1.7|Lower Bound]] of $\large{E}$, then $\large{\forall x \in E(x \ge \alpha)}$, similarly suppose that $\large{\beta}$ is the [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{E}$ and hence $\large{\forall x \in E(x \le \beta)}$. Assume that $\large{x}$ is an arbitrary member of $\large{E}$ then clearly $\large{\alpha \le x \le \beta}$ so $\large{\alpha \le \beta}$.
