Here’s a cheat sheet on common computer algorithms, focusing on key points, time complexities, and important aspects to remember.

---

### **Sorting Algorithms**

| **Algorithm** | **Time Complexity (Best)** | **Time Complexity (Average)** | **Time Complexity (Worst)** | **Space Complexity** | **Stability** | **Key Points** |
|---------------|---------------------------|-------------------------------|-----------------------------|----------------------|---------------|----------------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes | Simple, but inefficient for large datasets. |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | No | Always performs O(n²) comparisons, irrespective of the input. |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes | Efficient for small or nearly sorted data. |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Divide and conquer approach; stable but uses extra space. |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Fastest in practice for average cases; divide and conquer. |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Efficient and in-place, but not stable. |
| **Radix Sort** | O(nk) | O(nk) | O(nk) | O(n + k) | Yes | Non-comparative, good for integers or strings with fixed size. |
| **Bucket Sort** | O(n + k) | O(n + k) | O(n²) | O(n) | Yes | Distributes elements into buckets; good for uniformly distributed data. |

---

### **Search Algorithms**

| **Algorithm** | **Time Complexity (Best)** | **Time Complexity (Average)** | **Time Complexity (Worst)** | **Space Complexity** | **Key Points** |
|---------------|---------------------------|-------------------------------|-----------------------------|----------------------|----------------|
| **Linear Search** | O(1) | O(n) | O(n) | O(1) | Simple and works on any data structure. |
| **Binary Search** | O(1) | O(log n) | O(log n) | O(1) | Requires sorted array; divide and conquer approach. |
| **Jump Search** | O(√n) | O(√n) | O(√n) | O(1) | Ideal for large, sorted arrays. |
| **Interpolation Search** | O(log log n) | O(log log n) | O(n) | O(1) | Works well with uniformly distributed data. |
| **Exponential Search** | O(log n) | O(log n) | O(log n) | O(1) | Useful for unbounded or infinite lists. |

---

### **Graph Algorithms**

| **Algorithm** | **Time Complexity** | **Space Complexity** | **Use Case** | **Key Points** |
|---------------|---------------------|----------------------|--------------|----------------|
| **Breadth-First Search (BFS)** | O(V + E) | O(V) | Shortest path in unweighted graphs | Uses a queue; explores neighbors level by level. |
| **Depth-First Search (DFS)** | O(V + E) | O(V) | Pathfinding and cycle detection | Uses a stack (or recursion); explores as deep as possible. |
| **Dijkstra's Algorithm** | O(V²) / O(E + V log V) with min-heap | O(V) | Shortest path in weighted graphs | Greedy algorithm; doesn’t work with negative weights. |
| **Bellman-Ford Algorithm** | O(VE) | O(V) | Shortest path with negative weights | Handles negative weights; slower than Dijkstra's. |
| **Floyd-Warshall Algorithm** | O(V³) | O(V²) | All-pairs shortest paths | Dynamic programming; handles negative weights but not negative cycles. |
| **Kruskal's Algorithm** | O(E log E) | O(E + V) | Minimum Spanning Tree (MST) | Greedy; uses union-find data structure. |
| **Prim's Algorithm** | O(V²) / O(E + V log V) with min-heap | O(V) | Minimum Spanning Tree (MST) | Greedy; starts with a single vertex and grows the MST. |
| **A* Search Algorithm** | O(E) | O(E) | Pathfinding | Heuristic-based; combines elements of BFS and Dijkstra’s. |

---

### **Dynamic Programming Algorithms**

| **Algorithm** | **Time Complexity** | **Space Complexity** | **Use Case** | **Key Points** |
|---------------|---------------------|----------------------|--------------|----------------|
| **Fibonacci Sequence** | O(n) | O(n) | Calculating nth Fibonacci number | Simple memoization technique. |
| **Knapsack Problem** | O(nW) | O(nW) | Maximum value within weight capacity | Classic DP problem; can be optimized with space. |
| **Longest Common Subsequence (LCS)** | O(mn) | O(mn) | Finding longest subsequence common in two sequences | Used in DNA analysis, text diff tools. |
| **Longest Increasing Subsequence (LIS)** | O(n²) | O(n) | Finding the longest increasing subsequence | Can be optimized using binary search. |
| **Matrix Chain Multiplication** | O(n³) | O(n²) | Optimal way to parenthesize matrix multiplication | Used in computer graphics and dynamic systems. |
| **Edit Distance (Levenshtein Distance)** | O(mn) | O(mn) | Minimum number of edits to transform one string into another | Used in spell checkers and DNA sequence analysis. |
| **Subset Sum Problem** | O(nW) | O(nW) | Determines if there's a subset with sum equal to a given sum | Special case of the knapsack problem. |

---

### **Greedy Algorithms**

| **Algorithm** | **Time Complexity** | **Space Complexity** | **Use Case** | **Key Points** |
|---------------|---------------------|----------------------|--------------|----------------|
| **Huffman Coding** | O(n log n) | O(n) | Optimal prefix codes for data compression | Uses a priority queue; builds an optimal binary tree. |
| **Activity Selection** | O(n log n) | O(1) | Maximum number of non-overlapping activities | Sort activities by finish time; select the first that doesn’t overlap. |
| **Fractional Knapsack** | O(n log n) | O(1) | Maximize profit with fractional items allowed | Sort items by value/weight ratio; greedy selection. |
| **Job Sequencing Problem** | O(n²) | O(n) | Maximize profit with deadline constraints | Sort jobs by profit and schedule the highest-paying jobs first. |
| **Prim's MST Algorithm** | O(V²) | O(V) | Minimum spanning tree | Greedy; selects the minimum weight edge connected to the tree. |

---

### **Divide and Conquer Algorithms**

| **Algorithm** | **Time Complexity** | **Space Complexity** | **Use Case** | **Key Points** |
|---------------|---------------------|----------------------|--------------|----------------|
| **Merge Sort** | O(n log n) | O(n) | Efficient sorting | Divides array into halves; recursive sorting and merging. |
| **Quick Sort** | O(n log n) | O(log n) | Fastest average-case sorting | Chooses a pivot; partitions array around the pivot. |
| **Binary Search** | O(log n) | O(1) | Search in sorted array | Divides the search interval in half; recursive search. |
| **Strassen’s Algorithm** | O(n².81) | O(n²) | Matrix multiplication | Faster matrix multiplication than standard O(n³) methods. |
| **Closest Pair of Points** | O(n log n) | O(n) | Find closest pair of points in 2D space | Recursively divide points into subsets and combine results. |

---

### **Backtracking Algorithms**

| **Algorithm** | **Time Complexity** | **Space Complexity** | **Use Case** | **Key Points** |
|---------------|---------------------|----------------------|--------------|----------------|
| **N-Queens Problem** | O(N!) | O(N) | Placing N queens on an NxN chessboard | Recursive solution; place queens one by one and backtrack on conflict. |
| **Sudoku Solver** | O(9^(N*N)) | O(N*N) | Solving a Sudoku puzzle | Fill empty cells one by one; backtrack on invalid placements. |
| **Subset Sum** | O(2^n) | O(n) | Finding subsets that sum to a target value | Explore all subsets recursively; prune branches. |
| **Hamiltonian Cycle** | O(N!) | O(N) | Finding a Hamiltonian cycle in a graph | Backtrack to explore all possible paths; prune dead ends. |
| **Knight’s Tour Problem** | O(8^(N²)) | O(N²) | Finding a closed knight’s tour on a chessboard | Explore all moves recursively; backtrack on invalid paths. |

---

