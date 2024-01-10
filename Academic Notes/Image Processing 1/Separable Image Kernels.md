---
type: Academic
tags:
alias: Img-Proc-1-SeperableImageKernels
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
  type: "tbsection",
  start-page: 153,
  source-alias: "Img-Proc-1-3-4",
  end-page: 164,
  ISBN: "978-93-530-6298-9",
  section-name: "Fundementals of Spatial Filtering",
  class-alias: "Img-Proc-1",
  template: {
    name: "source-tbsection-obj",
    type: "object",
    version: 1
  }
}
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Spatial Filter Kernels]]"
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
template: {name: class-note-template, version: 1}
---
#### Description: 
A two-dimensional function $\large{G(x,y)}$ is said to be **==separable==** if it can be decomposed into a production of two one-dimensional functions $\large{G(x,y)= G_1(x)G_2(y)}$. Similarly a matrix $\large{w}$ such as an [[Spatial Filter Kernels#Description|Image Kernel]] is said to be **==separable==** if it can be expressed as the product of two vectors $\large{c}$ and $\large{r}$ in the equation $\large{w = cr^\intercal}$.

An interesting mathematical fact about separable matrices is that a separable matrix $\large{w}$ is equal to the [[Spatial Correlation and Convolution#Spatial Convolution|Two-Dimensional Convolution]] of the vectors $\large{c}$ and $\large{r^\intercal}$ (completed without the cropping step).

#### Example: 
The following matrix $\large{w}$ can be decomposed to vectors $\large{c}$ and $\large{r}$.$$\large{w = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 &1\end{bmatrix} = cr^\intercal = \begin{bmatrix}1 \\1\end{bmatrix}\begin{bmatrix}1 & 1 & 1\end{bmatrix}}$$

#### Computational Advantages of Separable Image Kernels:
The computational advantage of using separable image kernels is a consequence of [[Properties of Convolution and Correlation#Associativity|Convolution Associativity]]. As noted in the [[Separable Image Kernels#Description|definition of separability]] the kernel $\large{w}$ is equivalent to the convolution of its two component vectors so $\large{w = w_1 \star w_2}$. Using this equality in the image convolution formula we see that $\large{w \star f = (w_1 \star w_2) \star f = w_1 \star (w_2 \star f) = w_2 \star (w_1\star f)}$. Convolving a $\large{m}$x$\large{n}$ kernel with a $\large{M}$x$\large{N}$ image involves $\large{MNmn}$ additions and $\large{MNmn}$ multiplications when preforming [[Spatial Correlation and Convolution#Standard vs Extended or Full Convolution|Standard]] Convolution. This is because we need to preform $\large{mn}$ additions and multiplications at every image pixel value. When $\large{w = w_1 \star w_2}$ we can split the convolution into first a convolution with a $\large{1}$x$\large{n}$ kernel and then a $\large{1}$x$\large{m}$ kernel so the total number of addition and multiplication operations preformed is $\large{MNm + MNn=MN(m+n)}$.

#### Testing for Separability and Calculation of Component Vectors:
A necessary and sufficient condition for [[Separable Image Kernels#Description|Separability]] of a given matrix is the equality $\large{\operatorname{rank}(w) = 1}$. Once this equality has been met the component vectors $\large{w_1}$ and $\large{w_2}$ can be computed using the following algorithm. 
1. Let $\large{E}$ denote any nonzero element of $\large{w}$ 
2. let $\large{c}$ and $\large{r}$ denote the vectors corresponding to the column and row which contain $\large{E}$ respectively.
3. $\large{w_1 =c}$ and $\large{w_2^\intercal = \frac{r}{E} }$ 






