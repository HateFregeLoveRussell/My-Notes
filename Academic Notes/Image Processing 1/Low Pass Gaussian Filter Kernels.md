---
type: Academic
tags:
alias: Img-Proc-1-LPGFKernels
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
friends: ["[[Box Filter Kernels]]", "[[Image Smoothing]]", "[[Low Pass Filtering]]"]
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
The **==Gaussian Low Pass Filter Kernel==** is class of [[Spatial Filter Kernels|Filter Kernels]] which act as [[Low Pass Filtering|Low Pass Filter]]. Aiming to provide the same [[Box Filter Kernels#Properties and Applications of the Box Kernel|Computational Advantages]] as the [[Box Filter Kernels#Description|Box Filter]] without the directionality issues associated with it. Such Kernels are constructed by sampling the two-dimensional gaussian distribution, centered from the mean. 

The Gaussian Low pass Filter Kernel can be generated using the following equation: $$\large{w(s,t)= G(s,t) = Ke^{-\frac{s^2 + t^2}{2\sigma^2}}}$$
Here the parameter $\large{K}$ is used to scale the kernel as necessary and the parameter $\large{\sigma}$ represents the standard-deviation of the gaussian distribution(the kernel is centered on the mean so we take the distribution to be a zero-mean one).
Similarly to [[Box Filter Kernels#Description|Box Filter Kernels]] the distribution is normalized with the constant $\large{1/\sum^m_{r=-m}\sum^n_{s=-n}w(s,t)}$ where the kernel is assumed to be of size $\large{m}$x$\large{n}$ 

#### Properties:
##### Separability and Isotropy 
Similar to the [[Box Filter Kernels#Properties and Applications of the Box Kernel|Box Filter]] The [[Low Pass Gaussian Filter Kernels#Description|Gaussian Low-Pass Filter Kernel]] is both radially symmetric and [[Separable Image Kernels#Description|Separable]]. We can show that the kernel is [[Spatial Filter Kernels#Symmetry and Convolution|Isotropic]] by parametrizing its equation with $\large{r =\sqrt{s^2 + t^2}}$ to get $\large{G(r) = Ke^{-\frac{r^2}{2\sigma^2}}}$ which no longer depends on the spatial co-ordinates $\large{(s,t)}$. 

##### Maximum-Effective Size Property:
We know that the Gaussian Distribution decays rapidly as it is sampled further away from its mean. More specifically we know that contributions made by values further than $\large{3\sigma}$ from the mean are more or less negligible. This means that Gaussian Kernels effectively have a maximum size beyond which little contribution can be expected. This is in staunch difference to the [[Box Filter Kernels#Description|Box Filter Kernel]] which has no maximum effective size. So for Gaussian Lowpass filters we pick $\large{(m,n) =(\lceil 6\sigma \rceil,\lceil 6\sigma \rceil)}$  more specifically, we pick the closest odd integer to $\large{\lceil 6\sigma \rceil}$ as [[Spatial Filter Kernels#Description|Spatial Filter Kernels]] can only be odd size.

##### Product and Convolution of Gaussians:
Both the product and [[Spatial Correlation and Convolution#Spatial Convolution|Convolution]] of Gaussian distributions are also Gaussian. This means that we can ease computation of multiples and convolutions of Gaussian Kernels through the following relationships: 
$$\large{\begin{aligned} m_{f\star g}  = m_f + m_g && && m_{f.g} = \frac{m_f\sigma_g^2 +m_g\sigma_f^2}{\sigma_g^2 + \sigma_f^2} \\ \sigma_{f\star g} =\sqrt{\sigma_f^2 + \sigma_g^2} && &&  \sigma_{f.g} = \sqrt\frac{\sigma_f^2\sigma_g^2}{\sigma_f^2 + \sigma_g^2}\end{aligned}}$$

##### In Comparison to the Box Kernel:
Typically, a [[Low Pass Gaussian Filter Kernels#Description|Gaussian Kernel]] will achieve much weaker blurring compared to a [[Box Filter Kernels#Description|Box Filter kernel]] of the same size this is largely because the weights of a gaussian kernel decay with distance from the origin while this is not the case for the Box Kernel. 

Unlike the Box Filter however, the Gaussian Filter does not produce a [[Box Filter Kernels#Properties and Applications of the Box Kernel|Squeezing Effect]] on images filtered by it. this is because the kernel decays radially while the Box Filter stays constant. 

#### Examples: 
##### Difference Between Gaussian and Box Filter:
![[Comparison Between Gaussian and Box LPF Example.png]]
Above is a comparison between the [[Low Pass Gaussian Filter Kernels#Description|Gaussian Kernel]] and its [[Box Filter Kernels#Description|Box Kernel]] counterpart at various sizes. Notice how the gap in blur strength increases as size of the kernels increase. The gap could be minimized for a specific kernel size with a sufficiently large choice of sigma but it the strength of the Box Filter will always grow faster than that of the Gaussian. 

##### Maximum Effective Kernel Size:
Below is graph detailing the Mean Squared Error between an image blurred with a given kernel size and the same image blurred with the starting kernel size $\large{+12}$. As can can be seen, the difference between kernels which are $\large{12}$ units away from each other decays rapidly and is more or less unobservable after $\large{\lceil6\sigma\rceil}$.
![[Maximum Effective Gaussian Low Pass Kernel Size Example.png]]

#### Implementation: 
The following is an implementation of a gaussian kernel of size $\large{n}$ and standard deviation $\large{\text{sigma}}$. Note that `np.meshgrid` produces a 2D array corresponding to the indexing scheme used in image kernels and decomposes it into the spatial co-ordinates used to formulate the kernel. 
```python
def generate_gaussian_kernel(n, sigma, K=1.0):  
    # Ensure n is an odd number  
    if n % 2 == 0:  
        raise ValueError("Kernel size (n) must be an odd number.")  
  
    # Create a meshgrid representing the coordinates of the kernel  
    x, y = np.meshgrid(np.arange(-n//2 + 1, n//2 + 1), np.arange(-n//2 + 1, n//2 + 1))  
  
    # Compute the Gaussian kernel using the 2D Gaussian distribution formula  
    kernel = K * np.exp(-(x**2 + y**2) / (2 * sigma**2))  
    kernel /= kernel.sum()  # Normalize the kernel to ensure the sum of elements is 1  
  
    return kernel  
  
def generate_optimal_gaussian_kernel(n,sigma,K=1.0):  
    kernel_size = np.ceil(6*n)  
    kernel_size = kernel_size + 1 if kernel_size % 2 == 0 else kernel_size  
    return generate_gaussian_kernel(kernel_size,sigma,K)
```
In order to achieve the same blurring in the [[Low Pass Gaussian Filter Kernels#Examples|Examples Above]] make sure to use the custom convolution algorithm detailed in [[Box Filter Kernels#Example|the Box Filter Example]] instead of `cv2.filter2D`.

OpenCV also implements [[Low Pass Gaussian Filter Kernels#Description|Gaussian Blurs]] natively using the function:
```python
blurred_image = cv2.GaussianBlur(image, (ksize,ksize), sigma)
```
