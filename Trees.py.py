representation of the Tree : 
1. Binary Tree Preorder Traversal :
Inorder traversal : 
Post Order Traversal :
102. Binary Tree Level Order Traversal : 
104. Maximum Depth or Height of Binary Tree : 
110. Balanced Binary Tree : 
543. Diameter of Binary Tree  : 1️⃣ Diameter of a Binary Tree (MAX DIAMETER)
100. Same Tree or check identical trees or not : 
101. Symmetric Tree : 



700. Search in a Binary Search Tree : 
701. Insert into a Binary Search Tree
finding the kth smallest value in the BST : 
finding the smallest element in the BST 
Print root to node path in BT : T.C ==> O(n) and S.C ==> O(H) ==> h meams the max height of the binary ==> root to any node in the tree
===============================================================================================================================>
representation of the Tree :
class TreeNode : 
    # def __init__(self , val = 0 ,r=10 left = None , right = None): # note these are of the optional params wheather we gave or not they take the deafult values or 
    # if we call the function then they will assign those values in the order from the left to right 
    def __init__(self , val = 0 , left = None , right = None):
        self.val = val 
        self.left = left
        self.right = right
        
root = TreeNode(1)  
root.left = TreeNode(2)  
root.right = TreeNode(3)  
root.left.left = TreeNode(4)  
root.left.right = TreeNode(5)  
root.left.left.left = TreeNode(6)  
root.left.right.right = TreeNode(7)  

print(f"root : {root}")
print(f"root.val :{root.val}")
print(f"root.left: {root.left}")
print(f"root.right : {root.right}")

output :
root : <__main__.TreeNode object at 0x7fb7863b9b50>
root.val :1
root.left: <__main__.TreeNode object at 0x7fb7863b9b80>
root.right : <__main__.TreeNode object at 0x7fb7863b9bb0>

================================================================================================================================================>

1. Binary Tree Preorder Traversal : 

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]
Explanation:

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [1,2,4,5,6,7,3,8,9]
Explanation:

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]
----------------------------------------------------------->
T.C ==> O(n)  : 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None : 
            return [] # to return at the breck or recursion stop condition at the particular depth 
        # return the resuls to the level by level upward till the root node     
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)  

===============================================================================================================================================================================>
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = []
        result.append(root.val)
        result.extend(self.preorderTraversal(root.left))
        result.extend(self.preorderTraversal(root.right))
        return result

===============================================================================================================================================================================>
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = [] # this is the global variable so no need to return the result in the every function call 
        def dfs(Node):
            if not Node :
                return None
            result.append(Node.val)
            dfs(Node.left)
            dfs(Node.right)  

        dfs(root) 
        return result     

===============================================================================================================================================================================>

Inorder traversal : 

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]
Explanation:

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,2,6,5,7,1,3,9,8]
Explanation:

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(Node):
            if not Node : 
                return 
            dfs(Node.left)
            result.append(Node.val)
            dfs(Node.right)
        dfs(root)
        return result 

===============================================================================================================================================================================>

Post Order Traversal : 

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]
Explanation:

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,6,7,5,2,9,8,3,1]
Explanation:

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(Node):
            if not Node : 
                return 
            dfs(Node.left)
            dfs(Node.right)
            result.append(Node.val)
        dfs(root)
        return result 
===============================================================================================================================================================================>
102. Binary Tree Level Order Traversal : 

Example 1 : 
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # to retunr the final answer 
        ans = []
        if not root : 
            return ans # return empty list of the tree is empty 
            
        q = deque([root]) # initilize the queue with root node i.e with it's address EX : q = [ 0x101 ]

        while q : # execute until queue becomes empty 
            level =[] # to store the each level items or elements 
            for _ in range(len(q)):
                node = q.popleft()  # 
                level.append(node.val)
                if node.left : 
                    q.append(node.left) # store left elelment to queue of current node 
                if node.right : 
                    q.append(node.right) # store right elelment to queue of current node 
            ans.append(level) # aopend also works like extend so now ans contains [[],[],......]
        return ans 
===============================================================================================================================================================================>    
        
from collections import deque

class Solution:
    # Function to perform level-order traversal of a binary tree
    def levelOrder(self, root):
        # Create a list to store levels
        ans = []
        if not root:
            # If the tree is empty, return an empty list
            return ans
        
        # Create a queue to store nodes for level-order traversal
        q = deque([root])
        
        while q:
            # Create a list to store nodes at the current level
            level = []
            for _ in range(len(q)):
                # Get the front node from the queue
                node = q.popleft()
                # Add the node value to the current level list
                level.append(node.data)
                
                # Enqueue the child nodes if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # Add the current level to the answer list
            ans.append(level)
        # Return the level-order traversal of the tree
        return ans



