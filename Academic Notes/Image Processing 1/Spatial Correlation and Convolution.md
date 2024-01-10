---
type: Academic
tags:
alias: Img-Proc-1-SpatialCorrelationAndConvolution
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
friends: ["[[Spatial Filter Kernels]]","[[Spatial Filtering]]"]
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
#### Spatial Correlation:
**==Spatial Correlation==**(denoted through the operator $\large{*}$) refers to a method of computing the [[Spatial Filtering#Definition|Filter]] Output image denoted $\large{g(x,y)}$ utilizing the [[Spatial Filter Kernels#Description|Filter Kernel]] one pixel at a time. The underlying formula for correlation for a kernel of size $\large{m}$x$\large{n}$ with $\large{m = 2a+1}$ and $\large{n =2b + 1}$ for $\large{a,b \in \Bbb Z^+}$is expressed as: $$\large{(w*f)(x,y) = g(x,y) =\sum^a_{s = -a}\sum^b_{t=-b}w(s,t)f(x + s,y+t)}$$
Note that this formula in essence dictates that the kernel should be "dragged" over the image with it's centre located at the output pixel location. Once in position the the weights are multiplied by the pixel over which they are placed and summed. Notice that this algorithm necessitates that the image be [[Image Padding#Padding and Convolution|Padded]] before computation begins. 

#### Spatial Convolution: 
**==Spatial Convolution==** (denoted using the operator $\large{\star}$)is a very similar method of computing the [[Spatial Filtering#Definition|Filter]] output when compared to [[Spatial Correlation and Convolution#Spatial Correlation|Spatial Correlation]]. In fact it can be expressed using an identical expression. The difference however is that either the [[Spatial Filter Kernels#Description|Kernel]] or the image itself has been rotated $\large{180\degree}$. Similarly to correlation, spatial convolution requires the image to be [[Image Padding#Padding and Convolution|padded]] prior to the start of computation. 
The Convolution can be computed directly using: 
$$\large{(w \star f)(x,y) = g(x,y) = \sum^a_{s=-a}\sum
^b_{t=-b}w(s,t)f(x-s,y-t)}$$
although most implementations of spatial convolution simply utilize [[Spatial Correlation and Convolution#Spatial Correlation|Spatial Correlation]] but with a rotated kernel. 
#### Standard vs Extended or Full Convolution:
The method of Spatial [[Spatial Correlation and Convolution#Spatial Correlation|Correlation]] and [[Spatial Correlation and Convolution#Spatial Convolution|Convolution]] discussed above is known as **==Standard Spatial Correlation/Convolution==**. In which the centre entry of the [[Spatial Filter Kernels#Indexing and Example|Filter Kernel]] visits every pixel of the input image $\large{f(x,y)}$. **==Full or Extended Spatial Correlation/Convolution==** refers to a version where every entry in the [[Spatial Filter Kernels#Indexing and Example|Filter Kernel]] visits every pixel in the input image.

This is often achieved by positioning the kernel $\large{w}$ such that its bottom right entry is position on top of the top left pixel of $\large{f(x,y)}$ at the start of convolution/correlation. And then extending the convolution such that by the end the top left entry of $\large{w}$ is positioned at the bottom right of $\large{f(x,y)}$.

Note that when preforming full or extended correlation/convolution the [[Image Padding#Padding and Convolution|Padding]] of the image needs to be modified. The number of rows appended to the bottom and top of the image needs to be increased to $\large{m-1}$ and the number of columns appended to the right and left of the image must be increased to $\large{n-1}$.

#### Impulse Response Property: 
An important property of the [[Spatial Correlation and Convolution#Spatial Correlation|Spatial Correlation]] operation is that when the input image is the [[Two-Dimensional Extensions of Familiar Functions#Two Dimensional Impulse Function|Two Dimensional Unit Impulse]] $\large{\delta(x,y)}$ the resultant image $\large{g(x,y)}$ is a copy of the kernel $\large{w}$ rotated $\large{180\degree}$ centered on the location of the impulse. Similarly if the kernel $\large{w}$ contains $\large{\delta(x,y)}$ at its centre, the resultant image is the same as the input image but rotated $\large{180\degree}$ about its centre.
It stands to say that [[Spatial Correlation and Convolution#Spatial Convolution|Convolving]] a unit impulse with the kernel $\large{w}$ is equivalent to copying the kernel over to the location of the impulse. 