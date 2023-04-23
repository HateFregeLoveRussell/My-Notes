---
type: Academic
tags:
alias: P-DS-1-PandasNaN
class: {"class-name":"Python for Data Science","instructor":"Maxwell Armi","medium":"Online Course","start-date":"2023-04-01","online-platform":"FreeCodeCamp-Youtube","length":"12hr20min","class-alias":"P-DS-1","template":{"name":"class-online-course-obj","version":1}}
source: {link: "[[Python Data Science 1 Bibliography#The Pandas Python Data Science Library]]", alias: pandas-P-DS-1, template: {name: bib-source-obj , version: 1}}
relationship: 
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---

The Following is a list of methods meant to assist in manipulating [[Pandas Data Frame|Data Frames]] which have `NaN` entries.

### data.fillna(arg)

This method when enacted on the Data Frame `data`. Will replace all `NaN` entries in `data` with the parameter `arg`

### data.dropna()

When this method is called on the Data Frame `data`. It will remove any entries which contain a `NaN` element.