===============================================================================================================================================================================>
104. Maximum Depth or Height of Binary Tree : 
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
    
T.C ==> O(n)
S.C ==> O(n)     

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root : 
            return 0 # if the tree is empty then return height as 0 
        l = self.maxDepth(root.left)  # find the left sub Tree height 
        r = self.maxDepth(root.right)  # find the left sub Tree height 
        return 1 + max(l , r )    # 1 + max(left_sub_tree_height , right_sub_tree_height) 
    
    
    
⚠️ Common mistake to avoid
Some people think:
“It’s O(2ⁿ) because there are two recursive calls”

❌ WRONG
Because:
The calls split the tree
They do not overlap
Each node belongs to exactly one call

Space Complexity (bonus, interview extra 💡)
Auxiliary space = recursion stack
    
===> Final answer (say this confidently in interviews)
Time Complexity: O(N), because each node is visited once.
Space Complexity: O(H), where H is the height of the tree.

why space compleixyt is of O(h) here we using the 2 varbles only  : l , h so S.C is O(1) then why O(n) how it is correct  : 
    
    
==> O(1) × H = O(H) or O(1)+ O(1)+ O(1)+ O(1)+O(1)+ O(1)+ O(1)+ O(1) ===> both are same     

why T.C ==> On(n) : 
Recursion breakdown (simple)

For a tree like:

      1
     / \
    2   3
   /
  4

Function calls:

maxDepth(1)
 ├── maxDepth(2)
 │    ├── maxDepth(4)
 │    │    ├── maxDepth(None)
 │    │    └── maxDepth(None)
 │    └── maxDepth(None)
 └── maxDepth(3)
      ├── maxDepth(None)
      └── maxDepth(None)

Each node → one function call.

    
First: what is a stack frame? (plain English)

A stack frame is a box of memory created for one function call that stores everything that function needs while it is running.

Think of it as:
📦 “This function’s personal workspace.”

==> why it is not possble to use the same varbles instead of creating new varles forevery fucntion call is it only in python or else in all langues it will same 

It is NOT possible to reuse the same variables for recursive calls because each function call must remember its own state to return correctly
And this is true in ALL mainstream languages:

Python

Java

C

C++

JavaScript

Go
(not a Python-only thing)

understand height of the binary tree tracing we will understand why for each functoin call there indiduaval stack frames are requie  : 
    
if we use smae the values will be overwrited just trace and undertand it well     
    
==> in which case recursion becoms O(2^n) explain with a simple example code problem 
    
“When does recursion become O(2ⁿ)?”
Key rule 🔑  : 
Recursion becomes exponential when the same subproblem is solved repeatedly.

🔥 Simple example: Fibonacci (classic) 

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

Why is this O(2ⁿ)?
Call tree for fib(5):
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   └── fib(1)
│   └── fib(2)
└── fib(3)
    ├── fib(2)
    └── fib(1)


Notice:
fib(3) is computed twice
fib(2) is computed three times

👉 Massive repetition = exponential growth
Contrast with your tree problem    

===============================================================================================================================================================================>
110. Balanced Binary Tree : 
Given a binary tree, determine if it is height-balanced.


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

T.C ==> O(n)
S.C ==> O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfsHeight(root) != -1  # -1 != -1 ==> False other case 0 != -1 ==> True  

    def dfsHeight(self, root): # writting the helper function to find the sub tree heights     
        if not root : 
            return 0 
        lsh = self.dfsHeight(root.left) # find left sub tree height 
        if lsh == -1 : # check of lsh is -1 then return -1 
            return -1 
        rsh = self.dfsHeight(root.right) # find left sub tree height
        if rsh == -1 :  # check of rsh is -1 then return -1 
            return -1 
        if abs(lsh - rsh) > 1:  # check of lsh and rsh difference is > 1 then return -1 
            return -1 
        return 1 + max(lsh , rsh) # if the above conditions are not met then return the sub Tree height for the upper level nodes         

===============================================================================================================================================================================>
543. Diameter of Binary Tree  : 1️⃣ Diameter of a Binary Tree (MAX DIAMETER)
🔹 Meaning

