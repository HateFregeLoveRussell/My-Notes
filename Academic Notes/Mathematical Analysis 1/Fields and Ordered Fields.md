---
type: Academic
tags:
alias: Math-An-1-FieldsDefinition
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
  section-name: "The Real and Complex Number Systems: Fields",
  ISBN: "978-0-07-054235-8",
  book-title: "Principles of Mathematical Analysis",
  class-alias:  Math-An-1,
  source-alias: Math-An-1-TheRealAndComplexNumberSystems-Fields,
  start-page: 5,
  end-page: 8,
  template: {
    name: "source-tbsection-obj",
    version: 1,
    type: "object"
  }
}
status: {
  state: "Completed",
  template: {
    name: "status-obj",
    version: 1,
    type: "object"
  }
}
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Orders and Ordered Sets]]"
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
#### Definition 1.12:
A **==field==** is a set $\large F$ with two operations defined on it, called **==addition==** and **==multiplication==**, these operations must satisfy the **==field axioms==** denoted as (A), (M), and (D) which are defined below: 

##### (A) Axioms of Addition:
- (A1) If $\large{x \in F}$ and $\large {y \in F}$, then their sum $\large{x + y \in F}$ 
- (A2) Addition must be Commutative: $\large{\forall x,y \in F:x + y = y +x}$ 
- (A3) Addition must be Associative: $\large {\forall x,y,z \in F:(x + y) + z = x + (y + z)}$ 
- (A4) $\large F$ must contain an element denoted $\large 0$ such that $\large {\forall x \in F :x + 0 = x}$  
- (A5) For every element $\large {x \in F}$ there must correspond an element denoted $\large{-x \in F}$ such that $\large {x + (-x) = 0}$ 

##### (M) Axioms of Multiplication
- (M1) If $\large {x \in F}$ and $\large {y \in F}$ then their product $\large{xy \in F}$ 
- (M2) Multiplication must be Commutative: $\large{\forall x,y \in F: xy = yx}$ 
- (M3) Multiplication must be Associative: $\large {\forall x,y,z \in F:(xy)z = x(yz)}$ 
- (M4) $\large F$ must contain an element denoted $\large {1\ne0}$ such that $\large {\forall x \in F :1x = x}$
- (M5) If $\large {x \in F}$ and $\large {x \ne 0}$ then there exists an element denoted $\large{1/x \in F}$ such that $\large {x*(1/x)=1}$ 

##### (D) The Distributive Law
- The statement $\large {x(y + z) = xy + xz}$ must hold for all $\large{x \in F, y \in F, z\in F}$


##### Example:
- $\large \Bbb Q$ is clearly a field if addition and Multiplication hold their customary meanings


#### Definition 1.17: 
An **==Ordered Field==** is a [[Fields and Ordered Fields#Definition 1.12|Field]] $\large F$ which is also an [[Orders and Ordered Sets#Definition 1.6|Ordered Set]] such that:
- I) If $\large{x,y,z \in F}$ and $\large{y \lt z}$ then $\large{x + y \lt x + z}$ 
- II) If $\large{x \in F, y \in F}$ and $\large{x > 0, y > 0}$ then $\large{xy \gt 0}$
If $\large x\gt 0$ we say $\large x$ is **==positive==**, if $\large x \lt 0$ we call it **==negative==**

##### Note:
All familiar rules for working with inequalities apply in every ordered field. multiplication by a positive quantity will preserve the inequality, while multiplication by a negative quantity will reverse it. No square is negative, etc. These results can be seen in [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18]].

##### Example:
- $\large \Bbb Q$ is an ordered field