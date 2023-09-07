---
type: Academic
tags:
alias: Math-An-1-ConjugatesAndAbsValue
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
friends: ["[[The Complex Field]]", "[[Connection Between Tradition Complex Arithmetic And Complex Field Arithmetic]]"]
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
The following theorems pertain to the Complex Conjugate and the Absolute Value operation, which prove to be very useful tools in the [[The Complex Field|Complex Field]].

#### Definition 1.30:
If $\large{a,b \in \Bbb R}$ and $\large{z = a + bi}$ then $\large{\overline{z}  = a - bi}$ called the **==Complex Conjugate==** of $\large{z}$. The numbers $\large{a}$ and $\large b$ are called the **==Real Part==** denoted $\large{\operatorname{Re}(z)}$ and **==Imaginary Part==** denoted $\large{\operatorname{Im(z)}}$ respectively. 

#### Theorem 1.31:
If $\large{z,w}$ are [[The Complex Field#Definition 1.24|Complex Numbers]] then
- (a) $\large{\overline{z + w} = \overline z + \overline w}$ 
- (b) $\large{\overline{zw} = \overline{z}*\overline{w}}$ 
- (c) $\large{z + \overline z = 2 \operatorname{Re}(z) \quad z - \overline z = 2i \operatorname{Im}(z)}$ 
- (d) $\large{z\overline z}$ is both [[The Real Field|Real]] and positive except when $\large{z = 0}$

##### Proof: 
For all proofs below we let $\large{z = (a,b) = a + bi,\quad w = (c,d) = c + di}$
- (a): $\large{\overline{z +w} = \overline {a + bi + c + di}  = \overline{(a +c) + (b + d)i}}$ by the [[Fields and Ordered Fields#(D) The Distributive Law|The Distributive Axiom (D)]] of the [[The Complex Field|Complex Field]]. $\large{\overline{(a +c) + (b + d)i} = (a + c) - (b +d)i}$  by [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A1)]] of the [[The Complex Field|Complex Field]] in combination with [[Conjugates and Absolute Values#Definition 1.30|Definition 1.30]]. $\large{(a + c) - (b +d)i = a + c - bi -di = a -bi + c - di= \overline z +  \overline w}$ by the [[Fields and Ordered Fields#(D) The Distributive Law|The Distributive Axiom (D)]] of the [[The Complex Field|Complex Field]].
- (b): $\large{\overline{zw} = \overline{(a + bi)(c + di)} = \overline{ac - bd + (bc + ad)i}}$ by the definition of Multiplication under the [[The Complex Field|Complex Field]]. Applying [[Conjugates and Absolute Values#Definition 1.30|Definition 1.30]] we find that$\large{\overline{zw} = ac - bd - (bc + ad)i}$. Applying the [[Fields and Ordered Fields#(D) The Distributive Law|Distributive Axiom]] we see that $\large{\overline{zw} = ac - bd -bci -adi}$. Applying the [[Fields and Ordered Fields#(D) The Distributive Law|Distributive Axiom]] again we find that $\large{\overline{zw} = c(a -bi) -bd -adi}$. Through [[Properties of Fields and Ordered Fields#Proposition 1.14|Proposition 1.14(d)]] and [[Connection Between Tradition Complex Arithmetic And Complex Field Arithmetic#Theorem 1.28|Theorem 1.28]] we get the following result $\large{\overline{zw} = c(a-bi) - --bd - adi = c(a-bi)- -i^2bd - adi}$. Common factoring through [[Fields and Ordered Fields#(D) The Distributive Law|The Distributive Axiom]] twice we see that $\large{\overline{zw} = c(a-bi)-id(a -ib) = (c - id)(a -ib)}$. Which by [[Conjugates and Absolute Values#Definition 1.30|Definition 1.30]] gives us $\large{\overline{zw} = \overline w*\overline z}$   
- (c): $\large{z + \overline z = a + bi + \overline{a + bi} = a + bi + a - bi}$ by [[Conjugates and Absolute Values#Definition 1.30|Definition 1.30]]. Using [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A4)]] of the [[The Complex Field|Complex Field]] we see that $\large{z + \overline z = a + a = 2*a = 2*\operatorname{Re}(z)}$. $\large{z - \overline z = a + bi - \overline{a + bi} = a + bi -(a - bi)}$ by [[Conjugates and Absolute Values#Definition 1.30|Definition 1.30]]. Applying the [[Fields and Ordered Fields#(D) The Distributive Law|Distributive Axiom]] in the [[The Complex Field|Complex Field]] we see that $\large{z - \overline z = a + bi -a --bi}$. Through [[Properties of Fields and Ordered Fields#Proposition 1.14|Proposition 1.14(d)]] and [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A4)]] of the [[The Complex Field|Complex Field]] the equality turns to $\large{z - \overline z = bi + bi = 2ib = 2i\operatorname{Im}(z)}$  
- (d): $\large{z\overline z = (a + bi)\overline{(a + bi)}}$ which by [[Conjugates and Absolute Values#Definition 1.30|Definition 1.30]] is equivalent to $\large{(a + bi)(a - bi)}$. Multiplying the two terms using the defined multiplication operator of the [[The Complex Field|Complex Field]] we see that $\large{z\overline z = (a^2 + b^2 + bi - bi)}$. Applying [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A4)]] in the [[The Complex Field|Complex Field]] we reach the conclusion that $\large{z\overline z = (a^2 + b^2)}$.Assume $\large z$ is nonzero, we know that $\large{a^2 + b^2 \in \Bbb R}$ by [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A1)]] and [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M1)]] of the [[The Real Field|Real Field]].Finally by applying the same reasoning as the first paragraph of [[The Complex Field#Proof of (M5)|the Proof of Axiom (M5) in the Complex Field]] we see that $\large{z\overline z = a^2 + b^2 > 0 }$ completing the proof.


#### Definition 1.32:
If $\large z$ is [[The Complex Field#Definition 1.24|Complex Number]] its **==Absolute Value==** denoted $\large{|z|}$ is the non-negative square root of $\large{z\overline z}$, in other words $\large{|z| = {(z\overline z)^\frac{1}{2}}}$ 

##### Note: 
- Notice how both the existence and uniqueness of $\large{|z|}$ is guaranteed by [[Properties of the Real Field#Theorem 1.21|Theorem 1.21]]
- Additionally note that when $\large{x \in \Bbb R}$ then $\large{\overline x = x}$ (This fact can be proven trivially from [[Conjugates and Absolute Values#Theorem 1.31|Theorem 1.31(c)]]) and so $\large{|x| = \sqrt{x^2}}$. Thus $\large{|x| = x}$ when $\large{x > 0}$ and $\large{|x| = -x}$ when $\large{x < 0}$.


#### Theorem 1.33:
Let both $\large{z}$ and $\large{w}$ be [[The Complex Field#Definition 1.24|Complex Numbers]] then
- (a) $\large{|z| > 0 }$ unless $\large{z = 0}$, in which case $\large{|0| = 0}$ 
- (b) $\large{|\overline z| = |z|}$ 
- (c) $\large{|zw| = |z| |w| }$ 
- (d) $\large{|\operatorname{Re}(z)| \le |z|}$ 
- (e) $\large{|z+w| \le |z| + |w|}$ 

##### Proof:
- (a): Assume $\large{z \ne 0}$, then by [[Conjugates and Absolute Values#Theorem 1.31|Theorem 1.31(d)]] $\large{z\overline z \in \Bbb R}$ and $\large{z\overline z > 0}$. Applying [[Properties of the Real Field#Theorem 1.21|Theorem 1.21]] we see that $\large{|z| = \sqrt{z\overline z} > 0}$. Assume that $\large{z = 0}$ then $\large{z\overline z = (0)(0) = 0}$ by [[Conjugates and Absolute Values#Definition 1.30|Definition 1.30]] and [[Properties of Fields and Ordered Fields#Proposition 1.16|Proposition 1.16(a)]] in the [[The Complex Field|Complex Field]].
- (b): note that $\large{|\overline z| = \sqrt{\overline{z} \ \overline{\overline z}}}$, by [[Conjugates and Absolute Values#Definition 1.32|Definition 1.32]]. Now suppose that $\large{z = (a +bi)}$ then by [[Conjugates and Absolute Values#Definition 1.30|Definition 1.30]] $\large{\overline z = a -bi}$. Applying the definition again we see that $\large{\overline{\overline z} = a --bi }$ which by [[Properties of Fields and Ordered Fields#Proposition 1.14|Proposition 1.14(d)]] is equivalent to $\large{\overline{\overline z} = a + bi = z}$. Applying this fact to $\large{|\overline z|}$ we see that $\large{|\overline z|  = \sqrt{\overline z z}}$. Now applying [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M2)]] of the [[The Complex Field|Complex Field]] alongside [[Conjugates and Absolute Values#Definition 1.32|Definition 1.32]] again, we see that $\large{\sqrt{\overline z z} = \sqrt{z \overline z} = |z|}$
- (c): By [[Conjugates and Absolute Values#Definition 1.32|Definition 1.32]] we see that $\large{|zw| = \sqrt{zw\overline{zw}}}$. Using [[Conjugates and Absolute Values#Theorem 1.31|Theorem 1.31(b)]] and rearranging using [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M2)]] of the [[The Complex Field|Complex Field]] we get the equality $\large{|zw| = \sqrt{z\overline z w \overline w}}$. Use [[Properties of the Real Field#Corollary|Corollary 1.21]] to split the square root to get the equality $\large{|zw| = \sqrt{z \overline z} \sqrt{w \overline w}}$. Finally applying [[Conjugates and Absolute Values#Definition 1.32|Definition 1.32]] again we can complete the proof through the equality $\large{|zw| = |z||w|}$ 
- (d): Let $\large{z = a + bi}$. Then by following the reasoning of [[Conjugates and Absolute Values#Theorem 1.31|the proof of Theorem 1.31(d)]] we see that $\large{|z|^2 = a^2 + b^2}$, additionally by [[Conjugates and Absolute Values#Theorem 1.33|Theorem 1.33(a)]] we know that $\large{a^2 + b^2 \ge 0}$. By [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M1)]] of the [[The Real Field|Real Field]] we know that $\large{b^2 \in \Bbb R}$ so by applying [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(d)]] we see that $\large{b^2 \ge 0 }$. Adding the quantity $\large{a^2 \in \Bbb R}$ to both sides of the inequality using [[Fields and Ordered Fields#Definition 1.17|Property I of an Ordered Field]] in the [[The Real Field|Real Field]] we get $\large{a^2 + b^2 \ge a^2}$. Since $\large{a^2 + b^2 \ge 0}$ we can take the square root of both sides to get $\large{\sqrt{a^2 + b^2} \ge \sqrt{a^2}}$ which by [[Conjugates and Absolute Values#Definition 1.32|Definition 1.32]] alongside our previous findings means that $\large{|z| \ge |\operatorname{Re}(z)|}$ 
- (e): Note that $\large{|z + w|^2 = (z + w)\overline{(z + w)}}$. Apply [[Conjugates and Absolute Values#Theorem 1.31|Theorem 1.31(a)]] we get $\large{|z + w|^2 = (z + w)(\overline z + \overline w)}$. Multiplying the two terms using the definition of multiplication alongside it's [[Properties of Fields and Ordered Fields|Properties]]in the [[The Complex Field|Complex Field]] we get $\large{|z + w|^2 = z\overline z + z \overline w + w \overline z + w \overline w }$. Now consider the quantity $\large{\overline{\overline w z}}$, by [[Conjugates and Absolute Values#Theorem 1.31|Theorem 1.31 (b)]] we see that $\large{\overline{\overline w z} = \overline{\overline w} \overline z}$. Using the intermediate result $\large{\overline{\overline z} = z}$ from the Proof of Theorem 1.33(d) we see that $\large{\overline{\overline w z} = w\overline z}$. From this result we can obtain $\large{|z + w|^2 = z\overline z + w \overline w + \overline{\overline w z} + \overline w z}$ by substitution. Applying [[Conjugates and Absolute Values#Theorem 1.31|Theorem 1.31(c)]] we see that $\large{|z + w|^2 = |z|^2 +|w|^2 +2 \operatorname{Re}(\overline z w)}$. We know that $\large{\operatorname{Re}(\overline z w) \le |\overline z w|}$ So by [[Fields and Ordered Fields#Definition 1.17|Property I of an Ordered Field]] in [[The Real Field|Real Field]] alongside [[Conjugates and Absolute Values#Theorem 1.33|Theorem 1.33(a)]] we know that $\large{|z+w|^2 \ge |z|^2 + |w|^2 + |\overline z w|}$. Applying [[Conjugates and Absolute Values#Theorem 1.33|Theorem 1.33(b)]] and [[Conjugates and Absolute Values#Theorem 1.33|Theorem 1.33(c)]] we see that $\large{|z+w|^2 \ge |z|^2 + |w|^2 + |z| |w|}$ which through the [[Fields and Ordered Fields#(D) The Distributive Law|Distributive Axiom (D)]] of the [[The Complex Field|Complex Field]] means that $\large{|z + w|^2 \ge (|z| + |w|)^2}$, the proof is complete by taking square roots of both sides of the inequality. 