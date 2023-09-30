---
type: Academic
tags: [practice]
alias: Math-An-1-Ch1PP-Q6
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
#### Theorem 1.Q6a:
If $\large{b > 1}$, $\large{m,n,p,q \in \Bbb Z}$ and $\large{n>0,q>0}$ and $\large{r= \frac{m}{n}=\frac{p}{q}}$ then $\large{(b^m)^\frac{1}{n} = (b^p)^\frac{1}{q}}$.
Hence it is meaningful to define $\large{b^r = (b^m)^\frac{1}{n}}$. 

##### Proof:
Let $\large{pn=qm = k}$, from [[Properties of the Real Field#Theorem 1.21|Theorem 1.21]] we know that there exists some positive unique real number $\large{c > 0}$ such that $\large{c^{nq} = b^k}$ note that in this case $\large{y = b^k}$. Consider the quantity $\large{((b^m)^\frac{1}{n})^{nq}}$ this quantity by the cancellation of exponentiation is equal to $\large{(b^m)^q = b^{mq}}$ but by the definition of $\large{k}$ we know that $\large{((b^m)^\frac{1}{n})^{nq}=b^k}$ this tells us that $\large{c =(b^m)^\frac{1}{n}}$. Now Consider the quantity $\large{((b^p)^\frac{1}{q})^{qn}}$ similarly to the previous case we know that  $\large{((b^p)^\frac{1}{q})^{qn} = (b^p)^n = b^{pn}= b^k}$ so $\large{c = (b^p)^\frac{1}{q}}$. Since by construction $\large{c}$ is a unique number we can only conclude that $\large{(b^p)^\frac{1}{q}=(b^m)^\frac{1}{n}}$. 

#### Theorem 1.Q6b:
For $\large{b > 1}$ and $\large{r,s \in \Bbb Q}$ it is true that $\large{b^{r+s} = b^rb^s}$.

##### Proof:
If $\large{r,s \in \Bbb Q}$ then $\large{r = \frac{p}{q}, s = \frac{m}{n}, q \ne 0, n \ne 0}$. Note that $\large{r + s = \frac{p}{q} + \frac{m}{n} = \frac{pn + qm}{qn}}$, this would mean that $\large{b^{r+s} = b^{\frac{pn + qm}{qn}}}$. Now consider the following manipulation: $\large{b^\frac{pn + qm}{qn} = b^{\frac{1}{qn}(pn + qm)} = (b^{pn}b^{qm})^\frac{1}{qn}}$ by [[Properties of the Real Field#Corollary|Corollary 1.21]] we know that $\large{b^{r+s} = b^\frac{pn}{qn}b^\frac{qm}{qn} = b^\frac{p}{q}b^\frac{m}{n} = b^rb^s}$.

#### Theorem 1.Q6c:
If $\large{x \in \Bbb R}$ define $\large{B(x)}$ to be the set of all $\large{b^t}$ where $\large{t \in \Bbb Q}$ and $\large{t \le x}$.
It is true that $\large{b^r = \operatorname{sup}B(r)}$ when $\large{r \in \Bbb Q}$ and hence it is sensible to define $\large{b^x = \operatorname{sup}B(x)}$ for $\large{x \in \Bbb R}$.

##### Lemma 1.Q6c1:
If $\large{n > 0}$ and $\large{b > 1}$ then $\large{b^n > 1}$.

###### Proof
**Base Case (n = 2):**
Assume that $\large{b > 1}$, then $\large{b > 0}$ then by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] we know that $\large{b^2>b}$ since $\large{b>1}$ we know that $\large{b^2 > b > 1}$ so $\large{b^2 > 1}$.

**Induction Step:**
Assume that $\large{b^{n-1} > 1}$ and that $\large{b > 1}$ which means that $\large{b > 0}$, so by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] we know that $\large{b^{n-1}b > b>1}$ so $\large{b^n > 1}$.

##### Lemma 1.Q6c2:
If $\large{n < 0}$ and $\large{b > 1}$ then $\large{b^n < 1}$.

###### Proof:
**Base Case (n = -2):**
Assume that $\large{b> 1}$ then $\large{b > 1 > 0}$, so by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(e)]] we know that $\large{0 < b^{-1} < 1}$, since $\large{0 < b^{-1}}$ by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] applied to $\large{b^{-1} < 1}$ we know that $\large{b^{-2} < 1}$. 

