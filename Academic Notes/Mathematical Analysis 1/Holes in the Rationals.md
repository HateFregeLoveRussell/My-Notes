---
type: Academic
tags: []
aliases:
  - Math-An-1-HolesInTheRationals
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
  section-name: "The Real and Complex Number Systems: Introduction"
  ISBN: 978-0-07-054235-8
  book-title: Principles of Mathematical Analysis
  class-alias: Math-An-1
  source-alias: Math-An-1-TheRealAndComplexNumberSystems-Introduction
  start-page: 1
  end-page: 3
  template:
    name: source-tbsection-obj
    version: 1
    type: object
relationship:
  name: standard-relationship-obj
  version: 1
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

## Introduction:
The main goal of this section is to show that despite the fact that the rationals have properties we would deem favourable in a number system such as the fact that there is a rational number between every two rational numbers, it is still inadequate as a number system for certain uses. 
Firstly we will show that there are certain "gaps" within the rational number system despite the property mentioned above. 

## Proof that there exists no rational number $p$ such that $p^2 = 2$:
- Assume that there is such a number $\large p$ such that $\large{p^2 = 2}$.
- Since $p$ is rational we know that  $\large{p = \frac{m}{n}, \space\space m,n \in \Bbb{z}}$  
- $\large{m \space \text{and} \space n}$ cannot both be even as $\large{\frac{2k}{2j} = \frac{k}{j}}$ where $\large{k,j}$ are odd
	- Note that if $\large{k,j}$ are even we can refer back to the previous step
- $\large{(\frac{m}{n})^2 = 2 \implies m^2 = 2n^2}$ so we know that $\large{m^2}$ is even meaning that $\large{m}$ is even
- If $\large{m}$ is even then $\large{m^2}$ is divisible by $\large{4}$
- This means that $\large{2n^2}$ must also be divisible by $\large{4}$
- This means that $\large{n^2}$ is even which implies that $\large{n}$ is even
- This contradicts that both $\large{m, \space n}$ cannot be even 

Although this proof shows that there are such "gaps" in the rational numbers it struggles to give us much insight about their nature, the next proof will provide us with this insight

## Insightful Proof About the Gaps in the Rationals:

- Let $\large{A}$ be the set of all positive rationales such that $\large{p^2 \lt 2}$ 
- Let $\large{B}$ be the set of all positive rationales such that $\large{p^2 > 2}$ 
- Consider the following expression: 
$$
\begin{gather}
q = p - \frac{p^2 - 2}{p+2} = \frac{2p+2}{p+2} \tag{3} \\\
q^2  - 2= \frac{2(p^2 -2)}{(p+2)^2} \tag{4}
\end{gather}
$$
- If $\large{p \in A}$, then $\large{p^2 - 2 \lt 0}$ which means that $\large{\frac{p^2 - 2}{p +2}}$ is negative (since we established that $\large{p}$ is a positive rational)
- Looking at (3) we can see that this implies that $\large{q \gt p}$
- Similarly, looking at ${(4)}$ we can conclude that  $\large{\frac{2(p^2 -2)}{(p+2)^2} \lt 0 \implies q^2 < 2 }$
- This means that $\large{q \in A}$
- If $\large{q \gt p}$ and $\large{q \in A}$ since $\large{p}$ was arbitrarily picked we can conclude that $\large{A}$ has no largest element
- if $p \in B$ then $\large{p^2 - 2 \gt 0}$ so $\large{\frac{p^2 - 2}{p + 2}}$ is positive
- looking at ${(3)}$ we can see that $\large{q \lt p}$, looking at $(4)$ since $\large{\frac{2(p^2 -2)}{(p + 2)^2} > 0}$ we know that $\large{q^2 \gt 2}$ which means that $\large{q \in B}$ Therefore $\large B$ has no smallest value.