---
type: Academic
tags:
alias: Img-Proc-1-2DFamiliarFunctions
class: {
  class-name: "Image Processing 1",
  author: "Rafael C. Gonzalez, Richard E. Woods",
  medium: "Textbook",
  class-alias: "Img-Proc-1",
  title: "Digital Image Processing",
  edition: "fourth",
  publisher: "Pearson India Education Services",
  ISBN: "978-93-530-6298-9",
  length: 1019,
  template: {
    name: "class-textbook-obj",
    version: 1,
    type: "object"
  }
}
source: {
  book-title: "Digital Image Processing",
  section-name: "Extensions to Functions of Two Variables",
  class-alias: "Img-Proc-1",
  source-alias: "Img-Proc-1-4-5",
  ISBN: "978-93-530-6298-9",
  template: {
    name: "source-tbsection-obj",
    type: "object",
    version: 1
  },
  type: "tbsection",
  start-page: 207,
  end-page: 215
}
status: {
  state: "In Progress",
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
template: {name: class-note-template, version: 1}
---
#### Two Dimensional Impulse Function
The Two Dimensional Impulse is defined as $$\large{\delta[x,y] = \left\{
	\begin{array}{lr}
	1, & \text{if }x =y = 0\\
	0, & \text{otherwise}
	\end{array}
\right\}}$$
The function has the familiar sifting property as shown below: 
$$\large{
\sum_{x = -\infty}^{\infty} \sum^{\infty}_{y = -\infty} f(x,y)\delta(x,y) = f(0,0) 
}$$
$$
\large{
\sum^\infty_{x=-\infty}\sum^\infty_{y = -\infty}f(x,y)\delta(x - x_0, y-y_0) = f(x_0,y_0)
}
$$
#### Two Dimensional Continuous Fourier Transform:
The two dimensional Continuous Fourier Transform is defined below: 
$$\large{ F(u,v) = \iint_{\Bbb R^2} f(t,z)e^{-j2\pi (ut+vz)}dtdz}$$
$$\large{
f(t,z) = \iint_{\Bbb R^2}
 F(u,v)e^{j2\pi(ut + vz)}dudz}$$
 In this formulation the variables $\large{t,z}$ are known as the **==spatial variables==** while $\large{u,v}$ are known as **==frequency variables==**
 We will make little use of this transform outside of sampling but it builds strong intuition for the discrete versions used later. Specifically it is important to notice that $\large{e^{j2\pi(ut + vz)} = e^{j2\pi ut}e^{j2\pi vz}}$. 
#### Two Dimensional Box Function Example 
The following series of calculations will display the computational character of the two-dimensional continuous Fourier transform in addition to familiarizing us with the two-dimensional Sinc function.
$$\large{
\begin{array}
 FF(u,v)  =  \iint_{\Bbb R^2}f(t,z)e^{-j2\pi(ut + zv)} dtdz \\
  = \int_{T/2}^{T/2}\int_{Z/2}^{Z/2}A e^{-j2\pi(ut + zv)} dtdz \\
  =ATZ\operatorname{Sinc}(\pi \mu T)\operatorname{Sinc}(\pi vZ) 
\end{array}
}$$
#### Two Dimensional Sinusoid
The Cis function when extended to two dimensions is of the form $\large{e^{j2\pi(ut +vz)}}$
where $\large{u,v}$ are the frequencies of the function in the $\large{t,z}$ direction respectively.
Similarly to the single variable case when two cis functions are combined they can make a purely real two-dimensional sinusoid of the form $\large{A\sin(ut + vz +\phi)}$ where $\large{A,\phi}$ represent the sinusoid amplitude and phase respectively.
This resulting sinusoid is plotted below: 
![[2DSinusoidGraph.png]]
where the resulting slope of the sinusoid's bands are $\large{\operatorname{slope} = \frac{-u}{v}}$.
Some important observations:
- Number of bands increase as frequency increases
- Orientation about the origin of these bands are dependent on the ratio of the frequencies.
- Added Phase moves the sinusoid's origin to a different point in the plane.