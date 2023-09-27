# Lecture 2 AI
Tuesday 19.09.23\
Big prize for anyone that can spot all the spelling or typing mistakes.

## Uninformed Search
    - BFS / DFS / UCS
    - UCS path is optimal, even tho its inefficient
  
### uniform cost search
    - expand cheapest node first
    - exploring lots of nodes far from goal
    - cheap but inefficient

(sidenote: we know where our goal is.. does that make it 'informed search'?)

### Optimality vs Efficiency (vs my spelling!)
"im quick at math"
-"okei, whats 55 times 16"
"1200"
-"no. no way off"
"was fast tho"

So how to make an algorithm thats fast and correct?
Would be nice to just exclude the unimportant areas..

## Informed Search

Step up from local search, look into the deeper path.

### Search Heuristics
How to get hints to the goal. \
A function that estimates how close the goal is. \
Ex: manhatten dst, Euclidean dst

(sidenote: given the nature of sokoban, perhaps multip-manhatten dst, to inlcude the wierd paths of the warehouses.)

Again, efficient vs optimal algorithm..

Proposed heuristics for sokoban:
 - dst box to hole
 - manhattn dst to closest hole
 - ? different h for each box ?

## Informed Search algorithms
A look at different algorithmms 

### Greedy search
expand the cheapest node first, but instead of cost, we look at hueristic cost.\
can get stuck on wrong goal tho \
efficient, but non-optimal

### A* search
as Hannah montana said; the best of both worlds.\
combineing Greed and UCS, so g(x)+h(x) \
The curse of bad heuristics, can fuck up A*..

### Admissable Heuristics
Inadmissible h is pessimistic, admissible is optimistic. GOal is to slow down the bad path and improve the fast one. \
Should be less then the cheapest true cost. \

### Consistency
Not only h < g\
but h(A) - h(C) < cost(A to C), meaning ..

A* is optimal when h is admissible and consistent, and they are related, so it comes easy right???


## Graph Search vs Tree Search
Main diff, graphs keep 'memory' of whats been done.  \
Meaning, no repeating search, more lazy.




## For the project
should we compare all the different search algos, both unifnromed and informed with hueristics?
