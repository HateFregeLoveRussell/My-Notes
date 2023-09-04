---
type: Academic
tags:
alias: Math-An-1-RealFieldPRoperties
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
  section-name: "The Real and Complex Number Systems: The Real Field",
  ISBN: "978-0-07-054235-8",
  book-title: "Principles of Mathematical Analysis",
  class-alias: Math-An-1,
  source-alias: Math-An-1-TheRealAndComplexNumberSystems-TheRealField,
  start-page: 8,
  end-page: 11,
  template: {
    name: "source-tbsection-obj",
    version: 1,
    type: "object"
  }
}
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[The Real Field]]"
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

#### Theorem 1.20:
- (a) The Archimedean Property: If $\large x \in \Bbb R$ and $\large y \in \Bbb R$ and $\large x>0$, then there exists a positive integer $\large n$ such that: $\large nx > y$
- (b) $\Bbb Q$ is Dense in $\large \Bbb R$: If $\large x \in \Bbb R$ and $\large y \in \Bbb R$ and $\large {x < y}$ then there exists $\large p \in \Bbb Q$ such that $\large{x < p < y}$ 

##### Proof:
- (a): Let $\large A$ be the set of all number of the form $\large nx$ where $\large n$ runs through all the positive integers. If the [[The Real Field|Real Field]] did not have the Archimedean property than $\large y$ would be an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large A$. We know that $\large A$ has a [[Bounds and Bounded Sets#Definition 1.8|least-upper-bound]] in $\large \Bbb R$ from [[The Real Field#Theorem 1.19(The Existence Theorem)|The Existence Theorem]]. We will denote it as $\large {\alpha = \operatorname{sup}A}$. Since $\large x>0$, we will use [[Fields and Ordered Fields#Definition 1.17|Property I of an Ordered Field]] Alongside [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(a)]], to get the inequality $\large {\alpha - x< \alpha}$. Since $\large \alpha$ is the [[Bounds and Bounded Sets#Definition 1.8|Supremum]] of set $\large A$ we know that $\large{\alpha - x}$ cannot be an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{A}$, meaning that $\large{\alpha - x < mx }$ for some $\large{mx \in A}$. But then by using [[Fields and Ordered Fields#Definition 1.17|Property I of an Ordered Field]], alongside the [[Fields and Ordered Fields#(D) The Distributive Law|The Distributive Axiom]] we can manipulate the inequality to get $\large{\alpha \lt (m+1)x}$. Note that it must be the case that $\large{(m+1)x \in A}$. This is impossible by definition of $\large \alpha$ as the [[Bounds and Bounded Sets#Definition 1.8|Supremum]] of set $\large A$. Therefore, by contradiction we conclude that the [[Fields and Ordered Fields#Definition 1.17|Ordered Field]] $\large \Bbb R$ has the Archimedean property.
- (b): Since $\large x < y$ we know through the application of [[Fields and Ordered Fields#Definition 1.17|Property I of an Ordered Field]], alongside [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A5)]] that $\large{y - x > 0}$. Applying the quantities of $\large{y -x}$ and $\large 1$ to [[Properties of the Real Field#Theorem 1.20|Theorem 1.20(a)]] we find that there exists some positive integer $\large n$ such that $\large{n(y-x) > 1}$. Next, we apply [[Properties of the Real Field#Theorem 1.20|Theorem 1.20(a)]] once again, twice using $\large 1$ as the positive quantity and $\large{nx, -nx}$ as the remaining quantity to find the inequalities: $\large{m_1 > nx}$, $\large{m_2 > -nx}$ which by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(c)]] means that $\large{-m_2 < nx}$. So there exists two positive integers $\large m_1, m_2$  such that $\large -m_2 < nx < m_1$. Since $\large nx$ is bounded by two integers, it stands to say that there exists some integer $\large -m_2\le m\le m_1$ such that $\large{m-1 \le nx \lt m}$, By [[Fields and Ordered Fields#Definition 1.17|Property I of an Ordered Field]], we also know that $\large{m \le nx + 1 \lt m+ 1}$. Rearranging the earlier inequality using the [[Fields and Ordered Fields#(D) The Distributive Law|The Distributive Axiom]], [[Properties of Fields and Ordered Fields#Proposition 1.14|Proposition 1.14 (d)]] and [[Fields and Ordered Fields#Definition 1.17|Property I of an Ordered Field]] we find that $\large{ny > 1 + nx}$.Combining this with the former 2 inequality we know that $\large{nx < m \le 1 + nx < ny}$, which means that $\large{nx <m < ny}$. Since $\large n> 0$ we know by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18 (b)]] and [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M5)]] that $\large{x < \frac{m}{n} < y}$. The proof is complete when we let $\large{p = \frac{m}{n} \in \Bbb Q}$.


#### Theorem 1.21: 
For every real $\large{x > 0}$ and every integer $\large{n > 0}$ there is one and only one positive real $\large y$ such that $\large{y^n  = x}$, this number $\large y$ is often denoted as $\large{\sqrt[n]{x}}$ or $\large{x^{\frac{1}{n}}}$ 

##### Proof:

###### Uniqueness:
There could be at most one such $\large y$. Assume that there were two, distinct such $\large y$ $\large{0 < y_1 < y_2}$, this implies $\large{{y_1}^n < {y_2}^n}$ which means that $\large{{y_1}^n \ne {y_2}^n}$, completing this section of the proof.

###### Existence: 
Let $\large E$ be the set of all positive real numbers $\large{t}$ such that $\large{t^n < x}$.

We will first show that this set is non-empty, consider the entry $\large{t = \frac{x}{x + 1}}$, note that this entry satisfies the inequality $\large{0 \le t \lt 1}$, secondly, note that  $\large{t \lt x}$ this means that any positive integer power of $\large{t}$ must satisfy the inequality $\large{t^n \le t \lt x}$. Meaning that $\large E$ must be nonempty. 

Second we will show that the set $\large E$ is [[Bounds and Bounded Sets#Definition 1.7|Bounded Above]]. Consider the entry $\large{t = x + 1}$ note that $\large t > 1$,and that $\large {t > x}$, this means that any positive integer power of $\large t$ satisfies $\large{t^n > x}$, this means that $\large t \notin E$, and that $t = x +1$ is an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] if $\large E$.

Since $\large E$ is [[Bounds and Bounded Sets#Definition 1.7|Bounded Above]], and nonempty by [[The Real Field#Theorem 1.19(The Existence Theorem)|Theorem 1.19]] we know that there exists some element $\large{y = \operatorname{sup} E}$ as a member of $\large{\Bbb R}$. 

Now we will proceed by proving that this element $\large y$ satisfies the property $\large{y^n = x}$. This will be done through two proofs by contradictions where we assume that $\large{y^n < x}$ and $\large{y^n > x}$ in each. In each of this proof we will make use of the following identity: $\large{b^n - a^n  = (b-a)(b^{n-1} + b^{n-2}a + \ldots + a^{n-1})}$ which implies the following inequality: $\large{b^n - a^n < (b-a)nb^{n-1} }$ if $\large{0 < a < b}$.

Assume that $\large{y^n < x}$, then choose the value $\large h$ such that $\large h < \frac{x - y^n}{n(y + 1)^{n-1}}$, additionally $\large h$ must satisfy $\large{0 < h < 1}$. Since $\large{h < 1}$ we know that $\large{hn(y + h)^{n-1} < hn(y + 1)^{n-1}}$. Additionally, rearranging the first criteria for picking $\large h$ through [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] (note that we know $\large y$ is positive as it's a [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] to a set which is composed entirely positive numbers) we find that $\large{hn(y + 1)^{n-1} < x - y^n}$ . Finally applying the inequality $\large{b^n - a^n < (b-a)nb^{n-1} }$, with $\large{a = y}$ and $\large{b = y + h}$ (note that $\large{0 < y < y + h}$) we get, $\large{(y + h)^n - y^n < hn(y+h)^{n-1}}$. Combining these three inequalities yields: $\large{(y + h)^n - y^n < hn(y+h)^{n-1} < hn(y+1)^{n-1} < x -y^n}$ which implies the inequality $\large{(y + h)^n < x}$ through [[Fields and Ordered Fields#Definition 1.17|Property I of an Ordered Field]] In addition to [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A5)]]. This means that $\large{(y + h) \in E}$, but this contradicts the definition of $\large{y}$ as an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of the set $\large E$ therefore we conclude that $\large{y^n \not \lt x}$.

Assume that $\large{y^n > x}$, then choose the value $\large{k}$ such that $\large{k = \frac{ y^n - x}{ny^{n-1}}}$. Note that $\large k > 0$ since $\large{ny^{n-1}}$ is positive and $\large{y^n > x}$ by assumption. Secondly, Note that $\large{k < y}$ since $\large{k = \frac{y}{n} - \frac{x}{ny^{n-1}}}$ we know that $\large{k < \frac{y}{n}}$ as $\large \frac{x}{ny^{n-1}}$ is a positive number, since $\large n$ and $\large y$ are positive, we know that $\large{\frac{y}{n} < y}$ which implies that $\large{k \lt y}$. Combining the two inequalities tells us that $\large{0 < k < y}$. We will now attempt to prove that $\large{y - k}$ is an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] to $\large E$, this proof will be done by contrapositive by proving $\large {t \ge y - k \implies t \not \in E}$. Now assume an arbitrary number $\large t$ satisfying $\large{t \ge y -k}$. Since $\large{y > k}$ we know that $\large{y-k > 0}$ by [[Fields and Ordered Fields#Definition 1.17|Property I of an Ordered Field]] and [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A5)]], combining this with the previous inequality we find that $\large{t \ge y- k > 0}$ which implies that $\large{t^n \ge (y - k)^n}$ which by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(c)]] and [[Fields and Ordered Fields#Definition 1.17|Property I of an Ordered Field]] we know that $\large{y^n - t^n \le y^n - (y-k)^n}$. Since $\large{y-k > 0}$, and $\large{y-k < y}$ (since $\large{k > 0}$) we know that $\large{y > y-k > 0}$ which allows us to apply the inequality $\large{b^n - a^n < (b-a)nb^{n-1}}$ with $\large{b = y + k}$ and $\large{a = y}$ to get the inequality $\large{y^n - (y-k)^n < kny^{n-1}}$. Rearranging the definition of $\large k$ using [[Fields and Ordered Fields#(M) Axioms of Multiplication|Axiom (M5)]] we find that $\large{kny^{n-1} = y^n -x}$. Combining the latter 3 results we get the inequality $\large{y^n - t^n \le y^n - (y-k)^n < kny^{n-1} = y^n - x}$ meaning that $\large{y^n - t^n < y^n - x}$ which by the application of [[Fields and Ordered Fields#Definition 1.17|Property I of an Ordered Field]], [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(c)]], and [[Properties of Fields and Ordered Fields#Proposition 1.14|Proposition 1.14(d)]] tells us that $\large{t^n > x}$ or in other words that $\large{t \notin E}$. This proves by contrapositive that $\large{y-k}$ is an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] to $\large E$, but as we deduced earlier $\large{y-k < y}$ which violates the definition of $\large y$ as the [[Bounds and Bounded Sets#Definition 1.8|Supremum]] of $\large E$, hence we can only conclude that $\large {y^n \not > x}$.

Since $\large{y^n \not > x}$ and $\large{y^n \not < x}$ we can only conclude that $\large{y^n = x}$ completing the proof.

##### Corollary
If $\large a$ and $\large b$ are positive real numbers and $\large n$ is a positive integer then $\large{(ab)^{\frac{1}{n}} = a ^{\frac{1}{n}}b^{\frac{1}{n}}}$

###### Proof: 
let $\large \alpha = a^{\frac{1}{n}}$ and let $\large{\beta = b^{\frac{1}{n}}}$ then $\large{ab = \alpha^n\beta^n = (\alpha \beta)^{\frac{1}{n}}}$. The Uniqueness asserted by [[Properties of the Real Field#Theorem 1.21|Theorem 1.21]] allows us then to say $\large{(ab)^{\frac{1}{n}} = \alpha \beta}$ and that $\large{(ab)^{\frac{1}{n}} = a^{\frac{1}{n}}b^{\frac{1}{n}}}$ 