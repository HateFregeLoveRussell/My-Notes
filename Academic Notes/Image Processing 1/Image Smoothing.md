---
type: Academic
tags: [RepoNote]
alias: Img-Proc-1-ImgSmoothing
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
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Low Pass Filtering]]"
source: {
  type: "tbsection",
  source-alias: "Img-Proc-1-3-5",
  book-title: "Digital Image Processing",
  end-page: 175,
  class-alias: "Img-Proc-1",
  ISBN: "978-93-530-6298-9",
  section-name: "Smoothing (Lowpass) Spatial Filters",
  template: {
    version: 1,
    type: "object",
    name: "source-tbsection-obj"
  },
  start-page: 164
}
status: {
  state: "In Progress",
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
**==Image Smoothing==** is an enhancement objective where we try to flatten sharp transitions in image intensity giving the image an overall blurred look. This enhancement objective coincides with [[Low Pass Filtering|Low Pass Filtering]]. It is used to counter-act image aliasing during image capture, and has uses in [[Image Histograms#Description|Histogram Processing]].

#### Image Smoothing Filters: 
