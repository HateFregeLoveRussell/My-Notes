---
type: Academic
tags:
alias: Gi-1-SnapComm
class: {"class-name":"The Git and Github Bootcamp","instructor":"Colt Steele","medium":"Online Course","start-date":"2023-04-25","online-platform":"Udemy","length":"17 hours","class-alias":"Gi-1","template":{"name":"class-online-course-obj","version":1}}
source: [{link: "[[Git 1 Bibliography#Section 4: The Very Basics of Git: Adding & Committing]]", alias: Sec4-Gi-1, template: {name: bib-source-obj , version: 1}}, {link: "[[Git 1 Bibliography#Section 5: Commits in Detail (And Related Topics)]]", alias: Sec5-Gi-1, template: {name: bib-source-obj , version: 1}}, {link: [[Git 1 Bibliography#Section 6: Working With Branches]], alias: Sec6-Gi-1, template: {name: bib-source-obj , version: 1}}]
relationship: {name: standard-relationship-obj, version: 1}
friends: "[[Git Configuration Commands]]"
status: {state: In Progress, template: {name: status-obj, version: 1}}
validity:  {state: true, template: {name: validity-obj, version: 1}}
template: {name: class-note-temnplate, version: 1}
---
### Description: 
The following are commands in Git which aid in saving and viewing repository progress.

#### git add 
This method when provided with a path-type argument to a file in the git repository will add the said file to the [[Git 1 Dictionary#Staging Area|Staging Area]]. Multiple files can be added at once by separating their paths with spaces. 

The command `git add .` will add any changes made to the repository to the Staging Area.

You can check what files are in the Staging Area using [[Git Configuration Commands#git status|git status]] after using this command.

#### git commit 
This command will [[Git 1 Dictionary#Commit|Commit]] the files in the [[Git 1 Dictionary#Staging Area|Staging Area]] in the git repository.

Every Commit in git needs a message summarizing the changes made. When run in it's native form `git commit`, Git will attempt to use the system's default text editor in order to get this message. This editor in most cases is Vim. To exit Vim use `:` + `q` + `Enter`, If you ever end up needing to use vim for commit messages: Press `i` to enter inset mode, type your message, `Escape` + `w` + `q` + `Enter`. You can change the default editor for commits using [[Git Configuration Commands#git config core.editor|git config core.editor]].

The Commit Message can be added as a string in the terminal argument when using the flag `-m`. So the schema follows: `git commit -m "My Message"`.

It is good practice to write commit messages in present-tense not past-tense. Consistency using the same tense is more important however.

With the `--amend` flag in the form `git commit --amend` allows the user to amend their previous commit. The staging area can be modified and then committed again.

When the `-a` flag is used git will commit all file changes and removals that have not been staged, new files will be unaffected. 
#### git log
This command will print a log of all [[Git 1 Dictionary#Commit|Commits]] in the repository. The flag `--oneline` will print an abbreviated version of the log instead of the full one.