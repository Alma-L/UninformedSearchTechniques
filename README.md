# UninformedSearchTechniques

### Institution
- **Name**: University of Prishtina (UP)
- **Faculty**: Faculty of Electrical and Computer Engineering (FIEK)
- **Course**: "Artificial Intelligence" (AI)
- **Program**: First Semester, Master's

## Overview
This repository contains implementations for solving three classic AI problems using various uninformed search techniques, including Depth First Search (DFS), Depth Limited Search (DLS), Breadth First Search (BFS), Iterative Deepening Depth First Search (IDDFS), and Backtracking. These solutions are tailored for educational purposes as part of an assignment.



### **1. Social Golfers Problem**

#### **Problem Description**
32 golfers need to be arranged into groups of 4 players every week. The challenge is to determine how many weeks (`w`) they can play such that no two players play in the same group more than once.

#### **Generalized Problem**
Can we schedule `n = g × p` golfers into `g` groups of `p` players for `w` weeks, ensuring no two players play together more than once in the same group?

#### **Example Input and Output**

| **Group** | **Week 1**                   |
|-----------|------------------------------|
| Group 1   | 0,1,2,3                      |
| Group 2   | 4,5,22,23                    |
| Group 3   | 6,7,20,21                    |
| ...       | ...                          |

#### **Techniques Used**
1. **Depth First Search (DFS)**
2. **Depth Limited Search (DLS)**
3. **Backtracking**

#### **Files**
- `SocialGolfersProblem.py`: Contains the implementation of the scheduling algorithm using the above techniques.

---

### **2. Sudoku Solver**

#### **Problem Description**
Solve a Sudoku puzzle with three levels of difficulty: **Easy**, **Medium**, and **Hard**. A Sudoku is a 9x9 grid where each row, column, and 3x3 subgrid must contain the numbers 1 through 9 exactly once.

#### **Techniques Used**

1. **Breadth First Search (BFS)**
2. **Backtracking**


#### **Files**
- `sudoku_solver.py`: Contains the implementation of the Sudoku solver using BFS and Backtracking.

---

### **3. Latin Square**

#### **Problem Description**
A Latin Square is an `n x n` grid filled with `n` unique numbers such that each number appears exactly once in every row and column.

#### **Techniques Used**
1. **Iterative Deepening Depth First Search (IDDFS)**
2. **Backtracking**

#### **Files**
- `LatinSquare.py`: Contains the implementation for generating Latin Squares using IDDFS and Backtracking.

