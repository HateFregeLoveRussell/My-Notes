---
type: Academic
tags:
alias: Gi-1-UnixComm
class: {"class-name":"The Git and Github Bootcamp","instructor":"Colt Steele","medium":"Online Course","start-date":"2023-04-25","online-platform":"Udemy","length":"17 hours","class-alias":"Gi-1","template":{"name":"class-online-course-obj","version":1}}
source: {link: "[[Git 1 Bibliography#Section 3: Installation & Setup]]", alias: Sec3-Gi-1, template: {name: bib-source-obj , version: 1}}
relationship: 
status: {state: In Progress, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description: 
The following are a list of Unix-type commands that will prove useful in working with git through the system terminal.

##### ls
This command lists the contents of the current directory. When used with the flag `-a` is will show any hidden files present in the current directory as well. When given an argument in the form `ls <path>` it will list the contents of the directory pointed to by `path`.

##### pwd
This command prints the path to the working directory (current location) of the terminal.

##### cd 
This command, when presented an argument in the form `cd <path>` will move the working directory to the directory pointed to by `path`. When `path` = `..` the working directory will be set to the parent directory of the previous working directory. 

##### touch
This command, when presented an argument in the form `touch <name>` will create a file with the name:  `name` in the working directory. This file will be empty on creation. Multiple files can be created at once by providing several arguments separated by spaces. Files can also be created outside the working directory by instead of just providing the file name as the command argument(s), passing it's directory as well, so `touch <path/to/name>`

##### mkdir
This method when provided a path as it's argument will create a directory specified by that path. So `mkdir "path/to/name"` will create a directory `name` at `path/to/`. Similarly to [[Unix Type Commands#touch|touch]], separating arguments by spaces allows you to create multiple directories at once. If the directory itself has spaces in it's path use quotation marks to avoid confusing the terminal. 

##### rm
This method when provided a path as it's argument will delete the file located at said path. Similarly to both [[Unix Type Commands#touch|touch]] and [[Unix Type Commands#mkdir|mkdir]] spaces indicate separate files to be deleted so it's good practice to wrap paths in quotation marks. This deletion process is permanent. The `-rf` flag can be used if you wish to delete an entire directory. 

 