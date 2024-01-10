---
type: Academic
tags:
alias: Img-Proc-1-HistogramEqualization
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
  }, 
  ]
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
Histogram Equalization is an [[Intensity Transformations#Definition|Intensity Transform]] that aims to increase contrast in a given image through the manipulation of its [[Image Histograms#Description|Image Histogram]].

#### Derivation: 
First assume that the variables $\large{r,s}$ which represent the input intensity and the output sensitivity respectively. As mentioned [[Image Histograms#Description|here]] the Image Histograms $\large{p_r(r)}$ and $\large{p_s(s)}$ can be thought of as Probability Density Functions representing the intensity of a pixel sampled at random. 
A fundamental result in Probability Theory is the following Equality: 
$$\large{
p_s(s) = p_r(r)\left |\frac{dr}{ds} \right |
}
$$
This equality will hold if the mapping $\large{s = T(r)}$ is both continuous and differentiable on the interval $\large{r \in [0, L-1]}$

Now consider the transformation:
$$\large{s = T(r) = (L-1)\int^{r}_{0}p_r(w)dw}$$
Since $\large{p_r(w) \in [0, L-1]}$ it stands to say that $\large{\int_0^r p_r(w)dw}$ is a [[Criteria For Intensity Transformations#Monotonically Increasing|Monotonically Increasing]] function, so it's product with the constant $\large{L -1 }$ is also Monotonically Increasing. So it stands that this transforms satisfies that property. 
Additionally observe that $\large{\int^{L-1}_0p_r(w)dw = 1}$  so the maximum value for $\large{T(r)}$ is $\large{L-1}$. Similarly $\large{\int^r_0p_r(w)dw \ge 0}$ so the minimum value for $\large{T(r)}$ is $\large{0}$. This means that $\large{T(r)}$ also satisfies the [[Criteria For Intensity Transformations#Constrained Range|Constrained Range]] criteria.

Now calculating $\large{\left | \frac{ds}{dr} \right |}$ we see that $$\large{
\begin{aligned}
\dot{T}(r) &= (L-1)\frac{d}{dr}\left[\int_0^rp_r(w)dw\right] \\
&= (L-1)p_r(r)
\end{aligned}}$$
so $\large{p_s(s) = p_r(r)\frac{1}{(L-1)p_r(r)} = \frac{1}{L-1}}$  
This means that $\large{p_s(s)}$ is a Uniform Random Variable independent of the shape of $\large{p_r(r)}$. 
This would mean that such a transformation will spread the Intensity Values of the given image uniformly across the [[Image Histograms#Description|Image Histogram]].

Discretizing this equation we get $\large{T(r_k) = (L-1)\sum_{w=0}^{k}{p_r(r_w)}}$. Since Image Histograms are only approximations of Probability Density Functions and are not continuous and differentiable the transformation will almost never result in a perfectly uniform Image Histogram.

#### Example: 
Consider the following low-contrast image: 
![[Bright Camera Test Image.png]]
Looking at the [[Image Histograms#Description|Image Histogram]] we see a relatively small bandwidth which confirms our intuition.
![[Bright Camera Test Image Histogram.png]]
Equalizing the Image Histogram through the transformed described above we see a much less washed out image, and a significantly wider Image Histogram.
![[Histogram Equalized Bright Camera Test image.png]]
![[Equalized Bright Camera Example Histogram.png]]

#### Implementation: 
Histogram Equalization can be implemented manually through the following code using OpenCV: 
```python
def manual_histogram_equalization(image, L = 256):  
    # Calculate Normalized Image Histogram  
    hist, bins = np.histogram(image.flatten(), L, [0, L], density=True)  
    # Calculate Transform by multiplying histogram cumulative sum by L - 1  
    T_r = (L-1)*hist.cumsum()  
    # Use NumPy Interpolation to compute transform.  
    # bins[:-1] will delete last bin, the extra bin is introduced when using np.histogram
    equalized_image = np.interp(image.flatten(), bins[:-1], T_r).reshape(image.shape)  
    # Match pixel values to uint8.  
    equalized_image = np.uint8(equalized_image)  
    return equalized_image
```
Histogram Equalization also exists natively in OpenCV through the function: 
```python
equalized_img = cv2.equalizeHist(img)
```
In some implementations [[Contrast Stretching Through Linear Piecewise Transforms#Description|Contrast Stretching]] is utilized after equalization in order to spread intensity values further. 

