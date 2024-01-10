---
type: Academic
tags:
alias: Img-Proc-1-Gamma-Transform
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

#### Introduction: 
The **==Power Law or Gamma Transform==** is a [[Intensity Transformations#Definition|Intensity Transform]] specified by the equation $\large{s = cr^\gamma}$ where $r \in [0, L-1]$, and $\large{\gamma,c > 0}$.

#### Behaviour: 
When $\large{c = \gamma = 1}$ the transform reduces to the [[Image identity and Negative Intensity Transforms#Image Negative Transform|Image Identity Transform]]. 
When $\large{\gamma > 1}$ the transform is the same as the exponential transform. 
When $\large{\gamma < 1}$ the transform gains the same shape as a [[Log Intensity Transform#Description|Log Transform]]. As can be verified through the gif below. 
Similarly to the [[Log Intensity Transform#Description|Log Intensity Transform]] the constant $\large{c}$ can be fixed based on $\large{\gamma}$ so that the range of the transform matches its domain. In this case the $\large{c}$ value necessary for such a property is $\large{c = \frac{L-1}{(L-1)^\gamma}}$.
![[Gamma Transform Graph Animation.gif]]44

#### Practical Uses: 
Many monitors preform this transformation when displaying computer graphics. This is usually facet of the hardware utilized and not the intended way to display images. Because of this we usually use the Gamma Transform with the same gamma value (however inverted) to cancel out the transform done by the monitor. This process is called ==**Gamma Correcting**==, or **==Gamma Encoding==**.