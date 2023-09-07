---
type: Academic
tags:
alias: Math-An-1-SchwarzInequality
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
friends: ["[[Conjugates and Absolute Values]]", "[[The Complex Field]]"] 
status: {
  state: "In Progress",
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

#### Notation:
Let $\large{x_1,\ldots ,x_n}$ be $\large n$ [[The Complex Field#Definition 1.24|Complex Numbers]] we write $$x_1 + x_2 + \ldots + x_n = \sum_{j=1}^{n}{x_j} $$
#### Theorem 1.35
If $\large{a_1,\ldots ,a_n}$ and $\large{b_1,\ldots ,b_n}$ are [[The Complex Field#Definition 1.24|Complex Numbers]] then $$\left \vert \sum^n_{j=1}a_j\overline b_j \right \vert \le \sum_{j=1}^n\left \vert a_j \right \vert + \sum ^n _{j = 1}\left \vert b_j \right \vert$$
##### Proof: 
We will denote a few quantities to make our arithmetic easier. Additionally, note that all sums in this proof range from index $\large 1$ to $\large n$.

Let $\large{A = \sum \left \vert a_j \right \vert^2}$, $\large{B = \sum \left \vert b_j \right \vert^2}$, and $\large{C=\sum a_j \overline{b_j}}$.

If $\large{B = 0}$ then $\large{b_1, \ldots, b_n = 0}$ by [[Conjugates and Absolute Values#Theorem 1.33|Theorem 1.33(a)]] In which case the result is a trivial consequence of [[Conjugates and Absolute Values#Theorem 1.33|Theorem 1.33(d)]]. So henceforth $\large {B \ne 0}$. 
Note that $\large B$ is a sum of positive numbers if $\large B \ne 0$ by [[Conjugates and Absolute Values#Theorem 1.33|Theorem 1.33(a)]] so $\large{B > 0 }$. Consider the sum $\large{\sum \left \vert B a_j - C b_j \right \vert ^2}$, by [[Conjugates and Absolute Values#Definition 1.32|Definition 1.32]] we know that $\large{\sum \left \vert B a_j - C b_j \right \vert ^2 = \sum(Ba_j - Cb_j)\overline{(Ba_j - Cb_j)}}$. Using [[Conjugates and Absolute Values#Theorem 1.31|Theorem 1.31(a) and Theorem 1.31(b)]]  we see that $\large{\sum \left \vert B a_j - C b_j \right \vert ^2 = \sum (Ba_j - Cb_j)(\overline B \overline a_j - \overline {C} \  \overline b_j)}$. Since $\large{B \in \Bbb R}$ we know that $\large{\overline B = B}$ so $\large{\sum \left \vert B a_j - C b_j \right \vert ^2 = \sum (Ba_j - Cb_j)(B\overline a_j - \overline C \ \overline b_j)}$. Multiplying the two terms using the rules of multiplication from the [[The Complex Field|Complex Field]] we see that $\large{\sum \left \vert B a_j - C b_j \right \vert ^2 = \sum{B^2a_j\overline{a_j} -  B\overline{C}\overline{b_j}a_j} -Cb_j\overline{B}\overline{a_j} + Cb_j\overline{Cb_j}}$ Distributing the Sum operator $\large{\sum \left \vert B a_j - C b_j \right \vert ^2 = \sum{B^2a_j\overline{a_j} -  \sum B\overline{C}\overline{b_j}a_j} -\sum Cb_j B \overline{a_j} + \sum Cb_j\overline{Cb_j}}$  Common factoring through [[Fields and Ordered Fields#(D) The Distributive Law|The Distributive Axiom]] of the [[The Complex Field|Complex Field]] we get the equality:  $\large{\sum \left \vert B a_j - C b_j \right \vert ^2 =  B^2 \sum a_j\overline{a_j} - B \overline{C} \sum \overline{b_j} a_j - CB \sum b_j\overline{a_j} + C\overline C \sum b_j\overline{b_j}}$. Applying the definition of $\large B,C, A$ and [[Conjugates and Absolute Values#Definition 1.32|Definition 1.32]] we see that $\large{\sum \left \vert B a_j - C b_j \right \vert ^2 =  B^2 \sum |a_j|^2 - B \overline{C} C - CB \sum b_j\overline{a_j} + |C|^2\sum |b_j|^2= B^2 A- B |C|^2 - CB \sum b_j\overline{a_j} + |C|^2B}$ Finally notice that $\large{\sum b_j\overline a_j = \sum \overline{\overline b_j a_j} = \overline {\sum{\overline b_j a_j}} = \overline C}$  by [[Conjugates and Absolute Values#Theorem 1.31|Theorem 1.31(a) and (b)]] so $\large$ $\large{B^2 A- B |C|^2 - CB \sum b_j\overline{a_j} + |C|^2B= B^2 A- B |C|^2 - CB\overline C + |C|^2B = B^2 A- B |C|^2 - |C|^2B + |C|^2B}$ Common Factoring through [[Fields and Ordered Fields#(D) The Distributive Law|The Distributive Axiom]] and applying [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A4)]]we see that $\large{\sum \left \vert B a_j - C b_j \right \vert ^2 = B^2A - |C|^2B = B(AB - |C|^2)}$. Looking at the left hand side of the equality we see that it is a sum of non-negative real numbers, hence it stands to say $\large{B(AB- |C|^2) \ge 0}$. We already know that $\large{B > 0}$ so applying [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] of the [[The Real Field|Real Field]] we see that $\large{AB - |C|^2 \ge 0}$. Rearranging through [[Fields and Ordered Fields#Definition 1.17|Property I]] of the [[The Real Field|Real Field]] we see that $\large{AB \ge |C|^2}$ which is precisely the desired inequality. 