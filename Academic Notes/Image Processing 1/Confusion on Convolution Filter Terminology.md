---
type: Academic
tags:
alias: Img-Proc-1-ConfusionCorrelationConvolutionTerminology
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
#### Description: 
There tends to be some confusion on the terminology utilized in the academic literature with reference to [[Spatial Correlation and Convolution|Spatial Correlation or Convolutions]]. Typically, the terms "Convolution Filter", "Convolution Mask", or "Convolution Kernel" do not necessarily refer to the use of [[Spatial Correlation and Convolution#Spatial Convolution|Spatial Convolution]] or [[Spatial Correlation and Convolution#Spatial Correlation|Spatial Correlation]]. Similarly the term "Convolving the kernel with an image" does not necessarily imply the usage of spatial convolution and in reality could mean the use of correlation. 

In the book used the term "Linear Spatial Filtering" always refers to Spatial Convolution of an image with a kernel.

