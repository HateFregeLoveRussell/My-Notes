---
type: Academic
tags:
alias: Img-Proc-1-FTofBox
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
  type: "tbsection",
  section-name: "Perliminary Concepts",
  ISBN: "978-93-530-6298-9",
  book-title: "Digital Image Processing",
  class-alias: "Img-Proc-1",
  source-alias: "Img-Proc-1-4-2",
  start-page: 207,
  end-page: 215,
  template: {
    name: "source-tbsection-obj",
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
#### The Box Function and The Sinc Function
It is well known that $\large{\mathscr F\{ A\Pi_w(t)\} = Aw *{\operatorname{Sinc}(\pi \mu w)}}$ graphed below.
![[SincExample.png]]
Some important relationships of note:
- The spacing between zeros of $\large{\mathscr F\{\Pi_w(t)\}}$ are inverse proportional to the parameter $\large{w}$ 
- The lobes of the function $\large{\mathscr{F}\{\Pi_w(t)\}}$ decay as $\large{|\mu| \to \infty }$ 
- The function $\large{\mathscr{F}\{\Pi_w(t)\}}$ spans the entire real line 
- The maximum of $\large{\mathscr{F}\{A\Pi_w(t)\}}$ is proportional to $\large{A}$ it is $\large{1}$ by default

#### Impulse Train
The impulse train also known as "Dirac's Comb" is typically formulated as $\large{s_{\Delta T} = \sum^\infty_{k=-\infty}\delta(t - k\Delta T)}$  has the Fourier Transform $\large{S(\mu) = \frac{1}{\Delta T} \sum^\infty_{n = -\infty}\delta(\mu - \frac{n}{\Delta T})}$. What is important to note about this particular transform pair is that the spacing of frequency impulses compared to their time-domain counterpart is inversely proportional. **