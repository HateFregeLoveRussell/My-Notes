---
type: Academic
tags: [practice]
alias: Math-An-1-Ch1PP-Q2
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
#### Theorem 1.Q2:
There is no rational number whose square is $\large{12}$ 

##### Proof:
let $\large{x^2 = 12}$ and assume that $\large{x = \frac{p}{q}}$ where $\large{p \in \Bbb Z, q\in \Bbb Z, q \ne 0}$ in other words that $\large{x \in \Bbb Q}$. Then $\large{x^2 = \frac{p^2}{q^2} = 12}$, rearranging tells us that $\large{p^2 = 12q^2}$. Note that both $\large{p}$ and $\large{q}$ cannot be even for the reasons discussed in [[Holes in the Rationals#Proof that there exists no rational number $p$ such that $p 2 = 2$|this proof.]] If $\large{p}$ is odd then $\large{p^2}$ is odd, which means that $\large{12q^2}$ is odd. But $\large{12}$ is an even quantity which means that $\large{12q^2}$ must be even. This contradiction leads us to believe that $\large{p}$ is even. If $\large{q}$ is even we would have a contradiction as $\large{p,q}$ would have a common facto so $\large{q}$ is odd. This means that $\large{p =2m, m\in\Bbb Z}$ and $\large{q = 2n+1,n\in\Bbb Z}$ so $\large{4m^2 = 12(2n+1)^2}$ rearranging we get $\large{m^2 = 3(2n + 1)^2}$. If $\large{m}$ is even then $\large{2n+1}$ must be even which contradicts the fact that $\large{q}$ is odd, therefore $\large{m}$ is odd. If $\large{m}$ is odd then $\large{ m = 2l + 1, l \in \Bbb Z}$ so $\large{(2l + 1)^2  =3(2n+1)^2}$. Expanding tells us that $\large{4l^2 + 4l + 1 = 3(4n^2 + 4n + 1)}$ distributing gives us the equation $\large{4l^2 + 4l + 1 = 12n^2 + 12n + 3}$ rearranging we get $\large{4l^2 +4l-12n^2 -12n = 2}$. Finally, factoring and cancelling the shared quantity we can see that $\large{2(l^2 + 4l - 3n^2 - 3n) = 1}$. This leads to contradiction as an even quantity could not possibly equal $\large{1}$. Therefore there exists no rational $\large{x}$ such that $\large{x^2 = 12}$.