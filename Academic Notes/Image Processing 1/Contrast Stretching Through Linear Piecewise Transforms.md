---
type: Academic
tags:
alias: Img-Proc-1-ContrastStretchingPWLT
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
  class-alias: "Img-Proc-1",
  source-alias: "Img-Proc-1-3-2",
  ISBN: "978-93-530-6298-9",
  template: {
    version: 1,
    type: "object",
    name: "source-tbsection-obj"
  },
  start-page: 122,
  book-title: "Digital Image Processing",
  end-page: 133,
  section-name: "Some Basic Intensity Transformation Functions",
  type: "tbsection"
}

relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Piecewise Linear Transforms]]"
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
Contrast Stretching was defined first [[Intensity Transformations#Contrast Stretching|here]]. A common implementation of this [[Intensity Transformations#Definition|Transformation]] is through the use of a [[Piecewise Linear Transforms#Description|Piecewise Linear Function]] as detailed below. The user must specify four variables $\large{r_1,s_1,r_2,s_2}$. We additionally assume that $\large{r_2 \ge r_1}$ and that $\large{s_2 \ge s_1}$. These assumptions are necessary for the function to be both monotonically increasing and single valued.
![[Piecewise Linear Contrast Stretching Graph Example.png]]
As can be seen from the graph above the function is composed of 3 linear components from $\large{(0,0)}$ to $\large{(r_1,s_1)}$, from $\large{(r_1,s_1)}$ to $\large{(r_2,s_2)}$ and from $\large{(r_2,s_2)}$ to $\large{(L-1,L-1)}$. 
#### Behaviour: 
When $\large{r_1 = s_1}$ and $\large{r_2 = s_2}$ the transform becomes equivalent to the the [[Image identity and Negative Intensity Transforms#Image Identity Transformation|Image identity Transform]].
Additionally when $\large{r1=r2}$ and $\large{s_1= 0}$, $\large{s_2 = L-1}$ then the function is equivalent to [[Intensity Transformations#Thresholding|Thresholding Transformation]].
Any other values for these parameters simply interpolates between these two extremes. Allowing us to preform a wide range of contrast manipulating transformations using a single function. 

#### Example: 
We can try to utilize this form of contrast stretching in order to undo the [[Log Intensity Transform#Description|Log Transform]] utilized to create the following image: 
![[Log Transformed High Contrast Flower Example.png]]
Through manual tuning we choose the following iteration of the Piecewise Linear Contrast Stretching Transform: 
![[Inverse Log Transform Through PWL Contrast Stretching Graph.png]]
Note that this function resembles heavily the exponential transform. This is to be expected as the exponential transform is the inverse of the log transform. The resulting image from this inverse transformation is shown below: 
![[PWL Contrast Stretch Restored Contrast Flower.png]]
Comparing to the [[Log Intensity Transform#Example|original]] we can see that the restoration is not perfect. It is specifically missing some highlighting in the background. This is to be expected as the transform used is a 3-point linear approximation of the exponential transform. 

Setting $\large{(r_1,s_1,r_2,s_2) = (240,0,240,255)}$ we can threshold the image to gain the following binary image. 
![[PWLT Thresholding Flower Example.png]]
The following is the underlying transform graph: 
![[PWLT Flower Threshold Example Graph.png]]

#### Implementation:
A common implementation of this transform is through the piecewise expression: 
$$\large{
\begin{equation}
S = 
\begin{cases}
\frac{s_1}{r_1}r & & 0 \le r \le r_1 \\
\frac{s_2 - s_1}{r_2 - r_1}r + \frac{s_1r_2 - s_2r_1}{r_2 - r_1} & & r_1 \lt r \lt r_2 \\
\frac{L-1 -s_2}{L-1-r_2}r + (L-1)\frac{s_2 - r_2}{L-1-r_2} & & r_2 \le r \le L-1
\end{cases}
\end{equation}
}
$$
When we set $\large{r_1 = r_{min},  s_1 = 0, r_2 = r_{max}, s_2 = L-1}$ we can simplify to the expression:
$$\large{s= \operatorname{round}\left ( (L-1)\frac{r-r_{min}}{r_{max} - r_{min}}\right)}$$
