---
type: Academic
tags:
alias: Img-Proc-1-InterpretationOfImageHistograms
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
  source-alias: "Img-Proc-1-3-3",
  ISBN: "978-93-530-6298-9",
  template: {
    version: 1,
    type: "object",
    name: "source-tbsection-obj"
  },
  start-page: 133,
  book-title: "Digital Image Processing",
  end-page: 153,
  section-name: "Histogram Processing",
  type: "tbsection"
}
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Image Histograms]]"
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
Looking at various image and [[Image Histograms#Description|Image Histogram]] pairs we can see a few patterns between the general shape of a given image histogram, and qualities of the image it represents. 

#### Contrast and Band Size:
Typically, smaller banded (having a small distance between lowest intensity, moderately sized bin and highest intensity moderately sized bin) have less contrast than large banded images. It is important to not that logically the correspondence is only sufficient not necessary. If an image does have high contrast it will naturally have many dark and light pixels meaning that the resultant histogram would have a large bandwidth. However if a image Histogram has a large bandwidth that does not necessarily mean that the light and dark pixels occupy the same general area.

##### Example: 
We will compare the High Contrast Flower test image with its [[Log Intensity Transform#Example|Log Transformed Counterpart]].
**High Contrast Flower:**
![[High Contrast Flower Example.png]]
**High Contrast Flower Image Histogram:**
![[High Contrast Flower Image Histogram.png]]
As we expect the bandwidth of the Image Histogram is very high with the lowest bin located roughly at the intensity value of 10 and the highest near 250.
**Log Transformed High Contrast Flower:**
![[Log Transformed High Contrast Flower Example.png]]
**Log Transformed High Contrast Flower Image Histogram:**
![[Log Transformed High Contrast Flower Image Histogram.png]]
We observe in the Image Histogram of the Log Transformed High Contrast Flower a much smaller bandwidth with the smallest bin located at 105 and largest at 255. Which conforms to our understanding of the role of Image Histogram bandwidth in image contrast. 

#### Image Brightness and Histogram Distribution
When the majority of the area encompassed by the Image Histogram is located in the bright half of the histogram the Image itself is typically bright. Similarly when the majority of the area of the image is encompassed in the dark half of the image histogram, the image itself is typically dark. 

##### Example:
We will analyse two photos who have been [[Power Law (Gamma) Transform#Behaviour|Gamma Transformed]] into a dark and light variants through inverse Gamma values.

**Dark Image:**
![[Dark Camera Test Image.png]]
**Dark Image Histogram:**
![[Dark Camera Test Image Histogram.png]]
Looking at the histogram we can see that as expected, the majority of the pixels are located in the 0 to 100 intensity range.

**Bright Image:**
![[Bright Camera Test Image.png]]
**Bright Image Histogram:**
![[Bright Camera Test Image Histogram.png]]
Similarly, we note that most of the intensity levels in the bright image histogram are located in the intensity band between 180 to 235. Corresponding to our expectations.

