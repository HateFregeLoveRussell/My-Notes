---
type: Academic
tags:
alias: Math-An-1-TheComplexField
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
  start-page: 12,
  end-page: 16,
  type: "tbsection",
  class-alias: "Math-An-1",
  book-title: "Principles of Mathematical Analysis",
  source-alias: "Math-An-1-TheRealAndComplexNumberSystems-TheComplexField",
  ISBN: "978-0-07-054235-8",
  template: {
    name: "source-tbsection-obj",
    type: "object",
    version: 1
  },
  section-name: "The Real and Complex Number Systems: The Complex Field"
}
relationship: {name: standard-relationship-obj, version: 1}
friends: ["[[The Real Field]]", "[[Fields and Ordered Fields]]" ]
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
#### Definition 1.24
A **==Complex Number==** is an ordered pair of real numbers $\large{(a,b) \quad a \in \Bbb R, b \in \Bbb R}$.

Let $\large{x = (a,b) \quad y = (c,d) \quad a,b,c,d \in \Bbb R}$ we say $\large{x}$ and $\large{y}$ are equal, denoted $\large{x=y}$ if and only if $\large{c = a}$ and $\large{b =d}$. Addition and Multiplication of the complex numbers are defined through the Complex Field in [[The Complex Field#Theorem 1.25|Theorem 1.25]]
#### Theorem 1.25
The following definitions of addition and multiplication turn the set of all [[The Complex Field#Definition 1.24|Complex Numbers]] into a [[Fields and Ordered Fields#Definition 1.12|Field]] with $\large{(0,0)}$ serving the role of $\large 0$ and $\large{(0,1)}$ serving the role of $\large 1$. $\large{x +y = (a+c, b+d)\quad xy = (ac-bd,ad + bc) }$ for $\large{x = (a,b) \quad y=(c,d)}$ where $\large{a,b,c,d \in \Bbb R}$

##### Proof:
for all sections of the proof below $\large{x = (a,b) \quad y=(c,d) \quad z = (e,f)}$ where $\large{a,b,c,d,e,f \in \Bbb R}$ 
###### Proof of (A1): 
$\large x + y = (a + c, b + d)$, $\large{a+c, b+d \in \Bbb R}$ by [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A1)]] of the [[The Real Field|Real Field]]

###### Proof of (A2):
$\large{x + y = (a +c, b +d )}$ by the definition of addition, $\large{(a+c,b+d) = (c + a, d + b)}$ by [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A2)]] of the [[The Real Field|Real Field]]. And finally $\large{(c+a,d +b) = y +x}$ by the chosen definition of addition. 

###### Proof of (A3):
By the definition of addition $\large(x + y) + z= (a + c, b +d) + (e,f)$. Applying this definition again we see that $\large{(a+c,b+d) + (e,f) = (a + c +e, b +d +f)}$. Note that this is only possible due to [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A3)]] of the [[The Real Field|Real Field]]. Moving backwards now we see that $\large{(a + c + e, b+ d +f) = (a,b) + (c + e, d +f) = x + (y + z)}$

###### Proof of (A4):
By applying the chosen definition of addition we see that $\large{x + 0 = (a,b) + (0,0) = (a + 0, b +0)}$. Applying [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A4)]] of the [[The Real Field|Real Field]], we see that $\large{(a + 0, b+0) = (a,b) = x}$ 

###### Proof of (A5):
Let $\large{-x = (-a,-b)}$ then $\large{x + -x = (a,b) + (-a,-b) = (a-a,b-b)}$. By [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A5)]] of the [[The Real Field|Real Field]] we see that $\large{(a-a,b-b) = (0,0) = 0}$.

###### Proof of (M1):
By the chosen definition of multiplication we see that $\large{xy = (ac-bd, ad + bc)}$. By applying [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A1)]] and [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M1)]] of the [[The Real Field|Real Field]], we see that $\large{ac-bd,ad+bc \in \Bbb R }$

###### Proof of (M2):
By the chosen definition of multiplication we see that $\large{xy = (ac-bd, ad + bc)}$. By applying [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M2)]] of the [[The Real Field|Real Field]] we see that $\large{(ac-bd, ad+ bc) = (ca-db,da+cb) = yx}$ 

