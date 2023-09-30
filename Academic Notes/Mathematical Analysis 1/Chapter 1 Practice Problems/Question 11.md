---
type: Academic
tags: [practice]
alias: Math-An-1-Ch1PP-Q11
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

#### Theorem 1.Q11: 
If $\large{z \in \Bbb C}$ then there exists some $\large{r \ge 0 }$ and a [[The Complex Field#Definition 1.24|Complex Number]] denoted $\large w$ such that $\large{|w| = 1}$ and $\large{z = rw}$. This pair is always unique unless $\large{z = 0}$.

##### Proof:
Let $\large{z = a + bi}$. Assume that $\large{z \ne0 }$ and let $\large{w = \frac{1}{|z|}z}$ then $\large{w = \frac{a}{|w|} + i\frac{b}{|z|}}$ this would mean that $\large{|w| = \sqrt{a^2/|z|^2 + b^2/|z|^2} = \sqrt{\frac{a^2 + b^2}{|z|^2}} = \sqrt{\frac{|z|^2}{|z|^2}} = \sqrt{1}}$ 
so $\large{|w| = 1}$ let $\large{r = |z| \ge 0}$ so $\large{rw = |z|\frac{z}{|z|}=z}$. If $\large{z =0}$ then $\large{|z| =0}$ and $\large{w}$ can be any [[The Complex Field#Definition 1.24|Complex Number]] such that $\large{|w| = 1}$ and $\large{r =0}$ so $\large{z = rw = 0}$. 