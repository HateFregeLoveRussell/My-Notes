---
type: Academic
tags:
  - Entrynote
alias: Math-An-1-Portal
class:
  class-name: Mathematical Analysis 1
  author: Walter Rudin
  medium: Textbook
  class-alias: Math-An-1
  title: Principles Of Mathematical Analysis
  edition: Third
  publisher: McGraw-Hill Book Company
  ISBN: 978-0-07-054235-8
  length: 334
  template:
    name: class-textbook-obj
    version: 1
    type: object
relationship:
  name: standard-relationship-obj
  version: 1
parent:
  - "[[Class-Sched]]"
  - "[[Class-Display-Portal]]"
  - "[[Class-Bibliography]]"
class-status:
  state: In Progress
  template:
    name: status-obj
    version: 1
    type: object
status:
  state: Completed
  template:
    name: status-obj
    version: 1
    type: object
validity:
  state: true
  template:
    name: validity-obj
    version: 1
    type: object
template:
  name: class-portal-template
  version: 2
---
### Class Description:
```dataview
TABLE class.class-name AS "Class Name", class.author AS "Class Author", class.medium AS "Class Medium", class.length AS "Class Length"
WHERE file = this.file
```

Textbook acting as Introduction to Real Analysis, intended to act as preliminary for Kolmogorov's book on Real Analysis.
### Class Content:
- Chapter 1: The Real and Complex Number Systems
- Chapter 2: Basic Topology
- Chapter 3: Numerical Sequences and Series
- Chapter 4: Continuity
- Chapter 5: Differentiation 
- Chapter 6: The Reimann-Stieltjes Integral
- Chapter 7: Sequences and Series of Functions
- Chapter 8: Some Special Functions
- Chapter 9: Functions of Several Variables
- Chapter 10: Integration of Differential Forms
- Chapter 11: The Lebesgue Theory

### Class Progress: 

**In Progress Notes:**
```dataview
LIST
FROM "Academic Notes/Mathematical Analysis 1"
WHERE status.state = "In Progress" OR status.state = "Stub"
```