**Induction Step:**
Assume that $\large{b^n  < 1}$ and $\large{b>1}$. We know that $\large{b > 1 >0}$ by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(e)]] this would mean that $\large{0 < b^{-1} < 1}$. So $\large{0 < b^{-1}}$, and by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] on $\large{b^n < 1}$ we know that $\large{b^{n-1} < b^{-1} < 1}$ so $\large{b^{n-1} < 1}$. 

##### Lemma 1.Q6c3:
For all $\large{n \in \Bbb Z}$ if $\large{a > 0}$ then $\large{a^n > 0}$.

###### Proof:
**Case I $\large{n > 0}$:** 
[[Gap In Proof of Theorem 1.33(d)#Lemma|Proven in Previous Lemma]]
**Case II $\large{n = 0}$:** 
$\large{a^0 = 1 > 0}$ so $\large{a^n > 0}$.
**Case III $\large{n < 0}$:**
*Base Case(n=2):* 
Assume that $\large{a > 0}$ then $\large{\frac{1}{a}> 0}$ by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(e)]]. By [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(d)]] $\large{(\frac{1}{a})^2 = a^{-2} > 0}$ 
*Induction Step:* 
Assume that $\large{a^n > 0}$ and $\large{a > 0}$ then $\large{\frac{1}{a} > 0}$ by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(e)]], by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] we know that $\large{a^n\frac{1}{a} > 0}$ meaning that $\large{a^{n-1 }> 0}$.

##### Lemma 1.Q6c4:
If $\large{m,n \in \Bbb Z}$ $\large{n,m \ne 0}$ and $\large{n > m, b > 1}$ then $\large{b^n < b^m}$

