contents : 
1) Length of loop in LL 
2) Reverse Linked List or Reverse the linked list 
3) Sort a LL of 0's 1's and 2's  
4) Delete Node in a Linked List 
5) Middle of the Linked List 
6) 148. Sort List  :  
7) 2. Add Two Numbers 
8) 160. Intersection of Two Linked Lists  :  
9) 141. Linked List Cycle - i : to delete a cycle in the given ll 
10) Remove Nth Node From End of List : 
11) Delete the Middle Node of a Linked List
12) Linked List Cycle II : 
13) 234. Palindrome Linked List 
14) Odd Even Linked List 
15) 


===> Add one to a number represented by LL  : 

Input: head -> 1 -> 2 -> 3
Output: head -> 1 -> 2 -> 4
Explanation: The number represented by the linked list = 123.
123 + 1 = 124.

Input: head -> 9 -> 9
Output: head -> 1 -> 0 -> 0
Explanation: The number represented by the linked list = 99.
99 + 1 = 100.

=====> T.C ==> O(n) 
------------------------------------------------>
===> steps  : 
Step 1: Reverse the linked list
Step 2: Add 1 to the number
If carry still remains, add a new node
        if carry:
            prev.next = ListNode(carry)

Step 3: Reverse back to original order
------------------------------------------------>

# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addOne(self, head):
        # Helper: Reverse the linked list
        def reverse(node):
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev
        
        # Step 1: Reverse the linked list
        head = reverse(head)

        # Step 2: Add 1 to the number
        carry = 1
        curr = head
        prev = None
        while curr and carry:
            curr.val += carry
            carry = curr.val // 10
            curr.val %= 10
            prev = curr
            curr = curr.next

        # If carry still remains, add a new node
        if carry:
            prev.next = ListNode(carry)

        # Step 3: Reverse back to original order
        return reverse(head)



note : in the above code we are no changing the node addresses we are just changing/assigning new address to the head pointer 
and each nodes next address is chaning  in the above code 

Proof with 1 -> 2 -> 3 example
 
Original in memory:

head → [1 | next → addr2]
addr2 → [2 | next → addr3]
addr3 → [3 | next → None]
 
After reverse(head):

head → [3 | next → addr2]
addr2 → [2 | next → addr1]
addr1 → [1 | next → None]
 
The nodes are the same (addresses of nodes don’t change),
but the next pointers inside them are modified.
So, the chain is reversed in-place. 



----------------------------------------------------------->
example tracing for ex :1  :

===> Initial State   :

node = 1 -> 2 -> 3 -> None
prev = None
    
While Loop Iteration 1  :

nxt = node.next      # nxt = 2 -> 3 -> None
node.next = prev     # 1 -> None   (link reversed)
prev = node          # prev = 1 -> None
node = nxt           # node = 2 -> 3 -> None
Now the list is partially reversed:

Reversed part: 1 -> None
Remaining part: 2 -> 3 -> None

While Loop Iteration 2  : 

nxt = node.next      # nxt = 3 -> None
node.next = prev     # 2 -> 1 -> None
prev = node          # prev = 2 -> 1 -> None
node = nxt           # node = 3 -> None

Reversed so far:

2 -> 1 -> None
Remaining: 3 -> None


While Loop Iteration 3  :

nxt = node.next      # nxt = None
node.next = prev     # 3 -> 2 -> 1 -> None
prev = node          # prev = 3 -> 2 -> 1 -> None
node = nxt           # node = None

Reversed so far:
3 -> 2 -> 1 -> None
Remaining: None
Loop Ends
node is now None, so:

return prev
prev is:
3 -> 2 -> 1 -> None 

----------------------------------------------------------->
Alright ✅
Let’s trace only the reverse(node) function from your code using the example:

Example Input before reverse:

head → 9 → 9 → None

Initial State

node = 9 → 9 → None
prev = None


====> Iteration 1  :

nxt = node.next      # nxt = 9 → None
node.next = prev     # 9 → None   (link reversed)
prev = node          # prev = 9 → None
node = nxt           # node = 9 → None


===> Iteration 2  :

nxt = node.next      # nxt = None
node.next = prev     # 9 → 9 → None
prev = node          # prev = 9 → 9 → None
node = nxt           # node = None
Loop Ends

return prev          # returns 9 → 9 → None (reversed list)
=========================================================================================================================================>
==> Sort a LL of 0's 1's and 2's  : 

Given the head of a singly linked list consisting of only 0, 1 or 2. Sort the given linked list and return the head of the modified list.
Do it in-place by changing the links between the nodes without creating new nodes.


