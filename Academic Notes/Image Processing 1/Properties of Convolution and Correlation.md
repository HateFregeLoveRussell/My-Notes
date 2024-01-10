---
type: Academic
tags:
alias: Img-Proc-1-PropOfConvolutionAndCorrelation
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
#### Introduction: 
The following are some useful arithmetic properties of [[Spatial Correlation and Convolution#Spatial Correlation|Spatial Correlation]] and [[Spatial Correlation and Convolution#Spatial Convolution|Spatial Convolution]]. 

#### Commutativity:
Generally speaking [[Spatial Correlation and Convolution#Spatial Convolution|Convolution]] is a commutative operation meaning that $$\large{f\star g = g \star f}$$
This is however not generally true for [[Spatial Correlation and Convolution#Spatial Correlation|Correlation]]. This is important to keep in mind when you are implementing Convolution through Correlation as described [[Spatial Correlation and Convolution#Spatial Convolution|here]], as the order of operations do matter in Correlation but do not in Convolution.

#### Associativity: 
[[Spatial Correlation and Convolution#Spatial Convolution|Convolution]] is an associative operation, this means that:
$$\large{f \star(g \star h) = (f \star g) \star h = f\star g\star h}$$
Similarly to [[Properties of Convolution and Correlation#Commutativity|Commutativity]] however, [[Spatial Correlation and Convolution#Spatial Correlation|Correlation]] is not an associative operation. This is also important when implementing Convolution through Correlation as explained [[Spatial Correlation and Convolution#Spatial Convolution|here]].

#### Distributivity: 
[[Spatial Correlation and Convolution#Spatial Convolution|Convolution]] is a distributive operation, this means that: 
$$\large{f\star(g + h) = f \star g + f \star h}$$
Unlike both [[Properties of Convolution and Correlation#Commutativity|Commutativity]] and [[Properties of Convolution and Correlation#Associativity|Associativity]] however [[Spatial Correlation and Convolution#Spatial Correlation|Correlation]] is also a distributive operation meaning that: 
$$\large{f*(g+ h) = f*g + f*h}$$
