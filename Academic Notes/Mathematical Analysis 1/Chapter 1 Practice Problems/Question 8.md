---
type: Academic
tags: [practice]
alias: Math-An-1-Ch1PP-Q8
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

#### Theorem 1.Q8:
There is no [[Orders and Ordered Sets#Definition 1.5|Order]] that can be defined in the [[The Complex Field#Theorem 1.25|Complex Field]] that turns it into an [[Fields and Ordered Fields#Definition 1.17|Ordered Field]].

##### Proof:
Suppose $\large{\Bbb C}$ was an [[Fields and Ordered Fields#Definition 1.17|Ordered Field]] then some [[Orders and Ordered Sets#Definition 1.5|Ordering]] between $\large{0\in \Bbb C}$ and $\large{i \in \Bbb C}$ so either $\large{i = 0}$ or $\large{0 < i}$ or $\large{0 > i}$.

###### Case I ($\large{i = 0}$):
If $\large{i = 0}$ then $\large{i^2 = 0}$ but we know $\large{i^2 = -1}$ leading to contradiction.

###### Case II ($\large{0 > i}$):
If $\large{0 > i}$ then by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(c)]] we know that $\large{0*i < i^2}$ by [[Properties of Fields and Ordered Fields#Proposition 1.16|Proposition 1.16(a)]] this would mean that $\large{0 < i^2}$ which means that $\large{0 < -1}$. We know that by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(d)]] that $\large{1 > 0}$ applying [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(c)]] to this we see that $\large{-1 < 0}$ contradicting our previously derived statement of $\large{0 < -1}$.

###### Case III ($\large{0 < i}$): 
if $\large{0 < i}$ then by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] it is true that $\large{0*i < i^2}$, by [[Properties of Fields and Ordered Fields#Proposition 1.16|Proposition 1.16(a)]] this would mean that $\large{0 < i^2}$ which means that $\large{0 < -1}$.We know that by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(d)]] that $\large{1 > 0}$ applying [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(c)]] to this we see that $\large{-1 < 0}$ contradicting our previously derived statement of $\large{0 < -1}$.

So it stands to say that no [[Orders and Ordered Sets#Definition 1.5|Ordering]] exists such that $\large{\Bbb C}$ is an [[Fields and Ordered Fields#Definition 1.17|Ordered Field]].