Examples:
Input: head -> 1 -> 0 -> 2 -> 0 -> 1
Output: head -> 0 -> 0 -> 1 -> 1 -> 2
Explanation: The values after sorting are [0, 0, 1, 1, 2].

Input: head -> 1 -> 1 -> 1 -> 0
Output: head -> 0 -> 1 -> 1 -> 1
Explanation: The values after sorting are [0, 1, 1, 1].

steps  : 
Step 1: Count the occurrences of 0, 1, 2
Step 2: Overwrite values in sorted order based index value (i)  

T.C ==> O(n) 

# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head):
        # Step 1: Count the occurrences of 0, 1, 2
        count = [0, 0, 0]
        curr = head
        while curr:
            count[curr.val] += 1
            curr = curr.next

        # Step 2: Overwrite values in sorted order
        curr = head
        i = 0
        while curr:
            if count[i] == 0:
                i += 1
            else:
                curr.val = i
                count[i] -= 1
                curr = curr.next

        return head


====> tracing step-2 : very easy 
 
# Step 2: Overwrite values in sorted order
curr = head    # Start from the head of the linked list
i = 0          # Start filling from smallest value (0)

while curr:
    if count[i] == 0:
        # No more nodes left for this value 'i', move to next value
        i += 1
    else:
        # Assign current node the value 'i'
        curr.val = i
        # Decrease the count for value 'i' (one occurrence used)
        count[i] -= 1
        # Move to the next node in the list
        curr = curr.next

return head


=========================================================================================================================================>
===> Length of loop in LL  : 

using floyds cycle detection algorithm  : 
the node at which slow == fast at that node the loop is starting from that node  note : slow means one step moving fast means 2 steps moving

Given the head of a singly linked list, find the length of the loop in the linked list if it exists.
Return the length of the loop if it exists; otherwise, return 0.

A loop exists in a linked list if some node in the list can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index (0-based) of the node from where the loop starts.

Note that pos is not passed as a parameter.
Input: head -> 1 -> 2 -> 3 -> 4 -> 5, pos = 1
Output: 4
Explanation: 2 -> 3 -> 4 -> 5 - >2, length of loop = 4.

Input: head -> 1 -> 3 -> 7 -> 4, pos = -1
Output: 0
Explanation: No loop is present in the linked list.


==> T.C  ===> O(n) :
Step-by-step breakdown
for outer while loop  : 
1) Loop detection (while fast and fast.next:)
Slow moves 1 step each iteration, Fast moves 2 steps.
If there’s no loop → they traverse the list at most n steps → O(n).
If there is a loop → they will meet within n steps (Floyd’s Cycle Detection property).
                                                    
for inner while loop : 
2) Loop length counting (while fast != slow:)
Once they meet, you loop around the cycle exactly once to count its length.
This takes at most k steps, where k = loop length.
Since k ≤ n, this is also O(n).to travers  
 
# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findLengthOfLoop(self, head):
        # Step 1: Detect if a loop exists using slow & fast pointers
        slow = fast = head
        while fast and fast.next: # while fast.next: we should use this condition  
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # Loop detected
                # Step 2: Find length of the loop
                length = 1
                fast = fast.next # writting outside of while loop becaz some times self loop will be there for a single node 
                while fast != slow:
                    fast = fast.next
                    length += 1
                return length
        return 0  # No loop

===>  note :   while fast.next: we should use this condition    :
while fast = None : loop will terminated 
while fast = None and fast.next.next will be causes attribute error 
*** if we use both conditions i.e while fast and fast.next: while compiler check if fast =  None loop will be cloased becaz here and used

=========================================================================================================================================>
237. Delete Node in a Linked List  : 

Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Example 2:
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val 
        node.next = node.next.next        


====> deleting node speacial cases  : 

# Definition for singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 1️⃣ Delete first node
    def deleteFirst(self, head):
        if not head:  # Empty list
            return None
        return head.next  # Just move head to next
        # head = head.next
        # return head 

    # 2️⃣ Delete node with given target value
    def deleteTarget(self, head, target):
        if not head:
            return None
        if head.val == target:  # Target is first node
            return head.next

        curr = head
        while curr.next:
            if curr.next.val == target:
                curr.next = curr.next.next  # Skip target node
                break
            curr = curr.next
        return head

    # 3️⃣ Delete last node
    def deleteLast(self, head):
        if not head:  # Empty list
            return None
        if not head.next:  # Only one node
            return None

        curr = head
        while curr.next.next:  # Stop at second last node
            curr = curr.next
        curr.next = None
        return head


