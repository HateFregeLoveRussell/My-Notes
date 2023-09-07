---
type: Academic
tags:
alias: Math-An-1-ConnectionTraditionArithmeticComplexFieldArithmetic
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
  ISBN: "978-0-07-054235-8",
  class-alias: "Math-An-1",
  book-title: "Principles of Mathematical Analysis",
  source-alias: "Math-An-1-TheRealAndComplexNumberSystems-TheComplexField",
  end-page: 16,
  start-page: 12,
  section-name: "The Real and Complex Number Systems: The Complex Field",
  template: {
    name: "source-tbsection-obj",
    type: "object",
    version: 1
  }
}
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[The Complex Field]]"
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

#### Introduction:
The following theorems will show how our [[The Complex Field#Theorem 1.25|Definition of the Complex Numbers]] which lacks any mention of the square root of $\large{-1}$ is arithmetically equivalent to the traditional definition using $\large{i}$.


#### Definition 1.27:
We will denote $\large{i = (0,1)}$ 

#### Theorem 1.28: 
$\large{i^2 = -1}$ 
##### Proof: 
$\large{i^2 = (0,1)(0,1) = (0*0 - 1*1, 0*1+1*0)}$ this expression is equivalent to $\large{(1,0) = 1}$ by the use of [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M4)]], [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A4)]], and [[Properties of Fields and Ordered Fields#Proposition 1.16|Proposition 1.16(a)]] in the [[The Real Field|Real Field]].

#### Theorem 1.29:
If $\large{a,b \in \Bbb R}$ then $\large{(a,b) = a + bi}$
##### Proof: 
$\large{a + bi = (a,0)+(b,0)(0,1) = (a,0) + (b*0 - 0*1)}$. Apply [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M4)]], [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A4)]], [[Properties of Fields and Ordered Fields#Proposition 1.16|Proposition 1.16(a)]], and [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A5)]] in the [[The Real Field|Real Field]] to get $\large{a + bi = (a,0) + (0,b) = (a,b)}$ 