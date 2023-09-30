---
type: Academic
tags: [practice]
alias: Math-An-1-Ch1PP-Q1
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

#### Theorem 1.Q1:
If $\large{r \in \Bbb Q}$ and $\large{r \ne 0}$ and $\large{x}$ is an irrational quantity then $\large{r + x}$ and $\large{rx}$ are both irrational.

##### Proof:
Suppose that $\large{r \in \Bbb Q}$ and $\large{r \ne 0}$. Then $\large{r = \frac{p}{q}}$, where $\large{p \in \Bbb Z, p \ne 0, q \in \Bbb Z, q \ne 0}$. Now assume that $\large{x}$ is some irrational quantity. If $\large{rx}$ was rational then $\large{rx = \frac{a}{b}}$ for some $\large{a \in \Bbb Z, b \in \Bbb Z, b  \ne 0}$ so $\large{\frac{p}{q}x = \frac{a}{b}}$, rearranging tells us that $\large{x = \frac{aq}{pb}}$ since the product of integers are always integers and $\large{p \ne 0, b \ne 0 \implies pb \ne 0}$ we know that $\large{x \in \Bbb Q}$. But this is impossible as we defined $\large{x}$ as an irrational quantity, hence the product $\large{rx}$ cannot be rational. 

Now suppose that $\large{r + x}$ is rational or in other words that $\large{r + x = \frac{a}{b}}$ for some $\large{a \in \Bbb Z, b \in \Bbb Z, b \ne 0}$. Then $\large{\frac{p}{q} + x = \frac{a}{b}}$, rearranging the equality yields $\large{x = \frac{a}{b} - \frac{p}{q}}$ so $\large{x = \frac{aq - bp}{bq}}$ since products and differences of integers product integers and $\large{b \ne 0, q\ne 0 \implies bq\ne 0}$ we can then say that $\large{x}$ is rational which contradicts our assumption. Hence the sum $\large{r +x}$ must be irrational.