=========================================================================================================================================>
876. Middle of the Linked List : 

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
 
Example 2 :
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head 
        while fast and fast.next : 
            slow = slow.next 
            fast = fast.next.next 
        return slow    


=========================================================================================================================================>
==> 206. Reverse Linked List  :
Given the head of a singly linked list, reverse the list, and return the reversed list. 

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None 
        while node : 
            nxt = node.next
            node.next= prev
            prev = node
            node = nxt 
        return prev 


=========================================================================================================================================>
===>  148. Sort List  : 
Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []

===> using the merge sort and linked list logic : 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty or single node
        if not head or not head.next:
            return head
        
        # 1️⃣ Split list into two halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None  # Break the list

        # 2️⃣ Sort each half
        left = self.sortList(head)
        right = self.sortList(mid)

        # 3️⃣ Merge sorted halves
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        # Append remaining
        curr.next = l1 or l2
        return dummy.next

or 


148. Sort List   : 


T.C ===> O(n logn)  for using the merge sort 

==> steps :
Step 1: Store all values in a list 
Step 2: Sort the list 
Step 3: Reassign sorted values back to the linked list

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # Step 1: Store all values in a list
        vals = [] 
        curr = head 
        while curr : 
            vals.append(curr.val)
            curr = curr.next

        # Step 2: Sort the list   
        # vals.sort() 
        # but here we are using bubble sort to improve the logical skills 
        for i in range(len(vals)):
            for j in range(len(vals)-1) : 
                if  vals[j] > vals[j+1]:
                    vals[j] , vals[j+1] = vals[j+1] , vals[j]

        # Step 3: Reassign sorted values back to the linked list
        curr = head
        for val in vals :  
            curr.val = val
            curr= curr.next 
        return head     

==============================================================>

===> without linked list logic i.e using the array logic : 
T.C ===>O(nlogn)

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        # 1️⃣ Extract values from linked list into array
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        # 2️⃣ Sort the array
        arr.sort()
        
        # 3️⃣ Rebuild linked list from sorted values
        curr = head
        for val in arr:
            curr.val = val
            curr = curr.next
        
        return head


=========================================================================================================================================>
====>  2. Add Two Numbers   : 

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

T.C ==> O(n) 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()   # Dummy head to simplify list creation
        curr = dummy         # Pointer to build result list
        carry = 0            # For sum carry

        while l1 or l2 or carry:
            # Get values from nodes (0 if no node)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Sum + carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # Create new node
            curr.next = ListNode(digit)
            curr = curr.next

            # Move to next nodes
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next


===> best Example trace to understand the above problem completey.....  : 

Example 3  : 

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
Step-by-step trace

Step 1: total = 9 + 9 + 0 = 18 → digit=8 carry=1 → list=[8]
Step 2: total = 9 + 9 + 1 = 19 → digit=9 carry=1 → list=[8,9]
Step 3: total = 9 + 9 + 1 = 19 → digit=9 carry=1 → list=[8,9,9]
Step 4: total = 9 + 9 + 1 = 19 → digit=9 carry=1 → list=[8,9,9,9]
Step 5: total = 9 + 0 + 1 = 10 → digit=0 carry=1 → list=[8,9,9,9,0]
Step 6: total = 9 + 0 + 1 = 10 → digit=0 carry=1 → list=[8,9,9,9,0,0]
Step 7: total = 9 + 0 + 1 = 10 → digit=0 carry=1 → list=[8,9,9,9,0,0,0]
Step 8: total = 0 + 0 + 1 = 1  → digit=1 carry=0 → list=[8,9,9,9,0,0,0,1]
✅ Final output: [8,9,9,9,0,0,0,1]

------------------------------------------------------------------------------->

For l1 = [2,4,3] and l2 = [5,6,4]:

Step 1: total = 2+5+0 = 7 → digit=7 carry=0 → list=[7]
Step 2: total = 4+6+0 = 10 → digit=0 carry=1 → list=[7,0]
Step 3: total = 3+4+1 = 8 → digit=8 carry=0 → list=[7,0,8]
✅ Final output: [7,0,8]


=========================================================================================================================================>
===> 160. Intersection of Two Linked Lists  : 

Example 1:
Input: listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]
Output: Intersected at '8'

Example 2:
Input: listA = [1,9,1,2,4], listB = [3,2,4]
Output: Intersected at '2'


Example 3:
Input:  listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection

