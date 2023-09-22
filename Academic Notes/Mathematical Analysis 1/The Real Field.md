---
type: Academic
tags: 
alias: Math-An-1-RealField
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
- {
  end-page: 11,
  book-title: "Principles of Mathematical Analysis",
  start-page: 8,
  type: "tbsection",
  ISBN: "978-0-07-054235-8",
  template: {
    version: 1,
    type: "object",
    name: "source-tbsection-obj"
  },
  section-name: "The Real and Complex Number Systems: The Real Field",
  class-alias: "Math-An-1",
  source-alias: "Math-An-1-TheRealAndComplexNumberSystems-TheRealField"
}
- {
  book-title: "Principles of Mathematical Analysis",
  start-page: 17,
  source-alias: "Math-An-1-TheRealAndComplexNumberSystems-Appendix",
  type: "tbsection",
  end-page: 21,
  ISBN: "978-0-07-054235-8",
  template: {
    version: 1,
    type: "object",
    name: "source-tbsection-obj"
  },
  section-name: "The Real and Complex Number Systems: Appendix",
  class-alias: "Math-An-1"
}

relationship:
  name: standard-relationship-obj
  version: 1
friends:
  - "[[Fields and Ordered Fields]]"
  - "[[Holes in the Rationals]]"
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
trello_plugin_note_id: j-Rn0ntpRpTPLqQ5QZZmP
trello_board_card_id: 64fe9c5fd6e78727a9cfad79;64fea333ecfff6e36776cd55
---

