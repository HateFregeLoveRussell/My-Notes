---
type: Academic
tags: 
alias: Math-An-1-PropertiesofFields
class:
  class-name: Mathematical Analysis 1
  author: Walter Rudin
  medium: Textbook
  class-alias: Math-An-1
  title: Principles Of Mathematical Analysis
  edition: Third
  publisher: McGraw-Hill Book Company
  ISBN: 978-0-07-054235-8
  length: 334
  template:
    name: class-textbook-obj
    version: 1
    type: object
source:
  type: tbsection
  section-name: "The Real and Complex Number Systems: Fields"
  ISBN: 978-0-07-054235-8
  book-title: Principles of Mathematical Analysis
  class-alias: Math-An-1
  source-alias: Math-An-1-TheRealAndComplexNumberSystems-Fields
  start-page: 5
  end-page: 8
  template:
    name: source-tbsection-obj
    version: 1
    type: object
relationship:
  name: standard-relationship-obj
  version: 1
friends: "[[Fields and Ordered Fields]]"
status:
  state: Completed
  template:
    name: status-obj
    version: 1
    type: object
validity:
  state: true
  template:
    name: validity-obj
    version: 1
    type: object
template:
  name: class-note-template
  version: 1
---
#### Introduction:
We will proceed to show that some familiar properties of the rational number system are consequences of its classification as a [[Fields and Ordered Fields|Field]]/[[Fields and Ordered Fields#Definition 1.17|Ordered Fields]]. This way once the Real Number System is created as a field we don't need to prove that these properties hold.

#### Proposition 1.14:
The [[Fields and Ordered Fields#(A) Axioms of Addition|axioms of addition]] imply the following statements: 
- (a): If $\large{x + y = x + z}$ then $\large{x = z}$ 
- (b): If $\large{x + y = x}$ then $\large{y = 0}$
- (c): If $\large {x + y = 0}$ then $\large{y = -x}$ 
- (d): $\large{-(-x) = x}$ 
##### Proof:
- (a) Assume that $\large{x + y = x + z}$.
	- $\large {y = y + 0 }$ (A4)
	- $\large {y + 0 = (-x + x) + y}$ (A5)
	- $\large {(-x + x) + y = -x + (x + y)}$ (A3)
	- $\large {-x + (x + y) = -x + (x + z)}$ (First Assumption)
	- $\large {-x + (x + z) = (-x + x) + z}$ (A3)
	- $\large {(-x + x) + z = 0 + z}$ (A5)
	- $\large {0 + z = z}$ (A4)
- (b) This statement can be constructed from (a) by setting $\large {z = 0}$.
- (c) This statement can be constructed from (a) by setting $\large {z = -x}$ 
- (d) This statement can be constructed from (c) by setting $\large x$ to be $\large -x$ and $\large {y = x}$ 

#### Proposition 1.15:
The [[Fields and Ordered Fields#(M) Axioms of Multiplication|axioms of multiplication]] imply the following statements: 
- (a): If $\large {x \ne 0}$ and $\large {xy = xz}$ then $\large {y=z }$
- (b): If $\large {x \ne 0}$ and $\large{xy = x}$ then $\large {y= 1}$
- (c): If $\large {x \ne 0}$ and $\large xy = 1$ then $\large{y = 1/x}$ 
- (d): if $\large{x \ne 0}$ then $\large{1/(1/x) = x}$ 

##### Proof:
proof is near identical to the proof [[Properties of Fields and Ordered Fields#Proof|here]], replace operations and include extra assumption to avoid the case where $\large{x = 0}$ 

#### Proposition 1.16:
The [[Fields and Ordered Fields#Definition 1.12|field axioms]] imply the following statements for any $\large{x,y,z \in F}$.
- (a) $\large{0x = 0}$
- (b) if $\large{x \ne 0}$ and $\large{y \ne 0}$ then $\large{xy \ne 0}$
- (c) $\large{(-x)y = -(xy) = x(-y)}$
- (d) $\large{(-x)(-y) = xy}$

##### Proof: 
- (a): Consider, $\large{0x + 0x = (0 + 0)x = 0x}$ by the application of [[Properties of Fields and Ordered Fields#Proposition 1.14|Proposition 1.14(b)]] we can conclude that $\large 0x = 0$ 
- (b): Assume $\large{x \ne 0, y \ne0}$ but $\large xy=0$. Now consider the statement $\large{1 = \frac{1}{x}\frac{1}{y}xy}$ (by [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom M5]]). By substitution we find that $\large {1=\frac{1}{x}\frac{1}{y}0}$. By applying [[Properties of Fields and Ordered Fields#Proposition 1.16|Proposition 1.16(a)]] we find that $\large{1 = \frac{1}{x}\frac{1}{y}0 = 0}$, which is a contradiction. Meaning that $\large{xy \ne 0}$
- (c): $\large{(-x)y + xy = (-x + x)y}$ [[Fields and Ordered Fields#(D) The Distributive Law|by Axiom D]], $\large{(-x + x)y = 0y}$ [[Fields and Ordered Fields#(A) Axioms of Addition|by Axiom A5]], and by applying [[Properties of Fields and Ordered Fields#Proposition 1.16|Proposition 1.16(a)]] we see that $\large{0y = 0}$. By applying [[Properties of Fields and Ordered Fields#Proposition 1.14|Proposition 1.14(c)]] we see that $\large{(-x)y = -(xy)}$ and so the first equality is proven. Following this line of reasoning again with $\large{x(-y) +xy}$ will result in the second equality. 
- (d): Consider $\large{(-x)(-y) = -[x(-y)]}$ by the first half of [[Properties of Fields and Ordered Fields#Proposition 1.16|Proposition 1.16(c)]]. Apply the first half of [[Properties of Fields and Ordered Fields#Proposition 1.16|Proposition 1.16(c)]] again within the square brackets we see that $\large{-[x(-y)] = -[-(xy)]}$. Applying [[Properties of Fields and Ordered Fields#Proposition 1.14|Proposition 1.14(d)]], $\large{-[-(xy)] = xy}$ completing the proof.

#### Proposition 1.18: 
The following statements are true in every [[Fields and Ordered Fields#Definition 1.17|ordered field]]. 
- (a): If $\large{x \gt 0}$ then $\large{-x \lt 0}$, and vice-versa
- (b): If $\large x\gt 0$ and $\large{y\lt z}$ then $\large{xy \lt xz}$ 
- (c): If $\large{x \lt 0}$ and $\large{y \lt z}$ then $\large{xy \gt xz}$ 
- (d): If $\large{x \ne 0 }$ then $\large{x^2 \gt 0}$. In particular, $\large{1 \gt 0}$ 
- (e): If $\large{0 \lt x \lt y}$ then $\large {0 \lt 1/y \lt 1/x}$ 

##### Proof:
- (a): If $\large{x \gt 0}$ then $\large{0 = -x + x}$ by [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom A5]] and $\large{ -x + x> -x + 0}$ by [[Fields and Ordered Fields#Definition 1.17|property I of an ordered field]]. Resolving both sides of the inequality using [[Fields and Ordered Fields#(A) Axioms of Addition|Axioms A5 and A4]], we get $\large{-x \lt 0}$. The same method can be followed using $\large{x < 0}$ to get $\large {-x> 0}$
- (b): Since $\large{z \gt y}$, we can apply [[Fields and Ordered Fields#Definition 1.17|property I of an ordered field]] to get $\large{z - y \gt y - y = 0}$ by [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom A5]]. By [[Fields and Ordered Fields#Definition 1.17|property II of an ordered field]] we know that $\large{x(z-y) > 0}$. By the [[Fields and Ordered Fields#(D) The Distributive Law|Distributive Law]] $\large{xz= x(z-y) + xy}$. Using Property I again, we see that $\large{x(z-y)+xy \gt 0 + xy = xy}$, substituting the former inequality we find that $\large{xz \gt xy}$.
- (c): Assume $\large x < 0$. By [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(a)]] we know that $\large {-x > 0}$. Since $\large y < z$, we can apply [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] to get the inequality $\large (-x)y < (-x)z$. We use [[Fields and Ordered Fields#Definition 1.17|property I of an ordered field]] to get the inequality $\large{(-x)y - (-x)y < (-x)z - (-x)y}$ and then [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom A5]] to get $\large{0 < (-x)z - (-x)y}$. We can then common factor using the [[Fields and Ordered Fields#(D) The Distributive Law|Distributive Axiom]] to get $\large{0 < (-x)(z - y)}$. Applying  [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(a)]] in combination with [[Properties of Fields and Ordered Fields#Proposition 1.14|Proposition 1.14(d)]] we get the inequality $\large{0 > x(z-y)}$, using the [[Fields and Ordered Fields#(D) The Distributive Law|Distributive Axiom]] we can manipulate this inequality into $\large{0 > xz - xy}$ and applying [[Fields and Ordered Fields#Definition 1.17|property I of an ordered field]], [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom A5]], and [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom A4]] we get the our final inequality of $\large{xy > xz}$ completing the proof.
- (d): Assume that $\large {x > 0}$ then by [[Fields and Ordered Fields#Definition 1.17|property II of an ordered field]] we know that $\large{x^2 >0}$. Let $\large x <0$, then by the application of [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(a)]] we know that $\large -x > 0$, applying [[Fields and Ordered Fields#Definition 1.17|property II of an ordered field]] again we find that $\large{(-x)^2> 0}$. But by [[Properties of Fields and Ordered Fields#Proposition 1.16(d)|proposition 1.16(d)]] we know that $\large{(-x)^2 = x^2}$. So we can conclude that the result holds if $\large x \ne 0$. $\large{1>0}$ can be found through this proposition with $\large x = 1$ and applying [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M4)]]
- (e): Note that for any $\large x> 0$ and $\large v \le 0$, we know that $\large{xv \le 0}$ through the use of [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] and [[Properties of Fields and Ordered Fields#Proposition 1.16(d)|proposition 1.16(a)]]. Now let $\large v = 1/x$, by the application of [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M5)]] this would mean that $\large {1 \le 0}$, which we know is false from [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(d)]], so it follows that $\large {1/x > 0}$, the same reasoning can be applied to $\large y$ to yield $\large 1/y > 0$. This would mean that $\large{1/xy > 0}$ by[[Fields and Ordered Fields#Definition 1.17|property II of an ordered field]]. Now take the inequality $\large{y > x}$ and multiply both sides by positive quantity $\large{1/xy}$, through the use of [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]], yielding $\large{1/y < 1/x}$ through the use of [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M5)]].