listA = [2,6,4], listB = [1,5]
Output: No intersection

==> T.C ==> O(n) : 
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        p1, p2 = headA, headB
        
        # Traverse both lists; when one pointer reaches the end, jump to the other list
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        
        return p1  # Will be None if no intersection

------------------------------------------------>
===> Example Input  tracing  : 

ListA: 4 → 1 → 8 → 4 → 5
ListB: 5 → 6 → 1 → 8 → 4 → 5
Intersection starts at value = 8
Linked structure for tracing
We’ll assume the node with value 8 is the same object in memory for both lists.

Step-by-Step Table Tracing
Step	p1 position (ListA)	p2 position (ListB)	Are they equal?	Action taken
0	4	5	❌ No	Move both to next nodes
1	1	6	❌ No	Move both
2	8	1	❌ No	Move both
3	4	8	❌ No	Move both
4	5	4	❌ No	Move both
5	None (end of A)	5	❌ No	p1 jumps to headB, p2 moves next
6	5	None (end of B)	❌ No	p1 moves next, p2 jumps to headA
7	6	4	❌ No	Move both
8	1	1	❌ No (different nodes with same value)	Move both
9	8	8	✅ Yes (same node)	Stop loop

Final output: Node with value 8
------------------------------------------------>
===> Example input tracing  : 
Example 3:
Input:  listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection

tracing: 

p1: 2, 6, 4, 1, 5, None, 6, 4, None  
p2: 1, 5, None, 2, 6, 4, None, 1, 5, None
------------------------------------------------>

note : Ah — I see where the confusion is.

When both p1 and p2 point to 5 at some point, that does not mean 5 is the intersection node here.
The intersection is determined by reference in memory, not by the value inside the node
=========================================================================================================================================>
===> 141. Linked List Cycle - i : 

Given head, the head of a linked list, determine if the linked list has a cycle in it.
Return true if there is a cycle in the linked list. Otherwise, return false.
                                                             
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
                                                             
Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
                                                             
Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

===> T.C : O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head 

        while fast and fast.next : 
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast : 
                return True 
        return False        
        
=========================================================================================================================================>


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head 
        while fast and fast.next :
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast : # loop is there but not there is not guarantee slow or fast is the starting node of the loop  
                break 
        else :         
            return None  

        slow = head 
        while slow != fast : 
            slow = slow.next 
            fast= fast.next 

        return slow     

------------------------------------------->
2️⃣ Why I use break  : 
Using break lets us stop only the while loop for Phase 1 (cycle detection),
then start Phase 2 to find the real starting point:

Phase 2 logic after break:
Reset slow to head
Move slow and fast one step at a time until they meet
That meeting point is cycle start


===> best example to trace the above problem is  : 

Example  :

head = [1, 2, 3, 4]
pos = 1  (means: tail connects back to node 2)
Linked list shape:

1 → 2 → 3 → 4
    ↑       ↓
    ← ← ← ←
Cycle start = node 2.

Phase 1: Detect cycle
We use slow (1 step) and fast (2 steps):

Step	slow	fast
1	2	3
2	3	2
3	4	4 ✅ (meet)

We found a meeting point at node 4 → we break.

Phase 2: Find cycle start  :
Reset slow to head (node 1)
Keep fast at meeting point (node 4)
Move both 1 step at a time until they meet:

Step	slow	fast
1	2	2 ✅

They meet at node 2 → start of cycle.

Key Idea to Remember
Phase 1: Detect if a cycle exists (meeting point inside loop).
Phase 2: Reset one pointer to head, move both 1 step → first meeting = cycle start.
=========================================================================================================================================>

19. Remove Nth Node From End of List : 

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1] 

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      
        dummy = ListNode(0,head)
        first = second = dummy 

        for _ in range(n+1):
            first = first.next 

        while first :
            first = first.next 
            second = second.next 

        second.next = second.next.next
        return dummy.next          

        
=========================================================================================================================================>
2095. Delete the Middle Node of a Linked List : 

Example 1:
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 

Example 2:
Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.

Example 3:
Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next : # head.next == None   # if one element is there in linked list 
            return None 
        else : 
            slow , fast = head , head.next.next 
            while fast and fast.next : 
                fast = fast.next.next
                slow = slow.next 
            slow.next = slow.next.next
        return head 


=====> TRACING : 
Example 1
Input: [1, 3, 4, 7, 1, 2, 6]
(7 nodes total, middle = index 3 → value 7)

Steps:
Initialization
slow = head (1)
fast = head.next.next = 4

