---
type: Academic
tags: [practice]
alias: Math-An-1-Ch1PP-Q16
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
For all Theorems below make the following assumptions: 
Suppose that $\large{k \ge 3}$ $\large{\textbf x, \textbf y \in \Bbb R^k, d = |\textbf x - \textbf y|, }$ $\large{|\textbf z -\textbf x| = |\textbf z - \textbf y| =r }$.

#### Theorem 1.Q16a:
If $\large{2r > d}$ then there are infinitely many $\large{\textbf z \in \Bbb R^k}$ such that the assumptions above are satisfied. 

##### Proof:
Proof could not be constructed and proof in textbook solutions not understood.

#### Theorem 1.Q16b:
If $\large{2r = d}$ then there exists only one $\large{\textbf{z}\in \Bbb R^k}$ such that the assumptions above are satisfied

##### Proof:
Note that by [[Euclidean Spaces#Theorem 1.37|Theorem 1.37(f)]] we know that $\large{|\textbf{x} - \textbf{y}| \le |\textbf x - \textbf z| + |\textbf z - \textbf y|}$ and since $\large{|\textbf z - \textbf y | = |-(\textbf y - \textbf z)| = |\textbf y - \textbf z|}$ we know that $$\large{
\begin{eqnarray}
|\textbf x - \textbf y| \le & \  |\textbf x - \textbf z| + |\textbf y - \textbf z| \\
d \le & 2r
\end{eqnarray}
}
$$
Note that equality in [[Euclidean Spaces#Theorem 1.37|Theorem 1.37(f)]] relies on equality in [[The Schwarz Inequality#Theorem 1.35|The Schwarz Inequality]], this can be verified by looking at the [[Euclidean Spaces#Proof|proof for Theorem 1.37(f)]]. We know from [[Question 15#Note|Question 15]] that equality in the Schwarz Inequality relies on the linear dependence of its variables, in other words, we have equality in the expression $\large{d \le 2r}$ when $\large{\textbf x - \textbf y}$ and either $\large{\textbf x - \textbf z}$ or $\large{\textbf y - \textbf z}$ are linearly dependent. This would mean that for some $\large{\lambda \in \Bbb R}$ $\large{\textbf x - \textbf y = \lambda(\textbf z - \textbf y)}$.This would mean that $\large{|\textbf x - \textbf y | = |\lambda (\textbf z - \textbf y)|}$ from [[Euclidean Spaces#Theorem 1.37|Theorem 1.37(c)]] we know that $\large{|\textbf x - \textbf y| = |\lambda||\textbf z - \textbf y|}$ but if $\large{d = 2r}$ then $\large{|\textbf x - \textbf y| = 2|\textbf z - \textbf y|}$ so $\large{|\lambda| = 2}$ which means that either $\large{\lambda = 2}$ or $\large{\lambda = -2}$, in the latter case we know that $\large{\textbf x - \textbf y = -2(\textbf z - \textbf y)}$ rearranging we get $\large{\textbf z = \frac{3\textbf y - \textbf x}{2}}$ substituting this we can see that $\large{\textbf x - \textbf z = \frac{2\textbf x + \textbf x - 3\textbf y}{2} = \frac{3\textbf x-3\textbf y}{2} = \frac{3}{2}(\textbf x - \textbf y)}$. Similarly we see that $\large{\textbf y - \textbf z = \frac{2\textbf y - 3\textbf y +\textbf x}{2 } = \frac{\textbf x - \textbf y}{2}=\frac{1}{2}(\textbf x - \textbf y)}$. But we know that $\large{|\textbf x - \textbf z| = |\textbf y - \textbf z| = r}$ which contradicts $\large{|\textbf x- \textbf z| = \frac{3}{2}|\textbf x - \textbf y|}$ while $\large{|\textbf y - \textbf z| = \frac{1}{2}|\textbf x - \textbf y|}$. Now we will consider $\large{\lambda = 2}$ in such a case we know that $\large{\textbf x - \textbf y = 2(\textbf z - \textbf y)}$ rearranging we see that this condition is equivalent to $\large{\textbf z = \frac{(\textbf x + \textbf y)}{2}}$ preforming the substitutions as before we see that $\large{\textbf x - \textbf z = \frac{2\textbf x -\textbf x-\textbf y}{2} = \frac{\textbf x - \textbf y}{2}}$ and $\large{\textbf y - \textbf z = \frac{2\textbf y - \textbf x - \textbf y}{2} = \frac{\textbf y - \textbf x}{2}}$ which conforms to $\large{|\textbf x - \textbf z| = |\textbf y - \textbf z|}$. This means that in the case where equality holds the variable $\large{\textbf z \in \Bbb R^k}$ is uniquely determined by the equation $\large{\textbf z = \frac{\textbf x + \textbf y}{2}}$.

##### Note:
This theorem is actually false in the case of $\large{k = 1}$ as the notion of linear independence does not exist in $\large{\Bbb R}$.

#### Theorem 1.Q16c:
If $\large 2r < d$ then there exists no $\large{\textbf z \in \Bbb R^k}$ such that the assumptions above are satisfied.

##### Proof:
As we [[Question 16#Theorem 1.Q16b|have proven before]] we know that $\large{2r \ge d}$ for all choices of $\large{\textbf z}$. So it is impossible to pick some $\large{\textbf z \in \Bbb R^k}$ such that $\large{2r < d}$.