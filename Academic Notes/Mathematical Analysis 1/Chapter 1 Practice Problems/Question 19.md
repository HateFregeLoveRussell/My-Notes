---
type: Academic
tags: [practice]
alias: Math-An-1-Ch1PP-Q19
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
#### Theorem 1.Q19:
Suppose that $\large{\textbf a \in \Bbb R^k, \textbf b \in \Bbb R^k}$ then there exists $\large{\textbf c \in \Bbb R^k, \textbf c = \frac{4\textbf b - \textbf a}{3}}$ and $\large{r > 0, r = \frac{3}{2}|\textbf b - \textbf a|}$ such that $\large{|\textbf x - \textbf a| = 2|\textbf x - \textbf b|}$ if and only if $\large{|\textbf x - \textbf c| = r}$ 


##### Proof:
The following computation completes the proof (Adapted from textbook solutions).
$$\large{
\begin{eqnarray}
|\textbf x -\frac{4}{3}\textbf b + \frac{1}{3}\textbf a|^2 =& \frac{4}{9} |\textbf b - \textbf a|^2 \\ 
|\textbf x|^2 - \frac{4}{3}\textbf x. \textbf b + \frac{1}{3}\textbf x . \textbf a - \frac{4}{3}\textbf x .\textbf b + \frac{16}{9}|\textbf b|^2 - \frac{4}{9}\textbf b . \textbf a + \frac{1}{3} \textbf x. \textbf a - \frac{4}{9}\textbf b.\textbf a + \frac{1}{9}|\textbf a|^2 =& \frac{4}{9}|\textbf b|^2 -\frac{8}{9}\textbf b . \textbf a + \frac{4}{9}|\textbf a|^2 \\ 
|\textbf x|^2 - \frac{8}{3} \textbf x . \textbf b + \frac{2}{3} \textbf x . \textbf a + \frac{16}{9}|\textbf b|^2 - \frac{8}{9}\textbf b . \textbf a + \frac{1}{9} |\textbf a|^2 =& \frac{4}{9}|\textbf b|^2 -\frac{8}{9}\textbf b . \textbf a + \frac{4}{9}|\textbf a|^2 \\ |\textbf x|^2 -\frac{8}{3}\textbf x. \textbf b + \frac{2}{3}\textbf x. \textbf a +\frac{12}{9}|\textbf b|^2 -\frac{3}{9}|\textbf a|^2 =& 0 \\
3|\textbf x|^2  - 8\textbf x.\textbf b + 2\textbf x.\textbf a
 + 4|\textbf b|^2 - |\textbf a|^2 = & 0  \\
4|\textbf x|^2 -8 \textbf x . \textbf b  + 4|\textbf b|^2 =&  |\textbf x|^2- 2\textbf x . \textbf a + |\textbf a|^2 \\
4|\textbf x - \textbf b|^2 =& |\textbf x - \textbf a|^2 \\ 
2|\textbf x - \textbf b| = & |\textbf x - \textbf a|
\end{eqnarray} 
}$$
