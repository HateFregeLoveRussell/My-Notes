---
type: Academic
tags: [practice]
alias: Math-An-1-Ch1PP-Q17
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
#### Theorem 1.Q17:
If $\large{\textbf x \in \Bbb R^k}$ and $\large{\textbf{y} \in \Bbb R^k}$ then $\large{|\textbf x + \textbf y|^2 + |\textbf x - \textbf y|^2 = 2|\textbf x|^2 + 2|\textbf y|^2}$

##### Proof:
Consider the following series of algebraic manipulations conforming to the rules which were discovered in [[Euclidean Spaces]]
$$\large{
\begin{eqnarray}
|\textbf x + \textbf y|^2 + |\textbf x - \textbf y|^2 = &(\textbf x + \textbf y).(\textbf x + \textbf y) + (\textbf x - \textbf y).(\textbf x - \textbf y) \\
=& \textbf x . \textbf x + 2\textbf x.\textbf y  + \textbf y.\textbf y + \textbf x.\textbf x -2\textbf x\textbf y + \textbf y.\textbf y \\
=& 2\textbf{x}.\textbf x + 2\textbf y. \textbf y \\
=& 2|\textbf x|^2 + 2|\textbf y|^2
\end{eqnarray}
}$$
