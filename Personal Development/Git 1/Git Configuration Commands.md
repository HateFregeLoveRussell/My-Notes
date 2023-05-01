---
type: Academic
tags:
alias: Gi-1-ConfigCommands
class: {"class-name":"The Git and Github Bootcamp","instructor":"Colt Steele","medium":"Online Course","start-date":"2023-04-25","online-platform":"Udemy","length":"17 hours","class-alias":"Gi-1","template":{"name":"class-online-course-obj","version":1}}
source: [{link: "[[Git 1 Bibliography#Section 3: Installation & Setup]]", alias: Sec3-Gi-1, template: {name: bib-source-obj , version: 1}}, {link: "[[Git 1 Bibliography#Section 4: The Very Basics of Git: Adding & Committing]]", alias: Sec4-Gi-1, template: {name: bib-source-obj , version: 1}}]
relationship: 
status: {state: In Progress, template: {name: status-obj, version: 1}}
validity: {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---

### Description:
The following is a list of commands used to configure either a repository or git itself in a system or directory.

#### git config user.name
This command will return the system's configured git username. when used in the following syntax scheme: `git config --global user.name <name>` it will set the system git username to `name`

#### git config user.email
This command works identically to `git config user.name`. When used in its ordinary form it will return the configured email for git in the system. When used through the scheme `git config --global user.email <email>` it will set the system git email to `email`

#### git config core.editor

#### git status
This command prints information on the state of the repository (or the lack of one) in the working directory.

#### git init
Initializes a new git repository at the working directory. Ideally this command should be ran once (at the start of) in a project. It is generally considered bad practice to initialize a git repository within another git repository, because of this it is recommended to always check using [[Git Configuration Commands#git status|git status]] whether if a git repository exists within the working directory before calling `git init`