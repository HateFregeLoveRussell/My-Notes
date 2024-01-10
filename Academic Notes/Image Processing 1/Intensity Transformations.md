---
type: Academic
tags:
alias: Img-Proc-1-IntensityTransformations
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
  section-name: "Background",
  type: "tbsection",
  ISBN: "978-93-530-6298-9",
  source-alias: "Img-Proc-1-3-1",
  book-title: "Digital Image Processing",
  template: {
    type: "object",
    name: "source-tbsection-obj",
    version: 1
  },
  start-page: 120,
  end-page: 122,
  class-alias: "Img-Proc-1"
}
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Spatial Domain Processing Terminology]]" 
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
==**Intensity Transformations**== refer to a special form of [[Spatial Domain Processing Terminology#Neighbourhood Processing vs Point Processing|Neighbourhood Processing]] where the transformation of pixel intensities relies only on the intensity of the given input point, not its position. Some however do treat Intensity Transformations as synonymous with [[Spatial Domain Processing Terminology#Neighbourhood Processing vs Point Processing|Point Processing]]. The general form of an intensity transform takes the shape $\large{s = T[r]}$ where $\large{r}$ is the intensity of the input point $\large{f(x,y)}$ and $\large{s}$ is the intensity of the output point $\large{g(x,y)}$.
 
#### Examples: 

##### Contrast Stretching:
One form of intensity transforms known as **==Contrast Stretching==** can be used to increase the contrast of a given image. The guiding principle behind this transform is that a narrow band of input intensities are mapped to a wide band of output intensities. Technically, any function satisfying this quality qualifies as a Contrast Stretching transform so the graph provided below is not unique. 
![[Contrast Stretching Intensity Transformation General Shape.png]]

##### Thresholding 
An idealized version of a [[Intensity Transformations#Contrast Stretching|Contrast Stretching]] transformation would be a binary **==Thresholding Transformation==** in which all input intensities are mapped to a binary set of output intensities. The graph below depicts the general shape of a Thresholding Transformation. This form of transformation finds use in image segmentation and edge detection.  
![[Thresholding Intensity Transformation General Shape.png]]

#### Implementation: 
Typically Intensity Transformations are implemented through the use of look up tables. This is because there is only a finite number of bits representing an intensity value inside of a computer. So an image representing image intensities through 8-bit integers would require a 256-entry look up table. 