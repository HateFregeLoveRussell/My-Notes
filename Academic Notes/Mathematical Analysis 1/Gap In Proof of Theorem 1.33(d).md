---
type: Thinking
tags: [entrynote]
relationship: {name: standard-relationship-obj, version: 1}
parent: "[[Conjugates and Absolute Values#Theorem 1.33]]"
status: {
  state: "Completed",
  template: {
    name: "status-obj",
    version: 1,
    type: "object"
  }
}
validity: {
  state: true,
  template: {
    name: "validity-obj",
    version: 1,
    type: "object"
  }
}
template: {name: premise-template, version: 1}
---
#### Introduction:
In the proof for [[Conjugates and Absolute Values#Theorem 1.33|Theorem 1.33(d and e)]] we never proved the intermediate step of $\large{a,b\in \Bbb R, a,b > 0 , a > b\implies \sqrt{a} > \sqrt {b}}$. Additionally we never proved the dual $\large{a,b\in \Bbb R, a,b > 0,a >b \implies a^n > b^n }$ which is used in [[Properties of the Real Field#Theorem 1.21|Theorem 1.21]].

#### Lemma:
For any positive integer $\large n$ and a positive real number $\large{a > 0 }$, $$\large{a^n > 0 }$$
##### Proof:
###### H(2): Induction Hypothesis
Apply [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] to $\large{a > 0}$ to get $\large{a^2 > 0}$

###### H(n) => H(n +1): Induction Step
Assume $\large{a^n > 0}$, combine this with the fact $\large{a>0}$ and [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] to get $\large{a^{n+1} > 0}$

By induction then the proof is complete


#### Theorem 1: 
For any $\large{a,b \in \Bbb R}$ $\large{a>0,b>0, a>b}$ then $\large{a^n > b^n}$

##### Proof: 
###### H(2): Induction Hypothesis
Assume $\large{a>b>0}$, apply [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] twice to get inequalities $\large{ab>b^2}$ and $\large{a^2 > ab}$ combining the two we find that $\large{a^2>b^2}$ 

###### H(n) => H(n+1): Induction Step
Assume $\large{a^n > b^n}$ we know that $\large{a>b>0}$ applying the latter inequality to the former using [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] $\large{a^{n+1}>b^n a}$. Applying [[Gap In Proof of Theorem 1.33(d)#Lemma|Our Lemma]] to $\large{b>0}$ we see that $\large{b^n > 0}$, applying this to $\large{a>b}$ using [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] we see that $\large{b^na>b^{n+1}}$. Combining this with our previous inequality we see that $\large{a^{n+1}>b^{n+1}}$.

By Induction the proof is complete


#### Theorem 2: 
For any $\large{a,b \in \Bbb R}$ $\large{a>b>0}$ then $\large{a^\frac{1}{n}> b^\frac{1}{n}}$.

##### Proof:
Assume $\large{a>b>0}$ by [[Properties of the Real Field#Theorem 1.21|Theorem 1.21]] we know there exists unique real numbers $\large{c,d}$ where $\large{a = c^n, b = d^n}$, so $\large{c^n > d^n >0}$ furthermore, the theorem tells us that $\large{c>0,d>0}$. Our goal is now to prove $\large{c > d}$, we will do this by contradiction. 
Assume $\large{c \not\gt d}$ so either $\large{c = d}$ or $\large{d > c}$.If $\large{c = d}$ then $\large{c^n = d^n}$, but by the uniqueness assertion from [[Properties of the Real Field#Theorem 1.21|Theorem 1.21]] we know that $\large{c^n \ne d^n}$; If $\large{d > c}$ and $\large{c>0, d>0}$ we will use [[Gap In Proof of Theorem 1.33(d)#Theorem|The Previous Theorem]] to get the inequality $\large{d^n > c^n}$ but we already know that $\large{c^n > d^n}$ which contradicts our finding. So we conclude that $\large{c < d}$ completing the proof.