### Theorem 1.19(The Existence Theorem):
There exists an ordered field $\large \Bbb R$ which has the [[Bounds and Bounded Sets#Definition 1.10|Least-Upper-Bound Property]]. Moreover, $\large \Bbb R$ contains $\large \Bbb Q$ as a subfield. The members of this field, known as the  **==Real Field==** are called **==Real Numbers==**.

#### Proof:
The following proof will be a direct construction of the real number system this construction is known as the **==Dedekind construction==**.

##### Step 1: Defining the Dedekind Cut
We will populate the set $\large \Bbb R$ with what are called **==Dedekind Cuts==**, denoted as $\large{\alpha, \beta, \gamma,...}$ which are subsets of the set $\large{\Bbb Q}$ defined through the following properties:
- (I): $\large{\alpha \ne \emptyset}$ and $\large{\alpha \ne \Bbb Q}$  ^1bec57
- (II): If $\large{p \in \alpha}$ and $\large{q \in \Bbb Q}$ and $\large{q \lt p}$ then $\large{q \in \alpha}$  ^8c7714
- (III): If $\large{p \in \alpha}$ then $\large{p < r}$ for some $\large{r \in \alpha}$ 
Members of a Dedekind Cut will be denoted through the letters $\large{p,q,r,t,...}$  ^72e0c6
###### Note:
property (III) of a Dedekind Cut simply means that $\large \alpha$ has no largest member. Additionally, from property (II) of a Dedekind Cut we can derive the following theorems. 
- (1): If $\large{p \in \alpha}$ and $\large{q \not \in \alpha}$ then $\large{p < q}$  ^7c898c
	- Proof: Assume that $\large{p \in \alpha, q \not \in \alpha}$. Say that $\large{p > q}$ then by [[The Real Field#^8c7714|Property(II) of the Dedekind Cut]] we know that $\large q \in \alpha$ contradicting our assumption, so $\large{p \le q}$. If $\large{p=q}$ then we know $\large q \in \alpha$ since $\large p \in \alpha$ contradicting our assumption again. So we conclude that $\large p \lt q$  
- (2): if $\large r \not \in \alpha$ and $\large r\lt s$ then $\large s \not \in \alpha$. ^6c91bf
	- Proof: Assume that $\large r\not \in \alpha, r < s$. Assume that $\large{s \in \alpha}$ then by [[The Real Field#^8c7714|Property(II) of the Dedekind Cut]] we know that $\large{r \in \alpha}$ contradicting our assumption so we must conclude that $\large{r \not \in \alpha}$ 
##### Step 2: Defining an Order on $\large{\Bbb R}$
We Define $\large{\alpha \lt \beta}$ to mean that $\large \alpha$ is a [[Basic Set Notation#Definition 1.3|Proper Subset]] of $\large \beta$. In order to prove that this definition can be considered as an [[Orders and Ordered Sets#Definition 1.5|Order]] on $\large{\Bbb R}$ we will first show that it satisfies transitivity and then show that $\large{\alpha < \beta, \alpha > \beta, \alpha = \beta}$ are exclusive and that one is true for any given pair $\large{(\alpha,\beta)}$.

###### Proof of Transitivity: 
Assume that $\large{\alpha < \beta}$ and that $\large{\beta \lt \gamma}$. If $\large{x \in \alpha}$ then $\large{x \in \beta}$ since $\large{\alpha \subset \beta}$, and then since $\large{x \in \beta}$ we know that $\large{x \in \gamma}$ since $\large{\beta \subset \gamma}$, so we conclude that $\large{\alpha \subset \gamma}$. Assume that $\large{\gamma \subset \alpha}$ since we know that $\large \alpha \lt \beta$ we know that $\large{\gamma \subset \beta}$. Since $\large{\beta \lt \gamma}$ we know that $\large{\beta \subset \gamma}$ which means that $\large{\beta = \gamma}$ but we know that $\large{\beta \ne \gamma}$ since $\large{\beta \lt \gamma}$ which leads to contradiction so we conclude that $\large{\gamma \not \subset \alpha}$, since $\large{\alpha \subset \gamma}$ and $\large{\gamma \not \subset \alpha}$ we know that $\large{\alpha \lt \gamma}$ completing our proof of transitivity. 

###### Proof of Exclusivity: 
Assume that there exists a pair of Dedekind Cuts $\large{(\alpha, \beta)}$. Note that if $\large{\alpha = \beta}$ we know that $\large{\alpha \not \lt \beta}$ and $\large{\alpha \not \gt \beta}$ by the definition of a [[Basic Set Notation#Definition 1.3|Proper Subset]]. So assume that $\large{\alpha \ne \beta}$. Say that $\large{\alpha \lt \beta}$ and that $\large{\alpha \gt \beta}$ but by definition of a [[Basic Set Notation#Definition 1.3|Proper Subset]] this would mean that $\large{\alpha = \beta}$ contradicting our assumption so we must conclude that $\large{\alpha \lt \beta}$ and $\large{\alpha \gt \beta}$ are mutually exclusive. This means that for any given pair of Dedekind Cuts $\large{(\alpha,\beta)}$ the statements $\large{\alpha = \beta, \alpha \lt \beta, \alpha \gt \beta}$ are mutually exclusive. 
 
Now to show that for any given pair of Dedekind Cuts $\large{(\alpha,\beta)}$ one of the following statements is true $\large{\alpha = \beta, \alpha < \beta, \alpha > \beta}$. To do this first assume that $\large{\alpha \ne \beta, \alpha \not \lt \beta}$ and let $\large{q \in \beta}$ note that the existence of $\large{q}$ is guaranteed by [[The Real Field#^1bec57|Property I of a Dedekind Cut]]. Since $\large{\alpha \not \lt \beta}$ and $\large{\alpha \ne \beta}$ we know that $\large{\alpha \not \subset \beta}$ which means that there exists some rational number $\large{p}$ such that $\large{p \not \in \beta}$ and $\large{p \in \alpha}$ by applying [[The Real Field#^7c898c|Theorem (1) of a Dedekind Cut]] on to $\large{p}$ and $\large{q}$ we know that $\large{q < p}$. Since we know $\large{p \in \alpha}$ and $\large{q < p}$ through [[The Real Field#^8c7714|Property II of a Dedekind Cut]] we know that $\large{q \in \alpha}$. Since $\large{q}$ was arbitrarily chosen we know that $\large{\beta \subset \alpha}$, but we know that $\large{\beta \ne \alpha}$ so $\large{\beta \lt \alpha}$. 

##### Step 3: $\large{\Bbb R}$ has the Least-Upper-Bound Property
Now we will prove that $\large{\Bbb R}$ has the [[Bounds and Bounded Sets#Definition 1.10|Least-Upper-Bound Property]]. This will be done by first constructing a set $\large{\gamma}$ from an arbitrary subset of $\large{\Bbb R}$ called $\large{A}$, proving that $\large{\gamma}$ is a Dedekind Cut, and that it is the [[Bounds and Bounded Sets#Definition 1.8|Supremum]] of $\large{A}$.
 
Let $\large{A}$ be some nonempty subset of $\large{\Bbb R}$ and assume that $\large{\beta \in \Bbb R}$ is an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{A}$, in other words $\large{A}$ is [[Bounds and Bounded Sets#Definition 1.7|Bounded Above]].
Define $\large{\gamma}$ as the union of all the members of $\large{A}$, in other words $\large{p\in \gamma \implies \exists \alpha \in A(p \in \alpha)}$.
Since $\large{A}$ is a nonempty set there must exist some set $\large{\alpha_0}$. Since $\large{\alpha_0}$ is a Dedekind Cut we know $\large{\alpha_0}$ is nonempty by [[The Real Field#^1bec57|Property (I) of a Dedekind Cut]] and by definition of $\large{\gamma}$ we know $\large{\alpha_0 \subset \gamma}$ so $\large{\gamma}$ is also nonempty. We know that $\large{\forall \alpha \in A(\alpha \le \beta)}$ so the union of every set in $\large{A}$, also known as $\large{\gamma}$ is a subset of $\large{\beta}$. But $\large{\beta}$ is a Dedekind Cut so by [[The Real Field#^1bec57|Property (I) of a Dedekind Cut]] we know that $\large{\beta \ne \Bbb Q}$ so it follows to say that $\large{\gamma \ne \Bbb Q}$. 
Since $\large{\gamma \ne \Bbb Q}$ and $\large{\gamma}$ is nonempty we know that $\large{\gamma}$ satisfies [[The Real Field#^1bec57|Property (I) of a Dedekind Cut]].
Pick some $\large{p \in \gamma}$. This means that there exists some $\large{\alpha_1 \in A}$ such that $\large{p \in \alpha_1}$ suppose there is some $\large{q \in \Bbb Q}$ such that $\large{q < p }$. By [[The Real Field#^8c7714|Property (II) the Dedekind Cut]] $\large \alpha_1$ we know that $\large{q \in \alpha_1}$ and hence $\large{q \in \gamma}$. This proves that $\large{\gamma}$ satisfies [[The Real Field#^8c7714|Property (II) of a Dedekind Cut]]. 
By [[The Real Field#^72e0c6|Property (III) of a Dedekind Cut]] we know that there exists some $\large{r \in \alpha_1}$ such that $\large{p < r}$ then $\large{r \in \gamma}$ which means that $\large{\gamma}$ satisfies [[The Real Field#^72e0c6|Property (III) of a Dedekind Cut]].
This means that $\large{\gamma}$ is a Dedekind Cut and hence $\large{\gamma \in \Bbb R}$. By the construction of $\large{\gamma}$ we know that $\large{\forall \alpha \in A(\alpha \le \gamma)}$.
Assume that there exists some cut $\large{\delta}$ such that $\large{\delta \lt \gamma}$ then by definition of the chosen [[The Real Field#Step 2 Defining an Order on $ large{ Bbb R}$|Order]] on $\large{\Bbb R}$ we know that there must exist some $\large{s \in \gamma}$ such that $\large{s \not \in \delta}$ since $\large{s \in \gamma }$ we know there exists some cut $\large{\alpha_2 \in A}$ such that $\large{s \in \alpha_2}$ which means that $\large{\alpha_2 \gt \delta}$ so $\large{\delta}$ is not an [[Bounds and Bounded Sets#Definition 1.7|Upper Bound]] of $\large{A}$. Therefore we know that $\large{\gamma \in \Bbb R}$ is the [[Bounds and Bounded Sets#Definition 1.8|Supremum]] of $\large{A}$. 

##### Step 4: $\large{\Bbb R}$ Satisfies the Field Axioms of Addition
We define the sum of two real numbers $\large{\alpha + \beta}$ to be the set of all sums $\large{r \in \alpha, s\in \beta, s + r}$.

We also define the additive identity of the real [[Fields and Ordered Fields#Definition 1.12|Field]], is denoted as $\large{0^*}$ which is defined to be the set of negative rational numbers.
First we will show that $\large{0^*}$ is a Dedekind Cut.

Clearly $\large{0^*}$ satisfies [[The Real Field#^1bec57|Property (I) of a Dedekind Cut]] since $\large{0^*}$ is neither an empty set or equal to $\large{\Bbb Q}$. Assume that $\large{p \in 0^*}$, and pick $\large{q \in \Bbb Q}$ such that $\large{q < p}$. Clearly $\large{p < 0}$ so $\large{q < 0}$ which means that $\large{q \in 0^*}$, so $\large{0^*}$ satisfies [[The Real Field#^8c7714|Property (II) of a Dedekind Cut]]. We know that $\large{0 \in \Bbb Q}$ and that $\large{p \in \Bbb Q}$ so there must exist some entry $\large{q \in \Bbb Q}$ such that $\large{p < q < 0}$ so $\large{q \in 0^*}$ which means that [[The Real Field#^72e0c6|Property (III) of a Dedekind Cut]]. It follows to say that $\large{0^*}$ is a Dedekind Cut.

###### Proof of Axiom (A1):
We must show that $\large{\alpha + \beta}$ is a cut or that $\large{\alpha + \beta \in \Bbb R}$. Clearly if $\large{\alpha \ne \emptyset}$ and $\large{\beta \ne \emptyset}$ we know that $\large{\alpha + \beta \ne \emptyset}$, we know this to be true through [[The Real Field#^1bec57|Property (I) of the Dedekind Cut]] as applied to sets $\large{\alpha}$ and $\large{\beta}$. Assume that $\large{r \in \alpha, s \in \beta, r^\prime \not \in \alpha, s^\prime \not \in \beta }$ then by the application of [[The Real Field#^7c898c|Theorem (1)]] we know that $\large{r^\prime > r}$. Since $\large{\Bbb Q}$ is an ordered field we will use [[Fields and Ordered Fields#Definition 1.17|Property I of an Ordered field]]  to get the inequality $\large{r^\prime + s^\prime > r + s^\prime}$. Through the same line of reasoning we also arrive at the inequality $\large{s^\prime + r > s + r}$ which means that $\large{r^\prime  + s^\prime > r + s}$ so $\large{r^\prime + s^\prime \ne r+s}$ since $\large{r}$ and $\large{s}$ were chosen arbitrarily we know that $\large{r^\prime + s^\prime \not \in \alpha + \beta}$ since $\large{r^\prime + s^\prime \in \Bbb Q}$ we know that $\large{\alpha + \beta \ne \Bbb Q}$. Note that this proof relies on the fact that $\large{\Bbb Q}$ is not partitioned by $\large{(\alpha,\beta)}$, this is impossible as any partitioning of $\large{\Bbb Q}$ by Dedekind Cuts would necessarily involve the inclusion of a cut that spans the entirety of $\large{\Bbb Q}$. Since $\large{\alpha + \beta \ne \emptyset}$ and $\large{\alpha + \beta \ne \Bbb Q}$ we know that $\large{\alpha + \beta}$ satisfies [[The Real Field#^1bec57|Property (I)of a Dedekind Cut]]

Pick some $\large{p \in \alpha + \beta}$ then $\large{p = r + s}$ for some $\large{r \in \alpha}$ and $\large{s \in \beta}$. Pick some $\large{q \in \Bbb Q}$ such that $\large{q < p}$, then $\large{q < r -s}$ by substitution and $\large{q-s < r}$ by [[Fields and Ordered Fields#Definition 1.17|Property I of the Ordered Field]] $\large{\Bbb Q}$ alongside [[Fields and Ordered Fields#(A) Axioms of Addition|Axioms (A4) and (A5)]] in $\large{\Bbb Q}$. Since $\large{r\in \alpha}$ by applying [[The Real Field#^8c7714|Property (II) of a Dedekind Cut]] we know that $\large{q-s \in \alpha}$, since $\large{q = q-s + s}$ and $\large{q-s \in \alpha, s \in \beta}$ we know that $\large{q \in \alpha + \beta}$. And hence $\large{\alpha + \beta}$ satisfies [[The Real Field#^8c7714|Property (II) of a Dedekind Cut]].

Consider $\large{p = r + s}$ where $\large{r \in \alpha}$ and $\large{s \in \beta}$ so $\large{p \in \alpha + \beta}$. By [[The Real Field#^72e0c6|Property (III) of a Dedekind Cut]] we know there exists some $\large{t \in \alpha}$ such that $\large{t > r}$, adding $\large{s}$ to both sides through [[Fields and Ordered Fields#Definition 1.17|Property I of the Ordered Field]] $\large{\Bbb Q}$ we get the inequality $\large{t + s > r +s}$ and since $\large{t \in \alpha}$ and $\large{s \in \beta}$ we know that $\large{t + s \in \alpha + \beta}$ and so [[The Real Field#^72e0c6|Property (III) of Dedekind Cuts]] hold for $\large{\alpha + \beta}$. 
And so $\large{\alpha + \beta \in \Bbb R}$.

###### Proof of Axiom (A2):
$\large{\alpha + \beta}$ is the set of all $\large{r +s}$ where $\large{r \in \alpha, s \in \beta}$. By [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A2)]] in the field $\large{\Bbb Q}$ we know that $\large{r + s = s + r}$ but $\large{s + r \in \beta + \alpha}$. so $\large{\alpha + \beta = \beta + \alpha}$ 

###### Proof of Axiom (A3):
$\large{(\alpha + \beta) + \gamma}$ is the set of all $\large{(r + s) + t}$ such that $\large{r \in \alpha, s \in \beta, t \in \gamma}$. By [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A3)]] of the field $\large{\Bbb Q}$ we know that $\large{(r + s) + t = r + (s + t)}$ but $\large{r + (s + t) \in \alpha + (\beta + \gamma)}$ so $\large{(\alpha + \beta) + \gamma = \alpha + (\beta + \gamma)}$.

###### Proof of Axiom (A4):
Assume that $\large{r \in \alpha}$, $\large{s \in 0^*}$, since $\large{s < 0}$ then $\large{r + s < r }$ by [[Fields and Ordered Fields#Definition 1.17|Property I of the Ordered Field]] $\large{\Bbb Q}$. By [[The Real Field#^8c7714|Property (II) of a Dedekind Cut]] we know that $\large{r + s \in \alpha}$ this means that $\large{\alpha + 0^* \subset \alpha}$. 
Now assume that $\large{p \in \alpha}$, by [[The Real Field#^72e0c6|Property (III) of a Dedekind Cut]] we know that there exists some $\large{r\in \alpha}$ such that $\large{p < r}$ by [[Fields and Ordered Fields#Definition 1.17|Property I of the Ordered Field]] $\large{\Bbb Q}$ in combination with [[Fields and Ordered Fields#(A) Axioms of Addition|Axiom (A4) and Axiom (A5)]] in $\large{\Bbb Q}$ we know that $\large{p-r < 0}$ so $\large{p-r \in 0^*}$. Note that $\large{p-r + r = p}$ so $\large{p \in \alpha + 0^*}$ thus $\large{\alpha \subset \alpha + 0^*}$ 
We can now conclude that $\large{\alpha = \alpha + 0^*}$ for an arbitrary Dedekind Cut $\large{\alpha }$.

###### Proof of Axiom (A5):
Fix $\large{\alpha \in \Bbb R}$. Let $\large{\beta}$ be the set of all $\large{p \in \Bbb Q}$ such that there exists some $\large{r > 0, r \in \Bbb Q}$ where $\large{-p-r \not \in \alpha}$.
We will first show that $\large{\beta}$ is a Dedekind Cut, or in other words we will first prove $\large{\beta \in \Bbb R}$. 

If $\large{s \not \in \alpha}$ consider $\large{p = -s -1}$ which means that $\large{s = -p-1}$ so we can conclude that $\large{-p -1 \not \in \alpha }$ this means that $\large{p \in \beta}$. Since $\large \alpha$ is a Dedekind Cut we know it does not equal the set of rational numbers which means that $\large{s}$ and by consequence $\large{p}$ necessarily exist, so we can conclude that $\large{\beta}$ is a nonempty set.
If $\large{q \in \alpha}$ consider an arbitrary positive rational number $\large{r}$, by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(a)]] over the field $\large{\Bbb Q}$ we know that $\large{-r < 0}$. By [[Fields and Ordered Fields#Definition 1.17|Property I of the Ordered Field]] $\large{\Bbb Q}$ we know that $\large{q-r < q}$. Which means that by [[The Real Field#^8c7714|Property II of a Dedekind Cut]] $\large{q-r \in \alpha}$. Note that $\large{--q = q}$ by [[Properties of Fields and Ordered Fields#Proposition 1.14|Proposition 1.14(d)]] in $\large{\Bbb Q}$ so $\large{--q -r \in \alpha}$. Since $\large{r}$ was chosen arbitrarily we know that $\large{-q \not \in \beta}$. This means that $\large{\beta \ne \Bbb Q}$ since there will always exist an element in $\large{\Bbb Q}$ which is not a member of it. Since $\large{\beta \ne \Bbb Q}$ and $\large{\beta \ne \emptyset}$ we know that $\large{\beta}$ satisfies [[The Real Field#^1bec57|Property I of a Dedekind Cut]]. 

Pick some $\large{p \in \beta}$. Then there must exist some $\large{r\in\Bbb Q, r >0}$ such that $\large{-p -r \not \in \alpha}$. Consider a quantity $\large{q\in\Bbb Q}$ such that $\large{q < p}$. Applying [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(c)]] we know that $\large{-q > -p}$, applying [[Fields and Ordered Fields#Definition 1.17|Property I of the Ordered Field]] $\large{\Bbb Q}$ we see that $\large{-q-r > -p-r}$. By [[The Real Field#^6c91bf|Theorem (2)]] of the Dedekind Cut we know that $\large{-q-r \not \in \alpha}$ which by definition of $\large{\beta}$ means that $\large{q\in \beta}$. This mean that $\large{\beta}$ satisfies [[The Real Field#^8c7714|Property (II) of a Dedekind Cut]].

Pick some $\large{p \in \beta}$ then there exists some $\large{r \in \Bbb Q, r > 0}$ such that $\large{-p-r \not \in \alpha}$. Consider a quantity $\large{t= p + \frac{r}{2}}$. Since $\large{r > 0}$ we know that $\large{t > p}$ by the application of [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(b)]] in $\large{\Bbb Q}$ and [[Fields and Ordered Fields#Definition 1.17|Property I of the Ordered Field]] $\large{\Bbb Q}$. Additionally it is clear that $\large{-t = -p -\frac{r}{2}}$ which means that $\large{-t-\frac{r}{2} = -p-r}$ or in other words $\large{-t -\frac{r}{2} \not \in \alpha}$ which means that $\large{t \in \beta}$. So there always exists a quantity $\large{t\in \beta}$ for which $\large{t > p}$ for any $\large{p \in \beta}$. So $\large{\beta}$ satisfies [[The Real Field#^72e0c6|Property (III) of a Dedekind Cut]].

This means that $\large{\beta}$ qualifies as a Dedekind Cut. Now to prove that $\large{\alpha + \beta = 0^*}$.

(=>) Assume that $\large{s \in \beta}$ then for some $\large{t_0 \in \Bbb Q, t_0 >0}$ we know that $\large{-s-t_0 \not \in \alpha}$. Say that $\large{-s \in \alpha}$, and consider an arbitrary positive quantity $\large{t \in \Bbb Q, t>0}$ then by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(a)]] in $\large{\Bbb Q}$ we know that $\large{-t < 0}$. By [[Fields and Ordered Fields#Definition 1.17|Property I of the Ordered Field]] $\large{\Bbb Q}$ we can add $\large{-s}$ to both sides yielding the inequality $\large{-s-t < -s}$. Since we assumed that $\large{-s\in \alpha}$ we can use [[The Real Field#^8c7714|Property (II) of a Dedekind Cut]] to conclude that $\large{-s-t \in \alpha}$. Since $\large{t}$ was arbitrarily chosen this result holds for all $\large{t}$. But this contradicts the fact that for some $\large{t_0}$ it is true that $\large{-s-t_0 \not \in \alpha}$, hence we must conclude that $\large{-s \not \in \alpha}$. Consider $\large{r \in \alpha}$, by [[The Real Field#^7c898c|Theorem (1) of the Dedekind Cut]] we know that $\large{r < -s}$, using [[Fields and Ordered Fields#Definition 1.17|Property I of the Ordered Field]] $\large{\Bbb Q}$ we can see that $\large{r + s < 0}$. Thus $\large{\alpha + \beta \subset 0^*}$.

(<=) pick some $\large{v \in 0^*}$, put $\large{w = \frac{-v}{2}}$, since $\large{v <0 }$ we know that $\large{w> 0}$ by [[Properties of Fields and Ordered Fields#Proposition 1.18|Proposition 1.18(a) and Proposition 1.18(b)]]. Since $\large{\Bbb Q}$ has the [[Properties of the Real Field#Theorem 1.20|Archimedean Property]] we know there exists some integer $\large{n}$ such that $\large{nw \in \alpha}$ but $\large{(n+1)w \not \in \alpha}$. Put $\large{p = -(n+2)w}$ note that since $\large{(n+1)w \not \in \alpha}$ and $\large{(n+1)w = (n+2)w -w= -p -w}$, so $\large{-p -w \not \in \alpha}$ and since $\large{w > 0}$ we know that $\large{p \in \beta}$. The manipulation $\large{p + nw = -(n+2)w + nw= -nw -2w + nw = -2w= -2\frac{-v}{2} = v}$ tells us that $\large{v \in \beta + \alpha}$, since $\large{p \in \beta}$ and $\large{nw \in \alpha}$. From this we can conclude that $\large{0^* \subset \alpha + \beta}$.

Since $\large{0^* \subset \alpha + \beta}$ and $\large{\alpha + \beta \subset 0^*}$ we know that $\large{\alpha + \beta = 0^*}$. Henceforth the element denoted $\large{\beta}$ in this proof will be denoted by $\large{-\alpha}$.


##### Step 5: $\large{\Bbb R}$ Satisfies the First Property of an Ordered Field
Having proven the [[Fields and Ordered Fields#(A) Axioms of Addition|Field Axioms of Addition]] hold in $\large{\Bbb R}$ we now know that [[Properties of Fields and Ordered Fields#Proposition 1.14|Proposition 1.14]] holds in $\large{\Bbb R}$. 

Suppose that $\large{\alpha,\beta,\gamma \in \Bbb R}$ and $\large{\beta < \gamma}$. The latter assumption means that $\large{\beta}$ is a proper subset of $\large{\gamma}$ meaning that if $\large{t \in \beta}$ then $\large{t \in \gamma}$.

Suppose that $\large{s \in \alpha}$, $\large{t \in \beta}$ so $\large{s + t \in \alpha + \beta}$ since $\large{\beta}$ is a proper subset of $\large{\gamma}$ meaning that $\large{t \in \gamma}$ so $\large{s + t \in \alpha + \gamma}$. This means that $\large{\alpha + \beta \subset \alpha + \gamma}$. Now suppose that $\large{\alpha + \beta = \alpha + \gamma}$ by [[Properties of Fields and Ordered Fields#Proposition 1.14|Proposition 1.14(a)]] $\large{\beta = \gamma}$. But we know that $\large{\beta < \gamma}$ so it stands to say that $\large{\alpha + \beta \ne \alpha + \gamma}$. Since $\large{\alpha + \beta \subset \alpha + \gamma}$ and $\large{\alpha + \beta \ne \alpha + \gamma}$ we know that $\large{\alpha + \beta < \alpha + \gamma}$. So if $\large{\beta < \gamma}$ then $\large{\alpha + \beta < \alpha + \gamma}$. This means that $\large{\Bbb R}$ satisfies [[Fields and Ordered Fields#Definition 1.17|Property I of Ordered Field]].

##### Step 6: $\large{\Bbb R}$ Satisfies the Field Axioms of Multiplication and the Second Property of an Ordered Field:
In order to prove that $\large{\Bbb R}$ satisfies the [[Fields and Ordered Fields#(M) Axioms of Multiplication|Field Axioms of Multiplication]] we first should prove that they hold in $\large{\Bbb R^+}$ (the set of all Dedekind Cuts $\large{\alpha}$ for which $\large{\alpha > 0^*}$) 
Multiplication is defined as follows. Let $\large{\alpha \in \Bbb R^+}$ and $\large{\beta \in \Bbb R^+}$ then $\large{\alpha\beta}$ is the set of all $\large{p \in \Bbb Q}$ such that $\large{p \le rs}$ for some $\large{r \in \alpha, r>0}$ and $\large{s\in\beta, s > 0}$.
We define the multiplicative identity to be $\large{1^*}$ the set of all $\large{q \in \Bbb Q}$. such that $\large{1 > q}$.
The proof of the axiom sets [[Fields and Ordered Fields#(M) Axioms of Multiplication|(M)]] and [[Fields and Ordered Fields#(D) The Distributive Law|(D)]] were omitted from the textbook.

Assume that $\large{\alpha > 0^*}$ and $\large{\beta > 0^*}$. Suppose that $\large{q \in 0^*}$, since $\large{\alpha > 0^*}$ we know that $\large{q \in \alpha}$ through the same reasoning we know that $\large{q \in \beta}$, additionally not that since $\large{q\in0^*}$ we know that $\large{q < 0}$. Now assume that $\large{q \not \in \alpha\beta}$, this would mean that there does not exist an $\large{r > 0, r \in \alpha, s > 0, s \in \beta}$ such that $\large{q \le rs}$, in other words $\large{q > rs}$ for all such $\large s$ and $\large r$. Since $\large{q < 0}$ however we know that $\large{rs < 0}$. This would mean that either $\large{r < 0}$ or $\large{s < 0}$ which is impossible by the construction of both $\large{r}$ and $\large{s}$. So it stands to say that $\large{q \in \alpha \beta}$ hence $\large{0^* \subset \alpha\beta}$.

For the next section of the proof note that [[Properties of Fields and Ordered Fields#Proposition 1.16|Proposition 1.16]] holds in $\large{\Bbb R}$ since the Multiplicative and Distributive axioms were shown to hold. Since $\large{\alpha > 0^*}$ and $\large{\beta > 0^*}$ by [[Properties of Fields and Ordered Fields#Proposition 1.16|Proposition 1.16(b)]] we know that $\large{\alpha\beta \ne 0^*}$ but we know that $\large{0^* \subset \alpha\beta}$ so $\large 0^*$ is a proper subset of $\large{\alpha\beta}$ so $\large{0^* < \alpha\beta}$. Therefore [[Fields and Ordered Fields#Definition 1.17|Property II of an Ordered Field]] hold in $\large{\Bbb R}$. 


##### Step 7: Extending the Definition of Multiplication in $\large{\Bbb R}$:
The definition of multiplication in $\large{\Bbb R}$ will now be extended to encompass negative quotients. This will be done by first setting $\large{0^*\alpha = \alpha0^* = 0^*}$ and defining:$$\large{\begin{equation}
\alpha\beta =
\left\{
\begin{array}{lr}
(-\alpha)(-\beta), & \text{if } \alpha < 0^*,\beta < 0^*\\
-[(-\alpha)\beta], & \text{if } \alpha < 0^*, \beta > 0^* \\
-[\alpha(-\beta)], & \text{if } \alpha > 0^*, \beta < 0^* \\ 
\alpha\beta & \text{if } \alpha > 0^*, \beta > 0^*
\end{array}
\right\}
\end{equation}}$$
Note that with this definition in all cases we've reduced the multiplication of one or more negative members of $\large{\Bbb R}$ to two positive members of $\large{\Bbb R}$. 

Similarly the proof of the Multiplicative Axioms [[Fields and Ordered Fields#(M) Axioms of Multiplication|(M)]] and the Distributive Axiom [[Fields and Ordered Fields#(D) The Distributive Law|(D)]] were omitted from the textbook outlines however were provided. 

Proving the multiplicative axioms can be done through repeated application of [[Properties of Fields and Ordered Fields#Proposition 1.14|Proposition 1,14(d)]]. 
Proving the distributive axiom is done through splitting the proof into cases (example: $\large{\alpha > 0^* \beta <0^*, \beta + \gamma > 0^*}$)

We have now shown that $\large{\Bbb R}$ is an [[Fields and Ordered Fields#Definition 1.17|Ordered Field]].

##### Step 8: Creating an Association between $\large{\Bbb Q}$ and $\large{\Bbb Q^*}$ 
We will now associate each rational number $\large{r \in \Bbb Q}$ with $\large{r^* \in \Bbb Q^*}$. where $\large{r^*}$ consist of all $\large{p \in \Bbb Q}$ where $\large{p < r}$. It is clear that $\large{r^*}$ is a Dedekind Cut, so $\large{r^* \in \Bbb R}$. Additionally these cuts satisfy:
- (a): $\large{r^* + s^* = (r + s)^*}$
- (b): $\large{r^*s^* = (rs)^*}$ 
- (c): $\large{r^* < s^*}$ if and only if $\large{r  < s}$ 

##### Step 9: Proving $\large{\Bbb Q}$ is a Subfield of $\large{\Bbb R}$.
Since the association in the previous step preserves multiplication, addition, and order we can regard $\large{\Bbb Q}$ as a subfield of $\large{\Bbb R}$. This type of association is commonly called an **==isomorphism==**.

In general it is true any two [[Fields and Ordered Fields#Definition 1.17|Ordered Fields]] with the [[Bounds and Bounded Sets#Definition 1.10|Least-Upper-Bound Property]] are isomorphic.
