---
type: Academic
tags:
alias: Gi-1-DiffOutput
class: {"class-name":"The Git and Github Bootcamp","instructor":"Colt Steele","medium":"Online Course","start-date":"2023-04-25","online-platform":"Udemy","length":"17 hours","class-alias":"Gi-1","template":{"name":"class-online-course-obj","version":1}}
source: {link: "[[Git 1 Bibliography#Section 8: Comparing Changes With Git Diff]]", alias: Sec8-Gi-1, template: {name: bib-source-obj , version: 1}}
relationship: 
status: {state: Completed, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description: 
Below is a description of the structure of the output of the `git diff` command, information on how to use the command can be found [[Git Diff Command|here]].

### Output:
The output of `git diff` will consist of one or more blocks of the following form:
This block will begin with an output of the form: `diff --git a/<file1> b/<file2>`
which will inform the user of the files being compared, in the usual case where the files have the same name, one will be preceded with `a/` and the other with `b/`
The next line in the output can be ignored. 
After that the "Markers" are assigned, in a statement of the form:
```
--- a/<file1>
+++ b/<file2>
```
Each file is assigned a symbol, file a gets `-` and file b gets `+`
After the Markers are assigned, one or more "chunk" is printed, these are the areas inside the file in which content differs.
Every Chunk has a "Header" of the form `@@-<int1>,<int2>,+<int3>,<int4>@@`
`int1` will denote the starting line of file a, `int2` will denote the number of lines from file a included, Similarly, `int3` denotes the starting line of file b, and `int4` will denote the number of lines included from file b.
The chunk itself consists of content from both files where the lines preceded by a `-` are in file a and not in file b, the lines preceded by a `+` are in file b and not in file a, and lines not preceded by either are present in both files. 