---
type: Academic
tags: [Entrynote]
alias: Img-Proc-1-Protal
class: {
  class-name: "Image Processing 1",
  author: "Rafael C. Gonzalez, Richard E. Woods",
  medium: "Textbook",
  class-alias: "Img-Proc-1",
  title: "Digital Image Processing",
  edition: fourth,
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
parent: ["[[Class-Sched]]","[[Class-Display-Portal]]","[[Class-Bibliography]]"]
class-status: {
  state: "In Progress",
  template: {
    name: "status-obj",
    version: 1,
    type: "object"
  }
}
status: {
  state: "Completed",
  template: {
    name: "status-obj",
    version: 1,
    type: "object"
  }
}
validity: {
  state: true,
  template: {
    name: "validity-obj",
    version: 1,
    type: "object"
  }
}
template: {name: class-portal-template, version: 2} 
---
### Class Description:
```dataview
TABLE class.class-name AS "Class Name", class.author AS "Class Author", class.medium AS "Class Medium", class.length AS "Class Length"
WHERE file = this.file
```
Textbook read in preparation for upcoming image processing class. Content from class notes obtained in advance will be mixed with content learned from the textbook. Not all chapters will be covered instead the class notes will be read and the corresponding textbook chapters covered. 

### Class Content:
- Chapter 1: Introduction 
- Chapter 2: Digital Image Fundamentals 
- Chapter 3: Intensity Transformations and Spatial Filtering
- Chapter 4: Filtering in the Frequency Domain
- Chapter 5: Image Restoration and Reconstruction 
- Chapter 6: Colour Image Processing
- Chapter 7: Wavelet and Other Image Transforms 
- Chapter 8: Image Compression and Watermarking
- Chapter 9: Morphological Image Processing
- Chapter 10: Image Segmentation 
- Chapter 11: Feature Extraction 
- Chapter 12: Image Pattern Classification

### Class Progress: 
**In Progress Notes:**
```dataview
LIST
FROM "Academic Notes/Image Processing 1"
WHERE status.state = "In Progress" OR status.state = "Stub"
```

