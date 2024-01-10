---
type: Academic
tags:
alias: Img-Proc-1-IdentityAndNegativeIntensityTransforms
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
  start-page: 122,
  ISBN: "978-93-530-6298-9",
  template: {
    version: 1,
    type: "object",
    name: "source-tbsection-obj"
  },
  book-title: "Digital Image Processing",
  section-name: "Some Basic Intensity Transformation Functions",
  type: "tbsection",
  source-alias: "Img-Proc-1-3-2",
  end-page: 133
}
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Intensity Transformations]]"
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

#### Image Negative Transform: 
This [[Intensity Transformations|transform]] is used to reverse the intensity range present in an image. So if the intensity of a pixel is 0 it becomes the maximum allowable intensity and vice versa. For an image that has $\large{L}$ intensity levels (256 in the case of an 8-bit image) the **==Image Negative Intensity Transform==** is described through the equation: 
$$\large{s = L -1 -r}$$
It is graphically illustrated below: 
![[Image Negative Intensity Transform Example.png]]

##### Example:
**Pre-Transformation Image:**
![[Camera Test Image.png]]
**Post-Transformation Image:**
![[Image Negative Transformation Camera Example.png]]

#### Image Identity Transformation
The **==Image Identity Transformation==** is simply returns the input intensity transformation. It serves a conceptual purpose rather than a practical one. 
$$s = r$$
![[Image Identity Intensity Transformation Example.png]]