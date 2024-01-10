---
type: Academic
tags:
alias: Img-Proc-1-LocalGlobalHistogramProcessing
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
  ISBN: "978-93-530-6298-9",
  template: {
    version: 1,
    type: "object",
    name: "source-tbsection-obj"
  },
  source-alias: "Img-Proc-1-3-3",
  end-page: 153,
  section-name: "Histogram Processing",
  book-title: "Digital Image Processing",
  type: "tbsection",
  start-page: 133
}
relationship: {name: standard-relationship-obj, version: 1}
friends: ["[[Image Histograms]]", "[[Intensity Transformations]]"]
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
#### Introduction: 
**==Global Histogram Processing==** refers to [[Image Histograms#Description|Histogram Processing]] that applies tot the entirety of the image. Traditional implementations of transformations such as [[Histogram Equalization#Introduction|Histogram Equalization]] or [[Histogram Specification#Introduction|Histogram Specification]] are all instances of Global Histogram Processing. **==Local Histogram Processing==** refers to Histogram Processing in which first a neighbourhood is defined, and for each pixel in the image we calculate the image histogram of the neighbourhood centered around said pixel. Such neighbourhoods are typically squares of odd size. The histogram processing is then preformed, and the corresponding pixel location in the neighbourhood image is returned. Local Histogram Processing algorithms usually make use of local [[Statistical Measures and Their Role in Local Spatial Domain Processing|Statistical Measures]] in comparison to global ones in their calculation. 
 
#### Comparing Local and Global Histogram Processing:
There are tasks that Local Histogram Processing is better suited for compared to Global Histogram Processing. Specifically tasks which involve image enhancement over a small area are well suited for Local Processing. This is because such areas often have small contributions to the global [[Image Histograms#Description|Image Histograms]] and hence are not isolated with global methods.

#### Optimization in Local Histogram Processing: 
An important optimization in local histogram processing is to construct new neighbourhood histograms from old ones. When the neighbourhood is dragged to an adjacent pixel (presuming the neighbourhood is square) about two thirds of the new neighbourhood consists of pixel values that were present in the old neighbourhood. So this optimization can speed up the algorithm considerably. 