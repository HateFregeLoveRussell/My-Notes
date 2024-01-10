---
type: Academic
tags:
alias: Img-Proc-1-SpatialFilterKernels
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
friends: "[[Spatial Filtering]]"
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
The **==Spatial Filter Kernel==** defines the neighbourhood of [[Spatial Filtering#Linear vs Non-Linear Spatial Filtering|filter operations]]. It is an (typically) odd-dimensioned matrix, each entry of which determines the weight applied to the corresponding pixel in the product-of-sums operation that is preformed at each stage of [[Spatial Correlation and Convolution|Kernel Convolution]].

#### Indexing and Example:
Contrary to traditional matrices filter kernels are not indexed from the top-left. Instead the nought index is given to the centre entry of the matrix, and the remaining entries are indexed according to the scheme presented below for the 3x3 case: 
$$\large{\begin{bmatrix}w(-1,-1) & w(-1,0) & w(-1,1) \\ w(0,-1) & w(0,0) & w(0,1) \\ w(1,-1) & w(1,0) & w(1,1) \end{bmatrix}}$$
where $\large{w(x,y)}$ determines the weight of the kernel at index $\large{(x,y)}$.
Note that the centre entry will always exist as we have assumed that such kernels are always of odd dimensions. In such a case the sum-of-products calculation would be of form: $$\large{\begin{aligned}g(x,y) = w(-1,-1)f(x-1,y-1) + w(-1,0)f(x-1,y)+ \\ w(0,0)f(x,y)+ \ldots +w(1,1)f(x+1,y+1)\end{aligned}}$$

#### Symmetry and Convolution:
Since [[Spatial Correlation and Convolution#Spatial Convolution|Spatial Convolution]] is identical in form to [[Spatial Correlation and Convolution#Spatial Correlation|Spatial Correlation]] with the only difference being that either the [[Spatial Filter Kernels#Description|Kernel]] or the Image has been rotated by $\large{180\degree}$, it stands that for filter kernels which are symmetric about their centre (called **==Isotropic==**) Convolution and Correlation produce Identical results.

#### Design Methodology:
Typically, [[Spatial Filter Kernels#Description|Filter Kernels]] are designed using one of the 3 methods below: 
1. Design the kernel directly through the mathematical properties of the kernel (Averaging pixel values blurs the image, etc)
2. Take a two-dimensional(typically continuous) spatial function and sample it 
3. Specify desired frequency response of the filter, construct the corresponding kernel (this is typically done through filter design software)