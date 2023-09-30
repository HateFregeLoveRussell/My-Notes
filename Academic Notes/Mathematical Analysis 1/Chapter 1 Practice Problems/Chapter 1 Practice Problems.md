---
type: Academic
tags: RepoNote
alias: Math-An-1-Ch1PP
class: {
  class-name: "Mathematical Analysis 1",
  author: "Walter Rudin",
  medium: "Textbook",
  class-alias: "Math-An-1",
  title: "Principles Of Mathematical Analysis",
  edition: "Third",
  publisher: "McGraw-Hill Book Company",
  ISBN: "978-0-07-054235-8",
  length: 334,
  template: {
    name: "class-textbook-obj",
    version: 1,
    type: "object"
  }
}
source: {
  source-alias: "Math-An-1-TheRealAndComplexNumberSystems-PracticeProblems",
  book-title: "Principles of Mathematical Analysis",
  section-name: "The Real and Complex Number Systems: Practice Problems",
  type: "tbsection",
  ISBN: "978-0-07-054235-8",
  template: {
    version: 1,
    type: "object",
    name: "source-tbsection-obj"
  },
  start-page: 21,
  class-alias: "Math-An-1",
  end-page: 23
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

#### Query:
```dataview
TABLE status
FROM "Academic Notes/Mathematical Analysis 1/Chapter 1 Practice Problems"
WHERE template.name = "class-textbook-practice-problem"
```


