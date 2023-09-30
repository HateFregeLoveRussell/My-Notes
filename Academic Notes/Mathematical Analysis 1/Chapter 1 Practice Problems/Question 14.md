---
type: Academic
tags: [practice]
alias: Math-An-1-Ch1PP-Q14
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

#### Theorem 1.Q14:
If $\large{z}$ is a [[The Complex Field#Definition 1.24|Complex Number]] such that $\large{|z| = 1}$ then $\large{|1 + z|^2 + |1 - z|^2 = 4}$.

##### Proof:
Note that $\large{|z| = 1}$ is equivalent to saying $\large{z\overline z = 1}$. Consider the following manipulations: 
$$\large{
\begin{eqnarray}
|1 + z|^2 + |1 -z|^2 =& (1 +z)\overline{(1 + z)} + (1-z)\overline{(1-z)} \\
=& (1 + z)(1 + \overline z) + (1 - z)(1 - \overline z) \\
=& 1 + \overline z + z +z\overline z + 1 -z-\overline z + z \overline z \\ 
=& 2 +2z\overline z \\ 
=& 2 + 2|z|^2 \\ 
=&2 + 2 \\
=&4
\end{eqnarray}
}
$$
