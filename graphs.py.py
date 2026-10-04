


from ast import Return


=========================================================================================================================================>
=========================================================================================================================================>
==================================================================   GRAPHS   =======================================================================>
=========================================================================================================================================>
=========================================================================================================================================>
=========================================================================================================================================>
Traversal Techniques  : BFS AND DFS 


Input: V = 5, adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
Output:[0, 2, 4, 3, 1], [0, 2, 3, 1, 4]



Time Complexity: O(V + E)
 Each vertex is visited once → O(V) 
 Each edge is checked once → O(E) 

=> BFS of Graph — High-Level Workflow : 

1) Create a visited array of size V to track visited nodes. 
2) Create a result list to store the BFS traversal order. 
3) Start BFS from node 0 → add it to the queue and mark it as visited. 
4) While the queue is not empty, remove the front node. 
5) Add the removed node to result. 
6) Visit all its neighbors → if a neighbor is not visited, mark it visited and add it to the queue. 
7) Repeat until the queue becomes empty. 
Return result containing the BFS traversal.




DFS of Graph — High-Level Workflow
1) Create a visited array of size V to keep track of visited nodes. 
2) Create a result list to store the DFS traversal order. 
3) Create a stack and start DFS from node 0 → add 0 to the stack and mark it visited. 
4) While the stack is not empty, remove the last element using stack.pop(). 
5) Add the removed node to result. 
6) Check all neighbors of the current node. 
7)Push unvisited neighbors into the stack and mark them as visited. 
8) Use reversed(adj[node]) only if you want to control the visiting order (for example, to match recursive DFS order). 
9) Repeat until the stack is empty. 
10) Return result containing the DFS traversal.

=> Complexity : 
Time: O(V + E) 
Space: O(V) 

Where:
V = number of vertices 
E = number of edges 


class Solution:
    def dfsOfGraph(self, V, adj):
        visited = [False] * V
        result = []
        stack = []

        # Start DFS from node 0
        stack.append(0)
        visited[0] = True

        while stack:
            node = stack.pop() # it should remove the last element not the 1st element so dont use stack.pop(0) but not mandatory
            result.append(node)

            # Push neighbors in reverse order
            # so that smaller node is visited first (like in recursion)
            for neighbor in reversed(adj[node]):  #The reversed(adj[node]) part is not mandatory for DFS correctness. It’s used mainly for controlling the visiting order of neighbors so that the result matches the recursive DFS output.
                if not visited[neighbor]:
                    stack.append(neighbor)

        return result


    def bfsOfGraph(self, V, adj):
        visited = [False] * V
        result = []
        queue = []

        # Start BFS from node 0
        queue.append(0)
        visited[0] = True

        while queue:
            node = queue.pop(0)
            result.append(node)

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return result

-------------------------------->
note : list.pop() vs list.pop(0) difference  : 

🔹 list.pop()
By default, pop() removes and returns the last element (rightmost).
Works like a stack (LIFO: Last In, First Out).
Example:

x = numbers.pop()
print(x)        # 40
print(numbers)  # [10, 20, 30]

🔹 list.pop(0)

If you give an index, pop(index) removes and returns the element at that position.
pop(0) removes the first element (leftmost).
Works like a queue (FIFO: First In, First Out).

Example:
y = numbers.pop(0)
print(y)        # 10
print(numbers)  # [20, 30]

⚖️ Comparison
pop() → removes from end → stack behavior (DFS usually uses this).
pop(0) → removes from front → queue behavior (BFS usually uses this).
------------------------------------------------------------------------>


Step-by-step BFS traversal:

V = 5
adj = [
  [1, 2],   # Node 0 → 1,2
  [0, 3],   # Node 1 → 0,3
  [0, 4],   # Node 2 → 0,4
  [1],      # Node 3 → 1
  [2]       # Node 4 → 2
]


Initialization:
visited = [False, False, False, False, False]
result = []
queue = []

Step 1: Start from node 0
queue = [0]
visited = [True, False, False, False, False]

Step 2: Pop 0 from queue
result = [0]
Neighbors of 0: [1, 2]
1 not visited → mark visited, push to queue
2 not visited → mark visited, push to queue
queue = [1, 2]
visited = [True, True, True, False, False]

Step 3: Pop 1 from queue
result = [0, 1]
Neighbors of 1: [0, 3]
0 already visited → skip
3 not visited → mark visited, push to queue
queue = [2, 3]
visited = [True, True, True, True, False]


Step 4: Pop 2 from queue
result = [0, 1, 2]
Neighbors of 2: [0, 4]
0 already visited → skip
4 not visited → mark visited, push to queue
queue = [3, 4]
visited = [True, True, True, True, True]


Step 5: Pop 3 from queue
result = [0, 1, 2, 3]
Neighbors of 3: [1] → already visited
queue = [4]


Step 6: Pop 4 from queue
result = [0, 1, 2, 3, 4]
Neighbors of 4: [2] → already visited
queue = [] (empty)


✅ Final Output:
BFS traversal = [0, 1, 2, 3, 4]


===> DFS USING THE RECUSRIVE APPROACH : 


Complexity
Time: O(V + E) 
Space: O(V) 
Here, the O(V) space is mainly for the visited array + recursion call stack.
     
DFS Using Recursion — High-Level Workflow : 

1) Create a visited array of size V to track visited nodes. 
2) Create a result list to store the DFS traversal order. 
3) Start DFS from node 0 by calling dfs(0). 
4) Mark the current node as visited and add it to result. 
5) Check all neighbors of the current node. 
6) If a neighbor is not visited, recursively call dfs(neighbor). 
7) Recursion continues deeper until there are no unvisited neighbors. 
8) Backtrack to the previous node and continue checking its remaining neighbors. 
9) Return result after all reachable nodes have been visited.
class Solution:
    def dfsOfGraph(self, V, adj):
        visited = [False] * V
        result = []

        def dfs(node):
            visited[node] = True
            result.append(node)

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        # Run DFS starting from node 0
        dfs(0)
        return result 





