---
type: Academic
tags: [practice]
alias: Math-An-1-Ch1PP-Q7
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

#### Introduction:
The following series of Theorems will act as proof sketch for the following statement: for a fixed $\large{b> 1, y > 0}$ there exists a unique real quantity $\large{x}$ such that $\large{b^x = y}$. This $\large{x}$ is known as the **==Logarithm==** of $\large y$ to the base $\large{b}$.

#### Theorem 1.Q7a:
For any positive Integer $\large{n}$ it is true that $\large{b^n - 1\ge n(b-1)}$.

##### Proof: 
###### Base Case $\large{n = 2}$:
Since we know that $\large{b > 1}$ we know that $\large{b+1 > 2}$ and $\large{b-1 > 0}$. Applying the latter inequality to the former using [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] we see that $\large{(b+1)(b-1)> 2(b+1)}$.

###### Induction Step:
Assume that $\large{b^n - 1 \ge n(b-1)}$ we know that $\large{(b-1)^2 \ge 0}$ by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(d)]] and so we know that $\large{b^2 -2b + 1 \ge 0}$. Rearranging through [[Fields and Ordered Fields#Definition 1.17|Property I of the Ordered Field]] $\large{\Bbb R}$, we see that $\large{b^2 - 1 \ge 2b}$. Since $\large{b > 0}$  we know that $\large{b^{-1} > 0}$ through [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(e)]] we can combine it with the former inequality using [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] giving us the inequality $\large{\frac{b^2-1}{b} \ge 2}$ this statement is equivalent to $\large{b + \frac{1}{b} \ge 2}$ which can then again be rearranged through [[Fields and Ordered Fields#Definition 1.17|Property I of the Ordered Field]] $\large{\Bbb R}$ to get $\large{b  - 1\ge 1- \frac{1}{b}}$. Since $\large{n > 0}$ we can use [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] yet again to get the inequality $\large{n(b-1) \ge n(1 - \frac{1}{b})}$. But we know that $\large{b^n  - 1\ge n(b-1)}$ so it stands to say $\large{b^n - 1 \ge n(1 - \frac{1}{b})}$ which is equivalent to saying $\large{b^n -1 \ge n(\frac{b - 1}{b})}$ since $\large{b > 1}$ we can yet again use [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] to get the inequality $\large{b^{n+1} - b \ge n(b -1)}$ distributing $\large{n}$ we get $\large{b^{n+1} - b \ge nb - n}$ we will rearrange again using [[Fields and Ordered Fields#Definition 1.17|Property I of the Ordered Field]] $\large{\Bbb R}$ to see that $\large{b^{n+1} + n \ge nb +b}$ factoring $\large{b}$ we get the equivalent statement of $\large{b^{n+1} + n \ge b(n+1)}$ we can then again use [[Fields and Ordered Fields#Definition 1.17|Property I of the Ordered Field]] $\large{\Bbb R}$ to get the inequality $\large{b^{n+1} - 1 \ge b(n+1) - n - 1}$, with more factoring we will arrive at the statement $\large{b^{n+1} - 1 \ge (n+1)(b-1)}$ completing the proof.


#### Theorem 1.Q7b: 
For the beforementioned variables it is true that $\large{b-1 \ge n(b^\frac{1}{n} - 1)}$ 

##### Proof:
If $\large{b > 1}$ then by [[Gap In Proof of Theorem 1.33(d)#Theorem 2|this]] previously proven Theorem we know that $\large{b^{\frac{1}{n}} > 1^\frac{1}{n} = 1}$ so by applying [[Question 7#Theorem 1.Q7a|Theorem 1.Q7a]] to $\large{b^\frac{1}{n} > 1}$ we see that $\large{(b^n)^\frac{1}{n} - 1 \ge n(b^\frac{1}{n} - 1)}$ which is equivalent to $\large{b-1 \ge n(b^\frac{1}{n} - 1)}$.

#### Theorem 1.Q7c:
If $\large{t > 1}$ and $\large{n > \frac{b-1}{t-1}}$ then $\large{b^\frac{1}{n} < t}$

##### Proof: 
If $\large{t > 1 }$ then $\large{t - 1 > 0}$. We know that $\large{n > \frac{b-1}{t-1}}$ and that $\large{t -1 > 0}$ which means that through [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] we know that $\large{(t-1)n > b-1}$.We know by [[Question 7#Theorem 1.Q7b|Theorem 1.Q7b]] that $\large{b-1 \ge n(b^\frac{1}{n} - 1)}$ so it stands to say that $\large{n(t-1) > n(b^\frac{1}{n} - 1)}$ since $\large{n >0}$ we know that $\frac{1}{n} > 0$ by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(e)]] and hence our inequality reduces to $\large{t-1 > b^\frac{1}{n} - 1}$ by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]], adding $\large{1}$ to both sides through [[Fields and Ordered Fields#Definition 1.17|Property I of the Ordered Field]] $\large{\Bbb R}$ we see that $\large{t > b^\frac{1}{n}}$ completing the proof.

#### Theorem 1.Q7d:
If $\large{w}$ is such that $\large{b^w < y}$ then $\large{b^{w + \frac{1}{n}} < y}$ for some sufficiently large $\large{n}$.

##### Proof:
Suppose that $\large{b^w < y}$ note that since $\large{b^w}$ is a quantity which is a product of exponentiation we know that $\large{b^w > 0}$. So $\large{0 < b^w < y}$, by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(e)]] we know that $\large{0 < y^{-1} < b^{-w}}$ multiplying both sides by $\large{y > 0}$ through [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] we know that $\large{y^{-1}y = 1 < b^{-w}y}$. Let $\large{t = b^{-w}y > 1}$ so $\large{t-1 > 0}$. Note that $\large{t-1\in \Bbb R}$ and $\large{b-1 \in \Bbb R}$, so by [[Properties of the Real Field#Theorem 1.20|The Archimedean Property]] there exists some $\large{n \in \Bbb Z}$ such that $\large{n(t-1) > b-1}$, since $\large{t-1 > 0}$ we can obtain the following inequality through [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] $\large{n > \frac{b-1}{t-1}}$. Since $\large{n > \frac{b-1}{t-1}}$ and $\large{t > 1}$ by [[Question 7#Theorem 1.Q7c|Theorem 1.Q7c]] we know that $\large{b^\frac{1}{n} < t}$. Then $\large{b^\frac{1}{n} < b^{-w}y}$ note that since $\large{b^{w} > 0}$ we can apply [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] to get $\large{b^\frac{1}{n}b^w < y}$ by [[Question 6#Theorem 1.Q6d|Theorem 1.Q6d]] we know that $\large{b^{\frac{1}{n} + w} < y}$.

#### Theorem 1.Q7e:
If $\large{b^w > y}$ then $\large{b^{w-\frac{1}{n}} < y}$ for a sufficiently large $\large{n}$. 

##### Proof:
Suppose that $\large{y < b^w}$, and $\large{y > 0}$, so $\large{\frac{1}{y} > 0}$ by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(e)]]. This would mean that by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] we know that $\large{y\frac{1}{y} = 1 < b^w\frac{1}{y}}$ let $\large{t = b^wy^{-1} > 1}$ so $\large{t - 1 > 0}$. Note that $\large{t-1 \in \Bbb R}$ and $\large{b-1 \in \Bbb R}$ this would mean that through [[Properties of the Real Field#Theorem 1.20|The Archimedean Property]] we know that there exists some integer $\large{n}$ such that $\large{n(t-1) > b-1}$ since $\large{t-1 > 0}$ we know that $\large{(t-1)^{-1} > 0}$ by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(e)]] and hence through [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] $\large{n > \frac{b-1}{t-1}}$. Since $\large{n > \frac{b-1}{t-1}}$ and $\large{t>1}$ through [[Question 7#Theorem 1.Q7c|Theorem 1.Q7c]] we know that $\large{b^\frac{1}{n} < t}$ this means that $\large{b^\frac{1}{n} < b^w y^{-1}}$ since $\large{y > 0}$, $\large{b^\frac{1}{n}y < b^w}$ by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]]. By [[Question 6#Lemma 1.Q6c3|Lemma 1.Q6c3]] we know that $\large{b^\frac{1}{n} > 0}$ so $\large{b^\frac{-1}{n} > 0}$ by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(e)]] which means that $\large{y < b^wb^\frac{-1}{n}}$, and so by [[Question 6#Theorem 1.Q6d|Theorem 1.Q6d]] we know that $\large{y < b^{w -\frac{1}{n}}}$.

#### Theorem 1.Q7f:
If $\large A$ be the set of all $\large w$ such that $\large{b^w < y}$ and if $\large{x = \operatorname{sup} A}$ then $\large{b^x = y}$.

##### Proof:
Say that $\large{b^x \ne y}$ so either $\large{b^x > y}$ or $\large{b^x < y}$. Consider the case of $\large{b^x < y}$, then by [[Question 7#Theorem 1.Q7d|Theorem 1.Q7d]] we know that for some $\large{n}$ it is true that $\large{b^{x + \frac{1}{n}} < y}$ this would mean that $\large{x + \frac{1}{n} \in A}$, we know that $\large{x}$ is an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{A}$ since it is the [[Bounds and Bounded Sets#Definition 1.8|Supremum]] of $\large{A}$ so $\large{x + \frac{1}{n} < x}$ but this is impossible as $\large{n > 0}$. Similarly assume that $\large{b^x > y}$ then by [[Question 7#Theorem 1.Q7e|Theorem 1.Q7e]] we know that $\large{b^{x - \frac{1}{n}} > y }$ for some $\large{n > 0}$. Assume that $\large{w}$ is some arbitrary member of $\large{A}$ it stands to say that $\large{b^w < y < b^{x - \frac{1}{n}}}$ so $\large{b^w < b^{x - \frac{1}{n}}}$ through [[Question 7#Lemma 1.Q7f1|Lemma 1.Q7f1]] this tells us that $\large{w < x - \frac{1}{n}}$ this would mean that $\large{x - \frac{1}{n}}$ is an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{A}$ since $\large{x}$ is the [[Bounds and Bounded Sets#Definition 1.8|Supremum]] of $\large{A}$ we know that $\large{x -\frac{1}{n} > x}$ but this is similarly impossible as $\large{n > 0}$. So we must conclude that $\large{b^x = y}$.
 
##### Lemma 1.Q7f1:
If $\large{b >1}$ $\large{,b^n > b^m}$ then $\large{n > m}$. 

###### Proof:
If $\large{n \not \ge m}$ then either $\large{n = m}$ or $\large{n < m}$. If $\large{n < m}$ then by [[Question 6#Lemma 1.Q6c8|Lemma 1.Q6c8]] $\large{b^n < b^m }$ which contradicts $\large{b^m < b^n}$. If $\large{n = m}$ then $\large{b^n = b^m}$ which contradicts $\large{b^m < b^n}$. Therefore $\large{n > m}$.
#### Theorem 1.Q7g:
$\large{x}$ as described in [[Question 7#Theorem 1.Q7f|Theorem 1.Q7f]] is unique.  

##### Proof:
Assume that there exists some quantity $\large{x_2}$ such that $\large{x_2 \ne \operatorname{sup} A}$ and $\large{b^{x_2} = y}$. Since $\large{x_2 \ne \operatorname{sup} A}$ it true that either $\large{x_2 > \operatorname{sup} A}$ or $\large{x_2 < \operatorname{sup} A}$. In the former case we can then say by [[Question 6#Lemma 1.Q6c8|Lemma 1.Q6c8]] that $\large{b^{x_2} > b^x = y}$ so $\large{b^{x_2} > y}$ this contradicts our assumption that $\large{b^{x_2} = y}$. Now consider the latter case, we can then say by [[Question 6#Lemma 1.Q6c8|Lemma 1.Q6c8]] that $\large{y=b^x > b^{x_2}}$ so $\large{y > b^{x_2}}$ contradicting our assumption that $\large{b^{x_2} = y}$ so it stands to say that $\large{x_2 =x}$ necessarily, which means that $\large{x}$ is unique. 

