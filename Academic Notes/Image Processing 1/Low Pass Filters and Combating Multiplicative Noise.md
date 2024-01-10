---
type: Academic
tags:
alias: Img-Proc-1-LPFCombatingMultiplicativeNoise
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
  end-page: 175,
  type: "tbsection",
  section-name: "Smoothing (Lowpass) Spatial Filters",
  book-title: "Digital Image Processing",
  start-page: 164,
  class-alias: "Img-Proc-1",
  source-alias: "Img-Proc-1-3-5",
  ISBN: "978-93-530-6298-9",
  template: {
    version: 1,
    type: "object",
    name: "source-tbsection-obj"
  }
}
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Low Pass Filtering]]"
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
One technique typically used to counter-act multiplicative noise in an image is to take the reciprocal of the noise image and multiply it with the input image. If knowledge of the noise-image was perfect, then the noise would be perfectly cancelled out through this process. Unfortunately, in practice, we often never have perfect knowledge of the noise-image and so we try to obtain some approximation of it. 

An adequate but crude method for obtaining such an approximation if the noise-image is sufficiently smooth is to take a sufficiently large [[Low Pass Filtering|Low Pass Filter]] of the image. 