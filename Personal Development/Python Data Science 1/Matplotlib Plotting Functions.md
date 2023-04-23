---
type: Academic
tags:
alias: P-DS-1-MatplotlibPlotting
class: {"class-name":"Python for Data Science","instructor":"Maxwell Armi","medium":"Online Course","start-date":"2023-04-01","online-platform":"FreeCodeCamp-Youtube","length":"12hr20min","class-alias":"P-DS-1","template":{"name":"class-online-course-obj","version":1}}
source: {link: "[[Python Data Science 1 Bibliography#The Matplotlib Python Data Science Library]]", alias: matplotlib-P-DS-1, template: {name: bib-source-obj , version: 1}}
relationship: {name: standard-relationship-obj, version: 1}
friends: ["[[Numpy Arrays]]"]
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---

### plt.plot(x, y, colour?)

This method will create a classical two-dimensional graph containing the points described by the coordinate arrays `x` and `y`. These parameters are typically [[Numpy Arrays|Numpy Arrays]]. Similarly to MATLAB lines will be drawn in-between data points for interpolation purposes.  Note that this method does not actually generate the graph in the command line, rather saves it to memory, the plot can be manipulated further with successive uses of other methods and will only be moved out of memory when [[Matplotlib Plotting Functions#plt.show()|plt.show()]]. The `colour` parameter determines the colour of the line drawn on the graph, successive calls to this function will draw multiple lines on the graph.  This parameter is string which can address colours explicitly or by short hand. Some examples include: 
`-g` => solid green line
`--c` => dashed cyan line
`-.k` => dash-dotted black line
`:r` => dotted red line

### plt.scatter(x, y) 

This method works identically to [[Matplotlib Plotting Functions#plt.plot()|plt.plot()]] except instead of interpolating between data points, the graph is presented as a scatter-plot. 

### plt.xlabel(label)

Puts a label determined by string parameter `label` on the x-axis of the current graph.

### plt.ylabel(label)

Works identically to [[Matplotlib Plotting Functions#plt.xlabel(label)|plt.xlabel()]] but for the y-axis

### plt.title(title)

Puts a Title on the current graph determined by the string parameter `title`

### plt.show()

Will display current graph in terminal or the SciView tab. 