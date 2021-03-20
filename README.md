I'm currently a student at Hochiminh University of Science. And this is the requirement of the practice exercise for AI on local search and the 8-Queens problem. This is the source code of my teacher, I just code some few functions.

Local Search (Local Search):
The search algorithms that we have looked at so far are designed to browse in some system's search space. The system calculates by keeping in a memory or multiple paths and by noting what has been reviewed along the way and which has not. When the target is found, the path to this goal is also the solution to the problem.

In some problems, to find the most optimal (global optimization) requires a lot of resources and computation costs, especially problems that do not search very wide, infinite or near as infinite. Do that, the search on the best solution for the worksheet that near as not be, or only can be found for the your value start near the end of the point.

For such problems, the local search algorithm (Local Search) is the commonly applied method. Local search algorithm uses a single current state (instead of many different paths) and only transitions to neighboring state. Usually, the paths in the search process are not retained.

Local Search algorithm has two outstanding advantages:
1. Uses very little memory, usually a fixed amount.
2. Often a plausible solution can be found in a large or infinite state space.
![image](https://user-images.githubusercontent.com/61641601/111863602-30fabf00-898f-11eb-883d-cb1cf8a20f69.png)


Hill Climbing Algorithm:

Hill climbing algorithm is an algorithm in the group of local search algorithms. The hill climb algorithm is built on the idea of greed, continuously moving in the direction of increasing value at a given state.

The simple algorithm uses a loop in which it continuously searches for neighboring states with a more optimal value and moves to that state. The algorithm stops when it reaches "local optimal state" but neighboring states have no higher value.
Note: That "optimal peak" may not be the most optimal of the problem.

![image](https://user-images.githubusercontent.com/61641601/111863609-3a842700-898f-11eb-89cc-dc708c01cb81.png)

Describe the 8-post problem:
Given an 8x8 chess board, on which 8 queens are available in any 8 positions with the constraint that each column has at least one queen. For example, as shown below.
![image](https://user-images.githubusercontent.com/61641601/111863627-4c65ca00-898f-11eb-8eef-e15be9cd633c.png)

Heuristic function h (x) is defined as the number of queens that can attack each other, directly or indirectly. For example, the upper left state h (x) = 17, the right state has h (x) = 1.

Requirements: With the given state as above of the chess board. Calculate the value of the function h (x) in the cells of the matrix when moving the queens to that position. Know that in any state of the board, queens can be moved vertically from the position where they are standing.
Sample input and output:
![image](https://user-images.githubusercontent.com/61641601/111863657-70c1a680-898f-11eb-84c7-563f6daca388.png)
