---
type: Academic
tags: [practice]
alias: Math-An-1-Ch1PP-Q10
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

#### Theorem 1.Q10
Suppose that $\large{z = a+bi, w= u +vi}$ and  $$\large{a = \left(\frac{|w| + u}{2}\right)^\frac{1}{2}, \quad b = \left( \frac{|w| - u}{2}\right)^\frac{1}{2}}$$
then if $\large{v \ge 0 }$ then $\large{z^2 = w}$ and if $\large{v \le 0}$ then $\large{(\overline z)^2 = w}$. Additionally every [[The Complex Field#Definition 1.24|Complex Number]] with the exception of $\large{0}$ has two complex square roots.

##### Proof:
Consider the following series of manipulations:
$$\large{
\begin{eqnarray}
z^2 =& a^2 -  b^2 +2abi \\
z^2 =& \left(\frac{|w| + u}{2} \right) - \left(\frac{|w| - u}{2}\right) + 2i\left(\frac{|w| + u}{2}\right)^\frac{1}{2}\left(\frac{|w| - u}{2}\right)^\frac{1}{2} \\
z^2 =& \frac{1}{2}(|w| - |w| + u +u) + 4^\frac{1}{2}i\left(\frac{|w| + u}{2}\right)^\frac{1}{2}\left(\frac{|w| - u}{2}\right)^\frac{1}{2} \\
z^2 =& \frac{1}{2}2|w| + i\left(\frac{|w| + u}{2}\frac{|w|-u}{2}\right)^\frac{1}{2} \\ 
z^2 = &u + i((|w| + u)(|w| - u))^\frac{1}{2} \\
z^2 = &u + i(|w|^2 + -|w|u + |w|u -u^2)^\frac{1}{2} \\
z^2 =& u + i(|w|^2 -u^2)^\frac{1}{2} \\
z^2 =& u + i(u^2 + v^2 - u^2)^\frac{1}{2} \\
z^2 =& u + i(v^2)^\frac{1}{2} \\
z^2 =& u + i|v|
\end{eqnarray}
}
$$
Then if $\large{v \ge 0}$ then $\large{|v| = v}$ and hence $\large{z^2 = u +iv = w}$.
If $\large{v \le 0}$ then $\large{|v| = -v}$. Additionally note that $\large{\left(\overline z\right)^2 = \overline {(z^2)}}$ by [[Conjugates and Absolute Values#Theorem 1.31|Theorem 1.31(b)]] so $\large{\overline{z^2} = u - i|v|= u + iv = w}$ completing the proof. 