---
type: Academic
tags: [practice]
alias: Math-An-1-Ch1PP-Q9
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

#### Theorem 1.Q9:
Suppose that $\large{z = a +bi, w = c + di}$. Define the [[Orders and Ordered Sets#Definition 1.5|Order]] $\large{z < w}$ if $\large{a < c}$ and also if $\large{a = c, b < d}$. Then this type of ordering known as a **==dictionary/lexicographic order==** turns $\large{\Bbb C}$ into an [[Orders and Ordered Sets#Definition 1.6|Ordered Set]]. 

##### Proof:
Let $\large{z = a + bi, w = c + di}$ since $\large{a \in \Bbb R}$ and $\large{c \in \Bbb R}$ and [[The Real Field|The Real Field]] is [[Fields and Ordered Fields#Definition 1.17|Ordered Field]] we know that one of these statements is true $\large{a > c, a=c, c > a}$. Consider the first case, $\large{a > c}$ then $\large{w < z}$ by our definition. Consider the other case where $\large{a < c}$ then $\large{z < w}$. The only case remaining where we have yet to prove that the order is defined is the case where $\large{c =a}$, in this case consider the quantities $\large{b \in \Bbb R}$ and $\large{d \in \Bbb R}$ so by the same reasoning either $\large{b > d, d > b, b=d}$. Consider the first subcase, so $\large{a =c, b> d}$ then by our definition it stands to say that $\large {z > w}$, next consider the case where $\large{a = c, d> b}$ in such a case by our definition it is true that $\large{w > z}$. Finally the case where $\large{a=c, b=d}$ then by [[The Complex Field#Definition 1.24|Definition of equality in the Complex Numbers]] it is true that $\large{z =w }$. So it is true that in all cases an [[Orders and Ordered Sets#Definition 1.5|Order]] is defined in the [[The Complex Field#Definition 1.24|Complex Numbers]]. Furthermore, notice that by the definition of [[Orders and Ordered Sets#Definition 1.5|Order]] makes all cases considered in the proof exclusive to each other, this means that the Ordering we picked is also exclusive, completing the proof.