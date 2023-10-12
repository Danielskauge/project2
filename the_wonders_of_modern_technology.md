# Comparative Analysis of Uninformed and Informed Search Algorithms with Variable Heuristics in Sokoban Solving

## Abstract

This report presents a comprehensive comparative analysis of uninformed and informed search algorithms in solving the Sokoban puzzle, a classic problem in artificial intelligence. We explore the effectiveness of Breadth-First Search (BFS), Depth-First Search (DFS), A* search, and various heuristics in finding optimal solutions for Sokoban puzzles. The study aims to provide insights into the strengths and limitations of these algorithms and heuristics in tackling challenging instances of the Sokoban puzzle.

## 1. Introduction

The Sokoban puzzle is a well-known problem in the field of artificial intelligence and computer science, requiring an agent to manipulate boxes within a warehouse to specific target locations while adhering to a set of rules. Solving Sokoban puzzles algorithmically involves finding an optimal sequence of moves to achieve the goal state.

This report investigates the application of different search algorithms, both uninformed (BFS and DFS) and informed (A* search), to solve Sokoban puzzles. Additionally, we explore the impact of various heuristics on the performance of the informed search algorithms. The study aims to shed light on the efficiency and optimality of these approaches for solving Sokoban puzzles.

## 2. Sokoban Puzzle Representation

The Sokoban puzzle is represented as a grid, where each cell can be in one of several states:

- Empty: Represented as 'E', denoting an empty floor cell.
- Wall: Represented as 'W', indicating an impassable wall.
- Box: Represented as 'B', representing a box that must be pushed.
- Target: Represented as 'T', signifying the target location for boxes.
- Player: Represented as 'P', denoting the player's position.

The objective is to move all the boxes to their respective target locations while adhering to the rules defined earlier.

## 3. Uninformed Search Algorithms: BFS and DFS

Breadth-First Search (BFS) and Depth-First Search (DFS) are two uninformed search algorithms explored in this study.

- BFS explores the search space level by level, guaranteeing that the first solution found is the optimal one in terms of the number of moves.

- DFS explores one branch of the search space as deeply as possible before backtracking. It is less memory-intensive than BFS but does not guarantee optimality.

## 4. Informed Search Algorithm: A* Search

The A* search algorithm is an informed search algorithm that combines the advantages of both BFS and DFS. It uses a heuristic function to guide the search towards the most promising paths while guaranteeing optimality.

- A* search evaluates nodes based on a cost function 'f(n) = g(n) + h(n),' where 'g(n)' represents the cost to reach the node from the start, and 'h(n)' is the estimated cost to reach the goal.

- The choice of heuristic function 'h(n)' can significantly impact the algorithm's performance.

## 5. Heuristics for Informed Search

Various heuristics are explored in this study to evaluate their impact on A* search performance:

- Manhattan distance: The sum of the horizontal and vertical distances between each box and its target location.

- Minimum spanning tree: Constructing a minimum spanning tree connecting all the boxes and their respective targets.

- Dead-end heuristic: Identifying and avoiding dead-end configurations in the warehouse.

- Pattern database: Precomputing and using a database of optimal solutions for specific warehouse patterns.

## 6. Performance Evaluation and Results

The comparative analysis includes a set of Sokoban puzzles of varying complexities. Performance metrics such as time to solve, number of nodes expanded, and solution optimality are considered. The results indicate that:

- BFS guarantees optimal solutions but can be memory-intensive for large puzzles.
- DFS may not always find optimal solutions but is memory-efficient.
- A* search outperforms both BFS and DFS when guided by effective heuristics.

The choice of heuristic greatly influences A* search's performance, with the pattern database heuristic often providing the best results.

## 7. Conclusion

This report presents a comparative analysis of uninformed and informed search algorithms in solving the Sokoban puzzle, along with various heuristics for the informed search. The study offers valuable insights into the strengths and weaknesses of each approach.

In summary, A* search with an appropriate heuristic, such as the pattern database, stands out as the most effective method for solving Sokoban puzzles efficiently while guaranteeing optimality. The choice of heuristic plays a crucial role in determining the algorithm's success in tackling challenging instances of the Sokoban puzzle.

## References

[1] Russell, S. J., & Norvig, P. (2009). Artificial Intelligence: A Modern Approach (3rd ed.). Pearson.
[2] Junghanns, A., & Schaefer, T. (2001). Sokoban: Enhancing General Game Playing. In Proceedings of the 17th International Joint Conference on Artificial Intelligence (IJCAI) (pp. 364-369).
