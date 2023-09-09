---
type: Academic
tags:
alias: Math-An-1-EuclideanSpaces
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
  source-alias: "Math-An-1-TheRealAndComplexNumberSystems-EuclideanSpaces",
  end-page: 16,
  start-page: 12,
  section-name: "The Real and Complex Number Systems: Euclidean Spaces",
  template: {
    name: "source-tbsection-obj",
    type: "object",
    version: 1
  }
}
relationship: {name: standard-relationship-obj, version: 1}
friends: ["[[The Complex Field]]","[[The Real Field]]"]
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
#### Definition 1.36:
For each positive integer $\large k$, let $\large{\Bbb R^k}$ be the set of all ordered k-tuples $\large{\textbf{x} \in \Bbb R^k, \textbf{x} = (x_1,x_2,\ldots,x_k)}$ where $\large{x_1,x_2,\ldots,x_k \in \Bbb R}$ called the **==coordinates==** of $\large{\textbf{x}}$. The elements of $\large{\Bbb R^k}$ are called **==points==**, **==vectors==** especially when $\large{k > 1}$.
vectors in general are denoted by boldface letters.

If $\large{\textbf{y} = (y_1,y_2, \ldots,y_k),\ \textbf{x} = (x_1,x_2, \ldots,x_k)}$ and $\large{\alpha \in \Bbb R}$ let 
$$\large\begin{eqnarray}\textbf{x} + \textbf{y} &=&(x_1+y_1,x_2,+y_2, \ldots, x_k+y_k) \nonumber \\
\alpha\textbf{x} &=& (\alpha x_1, \alpha x_2, \dots, \alpha x_k)
\end{eqnarray}$$
so that  $\large{\textbf{x} + \textbf{y} \in \Bbb R^k}$ and $\large{\alpha \textbf{x} \in \Bbb R^k}$. 
##### Note 1:
These two operations necessarily satisfy Commutativity, Associativity and the Distributive Laws, making $\large{\Bbb R^k}$ into a **==vector space==** over the [[The Real Field|Real Field]]. The zero element of $\large{\Bbb R^k}$ also called the **==null vector==**, or the **==origin==**, is the element denoted $\large{\textbf{0}}$ which is a point composed entirely of $\large 0$ coordinates.

##### Note 2:
We define the **==inner-product==** or the **==scalar product==** as $\large{\textbf{x} . \textbf{y} = \sum^{k}_{i = 1}x_i y_i}$. Additionally we define the **==norm==** of $\large{\textbf{x}}$, denoted $\large{|\textbf{x}|}$ as $\large{|\textbf{x}| = (\textbf{x}.\textbf{x})^{\frac{1}{2}} = (\sum^{k}_{i=1}x_i^2)^{\frac{1}{2}}}$ 

##### Note 3: 
The vector space $\large{\Bbb R^k}$ with the above definitions of the inner-product and norm is known as a **==Euclidean k-space==**.

##### Note 4:
Typically $\large{\Bbb R}$ is called a **==line==** or **==real-line==** while $\large{\Bbb R^2}$ is called the **==plane==** or **==complex-plane==**.

#### Theorem 1.37:
Suppose $\large{\textbf{x}, \textbf{y}, \textbf{z} \in \Bbb R^k}$ and $\large{\alpha \in \Bbb R}$ then:
(a): $\large{|\textbf{x}| \ge 0}$ 
(b): $\large{|\textbf{x}| = 0}$ if and only if $\large{\textbf{x} = 0}$ 
(c): $\large{|\alpha \textbf{x}| = |\alpha||\textbf{x}|}$ 
(d): $\large{|\textbf{x}.\textbf{y}| \le |\textbf{x}||\textbf{y}|}$ 
(e): $\large{|\textbf{x} + \textbf{y}| \le |\textbf{x}| + |\textbf{y}|}$ 
(f): $\large{|\textbf{x} - \textbf{z}| \le |\textbf{x} - \textbf{y}| + |\textbf{y}- \textbf{z}|}$ 

