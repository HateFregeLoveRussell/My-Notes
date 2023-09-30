---
type: Academic
tags: [practice]
alias: Math-An-1-Ch1PP-Q20
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

#### Theorem 1.Q20: 
If [[The Real Field#Step 1 Defining the Dedekind Cut|Property III of a Dedekind Cut]] was omitted from the definition the resulting structure would satisfy [[Fields and Ordered Fields#(A) Axioms of Addition|Axioms (A1-A4) but not (A5)]].

##### Proof:
We first define the zero-element of the field to be the set of all non-positive rationals, denoted $\large{\textbf 0^*}$.

Looking at the construction of [[The Real Field#Proof|The Real Field]] we see that the proofs for [[The Real Field#Proof of Axiom (A1)|Axiom (A1)]], [[The Real Field#Proof of Axiom (A2)|Axiom (A2)]], and [[The Real Field#Proof of Axiom (A3)|Axiom (A3)]] are all sub-proofs of the construction's proof. What remains is a proof of [[Fields and Ordered Fields#(A) Axioms of Addition|Axioms (A4)]] and a disproof of [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A5)]].

###### Proof of Axiom (A4):
The forwards inclusion $\large{\alpha + \textbf 0^* \subset \alpha}$ is a sub-proof of the [[The Real Field#Proof of Axiom (A4)|proof]] presented in the construction of the Real Field.  
As for the backwards inclusion $\large{\alpha \subset \alpha + \textbf 0^*}$. Consider some $\large{p \in \alpha}$ and $\large{0 \in \textbf 0 ^*}$ then $\large{p = p + 0\in \alpha + \textbf 0^*}$ completing the proof.

###### Disproof of Axiom (A5):
Assume that [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A5)]] so there always exists some $\large{\beta \in \Bbb R}$ such that $\large{\alpha + \beta = \textbf 0^*}$. Say $\large{\alpha = \{p \in \Bbb Q, p < 0\}}$ then for $\large{l \in \alpha + \beta}$ it is true that $\large{l = p + q}$ where $\large{p \in \alpha}$ and $\large{q \in \beta}$. Since $\large{p < 0}$ there must necessarily exist some $\large{r \in \Bbb Q}$ such that $\large{p < r < 0}$. Since $\large{r < 0}$ it stands to say that $\large{r \in \alpha}$. so $\large{p < r}$ then $\large{p + q < r + q}$ by [[Fields and Ordered Fields#Definition 1.17|Property I of the Ordered Field]] $\large{\Bbb Q}$. Note that $\large{r + q \in \alpha + \beta}$ since $\large{r \in \alpha}$ and $\large{q \in \beta}$. This would mean that if $\large{l \in \textbf 0^*}$ then there exists some $\large{m = r + q \in \textbf 0^*}$ such that $\large{m > l}$, This statement is equivalent to saying $\large{\textbf 0^*}$ has no [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] which we know is false for the set $\large{\textbf 0^* = \{ p \in \Bbb Q, p \le 0 \}}$, so it is true that [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A5)]] does not hold when [[The Real Field#Step 1 Defining the Dedekind Cut|Property III of a Dedekind Cut]] is excluded.