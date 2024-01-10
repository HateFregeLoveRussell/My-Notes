---
type: Academic
tags:
alias: Img-Proc-1-IterativeSpatialFiltringCombinedKernel
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
friends: ["[[Spatial Filter Kernels]]", "[[Spatial Correlation and Convolution]]"]
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
There are times where it is desirable to filter an image iteratively. Where [[Spatial Filter Kernels#Description|Filter Kernels]] are [[Spatial Correlation and Convolution#Spatial Convolution|Convolved]] with an image sequentially. For $\large{Q}$ spatial filters we denote $\large{w_1,w_2,\ldots,w_Q}$ as the sequence of kernels convolved with the image in sequence. 

In such cases we can take advantage of the [[Properties of Convolution and Correlation#Associativity|Associativity Property of Spatial Convolution]] to lower overall computation by convolving $\large{w_1,w_2, \ldots, w_Q}$ into a single kernel $\large{w}$ using $$\large{w= w_1 \star w_2\star\ldots\star w_Q}$$
If the kernels $\large{w_1,w_2,\ldots,w_Q}$ are all of size $\large{m}$x$\large{n}$ the kernel $\large{w}$ is of dimensions $\large{W_v}$x$\large{W_h}$ where $\large{W_v = Q(m-1)+m}$ and $\large{W_h = Q(n-1) + n}$.


