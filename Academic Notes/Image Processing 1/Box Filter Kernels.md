---
type: Academic
tags:
alias: Img-Proc-1-BoxFilterKernels
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
  }
}
relationship: {name: standard-relationship-obj, version: 1}
friends: ["[[Image Smoothing]]", "[[Low Pass Filtering]]"]
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
Box Filter Kernels are a class of [[Spatial Filter Kernels#Description|Spatial Filter Kernels]] which act as [[Low Pass Filtering|Low Pass Filters]], which means they are also an adequate choice for [[Image Smoothing#Description|Image Smoothing Objectives]].

Every Entry in a Box Filter is the same quantity(typically $\large{1}$). It is important to note that when this is the case the output of the kernel is a weighted sum of pixel intensities. Additionally, a normalization factor is applied to the kernel equal to the reciprocal number of entries(in the case where every entry is $\large{1}$) $\large{\frac{1}{mn}}$. With the inclusion of this normalization factor the kernel output is equivalent to the average pixel value in the kernel neighbourhood. 

#### Example Kernel: 
The following is a standard $\large{3}$x$\large{3}$ [[Box Filter Kernels#Description|Box Kernel]]: 
$$\large{\frac{1}{9}\begin{bmatrix}1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1\end{bmatrix}= \begin{bmatrix}\frac{1}{9} & \frac{1}{9} & \frac{1}{9} \\ \frac{1}{9} & \frac{1}{9} & \frac{1}{9} \\ \frac{1}{9} & \frac{1}{9} & \frac{1}{9}\end{bmatrix}}$$

#### Properties and Applications of the Box Kernel: 
Two important properties of the [[Box Filter Kernels#Description|Box Kernel]] are that it is always both [[Separable Image Kernels#Description|Separable]] and [[Spatial Filter Kernels#Symmetry and Convolution|Isotropic]] giving us significant computational speed and flexibility. Additionally it should be noted that the strength of blur is correlated to the size of the kernel, this makes sense as a larger kernel simply implies a larger neighbourhood for averaging. It is however also inverse correlated to the size of the feature being blurred in the image. So in reality the strength of the resulting blur is a function of the ratio between kernel size and feature size. Such benefits come at the cost of the Box Filter Kernel being rather limited in application. Box kernels favour blurring in perpendicular directions, so they are a poor choice for [[Image Smoothing#Description|Smoothing]] high-detail images or images with strong geometric features. The Box Filter is also a poor choice for modelling most phenomenon typically modelled through [[Low Pass Filtering|Low Pass Filters]].

#### Example: 
Below is an example of a box filter applied to the camera example photo at various kernel sizes. As explained in [[Box Filter Kernels#Properties and Applications of the Box Kernel|Properties of the Box Filter]] we can see the strength of the blur increase proportionally to the size of the kernel. Additionally, we note that a dark border creeps in as kernel size increases, this is a consequence of using [[Image Padding#Zero-Padding|Zero-Padding]]. With larger kernel sizes a larger proportion of the border pixel's local mean will be 0, and hence a dark border will immerge in the output image.
![[Box Filter Camera Example Kerner Size 3 to 7.png]]![[Box Filter Camera Example Kernel Size 9 to 15.png]]

The directionality of the blurring can be observed in the image below. As noted [[Box Filter Kernels#Properties and Applications of the Box Kernel|here]] the Box Filter favours blurring in perpendicular directions. This can be observed as the filtered image has developed orthogonal features that are not present in the original. 
![[Box Filter Example Directionality Test.png]]

#### Implementation: 
A Box Kernel can be generated using:
```python
def generate_box_kernel(n):  
    # Ensure n is an odd number  
    if n % 2 == 0:  
        raise ValueError("Kernel size (n) must be an odd number.")  
  
    # Generate the box kernel  
    box_kernel = np.ones((n, n), dtype=np.float32) / (n * n)  
  
    return box_kernel
```
and Convoluted with a given image using Zero-Padding using:
```python
def custom_convolution(image, kernel):  
    # Get the size of the kernel and the input image  
    kernel_height, kernel_width = kernel.shape  
    image_height, image_width = image.shape  
  
    # Calculate the padding needed  
    pad_top = kernel_height // 2  
    pad_bottom = kernel_height - pad_top - 1  
    pad_left = kernel_width // 2  
    pad_right = kernel_width - pad_left - 1  
  
    # Pad the input image with zeros  
    padded_image = np.pad(image, ((pad_top, pad_bottom), (pad_left, pad_right)), mode='constant', constant_values=0)  
  
    # Initialize the result image  
    result_image = np.zeros_like(image, dtype=np.float32)  
  
    # Perform convolution  
    for y in range(pad_top, image_height + pad_top):  
        for x in range(pad_left, image_width + pad_left):  
            region = padded_image[y - pad_top:y + pad_bottom + 1, x - pad_left:x + pad_right + 1]  
            result_image[y - pad_top, x - pad_left] = np.sum(region * kernel)  
  
    return result_image
```
If one wishes to use OpenCV's native kernel convolution feature use the function: 
```python 
filtered_image = cv2.filter2D(image, -1, kernel)
```
However, keep in mind that `cv2.filer2D` does not preform [[Image Padding#Zero-Padding|Zero-Padding]] instead using [[Image Padding#Replicate-Padding|Border-Replicate-Padding]].
Box Filtering itself can be done directly using the following command in OpenCV with the previously discussed differences:
```python
filtered_image = cv2.boxFilter(image,-1,(kernel_size,kernel_size))
```