###### Proof: 
**Case I $\large{n > 0}$:**
Since $\large{n < m}$ we know that $\large{m > 0}$ and $\large{m-n > 0}$. By [[Question 6#Lemma 1.Q6c1|Lemma 1.Q6c1]] we know that $\large{b^{m-n} > 1}$. Additionally by [[Question 6#Lemma 1.Q6c3|Lemma 1.Q6c3]] we know that $\large{b^n > 0}$. So by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] we know that $\large{b^{m-n}b^n > b^n }$ this means that $\large{b^{m-n+n} > b^n}$ so $\large{b^m > b^n}$. 

**Case II $\large{n < 0, m > 0}$:**
Since $\large{m > 0}$ we know that $\large{b^m > 1}$ by [[Question 6#Lemma 1.Q6c1|Lemma 1.Q6c1]]. Additionally by [[Question 6#Lemma 1.Q6c2|Lemma 1.Q6c2]] we know that $\large{b^n < 1}$. So $\large{b^n < 1 < b^m}$ which means that $\large{b^n < b^m }$.

**Case III $\large{n < 0, m < 0}$:**
By [[Question 6#Lemma 1.Q6c3|Lemma 1.Q6c3]] we know that $\large{b^m > 0}$ but since $\large{n < m}$ we know that $\large{n-m < 0}$, so by [[Question 6#Lemma 1.Q6c2|Lemma 1.Q6c2]] we know that $\large{b^{n-m} < 1}$. By [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] we know $\large{b^{n-m}b^m < b^m}$ so $\large{b^{n-m+m} < b^m}$ which leads us to conclude that $\large{b^n < b^m}$.

**Case IV $\large{n = 0, m \ne 0}$:**
$\large{n< m}$ which means that $\large{0 < m}$ so $\large{b^m > 1 = b^n }$ by [[Question 6#Lemma 1.Q6c1|lemma 1.Q6c1]] which means that $\large{b^n < b^m}$.

**Case V $\large{n \ne 0, m = 0}$:** 
$\large{n < m}$ so $\large{ 0 < m}$ which means that $\large{b^n < 1 = b^m}$ by [[Question 6#Lemma 1.Q6c2|Lemma 1.Q6c2]] so $\large{b^n < b^m}$.

##### Lemma 1.Q6c5:
if $\large{n \in \Bbb Z}$ $\large{n < 0, a> 0, b> 0, a> b}$ then $\large{a^n < b^n}$.

###### Proof:
**Base Case $\large{n = -1}$**
Proven through [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(e)]].

**Induction Step:** 
Assume that $\large{b^n >  a^n}$, by [[Question 6#Lemma 1.Q6c3|Lemma 1.Q6c3]] we know that $\large{a^n > 0}$, by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(e)]] we know that $\large{\frac{1}{b} > \frac{1}{a}, b^{-1} > 0}$ and $\large{a^{-1}> 0}$. Using the fact that $\large{b^{-1} > 0}$ with $\large{a^n < b^n }$ in conjunction with [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]].we know that $\large{a^nb^{-1} < b^{n-1}}$. We know that $\large{a^n > 0}$ so applying this to $\large{b^{-1} > a^{-1}}$ through [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] we see that $\large{a^n b^{-1} > a^{n-1}}$, so $\large{b^{n-1} > a^n b^{-1} > a^{n-1}}$ which tells us that $\large{b^{n-1} > a^{n-1}}$.

##### Lemma 1.Q6c6:
If $\large{b>1}$, $\large{m,n \in \Bbb Z}$, $\large{m,n > 0}$ then $\large{b^\frac{1}{m} < b^\frac{1}{n}}$ 

###### Proof:
Since $\large{m > 0}$ and $\large{ n > 0}$ then $\large{mn> 0}$ by [[Fields and Ordered Fields#Definition 1.17|Property II of the Ordered Field]] $\large{\Bbb Q}$. Since $\large{b > 1}$ we know by [[Gap In Proof of Theorem 1.33(d)#Theorem 2|this previously proven theorem]] that $\large{b^\frac{1}{mn} > 1^\frac{1}{mn} = 1}$ so $\large{b^\frac{1}{mn} > 1}$. Since $\large{n < m}$ we know that $\large{n-m < 0}$ and so by [[Question 6#Lemma 1.Q6c5|Lemma 1.Q6c5]] we know that $\large{b^\frac{n-m}{mn} < 1}$. From [[Properties of the Real Field#Theorem 1.21|Theorem 1.21]] we know that $\large{b^\frac{1}{n} > 0}$ meaning that by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] we see that $\large{b^\frac{n-m}{mn}b^\frac{1}{n} < b^\frac{1}{n}}$ so $\large{b^{\frac{1}{m} -\frac{1}{n}}b^\frac{1}{n} = b^{\frac{1}{m} -\frac{1}{n} + \frac{1}{n}} = b^\frac{1}{m} < b^\frac{1}{n}}$ 

##### Lemma 1.Q6c7:
If $\large{t \in \Bbb Q}$ $\large{b > 1}$ $\large{t > 0}$  then $\large{b^t > 1}$.

###### Proof:
$\large{t = \frac{m}{n}, n,m\ne 0}$  since $\large{t > 0}$ either $\large{m,n > 0}$ or $\large{m,n < 0}$ the latter case follows the same line of reasoning as the former but with the substitution $\large{m = -m > 0, n = -n > 0}$. So without loss of generality we will assume that $\large{m,n  >0 }$. By [[Question 6#Lemma 1.Q6c1|Lemma 1.Q6c1]] we know that $\large{b^m > 1}$ and by this [[Gap In Proof of Theorem 1.33(d)#Theorem 2|previously proven theorem]] we know that $\large{b^\frac{m}{n} > 1^\frac{m}{n}  = 1}$ so $\large{b^\frac{m}{n} > 1}$. 

##### Lemma 1.Q6c8:
If $\large{p \in \Bbb Q, q \in \Bbb Q, b> 1, p<q}$ then $\large{b^p < b^q}$. 

###### Proof:
Let $\large{p = \frac{m}{n}, n \ne 0, m,n \in \Bbb Z}$ and let $\large{q = \frac{r}{s}, s\ne 0, s,r \in \Bbb Z}$.

If $\large{p < q}$ then $\large{q = p + t}$ where $\large{t \in \Bbb Q, t > 0}$. By [[Question 6#Lemma 1.Q6c7|Lemma 1.Q6c7]] this means that $\large{b^t > 1}$ and $\large{b^p > 1}$ this would mean that $\large{b^p > 0}$ so by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] we know that $\large{b^{p + t} > b^p}$ which by definition of $\large{q}$ tells us that $\large{b^q > b^p}$.

##### Proof:
Let us denote $\large{\operatorname{sup} B(r)}$ as $\large{\alpha}$.This means that $\large{\alpha}$ is an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{B(r)}$ and that for any other [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{B(r)}$ denoted $\large{\gamma}$ we know that $\large{\gamma \ge \alpha}$. 

First we will show that $\large{b^r \in B(r)}$. Clearly $\large{r \in \Bbb Q}$, additionally we know that $\large{r\le r}$ so we know that $\large{b^r \in B(r)}$ note that this would mean that $\large{b^r \le \alpha}$ since $\large{\alpha}$ is an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{B(r)}$. 

Second we will show that $\large{b^r}$ is an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{B(r)}$. Consider an arbitrary member of $\large{B(r)}$ denoted $\large{b^t}$. Naturally, $\large{t \in B(r)}$ and $\large{t \le r}$, so by [[Question 6#Lemma 1.Q6c8|Lemma 1.Q6c8]] we know that $\large{b^t \le b^r}$ since $\large{t}$ was arbitrarily chosen this would mean that $\large{b^r}$ is an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] to $\large{B(r)}$, which means that by the latter quality of $\large{\alpha}$ we know that $\large{\alpha \le b^r}$.

Since $\large{b^r \le \alpha}$ and $\large{\alpha \le b^r}$ we can only conclude that $\large{b^r = \alpha}$, and so $\large{b^r = \operatorname{sup}B(r)}$ completing the proof.

#### Theorem 1.Q6d:
If $\large{x,y \in \Bbb R}$ then $\large{b^xb^y = b^{x + y}}$.

##### Proof: 
First we will define the set $\large{B(x)B(y)}$ as the set of all products between the elements of $\large{B(x)}$ and $\large{B(y)}$.

Second we will show that $\large{B(x)B(y) = B(x + y)}$. let $\large{b^t \in B(x +y)}$, then $\large{t \in \Bbb Q}$ and $\large{t \lt x + y}$ this means that $\large{t -y < x}$.From [[Question 1#Theorem 1.Q1|Theorem 1.Q1]] we know that $\large{t-y \in \Bbb R}$ in general, of course $\large{x \in \Bbb R}$ by assumption. Since  [[Properties of the Real Field#Theorem 1.20|The rationals are dense in the Reals]] we know that there exists some $\large{p \in \Bbb Q}$ such that $\large{t-y < p < x}$, since $\large{t-y < p}$ by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] we know that $\large{y-t < -p}$ and by [[Fields and Ordered Fields#Definition 1.17|Property I of the Ordered Field]] $\large{\Bbb R}$ we know the inequality $\large{y-t+t = y < -p + t}$ is true, we let $\large{q \in \Bbb Q}$ be defined as $\large{q = t-p}$ which means that $\large{q \le y}$ and hence $\large{b^q \in B(y)}$. Since $\large{p \le x}$ we know that $\large{b^p \in B(x)}$. Since $\large{p +q = t}$ we know that $\large{b^t = b^{p + q}}$ by [[Question 6#Theorem 1.Q6b|Theorem 1.Q6b]] we know that $\large{b^{p+q} = b^pb^q}$. Since $\large{b^p \in B(x)}$ and $\large{b^q \in B(y)}$ we know that $\large{b^t \in B(x)B(y)}$ this means that $\large{B(x +y ) \subset B(x)B(y)}$. 

Let $\large{b^{t^\prime} \in B(x)B(y)}$ which means $\large{b^{t^\prime} = b^rb^s}$ where $\large{t^\prime \in \Bbb Q, r \in \Bbb Q, s \in \Bbb Q}$ and $\large{b^r \in B(x)}$ and $\large{b^s \in B(y)}$. From [[Question 6#Theorem 1.Q6b|Theorem 1.Q6b]] we know that $\large{b^{t^\prime} = b^{r + s}}$. Since $\large{b^r \in B(x)}$ we know that $\large{r \le x}$ similarly we know that $\large{s \le y}$. These two inequalities tell us that $\large{r + s \le x + y}$. Since $\large{r + s =t^{\prime}}$ and $\large{r + s \le x + y}$ we know that $\large{b^{t^\prime} \in B(x + y)}$. This means that $\large{B(x)B(y) \subset B(x + y)}$. 

This completes the proof that $\large{B(x)B(y) = B(x + y)}$. Since these two sets are equal we know that $\large{\operatorname{sup}B(x)B(y) = \operatorname{sup} B(x + y)}$. 

The next section of this proof is adapted by book solutions. we will show that $\large{\operatorname{sup}B(x)\operatorname{sup}B(y) =b^xb^y = \operatorname{sup}B(x)B(y) = \operatorname{sup}B(x + y) = b^{x+y}}$. To do this we will first show that $\large{b^xb^y}$ is an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{B(x)B(y)}$. Since $\large{b^y}$ is an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{B(y)}$ we know that for all $\large{b^r \in B(y), b^r \le b^y}$ by the same line of reasoning we know that for any arbitrary member of $\large{B(x)}$ denoted $\large{b^s}$ it is true that $\large{b^s \le b^x}$, note that both $\large{b^r}$ and $\large{b^s}$ are positive quantities by [[Question 6#Lemma 1.Q6c3|Lemma 1.Q6c3]], which would mean that $\large{b^x > 0}$.This means that we can use [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] to arrive at the inequalities $\large{b^rb^x \le b^xb^y}$ and $\large{b^sb^r \le b^xb^r}$. Combining the two tells us that $\large{b^sb^r \le b^rb^x \le b^xb^y}$, so $\large{b^rb^s \le b^xb^y}$. And since $\large{b^r}$ and $\large{b^s}$ are arbitrary members of $\large{B(y)}$ and $\large{B(x)}$ respectively this would mean that $\large{b^rb^s}$ is an arbitrary member of $\large{B(x)B(y)}$ and so $\large{b^xb^y}$ is an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] to $\large{B(x)B(y)}$.

We will now show that $\large{b^xb^y}$ is the [[Bounds and Bounded Sets#Definition 1.8|Least-Upper-Bound]] of $\large{B(x)B(y)}$. Say that there exists some quantity $\large{\beta < b^xb^y}$ such that $\large{\beta}$ is an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{B(x)B(y)}$. Since $\large{b^x > 0}$ we know that $\large{b^{-x} > 0}$ by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(e)]] this means that by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] $\large{\frac{\beta}{b^x}< b^y}$, we can add $\large{b^y}$ to both sides using [[Fields and Ordered Fields#Definition 1.17|Property I of the Ordered Field]] $\large{\Bbb R}$ and get the inequality $\large{\frac{\beta}{b^x} + b^y < 2b^y}$ applying [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] we know that $\large{\frac{\beta / b^x + b^y}{2} < b^y}$. Since $\large{B(x)B(y)= B(x +y)}$ we know that $\large{\beta}$ is an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{B(x + y)}$. Note that necessarily $\large{\beta > 0}$ since it must be greater than some member of $\large{B(x + y)}$. Since $\large{\frac{\beta/b^x + b^y}{2} < b^y}$ it is not an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{B(y)}$ and hence there must exist some member of $\large{B(y)}$ denoted $\large{b^n}$ such that $\large{b^n > \frac{\beta/b^x + b^y}{2}}$. Note that since $\large{\beta > 0}$ we know that $\large{\frac{\beta}{b^x} > 0}$ note that as previously derived $\large{\frac{\beta}{b^x} < b^y}$ adding $\large{\frac{\beta}{b^x}}$ to both sides through [[Fields and Ordered Fields#Definition 1.17|Property I of the Ordered Field]] $\large{\Bbb R}$ we see that $\large{2\frac{\beta}{b^x} < b^y + \frac{\beta}{b^x}}$ dividing by two using [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] we get the inequality $\large{0 < \frac{\beta}{b^x} < \frac{b^y+\beta/b^x}{2}}$ multiplying by $\large{b^x}$ through [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] we see that $\large{\beta < \frac{b^y + \beta/b^x}{2}b^x}$ note that $\large{0 < \frac{b^y + \beta/b^x}{2}}$ so $\large{0 < \frac{2}{b^y + \beta/b^x}}$ by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(e)]] multiplying by this quantity through [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] we see that $\large{\beta/(\frac{b^y + \beta/b^x}{2}) < b^x}$ this would mean that this quantity is not an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{B(x)}$ so there must exist some $\large{b^m \in B(x)}$ such that $\large{\beta/(\frac{b^y + \beta/b^x}{2}) < b^m}$. As previously shown $\large{\beta/b^x > 0}$ since $\large{b^y > 0}$ we know that $\large{\beta / b^x + b^y > 0}$ and hence $\large{\frac{\beta/b^x + b^y}{2} > 0}$ this means that we can use [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] to multiply both sides of the inequality to get $\large{\beta < b^m \frac{\beta/b^x + b^y}{2}}$ additionally we note that $\large{b^m > 0}$ which means we can get the following inequality though [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] $\large{b^nb^m > \frac{\beta/b^x + b^y}{2}b^m > \beta}$ so $\large{b^nb^m > \beta}$ for some $\large{b^n \in B(y)}$ and $\large{b^m \in B(x)}$ meaning that $\large{\beta}$ is not an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{B(x)B(y) = B(x+y)}$ which contradicts our assumption and leads to the conclusion that $\large{\beta \ge b^xb^y}$ or in other words that $\large{\operatorname{sup}B(x)\operatorname{sup}B(y) = \operatorname{sup} B(x)B(y) = b^xb^y}$. Since $\large{\operatorname{sup}B(x)B(y) = \operatorname{sup}B(x + y)}$ we know that $\large{b^x b^y = b^{x + y}}$.