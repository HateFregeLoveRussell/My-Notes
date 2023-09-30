---
type: Academic
tags: [practice]
alias: Math-An-1-Ch1PP-Q3
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
#### Theorem 1.Q3:
[[Properties of Fields and Ordered Fields#Proposition 1.15|Proposition 1.15 is true]]

##### Proof:
###### a) 
Assume that $\large{x \ne 0}$ and $\large{xy = xz}$
by [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M4)]] we know that $\large{y = y*1}$ but by [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M5)]] we know that $\large{y*1 = y(x*\frac{1}{x})}$. Additionally by [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M3)]] we see that $\large{y(x*\frac{1}{x}) = y*x*\frac{1}{x}}$ which by substitution means that $\large{y = xz*\frac{1}{x}}$. Finally using [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M4) and Axiom (M5)]] in conjunction allows us to say that $\large{y = x}$ 

###### b)
Suppose that $\large{x \ne 0 }$ and $\large{xy = x}$
By [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M4) and Axiom (M5)]] we know that $\large{y = y*(x*\frac{1}{x})}$ regrouping by [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M3)]] we see that $\large{y = (yx)\frac{1}{x}}$, substituting the latter assumption we get the result $\large{y= x\frac{1}{x}}$ finally applying [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M5)]] we can see that $\large{y = 1}$

###### c)
Assume that $\large{x \ne 0, xy = 1}$
then by [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M4) and Axiom (M5)]]we can see that $\large{y= y(x\frac{1}{x})}$ which can be regrouped by [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M3)]] to get $\large{y = (xy)\frac{1}{x}}$, substituting the latter assumption we get our final result of $\large{y = \frac{1}{x}}$.

###### d)
From [[Properties of Fields and Ordered Fields#Proposition 1.15|Proposition 1.15(c)]] with the arguments of $\large{\frac{1}{x}}$ and $\large{x}$ we see that $\large{x = \frac{1}{1/x}}$ only if $\large{x \ne 0}$.