###### Proof of (M3):
By the repeated application of the definition of multiplication alongside the use of [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M3)]] and [[Fields and Ordered Fields#(D) The Distributive Law|The Distributive Axiom (D)]] of the [[The Real Field|Real Field]] we see that $\large{(xy)z = (ac-bd,ad+ bc)(e,f) = (ace - bde - adf -bcf, acf - bcf + ade +bce)=(a,b)(ce-df,cf+de) = x(yz)}$ 
###### Proof of (M4):
By the chosen definition of multiplication $\large{1x = (1,0)(a,b) = (1a - 0b, 0a + 1b)}$. If we now apply [[Properties of Fields and Ordered Fields#Proposition 1.16|Proposition 1.16(a)]] and [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M4)]] in the [[The Real Field|Real Field]] we see that $\large{(1a - 0b, 0a +1b) = (1a,1b) = (a,b) = x}$

###### Proof of (M5):
Assume that $\large{x \ne 0 \iff x \ne (0,0)}$ which means that either $\large{a \ne 0}$ or $\large{b \ne 0}$. Without the loss of generality assume that $\large{b \ne 0}$. By the application of [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(d)]] in the [[The Real Field|Real Field]] we see that $\large{b^2> 0}$. By [[Fields and Ordered Fields#Definition 1.17|Property I of an Ordered Field]] (The [[The Real Field|Real Field]] in this case) we know that $\large{b^2 + a^2 > a^2 + 0}$ Apply [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A4)]] of the [[The Real Field|Real Field]] to get $\large{b^2 + a^2 > a^2}$. Now if $\large{a = 0}$ then $\large{a^2 = 0}$ and of $\large{a \ne 0}$ then $\large{a^2 > 0}$ by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(d)]] in the [[The Real Field|Real Field]], so it stands to say that in either case $\large{a^2 \ge 0}$. Combining this with the previous inequality yields $\large{b^2 + a^2 > a^2 \ge 0}$ which means that $\large{b^2 + a^2 > 0}$.

Now let $\large{1/x = (\frac{a}{a^2 + b^2}, \frac{-b}{a^2 + b^2})}$. Note that this element is only well defined because $\large{a^2 + b^2 \ne 0}$ from the previous paragraph. Finally we can see that $\large{x*1/x = (\frac{a^2}{a^2 + b^2} - \frac{(-b)b}{a^2 + b^2}, \frac{(-b)a}{a^2 + b^2} + \frac{ba}{a^2 + b^2})}$ By applying [[Fields and Ordered Fields#(D) The Distributive Law|The Distributive Axiom]] and [[Properties of Fields and Ordered Fields#Proposition 1.14|Proposition 1.14(d)]] in the [[The Real Field|Real Field]] we find that $\large{x*1/x = (\frac{a^2 + b^2}{a^2 + b^2}, \frac{ba-ba}{a^2 + b^2})}$ which by [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M5)]] and [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A4)]] in the [[The Real Field|Real Field]] means that $\large{x*1/x = (1,\frac{0}{a^2 + b^2})}$. Apply [[Properties of Fields and Ordered Fields#Proposition 1.16|Proposition 1.16(a)]] to find that $\large{x*1/x = (1,0) = 1}$ 

###### Proof of (D):
Apply the definition of addition to get $\large{x(y+z) = (a,b)(c +e, d +f)}$. Then apply the definition of multiplication alongside the [[Fields and Ordered Fields#(D) The Distributive Law|The Distributive Axiom]] in the [[The Real Field|Real Field]] to see that $\large{x(y+z) = (ac+ae - bd- bf, ad + af+bc+be)}$ Apply the definition of Addition again and we see $\large{x(y + z) = (ac-bd,ad+bc) + (ae-bf,af+be) = xy + xz}$ 

#### Theorem 1.26
For any [[The Real Field|Real Number]] $\large a$ and $\large b$, $\large{(a,0) + (b,0) = (a+b,0), \quad (a,0)(b,0) = (ab,0)}$.
In or in other words [[The Complex Field#Definition 1.24|Complex Numbers]] of the form $\large{(a,0) \ a\in \Bbb R}$ have the same arithmetic properties as the [[The Real Field|Real Number]] meaning that the [[The Real Field|Real Field]] is a subfield of the [[The Complex Field#Theorem 1.25|Complex Field]]. Because of this we will make the following notational shortcut: $\large{(a,0) = a}$ 

##### Proof:
By [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A4)]] of the [[The Real Field|Real Field]] we see that $\large{(a,0) + (b,0) = (a+b, 0+0) = (a+b,0)}$. Furthermore, using [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A4)]] in combination with [[Properties of Fields and Ordered Fields#Proposition 1.16|Proposition 1.16(a)]] (both in the [[The Real Field|Real Field]]) we can make the following algebraic manipulation $\large{(a,0)(b,0) = (ab -0*0, a0 - 0c)=(ab,0)}$  