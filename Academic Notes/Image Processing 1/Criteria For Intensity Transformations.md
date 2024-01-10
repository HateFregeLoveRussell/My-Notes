---
type: Academic
tags:
alias: Img-Proc-1-CriteriaForIntensityTransformations
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
There are several mathematical properties that are desirable for [[Intensity Transformations#Definition|Intensity Transformations]] designing transformations with them in mind will lead to much greater ease of use and flexibility. 
#### Monotonically Increasing: 
An Intensity Transformation should be **==Monotonically Increasing**== in the interval $\large{r \in [0, L-1]}$ with $\large{L}$ being the number of intensity values (typically 256 for 8-bit images).Mathematically this property can be expressed as: 
$\large{\forall r_1,r_2 \in [0, L-1] (r_1 \lt r_2 \implies T(r_1) \le T(r_2))}$
This property insures that the order between pixel intensities are preserved through the transformation, meaning that **==Intensity Artefacts==** are not introduced.

An Intensity Transformation is said to **==Strictly Monotonically Increasing==** if:
$\large{\forall r_1,r_2 \in [0, L-1] (r_1 \lt r_2 \implies T(r_1) \lt T(r_2))}$

#### Constrained Range: 
An Intensity Transformation fulfils this property if the following statement is true: $$\large{r\in[0, L -1 ] \implies T(r)\in[0, L-1]}$$
In other words it is not possible for the transformation to expand the intensity range of its input beyond the image intensity range.
Note that a necessary condition for this quality to exist is that the Intensity Transformation is defined across $\large{r \in [0, L-1]}$.

#### Invertibility: 
An Intensity Transformation is said to be **==Invertible==** if there exists an Intensity Transform which will return the original image once fed the Transform output. Invertibility is necessarily fulfilled if the Transform is [[Criteria For Intensity Transformations#Monotonically Increasing|Strict Monotonically Increasing]] and has a [[Criteria For Intensity Transformations#Constrained Range|Constrained Range]]. 
The former condition is rather difficult to meet when the underlying Intensity Transform is a Discrete function. 