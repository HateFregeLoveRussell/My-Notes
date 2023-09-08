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
One gap that has yet to be eliminated in the proof for [[Conjugates and Absolute Values#Theorem 1.33|Theorem 1.33(e)]] is the claim that $\large{\operatorname{Re}(z) \le |z|}$. We will attempt to resolve this gap below. 

#### Theorem:
For any [[The Complex Field#Definition 1.24|Complex Number]] $\large z$, $\large{\operatorname{Re}(z) \le |z|}$.

##### Proof:
We know that $\large{|\operatorname{Re}(z)| \le |z|}$ from [[Conjugates and Absolute Values#Theorem 1.33|Theorem 1.33(d)]]. Consider the case where $\large{\operatorname{Re}(z) = 0}$ then by [[Conjugates and Absolute Values#Definition 1.32|Definition 1.32]] $\large{|\operatorname{Re}(z)| = |0| = 0}$ so $\large{0=\operatorname{Re}(z) \le |z|}$. Now consider the case where $\large{\operatorname{Re}(z) \ne 0}$. Consider the case where $\large{\operatorname{Re}(z) > 0}$ then by [[Conjugates and Absolute Values#Definition 1.32|Definition 1.32]] $\large{|\operatorname{Re}(z)| = \operatorname{Re}(z)}$ applying this to the equality from [[Conjugates and Absolute Values#Theorem 1.33|Theorem 1.33(d)]] we see that $\large{\operatorname{Re}(z) \le |z|}$. Now consider the case where $\large{\operatorname{Re}(z) < 0}$ and the trivially true inequality $\large{-1 < 1}$, applying [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(c)]] we see that $\large{-\operatorname{Re}(z) > \operatorname{Re}(z)}$. By [[Conjugates and Absolute Values#Definition 1.32|Definition 1.32]] we know that $\large{|\operatorname{Re}(z)| = -\operatorname{Re}(z)}$ Applying this to the former inequality we find that $\large{|\operatorname{Re}(z)| > \operatorname{Re}(z)}$, relaxing the inequality we find that $\large{|\operatorname{Re}(z)| \ge \operatorname{Re}(z)}$ completing the proof in all cases.