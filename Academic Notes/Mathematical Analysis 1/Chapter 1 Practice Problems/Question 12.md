---
type: Academic
tags: [practice]
alias: Math-An-1-Ch1PP-Q12
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
#### Theorem 1.Q12:
If $\large{z_1,\ldots,z_n}$ are [[The Complex Field#Definition 1.24|Complex Numbers]] then $\large{|z_1 + z_2 +\ldots + z_n| \le |z_1| + |z_2| + \ldots + |z_n|}$.

##### Proof:
###### Base Case($\large{n=2}$):
This assertion has been proven in [[Euclidean Spaces#Theorem 1.37|Theorem 1.37(e)]].

###### Induction Step: 
Assume that $\large{|z_1 + z_2 + \ldots + z_{n-1} \le |z_1| + |z_2| + \ldots + |z_{n-1}|}$. Consider the quantity $\large{|z_1 + z_2 + \ldots + z_n| = |(z_1 + z_2 + \ldots + z_{n-1}) + z_n|}$ then by [[Euclidean Spaces#Theorem 1.37|Theorem 1.37(e)]] we know that $\large{|z_1 + z_2 + \ldots + z_n| \le |z_1 + z_2 +\ldots +z_{n-1}| + |z_{n-1}|}$ and by the inductive hypothesis we know that $\large{|z_1 + z_2 + \ldots + z_n| \le |z_1| + |z_2| + \ldots + |z_n|}$.