The longest path between any two nodes in the tree
(The path does NOT have to pass through the root)

🔹 Measured in

Edges (most common)

or Nodes (depends on problem)

🔹 Visualization
        1
       / \
      2   3
     /
    4
   /
  5


👉 Longest path = 5 → 4 → 2 → 1 → 3



Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1

T.C ==> O(n)
S.C ==> O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) :
        self.diameter = 0 # initilize default diameter variable as 0 to to find the max diameter for comparison

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.cal_height(root) # call the helper function to find the max diameter 
        return self.diameter # return updated diameter val. 

    def cal_height(self , root): # writting the helper function to cal. the height of the sub tree
        if not root :
            return 0 
        lsh = self.cal_height(root.left) # finding the left sub Tree 
        rsh = self.cal_height(root.right) # finding the left sub Tree 
        self.diameter = max(self.diameter , lsh + rsh) # finding the max diameter 
        return 1 + max(lsh , rsh)   # returning each nodes height to upper nodes 

===============================================================================================================================================================================>
2️⃣ Maximum Width of a Binary Tree (MAX WIDTH)  : 
🔹 Meaning

Maximum number of nodes present at the same level

🔹 Visualization
        1          ← level 0 (1 node)
       / \
      2   3        ← level 1 (2 nodes) ← MAX WIDTH
     /     \
    4       5      ← level 2 (2 nodes)


👉 Maximum width = 2



✅ The correct statement (very important)

In Python, if you create an instance variable using self.variable in any method,
then that variable can be accessed in any other method of the same object
after it has been created.

So your understanding is YES — with one condition.

⚠️ The important condition (don’t miss this)

The variable must be created before it is used.

Example:

class A:
    def m1(self):
        self.x = 10   # instance variable created here

    def m2(self):
        print(self.x)

✅ Works if:
obj = A()
obj.m1()
obj.m2()   # prints 10

❌ Fails if:
obj = A()
obj.m2()   # AttributeError: x does not exist

but is not possble in java and c++ lanagues 

python allows dynamically for other languea we have to define/initalize in the constructor




124. Binary Tree Maximum Path Sum : 

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

T.C ==> O(n)
S.C ==> O(n)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float('-inf')  # to define as the instance varble for this functin and other functoins we are calling inside this function 
        self.max_path_sum_helper(root) # to get updated correct val for maxi 
        return self.maxi

# to find max path sum and to assign that answer to maxi varble 
    def max_path_sum_helper(self , root):
        if not root :
            return 0
        left_subtree_sum  = max(0 , self.max_path_sum_helper(root.left))  # we are using the 0 here to get only the positive sum only sometimes nodes may have -ve values   
        right_subtree_sum  = max(0, self.max_path_sum_helper(root.right)) # we are using the 0 here to get only the positive sum only sometimes nodes may have -ve values 
        self.maxi = max(self.maxi , left_subtree_sum + right_subtree_sum + root.val) # we are finding the max path sum ==> left subtree sum + right sub tree + current node value 
        return root.val + max(left_subtree_sum , right_subtree_sum ) # returning only current node val + max of both sub tree values to parent node becaz from parent node we can go to only one subtree (and for this problem that sub tree must have max sum value ) 

===============================================================================================================================================================================>
100. Same Tree or check identical trees or not : 

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true


Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false


Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

T.C ==> O(n)
S.C ==> O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p == None or q == None):
            return p == q    
        return (p.val == q.val) and self.isSameTree(p.left , q.left) and self.isSameTree(p.right , q.right) 
        


===============================================================================================================================================================================>
101. Symmetric Tree : 
    
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false    

T.C ==> O(n)
S.C ==> O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # if the root is None if not call the helper function to getthe final result 
        return root == None or self.isSymmetricHelper(root.left , root.right)
    # call the helper function to getthe final result weather symmetric or not  
    def isSymmetricHelper(self , left , right):
        if left == None or right == None : # if either one of the node is None other right node also must be None 
            return left == right 
        if left.val != right.val : # check the left node val and right val same or not 
            return False
        return self.isSymmetricHelper(left.left , right.right) and self.isSymmetricHelper(left.right , right.left) # calling recursilvely checking opposite nodes of the sub Trees      
         





===============================================================================================================================================================================>
700. Search in a Binary Search Tree : 

You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
If such a node does not exist, return null.

T.C ==> O(n)
S.C ==> O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while(root != None and root.val != val) : # execute the loop until root becomes None or the value is matched 
            root =  root.left if val < root.val  else root.right # please traverse the sub Tree dynamically based on the current root node val  
        return root # if the root node is matched then return that node otherwise return None 
        