Iteration 1:
fast = 4 → 2 steps → 1
slow = 1 → 3

Iteration 2:
fast = 1 → 2 steps → 6
slow = 3 → 4

Iteration 3:
fast = 6 → 2 steps → None (loop ends)
slow = 4

Delete middle
slow.next = slow.next.next
→ slow = 4, so it skips 7

Final List: [1, 3, 4, 1, 2, 6] ✅ (Correct)

====> Example 2   : 
Input: [1, 2, 3, 4]
(4 nodes, middle = index 2 → value 2nd middle → 2 or 3?)

👉 Problem definition (LeetCode 2095): For even length, remove the second middle.
So here middle = 3.

Steps:
Initialization

slow = head (1)
fast = head.next.next = 3

Loop  : 

Iteration 1:
fast = 3 → 2 steps → None (loop ends)
slow = 1

Delete middle
slow.next = slow.next.next
→ slow = 1, so it skips 2

Final List: [1, 3, 4] ❌ (But expected [1, 2, 4])
=========================================================================================================================================>
142. Linked List Cycle II : 

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
 
Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
 
Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

===> Correct Steps for Detecting and Finding Start of Cycle

Initialize two pointers: slow and fast, both at the head.
Move slow by 1 step and fast by 2 steps in each iteration.
If fast becomes null (or fast.next is null) → No loop exists.
If slow == fast at some point → Loop exists.
To find the starting node of the cycle:
Move slow back to the head.
Now move both slow and fast 1 step at a time.
The node where they meet again is the start of the loop (where tail connects).


===> T.C ==>O(n) :                                                          
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head 
        while fast and fast.next :
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast : # loop is there but not there is not guarantee slow or fast is the starting node of the loop  
                break 
        else :         
            return None  

        slow = head 
        while slow != fast : 
            slow = slow.next 
            fast= fast.next 

        return slow 

=========================================================================================================================================>
==> 234. Palindrome Linked List   : 

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

===> steps to complete this problem :
1️⃣ Find middle (slow will be at middle)
2️⃣ Reverse second half
3️⃣ Compare first half & reversed second half 

==> T.C ==> O(n) 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1️⃣ Find middle (slow will be at middle)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2️⃣ Reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        # 3️⃣ Compare first half & reversed second half 
        left, right = head, prev # head means it contains all nodes in the ll so right node will ends 1st 
        while right:  # only need to check second half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True

==> Example tracing in both cases : 

🟢 Case 1: Even nodes (4 nodes)
List: 1 → 2 → 2 → 1

Step 1️⃣ Find middle
slow = head, fast = head
Move until fast reaches end:
Iteration 1: slow = 2, fast = 2
Iteration 2: slow = 2 (3rd node), fast = None
So slow ends at 3rd node (the first node of the second half).

Step 2️⃣ Reverse second half (slow onward)
Reverse 2 → 1 → becomes 1 → 2
prev = 1 (new head of reversed half)

Step 3️⃣ Compare
left = head (1), right = prev (1)
Compare 1 == 1 ✅
Compare 2 == 2 ✅
right ends → done.
✔ Palindrome confirmed. No node is skipped.


🔵 Case 2: Odd nodes (5 nodes)

List: 1 → 2 → 3 → 2 → 1

Step 1️⃣ Find middle
Iteration 1: slow = 2, fast = 3
Iteration 2: slow = 3, fast = 1 (last)
So slow ends at middle node (3).

Step 2️⃣ Reverse second half (slow onward)
Reverse 3 → 2 → 1 → becomes 1 → 2 → 3
prev = 1 (new head of reversed half)
But notice: because slow started at the middle, the 3 also gets included in the reversed half.
So, second half has ⌈n/2⌉ nodes (3 nodes), not just ⌊n/2⌋.

Step 3️⃣ Compare
left = head (1), right = 1 → match ✅
left = 2, right = 2 → match ✅
left = 3, right = 3 → match ✅
Done.
✔ Palindrome confirmed. Middle element (3) doesn’t cause a mismatch because it compares to itself.
=========================================================================================================================================>
328. Odd Even Linked List   : 

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

T.C ==> O(n) 

steps : 
1) take odd and even pointers 
2) make odd and even linked lists seperately when ever they reached null then attch odd linked list to the start of the even linked list 
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next : 
            return head 
        odd = head
        even = even_head = head.next 
        while even and even.next :
            odd.next = odd.next.next 
            odd = odd.next 

            even.next = even.next.next
            even = even.next 
        odd.next = even_head 
        return head     
=========================================================================================================================================>
