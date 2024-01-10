---
type: Academic
tags:
alias: Img-Proc-1-ImagePadding
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
friends: "[[Spatial Correlation and Convolution]]"
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
#### Padding and Convolution:
Both [[Spatial Correlation and Convolution#Spatial Correlation|Spatial Correlation]] and [[Spatial Correlation and Convolution#Spatial Convolution|Spatial Convolution]] require padding in order to be applied to an image if the underlying [[Spatial Filter Kernels#Description|Kernel]] has larger dimensions than $\large 1$x$\large{1}$. This makes sense, as to compute the border pixels of the filtered image $\large{g(x,y)}$ we need to sample the input image $\large{f(x,y)}$ at pixel values that lie outside its dimensions. For example, a $\large{3}$x$\large{3}$ kernel centered at the top left corner of the image $\large{f(x,y)}$ would require $\large{5}$ of its weights to be multiplied by pixel values that lie outside of the image dimensions. Typically [[Image Padding#Zero-Padding|Zero-Padding]] used in padding the image prior to output computation.

In general when preforming Image Correlation or Convolution on an image of dimensions $\large{M}$x$\large{N}$ and kernel dimensions of $\large{m}$x$\large{n}$ an extra $\large{\frac{m-1}{2}}$ rows and $\large{\frac{n-1}{2}}$ columns needs to be appended to each side of the image. After convolution these extra rows and columns can be cropped. 
  
#### Zero-Padding:
**==Zero-Padding==** is a method of image-padding in which the pixels not already part of the input image are set to the value $\large{0}$. Visually this manifests as a black border around the image extending it to the new image dimensions. 

##### Adverse Effects from Zero-Padding:
Zero-Padding for many applications can prove inadequate. As an example, when preforming [[Low Pass Filtering|Low-Pass Filtering]] a dark border can be seen creeping into the image. This is a consequence of averaging border pixels with the value $\large{0}$. This phenomenon can be observed when looking at the examples for [[Box Filter Kernels#Example|Box Filtering]] and [[Low Pass Gaussian Filter Kernels#Examples|Low-Pass Gaussian Blurs]].

#### Symmetric-Padding: 
**==Symmetric==** or **==Mirror-Padding==** is a method of image-padding in which the pixels which are not already part of the input image are set based on mirror reflecting the image. This form of padding is useful when dealing with images where details of interest are placed near the border of the image. 

##### Replicate-Padding:
**==Border-Replicate-Padding==** or simply **==Replicate-Padding==** fills pixel values not part of the input image with the nearest border value. This form of padding is ideal for images where the border of the image are near constant. 