===============================================================================================================================================================================>


701. Insert into a Binary Search Tree
Solved
Medium
Topics
premium lock icon
Companies
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

T.C ==> O(log n)
S.C ==> O(1)
 
Example 1:
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None : # if not root : 
            return TreeNode(val)
        current = root    
        while(True):
            if current.val <= val : 
                if current.right != None : 
                    current = current.right
                else :
                    current.right = TreeNode(val)
                    break 
            else : 
                if current.left != None :
                    current = current.left
                else : 
                    current.left = TreeNode(val)
                    break 
        return root                        





===============================================================================================================================================================================>
finding the kth smallest value in the BST : 

T.C ==> O(n) 
S.C ==> O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.values = []
        self.inorder_traversal(root)
        return self.values[k-1] # returning the kth smallest elemeeent => for kth largest element self.values[-k]
        
    def inorder_traversal(self , root):
        if not root : 
            return -1 
        self.inorder_traversal(root.left)
        self.values.append(root.val)
        self.inorder_traversal(root.right)



===> finding the smallest value in the BST : 

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.values = []
        self.inorder_traversal(root)
        return self.values[0] # returning the kth smallest element ==> for largest element values[-1]

    def inorder_traversal(self , root):
        if not root : 
            return -1 
        self.inorder_traversal(root.left)
        self.values.append(root.val)
        self.inorder_traversal(root.right)
===============================================================================================================================================================================>
Print root to node path in BT : T.C ==> O(n) and S.C ==> O(H) ==> h meams the max height of the binary ==> root to any node in the tree



# TreeNode class for Binary Tree
class TreeNode:
    def __init__(self, val):
        # Initialize node with value
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # Function to find the path from root to a given node
    def getPath(self, root, arr, x):
        # Base case: If root is None
        if root is None:
            return False

        # Add current node to path
        arr.append(root.val)

        # If current node is the target
        if root.val == x:
            return True

        # Recurse on left and right
        if self.getPath(root.left, arr, x) or self.getPath(root.right, arr, x):
            return True

        # Backtrack if not found
        arr.pop()
        return False

    # Function to return the final path list
    def solve(self, root, x):
        # Initialize result path
        arr = []

        # If tree is empty
        if root is None:
            return arr

        # Get path using helper
        self.getPath(root, arr, x)
        return arr


===============================================================================================================================================================================>










===============================================================================================================================================================================>




===============================================================================================================================================================================>












===============================================================================================================================================================================>





===============================================================================================================================================================================>
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root :
            return True
        if  root.left :    
            if root.val < root.left.val : 
                return False
        # if root.val > root.left.val : 
        #     return True 
        if root.right :    
            if root .val > root.right.val : 
                return False
        # if root .val < root.right.val : 
        #     return True    
        return  self.isValidBST(root.left) and self.isValidBST(root.right)     
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def helper(node, low, high):
#             if not node:
#                 return True
            
#             if not (low < node.val < high):
#                 return False
            
#             return (
#                 helper(node.left, low, node.val) and
#                 helper(node.right, node.val, high)
#             )
        
#         return helper(root, float('-inf'), float('inf'))




        # above commented code is working fine 




===============================================================================================================================================================================>

