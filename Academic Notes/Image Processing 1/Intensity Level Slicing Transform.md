---
type: Academic
tags:
alias: Img-Proc-1-PWLTInstensitySlicingTransform
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
#### Motivation: 
There are times where we want to highlight an intensity band in the input image corresponding to a feature we are interested in. An example of this would be the water in a satellite photo or the veins in an x-ray. 

#### Description: 
In such cases we rely on the [[Piecewise Linear Transforms#Description|Piecewise Linear Transformation]] known as ==**Intensity Slicing**==.In which we take a specified band of intensity values and elevate them in the resultant image to a desired intensity level. Sometimes intensity slicing also refers to thresholding the input image in accordance to said desired band, typically however this thresholding function is combined with the [[Image identity and Negative Intensity Transforms#Image Identity Transformation|Image Identity Transform]] in order to achieve the goal described above. A graph of a typical intensity slicing transform can be seen below: 
![[Intensity Level Slicing Transform Example Graph.png]]
In this case we see that the elevated band is intensity range $\large{r\in [50,100]}$ and the elevated intensity is $\large{200}$.

#### Example: 
Referring to the high contrast flower example. 
![[High Contrast Flower Example.png]]
we can utilize an intensity slicing transform to elevate high intensities and give the image a glossy look. The graph of the transform used and the resultant image are shown below. 
![[Intensity Level Slicing Transform Flower Example Graph.png]]
![[Intensity Slicing Transform Flower Example Transformed Image.png]]