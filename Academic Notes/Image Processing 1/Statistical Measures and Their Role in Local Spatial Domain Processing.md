---
type: Academic
tags:
alias: Img-Proc-1-StatisticalMeasuresLocalSpacialDomainProcessing
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
friends: ["[[Local vs Global Histogram Processing]]"]
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
Statistical Measures play an important role in Local Spatial Domain Processing, including [[Image Histograms#Description|Histogram Processing]]. Specifically, transform logic usually depends on the comparison between global statistical measures and local ones. 

#### Mean: 
The **==Global Image Mean==** is defined through the equation: 
$$m = \sum^{L-1}_{i=0}r_ip(r_i)$$
where $\large{r_i}$ represents the intensity level $\large{i}$ and $\large{p(r_i)}$ represents the normalized [[Image Histograms#Description|Image Histogram]] evaluated at $\large{r_i}$. 
The Global Mean represents the average image intensity. 
Similarly the **==Local Mean==** is the image mean restricted to the neighbourhood $\large{S_{xy}}$, defined through the equation: 
$$\large{m_{S_{xy}} = \sum^{L-1}_{i=0}r_ip_{S_{xy}}(r_i)}$$
where $\large{p_{S_{xy}}(r_i)}$ denotes the localized image histogram evaluated at intensity $\large{r_i}$. 

#### Variance:
The **==Global Image Standard Deviation==** is defined through the equation: $$\large{\sigma^2 = \sum^{L-1}_{i=0}(r_i - m)^2p(r_i)}$$
where $\large{p(r_i)}$ denotes the normalized [[Image Histograms#Description|Image Histogram]] evaluated at intensity value $\large{r_i}$, and $\large{m}$ denotes the [[Statistical Measures and Their Role in Local Spatial Domain Processing#Mean|Global Mean]]. The Image Standard Deviation is positively correlated with, and is a measure of overall image contrast. 
Similarly the **==Local Standard Deviation==** is the image standard deviation restricted to the neighbourhood $\large{S_{xy}}$ and hence is a measure of local contrast. It is defined through the equation:
$$\large{\sigma_{S_{xy}}^2 = \sum^{L-1}_{i=0}(r_i - m_{S_{xy}})^2p_{S_{xy}}(r_i)}$$
where $\large{p_{S_{xy}}(r_i)}$ represents the normalized image histogram for neighbourhood $\large{S_{xy}}$ evaluated at intensity level $\large{r_i}$ and $\large{m_{S_{xy}}}$ represents the [[Statistical Measures and Their Role in Local Spatial Domain Processing#Mean|Local Mean]] of neighbourhood $\large{S_{xy}}$.