##### Proof:
- a) let $\large{| \textbf{x}| = (\sum^{k}_{i=1} x_i^2)^\frac{1}{2}}$ . If $\large{\textbf{x} = \textbf{0}}$ then $\large{\sum^{k}_{i=1} x_i^2 = 0}$, since $\large{0^2 = 0}$ we know that $(\large{\sum^{k}_{i=1} x_i^2)^{\frac{1}{2}} = 0}$ which means that $\large{|\textbf{x}| = 0}$. If $\large{\textbf{x} \ne \textbf{0}}$ then we know there exists some $\large{x_i \in \textbf{x}}$ such that $\large{x_i \ne 0}$ which means by applying [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(d)]] in the [[The Real Field|Real Field]] we know that $\large{x_i^2>0}$ which means that $\large{\sum^k_{i=1} x_i ^2 > 0}$. Taking square roots of both sides through [[Gap In Proof of Theorem 1.33(d)#Theorem 2|the following theorem]] we see that $\large{(\sum^k_{i=1}x_i^2)^\frac{1}{2} = |\textbf{x}| \gt 0}$. Hence we conclude by case division that $\large{|\textbf{x}| \ge 0 }$
- b) ($\large{\Rightarrow}$) If $\large{\textbf{x} = \textbf 0}$ then $\large{\sum^{k}_{i=1} x_i^2 = 0}$ since $\large{0^2 = 0}$ we know that $\large{(\sum^{k}_{i=1} x_i^2)^{\frac{1}{2}} = 0}$ which means that $\large{|\textbf{x}| = 0}$. ($\large \Leftarrow$) Assume that $\large{(\sum^{k}_{i=1} x_i^2)^\frac{1}{2} = 0}$ squaring both sides yields $\large{\sum^{k}_{i=1} x_i^2 = 0}$ we know that for all real numbers $\large{x_i^2 \ge 0}$ because of this we know that the previous equality implies that $\large{\forall x\in \textbf{x}(x = 0)}$ which means that $\large{\textbf{x} = \textbf{0}}$
- c) $\large{|\alpha \textbf{x}| = (\sum^k_{i=1} (\alpha x_i)^2)^\frac{1}{2}}$ using the distributive law of exponentiation we know $\large{|\alpha \textbf{x}| = (\sum^k_{i=1} \alpha^2 x_i^2)^\frac{1}{2}}$ . Common factoring we see that $\large{|\alpha \textbf{x}| = (\alpha^2 \sum^k_{i=1}  x_i^2)^\frac{1}{2}}$ because of  [[Properties of the Real Field#Corollary|Corollary 1.21]] we get the equality $\large{|\alpha \textbf{x}| =  |\alpha|(\sum^k_{i=1}  x_i^2)^\frac{1}{2} = |\alpha||\textbf{x}| }$ 
- d) Starting with the [[The Schwarz Inequality#Theorem 1.35|Schwarz Inequality]] but with $\large{x_1,\ldots,x_n,y_1,\ldots,y_n \in \Bbb R}$ we get $\large \left \vert \sum^n_{j=1}x_j\overline y_j \right \vert ^2 \le \sum_{j=1}^n\left \vert x_j \right \vert^2  \sum ^n _{j = 1}\left \vert y_j \right \vert^2$. Since $\large{y_j \in \Bbb R}$ we know that $\large{\overline{y_j} = y_j}$,and so $\large \left \vert \sum^n_{j=1}x_j\overline y_j \right \vert ^2 = \large \left \vert \sum^n_{j=1}x_j y_j \right \vert ^2 =\large \left \vert \textbf{x} . \textbf{y}\right \vert ^2$. Before we move onto the other side of the inequality note that $\large{|x|^2 = |x||x| = |x^2|}$ by [[Conjugates and Absolute Values#Theorem 1.33|Theorem 1.33(c)]] and since $\large{x^2 \ge 0}$ by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(d)]] we know that $\large{|x^2| = x^2}$ by [[Conjugates and Absolute Values#Definition 1.32|Definition 1.32]]. so $\large{|x|^2 = x^2}$ if $\large{x \in \Bbb R}$. Applying this to the right hand side of the [[The Schwarz Inequality|Schwarz Inequality]] we see that $\large{\sum_{j=1}^n |x_j|^2 = \sum_{j=1}^n x_j^2 = |\textbf{x}|^2}$. And so $\large \left \vert \textbf{x}.\textbf{y} \right \vert ^2 \le \left \vert \textbf{x}\right \vert^2 \left \vert  \textbf{y} \right \vert^2$ Taking the square root of both sides through this [[Gap In Proof of Theorem 1.33(d)#Theorem 2|theorem]] we see that $\large{\left \vert \textbf{x}.\textbf{y} \right \vert \le \left \vert \textbf{x} \right \vert \left \vert \textbf{y} \right \vert}$ 
- e) Before beginning the proof we will show that if $\large{x \in \Bbb R}$ then $\large{x \le |x|}$. Assume that $\large{x \ge 0}$ then by [[Conjugates and Absolute Values#Definition 1.32|Definition 1.32]] we know that $\large{|x| = x}$ so $\large{|x| \ge x}$. If $\large{x < 0}$ then assume that $\large{|x| < x}$, we know by [[Conjugates and Absolute Values#Definition 1.32|Definition 1.32]] that $\large{|x| = -x}$ so $\large{-x < x}$ adding $\large{x}$ to both sides yields the inequality $\large{0 < 2x}$ meaning that $\large{x> 0}$ contradicting our assumption so $\large{x \le |x|}$. Start with $\large{|\textbf{x} + \textbf{y}|^2 = (\textbf{x} + \textbf{y}).(\textbf{x} + \textbf{y})}$ since by [[Euclidean Spaces#Note 2|Definition of the Inner Product]] $\large{\textbf{x}.\textbf{x} = \sum^k_{i=1}x_i^2 = |\textbf{x}|^2}$.  Using the distributive law we find that $\large{|\textbf{x} +\textbf{y}|^2 = \textbf{x}.\textbf{x} + 2\textbf{x}.\textbf{y} + \textbf{y}.\textbf{y}}$. Applying the inequality $\large{x \le |x|}$ we find that $\large{|\textbf{x} + \textbf{y}|^2 \le |\textbf{x}|^2 + |2\textbf{x}\textbf{y}| +|\textbf{y}|^2}$ using [[Euclidean Spaces#Theorem 1.37|Theorem 1.37(c)]]  we see that  $\large{|\textbf{x}|^2 + |2\textbf{x}\textbf{y}| + |\textbf{y}|^2 = |\textbf{x}|^2 + 2|\textbf{x}\textbf{y}| + |\textbf{y}|^2}$, now applying [[Euclidean Spaces#Theorem 1.37|Theorem 1.37(d)]] we get the inequality $\large{|\textbf{x} + \textbf{y}|^2 \le |\textbf{x}|^2 + 2|\textbf{x}||\textbf{y}| + |\textbf{y}|^2= (|\textbf{x}| +|\textbf{y}|)^2}$. Square rooting both sides through this [[Gap In Proof of Theorem 1.33(d)#Theorem 2|theorem]] we get the inequality $\large{|\textbf{x} + \textbf{y}| \le |\textbf{x}| + |\textbf{y}|}$ 
- f) This theorem is trivially proven by substituting $\large{\textbf{x} - \textbf{y}}$ for $\large{\textbf{x}}$ and $\large{\textbf{y}- \textbf{z}}$ for $\large{\textbf{y}}$ in [[Euclidean Spaces#Theorem 1.37|Theorem 1.37(e)]].