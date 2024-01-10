---
type: Academic
tags:
alias: Img-Proc-1-SpatialDomainProcessingTerm
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
  type: "tbsection",
  ISBN: "978-93-530-6298-9",
  book-title: "Digital Image Processing",
  start-page: 120,
  source-alias: "Img-Proc-1-3-1",
  template: {
    type: "object",
    name: "source-tbsection-obj",
    version: 1
  },
  end-page: 122,
  class-alias: "Img-Proc-1",
  section-name: "Background"
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
#### Introduction: 
The general Spatial Domain Processing problem can be distilled to the following equation $\large{g(x,y) = T[f(x,y)]}$ where the intensity of the resultant image $\large g$ evaluated at the spatial co-ordinates $\large{ (x,y)}$ is dependent on the intensity of the same point in the input image $\large{f(x,y)}$. The transformation $\large{T}$ dictates the mapping between input and output point intensities. 
#### Neighbourhood Processing vs Point Processing: 
Some Spatial Domain Processing involves the utilization of a neighbourhood of points around $\large{f(x,y)}$ in order to compute $\large{g(x,y)}$. An example of such a neighbourhood would be a 3x3 square centered around $\large{f(x,y)}$. This form of processing is known as ==**Neighbourhood Processing**==. A special case of Neighbourhood Processing in which the Neighbourhood is restricted to a single point (namely $\large{f(x,y)}$) is known as ==**Point Processing.**==
