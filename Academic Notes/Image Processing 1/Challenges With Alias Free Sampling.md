---
type: Academic
tags:
alias: Img-Proc-1-AliasFreeSamplingChallenges
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
  source-alias: "Img-Proc-1-4-3",
  class-alias: "Img-Proc-1",
  ISBN: "978-93-530-6298-9",
  template: {
    name: "source-tbsection-obj",
    type: "object",
    version: 1
  },
  section-name: "Sampling and the Fourier Transform of Sampled Functions",
  type: "tbsection",
  start-page: 207,
  end-page: 215
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

The note of importance here is that the sampling theorem guarantees that aliasing does not occur in the sampling of band attenuated functions provided the sampling frequency is twice that of the bandwidth of the function. The issue is that for a function to be band attenuated it would need to have a maximum and minimum frequency which is finite, which necessarily implies that there is no finite time interval in which the last or the first sample is made. This is clearly impossible in practice so aliasing is an inevitability in the real world.
