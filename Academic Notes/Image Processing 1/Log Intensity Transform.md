---
type: Academic
tags:
alias: Img-Proc-1-LogIntesnityTransform
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
#### Description:
The **==Log Intensity Transformation==** is an [[Intensity Transformations|Intensity Transformation]] of the general form: $\large{s = c\operatorname{log}(1 + r)}$  where $\large{r \in [0,L-1]}$ and $\large{c > 0}$. Looking at the graph of this function we can see the general purpose of such a transformation, a narrow dark band of intensities of the input is mapped to a wider dark bank in the output. Conversely, the wider light bank of the input is mapper to a narrower light band in the output. technically speaking, any function with this general graphical shape will have this effect.![[Log Intensity Transformation Example Graph.png|600]]

#### Picking an Appropriate C Value:
When $\large{c = 1}$ the curve will grow very slowly so for certain $\large{L}$ values the function range does not cover $\large{[0, L-1]}$. If we want to fix the range so that the transform range is equal to transform domain we have to set $\large{c = \frac{L-1}{log(L)}}$ in the case of base 2 logarithm and $\large{L =2 56}$ we have $\large{c = 255/8}$. 

#### Example:
The effect described [[Log Intensity Transform#Description|above]] can be exemplified with the following image. The image was transformed using $\large{c = 255/8}$, notice how the bright pixel values are largely unchanged while the dark ones are made brighter.
**Before Transformation:** 
![[High Contrast Flower Example.png]]**After Transformation:**
![[Log Transformed High Contrast Flower Example.png]]

#### Use in Enhancement of Fourier Transforms: 
The classical use of the [[Log Intensity Transform#Description|Log Intensity Transform]] is in the enhancement of image Fourier Transforms. The output range of a Fourier transform is very high, and low frequency components typically have much higher magnitudes that the higher frequency components (several orders of magnitude). The transform is used to enhance higher frequency components so they can be viewed with ease once the transform is normalized to integer range $\large{r \in [0, 255]}$.![[Log Transform in Fourier Spectrum of Images Example.png|700]]

 