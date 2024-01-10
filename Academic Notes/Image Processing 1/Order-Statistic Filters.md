---
type: Academic
tags:
alias: Img-Proc-1-OrderStatisticFilters
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
source: [{
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
  }},{} ]
relationship: 
status: {
  state: "Stub",
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
### Description:
**==Order-Statistic Filters==** are a class [[Spatial Filtering#Linear vs Non-Linear Spatial Filtering|Non-Linear Spatial Filters]] which work by first defining a neighbourhood around every pixel, sampling every pixel intensity in the neighbourhood, and then sorting the intensities from lowest to highest. The output of the filter at a given pixel location is dependent on the statistical operation preformed on this ordered-list. 

### Types of Order-Statistic Filters
#### Median Filters:
**==Median Filters==** are a class of [[Order-Statistic Filters#Description|Order Statistic Filter]] which returns the median of the sampled neighbourhood of pixel intensities. Median Filters are well known for their ability to eliminate [[Noise Models#Impulse Noise|Impulse Noise]], outperforming many [[Image Smoothing#Description|Image Smoothing Techniques]].This is to be expected as Impulse Noise manifests itself as a statistical anomaly in the neighbourhood of pixels which surround it and is hence very likely to be filtered out by median computation. 


#### Max and Min Filter: 
The ==**Max and Min Filter**== are a form of [[Order-Statistic Filters#Description|Order Statistic Filter]] which returns the maximum and minimum intensity in the sampled neighbourhood respectively.






