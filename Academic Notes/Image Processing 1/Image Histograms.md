---
type: Academic
tags:
alias: Img-Proc-1-ImgHistograms
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
Let $\large{h(r_k) = n_k}$ be a function where $\large{r_k}$ corresponds to an image intensity level and $\large{n_k}$ corresponds to how many pixels have the input intensity at a given image. This function is known as the **==Unnormalized Image Histogram==**. The function $\large{p(r_k) = \frac{h(r_k)}{MN} = \frac{n_k}{MN}}$ is then the **==Normalized Image Histogram==** or simply the **==Image Histogram==**, where $\large{M,N}$ refer to the dimensions of the input image. The entries of a Image Histogram are known as **==bins==**.

It should be clear that $\large{\sum^{L-1}_{k=0} p(r_k) = 1}$ as $\large{\sum^{L-1}_{k=0}h(r_k) = MN}$. Additionally we should note that $\large{p(r_k)}$ can be interpreted as the probability of encountering a certain intensity level if sampling the image at random.

Naturally an [[Intensity Transformations#Definition|Intensity Transformation]] imparts an effect onto the Image Histogram. Designing Intensity Transforms through the analysis of Image Histograms is called **==Histogram Processing==**.

#### Example: 
The Following are the Camera Test Image, It's Unnormalized Image Histogram, and it's Normalized Image Histogram
**Test Image:**
![[Camera Test Image.png]]
**Unnormalized Image Histogram:**
![[Camera Test image Unnormalized Histogram.png]]
**Normalized Image Histogram:**
![[Camera Test Image Normalized Histogram.png]]
As expected, the underlying shape of the histogram is preserved but it's scale has changed. 