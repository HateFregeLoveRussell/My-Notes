---
type: Academic
tags:
alias: Img-Proc-1-SpatialFiltering
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
  start-page: 153,
  class-alias: "Img-Proc-1",
  end-page: 164,
  section-name: "Fundementals of Spatial Filtering",
  ISBN: "978-93-530-6298-9",
  template: {
    version: 1,
    type: "object",
    name: "source-tbsection-obj"
  },
  book-title: "Digital Image Processing",
  type: "tbsection",
  source-alias: "Img-Proc-1-3-4"
}
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
#### Definition: 
The term **==Spatial Filtering==** refers to preforming tasks often accomplished through frequency domain filtering by directly processing the image. This often involves the use [[Spatial Filter Kernels|Spatial Filter Kernels]], applied to the image through [[Spatial Correlation and Convolution|Kernel Convolution or Correlation]].

#### Linear vs Non-Linear Spatial Filtering
==**Linear Spatial Filtering**== refers to spatial filtering done through linear operations. This type of filtering will always be done through a sum-of-products operation done through [[Spatial Filter Kernels|Spatial Filter Kernels]] which are [[Spatial Correlation and Convolution|Convolved]] across the image. 
==**Non-Linear Spatial Filtering**== refers to spatial filtering done through the use of non-linear operations. Examples of this type of filtering includes filters such as [[Order-Statistic Filters|Order-Statistic (OS) Filters]].