Representation of the graph using the Adjacency Matrix in the python : 

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        # Create a vertices x vertices matrix initialized with 0
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v):
        # For an undirected graph
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
        # removing an edge in the undirected graph 
    def remove_edge(self ,u,v) :
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0

    def display(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(row)
            
g = Graph(5)    
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(1,1)

g.display()

output : 

Adjacency Matrix:
[0, 1, 0, 0, 0]
[1, 1, 1, 0, 0]
[0, 1, 0, 1, 0]
[0, 0, 1, 0, 1]
[0, 0, 0, 1, 0]

===============================================================================================================================================================================>
Representation of the graph using the Adjacency List in the python : 

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        # Create a vertices x vertices matrix initialized with 0
        self.adj_list = {i:[] for i in range(vertices)}
        
    def add_edge(self, u, v):
        # For an undirected graph
        if v not in self.adj_list[u]: # to avoid the duplciate insertions for the both self loop and other node edges
            self.adj_list[u].append(v)
        if u != v and u not in self.adj_list[v]:
            self.adj_list[v].append(u)
            
        # removing an edge in the undirected graph 
    def remove_edge(self ,u,v) :
        if v in self.adj_list[u]:
            self.adj_list[u].remove(v)
        if u != v and u in self.adj_list[v]:
            self.adj_list[v].remove(u)

    def display(self):
        print("Adjacency List:")
        for key in self.adj_list: # eather we use the .keys() or we can directly the take the key value using the for loop in python
            print(f"{key} => {self.adj_list[key]}")
            
g = Graph(5)    
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(1,1)

g.display()


outupt :
Adjacency List:
0 => [1]
1 => [0, 2, 1]
2 => [1, 3]
3 => [2, 4]
4 => [3]
===============================================================================================================================================================================>

Python does not have a built-in stack() function, but stacks can be implemented using lists,
collections. deque , or queue. LifoQueue . These implementations provide the necessary 
stack functionalities such as push , pop and peek 


# STACK implementation using list
stack = []

# PUSH elements
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(20)
print("Stack after pushes:", stack)

# POP element
popped = stack.pop()
print("Popped element:", popped)
print("Stack after pop:", stack)

# PEEK (top element)
print("Top element:", stack[-1])

# SIZE
print("Stack size:", len(stack))

# COUNT
print("Count of 20:", stack.count(20))

# INDEX
print("Index of 20:", stack.index(20))

# MEMBERSHIP
print("Is 10 in stack?", 10 in stack)

# COPY
stack_copy = stack.copy()
print("Copied stack:", stack_copy)

# TRAVERSAL using for loop
print("Traversing stack:")
for item in stack:
    print(item)
    
# checking stack is empty or not : 
if not stack : # if len(stack) == 0 :
    print(f"### stack is empty")



# CLEAR stack
stack.clear()
print("Stack after clear:", stack)

output :
Stack after pushes: [10, 20, 30, 20]
Popped element: 20
Stack after pop: [10, 20, 30]
Top element: 30
Stack size: 3
Count of 20: 1
Index of 20: 1
Is 10 in stack? True
Copied stack: [10, 20, 30]
Traversing stack:
10
20
30
Stack after clear: [] 


===============================================================================================================================================================================>
# intialize
# append
# access
# peek/top remove or pop
# 1st item remove 
# lenght of the data structure
# count 
# how to find is it empty or not 
# how to use for loop over it 
# how to clear it means removing all the elelemnts from it  
# how to rotate it 

from collections import deque

# creating a queue
# queue = deque([1,2,3,4,5])
queue = deque() 

# appending or ENQUEUE elemlenet into the queue 
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.append(100)
print("Queue ==> ",queue)


# how to remove or dequeue the elements from the queue..
removed = queue.popleft()
print("removed element : ",removed)
print(f"after Dequeue queue is :{queue}")

#  ADD element at FRONT
queue.appendleft(100)
print(f"after the append_left queue : {queue}")

# REMOVE from REAR
removed =queue.pop()
print(f"### poped elelent :{removed}")
print(f"after pop queue is : {queue}")


# SIZE
print(f"size or length of the queue is :{len(queue)}")

# count => to count no of occurrrences of an element in the queue 
print(f"### count element 100 is :{queue.count(100)}")

# Rotate ==> rotate() rotates the deque to the RIGHT by n steps
queue.rotate(1)
print(f"after the 1 step rotation queue is : {queue}")


# queue traversal using a loop : 
for item in queue :
    print(item)
    
    
# accessing an elememnt from queue : 
print(f"accessing the 1st element from the queue :{queue[0]}")


# getting peel or top elememt frmo the queue 
print(f"peek or top item in the queue : {queue[-1]}")


# clearing or deleting all items in the queue 
queue.clear()
print(f"### after clear queue is :{queue}")


# how to check queue is empty or not 
if not queue: # or if len(queue) ==0 : 
    print("Queue is empty")
    
output :
Queue ==>  deque([1, 2, 3, 4, 5, 100])
removed element :  1
after Dequeue queue is :deque([2, 3, 4, 5, 100])
after the append_left queue : deque([100, 2, 3, 4, 5, 100])
### poped elelent :100
after pop queue is : deque([100, 2, 3, 4, 5])
size or length of the queue is :5
### count element 100 is :1
after the 1 step rotation queue is : deque([5, 100, 2, 3, 4])
5
100
2
3
4
accessing the 1st element from the queue :5
peek or top item in the queue : 4
### after clear queue is :deque([])
Queue is empty
    
===============================================================================================================================================================================>    