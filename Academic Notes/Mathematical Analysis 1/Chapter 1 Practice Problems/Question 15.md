---
type: Academic
tags: [practice]
alias: Math-An-1-Ch1PP-Q15
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

#### Theorem 1.Q15:
The [[The Schwarz Inequality|Schwarz Inequality]] has equality when $\large{a_j = \lambda b_j}$ for some $\large{\lambda \in \Bbb C}$ for all $\large{1 \le j \le n}$.

##### Proof:
Let $\large{C = \sum a_j\overline{b_j}, B = \sum |b_j|^2, A = \sum |a_j|^2}$ where all sums are over all $\large{1 \le j \le n}$. Looking at the [[The Schwarz Inequality#Proof|proof]] for the Schwarz Inequality we can see that it is true that $\large{\sum |Ba_j - Cb_j|^2 = B(AB - |C|^2)}$. It is important to note that we are interested in the condition $\large{AB - |C|^2 = 0}$. Assume that $\large{\sum|Ba_j - Cb_j|^2 = 0}$, this condition is equivalent to $\large{Ba_j = Cb_j}$ for all $\large{1\le j \le n}$. Rearranging we see that $\large{a_j = \frac{C}{B}b_j}$ for all $\large{1 \le j \le n}$ is equivalent to $\large{\sum{|Ba_j -Cb_j|^2} = 0}$. This would mean that $\large{a_j = \lambda b_j}$ for some $\large{\lambda \in \Bbb C}$. 
Now assume that there exists some $\large{\lambda \in \Bbb C}$ such that $\large{a_j = \lambda b_j}$ for all $\large{1 \le j \le n}$. This means that $\large{C= \sum{a_j \overline b_j} = \sum{\lambda b_j \overline b_j} = \lambda\sum{|b_j|^2} = \lambda B}$, additionally this would mean that $\large{Cb_j = \lambda B b_j = B(\lambda b_j) = Ba_j}$ what this implies that $\large{\sum{|Ba_j-Cb_j|^2} = \sum 0 = 0}$. So $\large{\sum{|Ba_j -Cb_j|^2} = 0}$ if and only if $\large{a_j = \lambda b_j}$ for some $\large{\lambda \in \Bbb C}$ for all $\large{1 \le j \le n}$.
Now we will prove that $\large{\sum|Ba_j - Cb_j|^2 = 0}$ if and only if $\large{AB - |C|^2 = 0}$.
The backwards inclusion has already been shown as if $\large{AB -|C|^2 =0}$ then $\large{0 = B(AB - |C|^2) = \sum{|Ba_j - Cb_j|^2}}$. As for the forwards inclusion we note that if $\large{\sum|Ba_j - Cb_j|^2 = 0}$ then either $\large{B =0}$ or $\large{AB-|C|^2 = 0}$ in the latter case the forwards inclusion is already proven so consider the former case. Substitute the definition of $\large{B}$ to get $\large{\sum |b_j|^2 = 0}$ note that this would mean that $\large{b_j = 0}$ for all $\large{1 \le j \le n}$ by [[Conjugates and Absolute Values#Theorem 1.33|Theorem 1.33(a)]]. Now consider $\large{C = \sum {a_j \overline{b_j}}}$ knowing that $\large{b_j = 0 }$ this would mean that $\large{C = \sum 0 = 0}$ which means that $\large{|C|^2 = 0}$ so $\large{AB-|C|^2 = AB}$ but $\large{B = 0 }$ so $\large{AB - |C|^2  = 0}$ so in either case if $\large{\sum{|Ba_j - Cb_j|^2} = 0}$ then $\large{AB- |C|^2 = 0}$ completing the forwards inclusion. 
We know that $\large{\sum{|Ba_j - Cb_j|^2 = 0}}$ if and only if $\large{AB- |C|^2 = 0}$ and that $\large{\sum|Ba_j -Cb_j|^2 =0 }$ if and only if $\large{a_j = \lambda b_j}$ for some $\large{\lambda \in \Bbb C}$ for all $\large{1 \le j \le n}$. So it stands to say $\large{AB- |C|^2 = 0 \iff a_j = \lambda b_j}$ or in other words the [[The Schwarz Inequality#Theorem 1.35|Schwarz Inequality]] has equality if and only if $\large{a_j = \lambda b_j}$ for some $\large{\lambda \in \Bbb C}$ for all $\large{1 \le j \le n}$.

#### Note:
If the [[The Schwarz Inequality#Theorem 1.35|Schwarz Inequality]] is used in the context of a [[Euclidean Spaces#Definition 1.36|Euclidean Spaces]] equality would mean that $\large{\textbf{a}}$ and $\large{\textbf{b}}$ are linearly dependent. 