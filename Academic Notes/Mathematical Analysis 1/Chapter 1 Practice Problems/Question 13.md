---
type: Academic
tags: [practice]
alias: Math-An-1-Ch1PP-Q13
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
#### Theorem 1.Q13:
If $\large{x,y \in \Bbb C}$ then $\large{||x| - |y|| \le |x-y|}$.

##### Proof:
Consider the inequality $\large{|x -y +y| \le |x - y| + y}$ which is a consequence of [[Euclidean Spaces#Theorem 1.37|Theorem 1.37(e)]]. Since we know that $\large{x = x -y +y}$ we know that $\large{|x| - |y| \le |x -y| }$. Since $\large{|x| - |y| \in \Bbb R}$ we know that either $\large{||x| - |y|| = |x| - |y|}$ or $\large{||x| - |y|| = |y| - |x|}$. In the former case we know that $\large{||x| - |y|| \le |x-y|}$, in the latter case, substitute $\large{x=y}$ and $\large{y = x}$ into the identity so $\large{||y| - |x||= |x| - |y|}$ this means that $\large{||y| - |x|| \le |x -y|}$. But we know that $\large{||y| - |x|| = |-(|x| - |y|)| = ||x| - |y||}$ so $\large{||x| - |y|| \le |x-y|}$, completing the proof.