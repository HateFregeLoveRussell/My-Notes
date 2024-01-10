---
type: Academic
tags:
alias: Img-Proc-1-BitSlicing
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
friends: "[[Piecewise Linear Transforms]]"
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
Traditionally an image is analysed through the numerical value of each pixel and its contribution to the intensity values seen in the image. First notice that these numerical values are represented through 8-bit integers. An alternative method of analysis is to measure the contributions to image intensity by each bit of pixel intensity instead of the numerical values they represent. This approach is called **==Bit-Slicing==** and it involves decomposing an image into 8 binary images with each representing a single intensity bit.
![[Mandrill Bit-Sliced Example.png]]
Notice how more significant image characteristics are captured by the bits which are closer to the most significant bit. 
#### Implementation: 
Bit slicing can be implemented as an [[Intensity Transformations#Definition|Intensity Transform]] through the following code: 
```python
def bit_slice(r, b):  
    return ((r >> b) & 1) * 255
```
where the variable $\large{b}$ corresponds to the the bit of interest. The input intensity value $\large{r}$ is right-shifted by the bit number, this results in the bit of interest being placed in the least-significant bit position. A bit-wise and operation with $\large{0000001}$ will result in a binary value of either $\large{00000000}$ or $\large{00000001}$ corresponding to the bit of interest which is then multiplied by $\large{255}$ in order to map $1$ to white and $\large{0}$ to black. 

#### Image Compression Through Bit-Slicing:
As noted earlier more significant image features often correspond to the bits closer to the most-significant-bit position. From this principle we can derive a compression scheme in which we only take bit slices with significant features in them and add them back together multiplying by the correct scaling factor $\large{2^b}$ where $\large{b}$ is the bit position. 

##### Example: 
The mandrill image which was sliced above can be seen below: 
![[Mandrill Test Image.png]]
Looking at the Bit Sliced Image array [[Bit Slicing#Description|above]] we can see that major image components are present in slices $\large{7,6,5,4}$.
![[Bit Sliced Mandrill Reconstruction Example.png]]
As can be observed above including the first 4 bit slices results in an image with a very similar level of quality. This is a compression of $\large{50\% }$.