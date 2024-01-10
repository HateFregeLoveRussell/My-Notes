---
type: Academic
tags:
alias: Img-Proc-1-DFT1Var
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
  book-title: "Digital Image Processing",
  section-name: "DFT of One Variable",
  class-alias: "Img-Proc-1",
  source-alias: "Img-Proc-1-4-4",
  ISBN: "978-93-530-6298-9",
  template: {
    name: "source-tbsection-obj",
    type: "object",
    version: 1
  },
  type: "tbsection",
  start-page: 207,
  end-page: 215
}

relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Observations about the Fourier Transform of Functions of Interest]]"
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
#### The Discrete Fourier Transform
Recall that given a discrete signal $\large{x[n]}$ we can capture its nature in the frequency domain using the Discrete Time Fourier Transform(DTFT) with a continuous and periodic domain (because we are sampling around the unit circle). If we treat $\large{x[n]}$ as the first cycle of a periodic function the information of the DTFT can be captured using the DFT.
Forward Transform: $\large{X[m]= \sum^{N-1}_{n=0}x[n]e^{\frac{-j2\pi n m}{N}}}$ 
Inverse Transform: $\large{x[n] = \frac{1}{N}\sum^{N-1}_{m=0}X[m]e^\frac{j2*\pi m n}{N}}$
Where $\large{N}$ is the number of samples.


If the function $\large{f(t)}$ consists of $\large{M}$ samples at an interval $\large{\Delta T}$ we know from [[Observations about the Fourier Transform of Functions of Interest#Impulse Train|Our Observations of the Impulse Train]] that the corresponding spacing of frequencies $\large{\Delta \mu}$ follows $\large{\Delta \mu = \frac{1}{M\Delta T} = \frac{1}{T}}$ where $\large{T}$ is the total amount of time captured by the function. Similarly the frequency range $\large{R}$ is governed by $\large{R = M\Delta \mu = \frac{1}{\Delta T}}$ 