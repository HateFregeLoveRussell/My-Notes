---
type: Academic
tags:
alias: Img-Proc-1-HistogramSpecification
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
friends: "[[Histogram Equalization]]"
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
template: {name: class-note-template, version: 1}
---
#### Introduction: 
[[Histogram Equalization#Introduction|Histogram Equalization]] is a method of flattening a given image histogram into a uniform one. From this technique we can create a method of transforming any image histogram into an arbitrary shape. This technique is known as **==Histogram Specification==**.

#### Derivation: 
Similarly to the [[Histogram Equalization#Derivation|Derivation of Histogram Equalization]] we will assume the three variables $\large{s,r,z}$ are continuous and in the range $\large{[0, L-1]}$. Variable $\large{s}$ will act as an intermediately variable, while $\large{r}$ will act as the input intensity and $\large{z}$ will act as the output intensity. 

Let the variables $\large{s,r}$ be related through: 
$$\large{
s = T(r) = (L-1)\int_0^rp_r(w)dw
}$$
So $\large{s}$ has a uniform histogram. Now we will define a mapping from $\large{z}$ to $\large{s}$:
$$\large{s = G(z) = (L-1)\int_0^zp_z(w)dw}$$
This naturally means $\large{z = G^{-1}(s) = G^{-1}(T[r])}$. So we have a mapping from $\large{r}$ to $\large{z}$, this requires that $\large{G(z)}$ is invertible.  

Discretizing we get the following expressions:
$$ \large \begin{aligned}
T(r_k) &= (L-1)\sum_{j=0}^k p_r(r_j) \\
G(z_q) &= (L-1)\sum_{i=0}^q p_z(z_i)
\end{aligned}$$

#### Practicalities:
The Inverse of $\large{G(z)}$ is often not analytically expressible, in practice it is often implemented through searching the $\large{G(z)}$ look up table and finding the closest entry for $\large{T[r]}$.
Additionally $\large{G(z)}$ is often non-invertible as it is rarely [[Criteria For Intensity Transformations#Monotonically Increasing|Strictly Monotonically Increasing]], by convention if we have multiple matches in the look up table, we will pick the smallest one to resolve this issue. 

#### Algorithm Summary:
1. Equalize the Image Histogram $\large{p_r(r)}$ and compute every $\large{s_k}$ rounded to nearest integer in $\large{[0, L-1]}$.
2. Compute $\large{G(z_q)}$ (also histogram equalization) where $\large{p_z(z_q)}$ is the desired histogram values. Similarly, round $\large{G(z_q)}$ to the nearest integer in range $\large{[0, L-1]}$.
3. For every value of $\large{s_k}$ find the closest value of $\large{G(z_q)}$ and map $\large{s_k}$ to $\large{z_q}$. If more than one such $\large{z_q}$ exists pick the smallest in the list by convention. 
4. Use the mapping from $\large{r_k}$ to $\large{s_k}$ and from $\large{s_k}$ to $\large{z_q}$ to make a mapping from $\large{r_k}$ to $\large{z_q}$ 
5. Use this mapping to compute the specified Image.

#### Example:
Consider the following Image: 
![[Log Transformed High Contrast Flower Example.png]]
It looks rather washed out and low contrast. Our first instinct would be to utilize [[Histogram Equalization#Introduction|Histogram Equalization]] in order to boost contrast in the image. However as we can this produces a poor result:
![[Bright Contrast Flower Histogram Equalized Example.png]]
This is because the image itself is rather dark, prior to it being brightened. And a large percentage of it's pixel intensities lie on the right hand side of it's histogram bandwidth:
![[Log Transformed High Contrast Flower Image Histogram.png]]
And so Histogram Equalization results in spreading these large bins over relatively large intensity range causing a discontinuous jumps in intensity in the resulting image.
Instead what we can do is use Histogram Specification, Specifying a histogram that conforms to this general shape. In our example we sampled the original image's histogram but in practice this histogram would need to be specified in some other way.
![[Contrast Flower Histogram Specification Example.png]]

#### Implementation: 
Histogram Specification can be implemented in OpenCV as an intensity transform through the following code: 
```python
def histogram_specification(img, specified_histogram, L = 256):  
    # Assuming Specified Histogram is normalized  
    # Equalize the Image    equalized_img = cv2.equalizeHist(img)  
    # Obtain Histogram Equalization of specified histogram  
    specified_cdf = (L - 1)*specified_histogram.cumsum()  
    # Invert Equalization Transform and apply to equalized_image pixles  
    specified_img = np.interp(equalized_img.flatten(),specified_cdf ,np.arange(0, 256)).reshape(img.shape)  
    # Mathc pixel values to uint8  
    specified_img = np.uint8(specified_img)  
    return specified_img
```
Here there is no need to search a Look Up Table and pick the smallest match in the case of a conflict. A linear interpolation of the inverse CDF will provide this functionality automatically. 
