---
type: Academic
tags: [practice]
alias: Math-An-1-Ch1PP-Q5
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
#### Theorem 1.Q5:
If $\large{A}$ is an nonempty subset of the [[The Real Field|Real Numbers]] which is [[Bounds and Bounded Sets#Definition 1.7|Bounded Below]] and the set $\large{-A}$ is defined to be composed of elements $\large{-x:x\in A}$ it is true that $\large{\operatorname{inf} A = -\operatorname{sup}(-A)}$.

##### Proof:
Let $\large{\alpha = \operatorname{inf}A}$. Suppose that $\large{x \in A}$ then $\large{x \ge \alpha}$ by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition1.18(c)]] we know that $\large{-x < -\alpha}$ we can then relax the inequality to get $\large{-x \le -\alpha}$. So $\large{-\alpha}$ is an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{-A}$.

Suppose there exists some real number $\large{\gamma}$ which is an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{-A}$ so $\large{-x \le \gamma}$ for all $\large{-x \in -A}$, by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(c)]] and [[Properties of Fields and Ordered Fields#Proposition 1.14|Proposition 1.14(d)]] we know that $\large{x > -\gamma}$, relaxing the inequality we get $\large{x \ge -\gamma}$ so $\large{-\gamma}$ is a [[Bounds and Bounded Sets#Definition 1.7|Lower Bound]] of $\large{A}$. Since $\large{\alpha}$ is the [[Bounds and Bounded Sets#Definition 1.8|Infimum]] of $\large{A}$ we know that $\large{\alpha \ge -\gamma}$, applying [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(c)]] and [[Properties of Fields and Ordered Fields#Proposition 1.14|Property 1.14(d)]] again we get $\large{-\alpha \le \gamma}$. Since $\large{-\alpha}$ is an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{-A}$ and for any arbitrary [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{-A}$ denoted $\large{\gamma}$ we know that $\large{-\alpha \le \gamma}$ so $\large{-\alpha = \operatorname{sup}(-A)}$ so $\large{\alpha = -\operatorname{sup}(-A)}$ meaning that $\large{\operatorname{inf}(A) = -\operatorname{sup}(-A)}$. 