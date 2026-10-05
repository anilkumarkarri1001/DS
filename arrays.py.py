📚 Striver A2Z — Arrays
🟢 Easy — 14 Problems
#	Problem
1	Largest Element in an Array
2	Second Largest Element in an Array
3	Check if the Array is Sorted
4	Remove Duplicates from Sorted Array
5	Left Rotate Array by One Place
6	Left Rotate Array by D Places
7	Move Zeros (to End)
8	Linear Search
9	Find the Union of Two Sorted Arrays
10	Find Missing Number in an Array
11	Maximum Consecutive Ones
12	Find the Number That Appears Once
13	Longest Subarray with Sum K — Positive
14	Longest Subarray with Sum K — Positive + Negative

Easy = 14

🟡 Medium — 14 Problems
#	Problem
15	2 Sum
16	Sort an Array of 0s, 1s and 2s
17	Majority Element (> N/2)
18	Kadane's Algorithm — Maximum Subarray Sum
19	Print Subarray with Maximum Sum or Kadane's Algorithm — Maximum Subarray Sum both are same 
20	Stock Buy and Sell
21	Rearrange Array Elements by Sign
22	Next Permutation
23	Leaders in an Array
24	Longest Consecutive Sequence
25	Set Matrix Zeroes
26	Rotate Matrix by 90 Degrees
27	Print Matrix in Spiral Manner
28	Count Subarrays with Sum K

Medium = 14

🔴 Hard — 12 Problems
#	Problem
29	Pascal's Triangle
30	Majority Element II (> N/3)
31	3 Sum
32	4 Sum
33	Largest Subarray with Sum 0
34	Count Subarrays with XOR K
35	Merge Overlapping Intervals
36	Merge Two Sorted Arrays Without Extra Space
37	Find Repeating and Missing Number
38	Count Inversions
39	Reverse Pairs
40	Maximum Product Subarray

Hard = 12

📊 Final Count
Difficulty	Count
🟢 Easy	14
🟡 Medium	14
🔴 Hard	12
TOTAL	40








1) Largest Element in an Array

class Solution:
    def largest(self, arr):
        # code here
        # return max(arr)  or 

        m1 = arr[0]
        n = len(arr)
        for i in range(1,n):
            if arr[i] > m1 :
                max = arr[i] 
        return max         
        
-------------------------------------------------------------------------->
2) Second Largest Element in an Array : 

TCS NQT problem ==> 

Problem: Given an array, find the second largest element without sorting.

Input: arr = [12, 35, 1, 10, 34, 1]
Output: 34

T.C => O(n) 


workflow steps  : 

Short Revision Steps (1-minute)

1) Initialize first and second to -∞.
2) Traverse every element.
3) If current element is greater than first:
3.1) Move first to second.
3.2) Update first.
4) Else if current element is greater than second and not equal to first:
4.1) Update second.
5) After traversal:
5.1) If second is still -∞, no second largest exists.
5.2) Otherwise, return second.
 

def second_largest(arr):
    first_large_ele = float('-inf')
    second_large_ele = float('-inf')

    for num in arr:
        if num > first_large_ele:
            second_large_ele = first_large_ele
            first_large_ele = num
        elif num > second_large_ele and num != first_large_ele:
            second_large_ele = num

    if second_large_ele == float('-inf'):
        return "No second largest element found"
    else:
        return second_large_ele


res = second_largest([12, 35, 1, 10, 34, 1])
print(res)

output : 
34


-------------------------------------------------------------------------->
Check Sorted Array or : Check if the Array is Sorted 

Given an array arr[], check whether it is sorted in non-decreasing order. 
Return true if it is sorted otherwise false.

Examples:

Input: arr[] = [10, 20, 30, 40, 50]
Output: true
Explanation: The given array is sorted.

Input: arr[] = [90, 80, 100, 70, 40, 30]
Output: false
Explanation: The given array is not sorted.


class Solution:
    def isSorted(self, arr):
        # code here
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False 
        return True         
            
-------------------------------------------------------------------------->
Remove Duplicates from Sorted Array : 

some other approaches : 
1) convert list into set and set into list then return 
2) use the extra list if the element is not present in that list then append then return that list ==> uses extra space of O(n) 


workflow steps : 
i = Index where the next unique element should be placed.
j = Scan or check every element.

1) Set i = 0 → tracks the last unique element.
2) Set j = 1 → scans the array.
3) Compare nums[i] and nums[j].
4) If same → skip duplicate.
5) If different → increment i and copy nums[j] to nums[i].
6) Continue until j reaches the end.
7) Return i + 1 → number of unique elements.
------------------------------------------------------------->

def removeDuplicates(nums):
    i = 0
    n = len(nums)
    for j in range(1, n):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    return nums[:i + 1]

nums = [1,2,3,3,3,4,4,5,6]
print(removeDuplicates(nums))

output :
[1, 2, 3, 4, 5, 6]

-------------------------------------------------------------------------->

===> Left Rotate Array by One  : 

Given an integer array nums, rotate the array to the left by one.

Example 1
Input: nums = [1, 2, 3, 4, 5]
Output: [2, 3, 4, 5, 1]
Explanation:
Initially, nums = [1, 2, 3, 4, 5]
Rotating once to left -> nums = [2, 3, 4, 5, 1]

Example 2
Input: nums = [-1, 0, 3, 6]
Output: [0, 3, 6, -1]

Explanation:
Initially, nums = [-1, 0, 3, 6]
Rotating once to left -> nums = [0, 3, 6, -1]


workflow steps  : 
1. Get the length of the array.
2. Store the first element in a temporary variable.
3. Traverse from index 1 to n-1.
4. Shift every element one position to the left.
5. Place the stored first element at the last index.
6. Return the rotated array (if required).

class Solution:
    def rotateArrayByOne(self, nums):
        n = len(nums)
        temp = nums[0]
        for i in range(1,n):
            nums[i-1] = nums[i]
        nums[n-1] = temp    
------------------------------------------------------------------------>
workflow steps  : 

1. Get the length of the array.
2. Store the last element in a temporary variable.
3. Loop from the second last element to the first element.
4. Shift each element one position to the right.
5. Place the stored last element at the first(0th index) index.
6. Return the rotated array.

def right_rotate_by_one_position(nums):
   n = len(nums)    
   temp = nums[-1]
   for i in range(n-2,-1,-1):
       nums[i+1] = nums[i]
   nums[0] = temp
   return nums
    
print(right_rotate_by_one_position([1,2,3,4,5,6,7]))             
-------------------------------------------------------------------------->
===================================================================================================================================================================>
===> Left Rotate Array by K Places 

Example 1
Input: nums = [1, 2, 3, 4, 5, 6], k = 2
Output: nums = [3, 4, 5, 6, 1, 2]

Explanation:
rotate 1 step to the left: [2, 3, 4, 5, 6, 1]
rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]


Example 2
Input: nums = [3, 4, 1, 5, 3, -5], k = 8
Output: nums = [1, 5, 3, -5, 3, 4]

Explanation:
rotate 1 step to the left: [4, 1, 5, 3, -5, 3]
rotate 2 steps to the left: [1, 5, 3, -5, 3, 4]
rotate 3 steps to the left: [5, 3, -5, 3, 4, 1]
rotate 4 steps to the left: [3, -5, 3, 4, 1, 5]
rotate 5 steps to the left: [-5, 3, 4, 1, 5, 3]
rotate 6 steps to the left: [3, 4, 1, 5, 3, -5]
rotate 7 steps to the left: [4, 1, 5, 3, -5, 3]
rotate 8 steps to the left: [1, 5, 3, -5, 3, 4]

brute force actaully the T.C is optimized but is using the extra space i.e temp array 
T.C => O(n) 
S.C => O(n)

class Solution:
    def left_rotateArray(self, nums, k: int) -> None:
        n = len(nums)
        k = k % n
        temp = []  
        # create temp list which contains the elements which we have to shift to last of the array or list 
        for i in range(k):
            temp.append(nums[i])
        # Shift remaining elements to the left    
        for i in range(k , n):
            nums[i-k] = nums[i]
        # Copy temp elements to the end
        for i in range(k):
            nums[n-k+i] = temp[i]
---------------------------------------------------------------------->

==> optimal without using the space complexity :
T.C => O(n) 

simple example tracing  : 
[1,2,3,4,5]  => left shift by 3 places 
reverse 1st 3 elemets => [3,2,1] 
reverse last n-k elements => [5,4]
[3,2,1,5,4] ==> reverse this the entire array ==> [4,5,1,2,3]

class Solution:
    def left_rotateArray(self, nums, k: int) -> None:
        k = k%len(nums)
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        nums.reverse()



===================================================================================================================================================================>
189. Rotate Right Array by k places : 

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]


Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]

Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
------------------------------------------------------>
brute force approach : 
T.C => O(n) 
S.C => O(k)

Better Solution (Same as Striver's Image)
from typing import List

class Solution:
    def right_rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)

        k = k % n

        # Store last k elements
        temp = []
        for i in range(n - k, n):
            temp.append(nums[i])

        # Shift remaining elements to the right
        for i in range(n - k - 1, -1, -1):
            nums[i + k] = nums[i]

        # Copy temp elements to beginning
        for i in range(k):
            nums[i] = temp[i]


Dry Run
nums = [1,2,3,4,5,6,7]
k = 3
n = 7
Step 1

Store last k elements.

temp = [5,6,7]
Step 2

Shift remaining elements to the right.

i = 3
nums[6] = nums[3]
[1,2,3,4,5,6,4]

i = 2
nums[5] = nums[2]
[1,2,3,4,5,3,4]

i = 1
nums[4] = nums[1]
[1,2,3,4,2,3,4]

i = 0
nums[3] = nums[0]
[1,2,3,1,2,3,4]
Step 3

Copy temp back.

nums[0] = 5
nums[1] = 6
nums[2] = 7

Final

[5,6,7,1,2,3,4]
Complexity
Time: O(n)
Space: O(k)

This is exactly the Better Solution shown in the TUF video.



------------------------------------------------------------------------------->
optimal approch here : 
T.C => O(n) 
S.C => O(1) 

class Solution:
    def right_rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # Reverse the first n-k elements
        nums[:n-k] = reversed(nums[:n-k])

        # Reverse the last k elements
        nums[n-k:] = reversed(nums[n-k:])

        # Reverse the entire array
        nums.reverse()


Dry Run  : 

nums = [1,2,3,4,5]
k = 3

Step 1: Reverse first n-k = 2 elements
[2,1,3,4,5]

Step 2: Reverse last k = 3 elements
[2,1,5,4,3]

Step 3: Reverse entire array
[3,4,5,1,2]

This is the correct right rotation by 3 places.

-------------------------------------------------------------------------------->
===> without using the reverse inbuilt function  : 

# class Solution:
def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1 # we have to indrease the start variable 
        end -= 1 # we have to decreasae the end 

def left_rotateArray(nums, k):
    n = len(nums)
    k = k % n

    # Reverse first k elements
    reverse(nums, 0, k - 1) # we have to pass the exact index values to the reverse function

    # Reverse remaining elements
    reverse(nums, k, n - 1)

    # Reverse entire array
    reverse(nums, 0, n - 1)
    print(nums)

left_rotateArray([1,2,3,4,5,6,7],3)


output :
[4, 5, 6, 7, 1, 2, 3]
-------------------------------------------------------------------------------->   

===================================================================================================================================================================>
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1: take this example to understnad this problem very well 
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]


-------------------------------------------------------------------------------->
BRUTE FORCE APPROACH : 

n => size of the given original array
x => size of the temporary arary 

T.C => O(n) + O(x) + O(n-x) => O(2n) => O(n)
S.C => O(n) ==> for using the temp array 
workflow steps : 

1. Create a temporary list.
2. Traverse the array.
3. Store all non-zero elements in the temporary list.
4. Copy all non-zero elements back to the original array.
5. Fill the remaining positions with zeros.
6. Return the modified array (or modify in-place).

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [] 
        n = len(nums)
        for i in range(0,n):
            if nums[i] != 0 :
                temp.append(nums[i])
        temp_list_size = len(temp)        
        for i in range(0,temp_list_size):
            nums[i] = temp[i]

        for i in range(temp_list_size,n):
            nums[i] = 0
            
--------------------------------------------------->            
===> by taking another array as support :  
      
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=[]
        b=[]
        for i in range(len(nums)):
            if nums[i]==0:
                a.append(nums[i])
            else:
                b.append(nums[i])
        return b+a            
-------------------------------------------------------------------------------->
OPTIMAL FORCE APPROACH :

n => no of elements in the array 
x => length of the array to found the 1st zero in the array 
T.C => O(x) + O(n-x) => O(n)  
S.C => O(n) 

workflow steps : 

1. Find the index of the first zero.
2. If there is no zero, return the array.
3. Traverse from the next index.
4. Whenever a non-zero element is found:
   - Swap it with the zero at index j.
   - Increment j.
5. Continue until the end of the array. 

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = -1 
        n = len(nums)
        # Find the index of the first zero.
        for i in range(0,n):
            if nums[i] == 0 :
                j = i 
                break
        # If there is no zero, return the array.
        if j == -1:
            return
                    
        for i in range(j+1,n): 
            # Whenever a non-zero element is found
            if nums[i] != 0 :
                # Swap it with the zero at index j
                nums[j] , nums[i] = nums[i] , nums[j] 
                j +=1 # we should incrase the j value 


==> tracing example to understand it very easily  : 

nums = [1, 0, 2, 0, 3]

                    START
                      │
                      ▼
                j = -1, n = 5
                      │
                      ▼
              Find first zero
                      │
          ┌───────────┴───────────┐
          │                       │
       i = 0                    i = 1
      nums[0] = 1             nums[1] = 0
      1 == 0 ❌                0 == 0 ✅
          │                       │
          │                       ▼
          │                    j = 1
          │                       │
          └───────────┬───────────┘
                      ▼
          Start second loop
        for i in range(j+1, n)
                      │
                      ▼
              i = 2, 3, 4
                      │
          ┌───────────┴───────────┐
          │                       │
        i = 2                    i = 3
      nums[2] = 2             nums[3] = 0
          │                       │
      2 != 0 ✅                0 != 0 ❌
          │                       │
          ▼                       ▼
       Swap                    Do nothing
 nums[j] ↔ nums[i]              │
          │                       │
 [1, 0, 2, 0, 3]                 │
      ↑     ↑                    │
      j     i                    │
          │                       │
          ▼                       │
 [1, 2, 0, 0, 3]                 │
          │                       │
       j += 1                     │
          │                       │
        j = 2                     │
          │                       │
          └───────────┬───────────┘
                      ▼
                    i = 4
                 nums[4] = 3
                      │
                   3 != 0 ✅
                      │
                      ▼
                    Swap
             nums[j] ↔ nums[i]
                      │
          [1, 2, 0, 0, 3]
               ↑        ↑
               j        i
                      │
                      ▼
          [1, 2, 3, 0, 0]
                      │
                      ▼
                   j += 1
                      │
                    j = 3
                      │
                      ▼
                 Loop ends
                      │
                      ▼
             FINAL ANSWER
           [1, 2, 3, 0, 0]

-------------------------------------------------------------------------->
Linear Search : 

Example 1
Input: nums = [2, 3, 4, 5, 3], target = 3
Output: 1

Explanation:
The first occurence of 3 in nums is at index 1

Example 2
Input: nums = [2, -4, 4, 0, 10], target = 6
Output: -1

Explanation:
The value 6 does not occur in the array, hence output is -1

T.C => O(n) 
S.C => O(1) for storing length of the array i.e variable n 
class Solution:
    def linearSearch(self, nums, target):
        n = len(nums)
        for i in range(0,n):
            if nums[i] == target : 
                return i 
        return -1                
-------------------------------------------------------------------------->
Find the Union of Two Sorted Arrays : 

Union of two sorted arrays : note : in this problem union does not include the duplicate elements 

Example 1
Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]
Output: [1, 2, 3, 4, 5, 7]

Explanation:
The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2

Example 2  : 
Input: nums1 = [3, 4, 6, 7, 9, 9], nums2 = [1, 5, 7, 8, 8]
Output: [1, 3, 4, 5, 6, 7, 8, 9]
Explanation:
The element 7 is common to both, 3, 4, 6, 9 are from nums1 and 1, 5, 8 is from nums2


brute force solution : 

workflow solution : 
1. Create an empty set.
2. Traverse nums1 and insert every element into the set.
3. Traverse nums2 and insert every element into the set.
4. Convert the set into a list.
5. Return the list.

T.C => O(nlogn) ==> for all elements in insertion into the set data structure  
S.c => O(n) ==> used to return the answer but not the solve the problem 
         
class Solution:
    def unionArray(self, nums1, nums2):
        s = set() 
        n1 = len(nums1)
        n2 = len(nums2)
        for i in range(0,n1):
            s.add(nums1[i])
        for i in range(0,n2):
            s.add(nums2[i])
        # return list(s)   # we can use list inbuilt function or use the below brute force logic also
        union = []
        for item in s : 
            union.append(item)
        return union         


optimal solution :             
-------------------------------------------------------------------------->
Find Missing Number in an Array : 

Find missing number : 
    
Given an integer array of size n containing distinct values in the range from 0 to n (inclusive),
 return the only number missing from the array within this range.


Example 1
Input: nums = [0, 2, 3, 1, 4]

Output: 5
Explanation:
nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]

Example 2
Input: nums = [0, 1, 2, 4, 5, 6]

Output: 3

Explanation:
nums contains 0, 1, 2, 4, 5, 6 thus leaving 3 as the only missing number in the range [0, 6]

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        # s = set(nums)
        for i in range(n+1):
            if i not in nums :
                return i 
      
optimal approach :             
workflow steps : 
                
1. Calculate the expected sum from 0 to n.
2. Calculate the actual sum of the array.
3. Subtract the actual sum from the expected sum.
4. Return the difference.     
       
class Solution:
    def missingNumber(self, nums):
        n = len(nums) 
        expected_sum = (n)*(n+1)//2 
        actual_sum = sum(nums)
        return expected_sum - actual_sum            
-------------------------------------------------------------------------->
Maximum Consecutive Ones
Max Consecutive Ones :


Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

T.C => O(n) 
S.P => O(1) # just to return the count 


workflow steps : 

1. Initialize count = 0 and max_count = 0.
2. Traverse the array from left to right.
3. If the current element is 1:
      • Increment count.
4. Otherwise (current element is 0):
      • Reset count to 0.
5. Update max_count with the maximum of max_count and count.
6. Continue until the end of the array.
7. Return max_count.

==> variables to remember :
count 
max_count 

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0 
        max_count  = 0 
        for i in range(0,n):
            if nums[i] == 1:
                count +=1
                max_count = max(max_count , count) 
            else :
                count = 0 
            # max_count = max(max_count , count)   we can use this line here also no problme by remove from above   
        return max_count    

            
-------------------------------------------------------------------------->
Find the Number That Appears Once
136. Single Number : 

Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1



Brute force :
    

workflow steps :
    
1) Pick one element.
2) Count its occurrences in the entire array.
3) If it appears only once, return it.
4) Otherwise, check the next element.
5) Repeat until the unique element is found.

T.C => O(n^2)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0,n):
            count = 0 
            num = nums[i]
            for j in range(0,n):
                if nums[j] == num : 
                    count +=1 
            if count == 1 :
                return nums[i]   
----------------------------------------------------------------------->
optimal : 
1. Create an empty hash map.
2. Count the frequency of every element.
3. Traverse the hash map.
4. Return the element whose frequency is 1.

T.C => O(n) 
S.C => O(n) ==> hashMap dict is used 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = {}
        for num in nums :
            hashMap[num] = hashMap.get(num,0)+1 
        for key , val in hashMap.items() : 
            if val == 1 :
                return key 
            
----------------------------------------------------------------------->
optimal :  
workflow steps : 

1) Initialize xor to 0.
2) Visit each element in the array.
3) XOR the current element with xor.
4) Repeated elements cancel each other (A ^ A = 0).
5) The unique element remains in xor.
6) Return xor.


==> best example to understand the below code : 
input : [1,1,2,2,3] 
output : 3     
    
T.C => O(n) 
S.C => O(1) 
    
xor operations :
0 1 => 1 if diff. them it is 1 
0 0 => 0 if same it is 0  

      
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0 
        for num in nums:
            xor^=num
        return xor  
      
=> Dry with an example : 
--------------------------------------------->          
remember this :

    00 => 0 
  ^ 10 => 2 
  ----
    10
And binary 10 is decimal 2.

so 0^any element = element only 
--------------------------------------------->              
nums = [1, 1, 2, 2, 3]

Start:
xor = 0

       ↓ 1
0 ^ 1 = 1

       ↓ 1
1 ^ 1 = 0
      ↑ ↑
      └─┴── 1 and 1 cancel

       ↓ 2
0 ^ 2 = 2

       ↓ 2
2 ^ 2 = 0
      ↑ ↑
      └─┴── 2 and 2 cancel

       ↓ 3
0 ^ 3 = 3

FINAL
  ↓
  3                  
-------------------------------------------------------------------------->
Longest Subarray with Sum K — Positive : 
or 
Longest Subarray with Sum K — Positive + Negative : 

560. Subarray Sum Equals K  : 
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

==> T.C ==> O(n) 
note : below solution is only for counting no of sub arrays which have sum equal to given k : 
                             
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_sums = {0: 1}  # sum: frequency

        for num in nums:
            current_sum += num
            if current_sum - k in prefix_sums:
                count += prefix_sums[current_sum - k]
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

        return count            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
MEDIUM PROBLEMS : 

-------------------------------------------------------------------------->
1. 2 sum  or Two Sum 

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2] ==> note: here same element addition is not allowed...

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target : 
                    return [i,j]
                    # return list(i,j) => not valid in python 
    
    
optimal :

Time Complexity: O(n)
Space Complexity: O(n)

workflow steps : 
    
1. Create an empty hash map.
2. Traverse the array.
3. Calculate complement = target - current element.
4. Check whether the complement exists in the hash map.
5. If it exists, return its index and the current index.
6. Otherwise, store the current element and its index.
7. Continue until the pair is found.      


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashMap = {} 
        for i in range(0,n):
            compliment = target - nums[i] 
            if compliment in hashMap:
                return [hashMap[compliment],i]
            else :
                hashMap[nums[i]] = i     
        
    
                    
--------------------------------------------------------------------------> 
Sort an Array of 0s, 1s and 2s
Sort Colors  : (dutch national flag problem) red => white => blow ==> rwb

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects 
of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]


Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

------------------------------>
brute force solution :
1) if we sore the given array using the bubble / insertion / selection / merge sort we will get the correct asnwer 
=> T.C => O(n^2) if we use the bubble sort 
=> T.C => O(nlogn) => if we use the merge sort i mean => nums.sort() inbuilt function 
------------------------------>
2) this approach is correct but we should not return the new array instead we shuold change given array only 

take 3 diff. arrays to collect 0s , 1s , 2s then return zero_arr + one_arr + two_arr  


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero_arr = []
        one_arr = []
        two_arr = []

        for num in nums:
            if num == 0:
                zero_arr.append(num)
            elif num == 1:
                one_arr.append(num)
            elif num == 2:
                two_arr.append(num)

        return zero_arr + one_arr + two_arr
------------------------------>    
optimal solutions : working solution 

workflow steps : 
        
1. Initialize low = 0, temp = 0, and high = n-1.
2. Traverse while temp <= high.
3. If nums[temp] == 0:
      • Swap nums[low] and nums[temp].
      • Increment low and temp.
4. If nums[temp] == 1:
      • Increment temp.
5. If nums[temp] == 2:
      • Swap nums[temp] and nums[high].
      • Decrement high.
      • Do NOT increment temp.
6. Continue until temp > high. ==> means temp <= high 
7. The array is sorted in-place.    
 
T.C => 
S.C =>     
    
    
why temp <= high than temp < high :   
there is one element left to process if we use this condition => temp < high . 
becaz temp is the variable to process each and every element in the array 
 
becaz high=high-1 if temp points 2 at anywhere in the array 
    
T.C → O(n)
S.C → O(1)

    
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = temp = 0 
        high = len(nums)-1 
        while temp <= high: # there is one element left to process if we use this condition => temp < high . 
            if nums[temp] == 0 :
                nums[low] , nums[temp] = nums[temp] , nums[low]
                low +=1 
                temp +=1 
            elif nums[temp] == 1:
                temp+=1
            elif nums[temp] == 2 :
                nums[high] , nums[temp] = nums[temp] , nums[high]
                high -=1
------------------------->                 
==> if we dont use the while temp <= high and if we use while temp < high :         
[2,0,1]

Use Testcase
Output
[1,0,2]

Expected
[0,1,2]        
------------------------->        
Best Dry run of the code : 

Initial:
[2, 0, 1, 2]
 ↑        ↑
temp     high
low=0    high=3


1. nums[temp] = 2
   ↓
Swap with high

[2, 0, 1, 2]
 ↓           ↓
[2, 0, 1, 2]   (same values)

high = 2
temp stays


2. nums[temp] = 2
   ↓
Swap with high

[1, 0, 2, 2]
 ↑     ↑
temp  high

high = 1
temp stays


3. nums[temp] = 1
   ↓
temp++

[1, 0, 2, 2]
    ↑
   temp


4. nums[temp] = 0
   ↓
Swap with low

[0, 1, 2, 2]

low++
temp++

        ↓

temp = 2
high = 1

temp > high → STOP

Final:
[0, 1, 2, 2]        
        
        
Initialize:
low = 0
temp = 0
high = n-1

        ↓

while temp <= high

        ↓

   nums[temp] ?

 ┌──────┼──────┐
 ↓      ↓      ↓
  0      1      2
 ↓       ↓      ↓
swap   temp++  swap
low++           high--
temp++          temp stays                  
-------------------------------------------------------------------------->
Majority Element (> N/2)
169. Majority Element  : 

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Trick steps :
Idea: Cancel out non-majority elements. The majority element will survive in the end.
count == 0: Choose a new candidate.
+1 or -1: If same as candidate, increase count; otherwise, decrease.


===>  very simple and memorable solution using the Boyer-Moore Voting Algorithm, which is optimal and easy to recall during interviews:

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate
            
-------------------------------------------------------------------------->
Kadane's Algorithm — Maximum Subarray Sum or Print Subarray with Maximum Sum : 

31))) : maximum subarray  : 
using Kadane's Algorithm
Given an integer array nums, find the subarray with the largest sum, and return its sum.


Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Workflow steps
1) Initialize curr_sum and max_sum with the first element.
2) Traverse the remaining elements from left to right.
3) For each num, choose the maximum between:
4) Starting a new subarray from num.
5) Adding num to the existing curr_sum.
6) Update curr_sum with that maximum value.
7) Update max_sum if curr_sum is greater.
8) Continue until the end of the array.
9) Return max_sum.

T.C => O(n) 
S.C => O(n) 

variables :
curr_sum 
max_sum 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]

        for num in nums[1:]:
            curr_sum = max(num , curr_sum+num)
            max_sum =max(curr_sum , max_sum)
        return max_sum 
    
==> Dry run of the code :

nums = [-2, 1, -3, 4, -1, 2]            
-------------------------------------------------------------------------->


121. Stock Buy and Sell or Best Time to Buy and Sell Stock 

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0 
     
        for i in range(1,len(prices)):
            curr_profit = prices[i] - min_price
            profit = max(profit , curr_profit)
            min_price = min(min_price , prices[i])
         
        return profit

-------------------------------------------------------------------------->
==> Rearrange Array Elements by Sign

You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the array follows the given conditions:

Every consecutive pair of integers have opposite signs.

For all integers with the same sign, the order in which they were present in nums is preserved.

The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the aforementioned conditions.


Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]

Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they
do not satisfy one or more conditions.  


Example 2:

Input: nums = [-1,1]
Output: [1,-1]

Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].


MY OWN BRUTE FORCE APPROACH : 
T.C => O(n)
S.C => O(n)

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n_arr = []
        p_arr = []
        res = []
        for num in nums :
            if num >=0: 
                p_arr.append(num)
            else:
                n_arr.append(num)    
                
        for i in range(len(n_arr)):
            res.append(p_arr[i])
            res.append(n_arr[i])
        return res     

==> without using the too many for loops and too many variables :

Workflow — rearrangeArray() : 
    
1) Get the length n of the input array.
2) Create ans of size n.
3) Set pos_idx = 0 for positive elements.
4) Set neg_idx = 1 for negative elements.
5) Traverse each number in nums.
6) If positive → place at ans[pos_idx], then pos_idx += 2.
7) If negative → place at ans[neg_idx], then neg_idx += 2.
8) Return ans.


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n 
        pos_idx = 0
        neg_idx = 1

        for num in nums :
            if num >=0:
                ans[pos_idx] = num 
                pos_idx +=2 
            else :
                ans[neg_idx] = num 
                neg_idx +=2 
                
        return ans      


==> special case  : when no of the + ve and -ve items are not same  : 
    
workflow steps  : 

1) Create three empty lists: pos, neg, and ans.
2) Traverse every element in nums.
3) If the element is non-negative (>= 0), add it to pos.
4) Otherwise, add it to neg.
5) Initialize two pointers:
    i = 0 → points to the current positive element.
    j = 0 → points to the current negative element.
6) Traverse while both positive and negative elements are available.
   Append pos[i] to ans.
   Append neg[j] to ans.
7) Increment both pointers: i += 1, j += 1.
8) If positive elements are still remaining, append them to ans.
9) If negative elements are still remaining, append them to ans.
10) Return ans.        

def rearrange_by_sign(nums): 
    pos = []
    neg =  []
    ans =  [] 
    for num in nums:
        if num >= 0 :
            pos.append(num)
        else:
            neg.append(num)
    i = 0 
    j = 0 
    while i< len(pos) and j < len(neg):
        ans.append(pos[i])
        ans.append(neg[j])
        i+=1
        j+=1 
    while i < len(pos):
        ans.append(pos[i])
        i+=1 
          
    while j < len(neg):
        ans.append(neg[j])
        j+=1 
    return ans 
nums = [-1, -2, -3, 4, 5]
print(rearrange_by_sign(nums))    
# nums = [-1, -2, -3, 4, 5]


output :
[4, -1, 5, -2, -3]                    
-------------------------------------------------------------------------->

48))) : Next Permutation 
For example, for arr = [1,2,3], 
the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
    
Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]    
    
🎯 Real-Life Analogy — "Next Bigger Ticket Number"
Imagine you are managing ticket numbers at a queue counter. 
The numbers are written on cards and arranged on a board. You want to find the next ticket number 
that's just a bit bigger than the current one — using the same cards (digits). 
If no such bigger number is possible (you’re at the biggest ticket), you just reset to the smallest (sort it ascending).


====> best tracing example  : 
===> A "dip" is the first place (from right to left) where the order stops decreasing — i.e., where a number is less than the number that comes after it.

💡 Example: [1, 3, 5, 4, 2]
Step-by-step Dry Run:
i = 3 because nums[3] = 4 and nums[4] = 2, but 4 > 2, so keep moving left

i = 2, nums[2] = 5, nums[3] = 4 → still 5 > 4, move left

i = 1, nums[1] = 3, nums[2] = 5 → YES! 3 < 5 → found the dip!

👉 Think: Ticket number is 13542. You want next bigger ticket using same digits.

Now find a digit just larger than 3 from the right:

Start from end, find 4 (> 3) → that's our swap candidate

Swap 3 and 4: → 14532

Now reverse the part after index 1 (532) → gives 12534

✅ Final result: [1, 4, 2, 3, 5]

🎓 Real-Life Analogy Summary:
Imagine you're trying to increase your ticket number using the same digits:

Find the digit where you can make a change (first dip from right).

Find the smallest larger number to replace it (next bigger option).

Rearrange the remaining digits to make the smallest possible number.

🧠 Memory Tip (Mnemonic):
"Find Dip → Swap Just Bigger → Reverse Right"

You can even remember it like:
📉 ➡️ 🔄 ➡️ 🔃
("Down, Swap, Reverse" – DSR)


from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2  # Start from the second last element (right to left)
        
        # 🧭 Step 1: Find the first "dip" from right
        # This means finding the first place where the current number is smaller than the next one
        # In real life: You scan your ticket number from right side,
        # looking for the first place where you can "make it bigger"
        while i >= 0 and nums[i] >= nums[i + 1]: # [3,5,4,2] 
            i -= 1
        
        # 🧠 Now i is the index where the "dip" happens (nums[i] < nums[i+1])
        # If we found such an index, that means we can make a bigger number
        if i >= 0:
            j = n - 1

            # 🎯 Step 2: Find the next **just larger number** than nums[i] from the right
            # Think of this like: swap the "dip" number with the next larger digit
            while nums[j] <= nums[i]:
                j -= 1

            # 🔄 Swap the numbers at i and j
            nums[i], nums[j] = nums[j], nums[i]

        # 🔁 Step 3: Reverse the part of the array after index i
        # Why? Because we want the **smallest possible number** after the change,
        # so we sort the remaining digits in ascending order
        nums[i + 1:] = reversed(nums[i + 1:])
-------------------------------------------------------------------------->

Leaders in an Array : 

Given an integer array nums, return a list of all the leaders in the array.

A leader in an array is an element whose value is strictly greater than all elements to its right in the given array.
The rightmost element is always a leader. The elements in the leader array must appear in the order they appear in the nums array.

Example 1 : 
Input: nums = [1, 2, 5, 3, 1, 2]
Output: [5, 3, 2]
Explanation:
2 is the rightmost element, 3 is the largest element in the index range [3, 5], 5 is the largest element in the index range [2, 5]

Example 2 : 
Input: nums = [-3, 4, 5, 1, -4, -5]
Output: [5, 1, -4, -5]
Explanation:
-5 is the rightmost element, -4 is the largest element in the index range [4, 5], 1 is the largest 

brute force approach : 
T.C => O(n^2) : 

class Solution:
    def leaders(self, nums):
        result = []
        n = len(nums)
        for i in range(0,n):
            leader = True
            for j in range(i+1,n):
                if nums[i] < nums[j]:
                    leader = False
                    break 
            if leader == True :
                result.append(nums[i])
        return result        

T.C => O(n) : 

class Solution:
    def leaders(self, nums):
        maxi = float('-inf')
        result = []
        for i in range(n-1,-1,-1):
            if nums[i] > maxi : 
                result.append(nums[i])
                maxi = max(maxi ,nums[i])
        return result[::-1] 
        # return result.reverse()       

-------------------------------------------------------------------------->

        
Longest Consecutive Sequence
                           
-------------------------------------------------------------------------->
73. Set Matrix Zeroes : 

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

 
Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]    


brute force : 

T.C => O(m × n × (m + n)) => O(n^3) 
S.C => O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def mark_rows(i,matrix):
            for j in range(0,cols):
                if matrix[i][j] != 0 : 
                    matrix[i][j] = 'a' # or we can also use -1 or any char if i use minus some of the test cases have the value -1 causng the wrong o/p

        def mark_cols(j,matrix):
            for i in range(0,rows):
                if matrix[i][j] != 0 : 
                    matrix[i][j] = 'a'

        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0 :
                    mark_rows(i,matrix)
                    mark_cols(j,matrix) 

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 'a' :
                    matrix[i][j] = 0 




optimal solution : 

T.C =>O(n^2) 
S.C => O(n+m) 
n=> rows list 
m=> cols list 

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_len = len(matrix)
        cols_len = len(matrix[0]) 

        rows =[0]*rows_len 
        cols = [0]*cols_len


        for i in range(rows_len):
            for j in range(cols_len):
                if matrix[i][j] == 0 :
                    rows[i] = 1 
                    cols[j] = 1
        
        for i in range(rows_len):
            for j in range(cols_len):
                if rows[i] or cols[j] :
                    matrix[i][j] = 0              
-------------------------------------------------------------------------->
Rotate Matrix by 90 Degrees 
===> rotation of image or matrix  : transpose + reversing each row in the tramnsposed matrix 

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Rotation (90° Clockwise)
Original

1 2 3
4 5 6
7 8 9

Rotate

7 4 1
8 5 2
9 6 3

Here, the matrix is turned, not just swapped.


T.C => O(n^2) 

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        # ans = [[0]* rows for _ in range(cols)]

        for i in range(0,rows):
            for j in range(i+1,cols):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
                # (0,0) , (1,1) , (2,2) values will not changed  
                # 0,1 => 1,0 
                # 0,2 => 2,0 
                # 1,2 => 2,1 
                # 2,1 => 1,2 
        for row in matrix:
            row.reverse()
        return matrix    
===================================================================================================================================================================>
TUF Solution (90° Anti-Clockwise)
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)

        # Step 1: Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse every column
        for col in range(n):
            top = 0
            bottom = n - 1

            while top < bottom:
                matrix[top][col], matrix[bottom][col] = matrix[bottom][col], matrix[top][col]
                top += 1
                bottom -= 1

        return matrix            
-------------------------------------------------------------------------->
Print Matrix in Spiral Manner : 

rblt => spiral order and looping start and end variables 
r => l to r 
b => t to b
l => r to l 
t => b to t 

direction 0,1,2,3 
direction = (direction+1) % 4 



increment or decrement : 
trbl => 

n => for travesing all the spirals layers 
m => for traversing all the elements in the each spiral layer  
T.C => O(n*m) 
S.C => O(n)

variables to remember  : 
left , right , top , bottom , rows , cols , res , direction (note : this problem related to matrix follow the zero based indexing every where)
workflow steps   :
    
1. Initialize top, bottom, left and right boundaries.
2. Traverse the top row.
3. Traverse the right column.
4. Traverse the bottom row.
5. Traverse the left column.
6. After each traversal, move the corresponding boundary inward.
7. Repeat until left > right or top > bottom.
8. Return the result.



    
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        top = left = 0 
        
        bottom = rows-1 
        right = cols -1 
        direction = 0 
        
        res = [] 
        
        while(left<= right and top<= bottom): # when the top and bottom variables(if it is 3*3 matrix) or left and right variables are crossed then one spiral is completed  
            if direction == 0 : 
                for i in range(left , right+1):
                    res.append(matrix[top][i])
                top+=1 
                
            elif direction == 1 :
                for i in range(top, bottom+1):
                    res.append(matrix[i][right])
                right-=1 
                
            elif direction ==2 :
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])  
                bottom -=1 
                
            elif direction ==3 :
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])  
                left +=1 
                
            direction = (direction+1)% 4 
        return res         
            
-------------------------------------------------------------------------->
 
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->

==> when the user given the no of the rows we have to print the pascal traingle pattern 

T.C => O(n^2)
S.C => O(1) 

def pascal(n):
    for i in range(0,n):
        for s in range(0,n-i-1):
            print("",end=" ")
        for j in range(0,i+1):
            if i == 0 or j == 0 : 
                c = 1 
            else : 
                c = c*(i-j+1)//j
            print(c,end=" ")   
        print("\n")    
pascal(5)

output : 
    1 

   1 1 

  1 2 1 

 1 3 3 1 

1 4 6 4 1 

------------------------------------------------------------------------------------------------->
118. Pascal's Triangle  : 
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

varibales to remember => 
ans
ansRow 
row
col 
curr 


1) Create an empty list ans to store all rows.
2) Loop from row 1 to numRows.
3) Create an empty list ansRow for the current row.
4) Initialize the first element as 1.
5) Add the first element (1) to the current row.
6) Loop through the remaining columns of the current row.
7) Calculate the next element using the previous element:
  curr = curr * (row - col)
  curr = curr // col
8) Add the calculated element to the current row.
9) After completing the current row, add ansRow to ans.
10) Repeat until all rows are generated.
11) Return ans.


T.C => O(n^2) 

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for row in range(1, numRows + 1):
            ansRow = []

            curr = 1
            ansRow.append(curr)

            for col in range(1, row):
                curr = curr * (row - col) # if row number = 4 => 4*3*2*1 / 1*2*3*4 
                curr = curr // col
                ansRow.append(curr)

            ans.append(ansRow)
        return ans 
output :

-----------------------------------------------------------------------------------------------------------------------------> 
==> printing the value for the given row and column in the pascla traingle  : 

def ncr(n,r):
    res = 1
    for i in range(0,r):
        res = res *(n - i)  # 4 * 3 * 2 * 1 / 1* 2* 3* 4
        res = res // (i+1)
    return res 
        
row =  5
col = 5 
print(ncr(row-1 , col-1))

output : 
1 
cross check using the below pattern  : 

        1
      1   1
    1   2   1
  1   3   3   1
1   4   6   4   1



-----------------------------------------------------------------------------------------------------------------------------> 
==> printing the row in the pascal traingle for the given row  : 

def print_row(row):
    ans = 1
    print(ans, end=" ")

    for i in range(1, row):
        ans = ans * (row - i) # 4 * 3 * 2 * 1 // 4 * 3 * 2 * 1 
        ans = ans // i
        print(ans, end=" ")

print_row(5)

output : 
1 4 6 4 1             
-------------------------------------------------------------------------->
15. 3Sum or 3 Sum : 

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = set()
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] + nums[j] + nums[k] == 0 :
                        triplet = tuple(sorted([nums[i] , nums[j] , nums[k]]))
                        result.add(triplet)

        return [list(tpl) for tpl in result]            
-------------------------------------------------------------------------->
18. 4Sum or 4 Sum : 
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        n = len(nums)
        for i in range(0,n):
            for j in range(i+1 , n):
                for k in range(j+1 , n):
                    for l in range(k+1,n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target : 
                            quadraple = tuple(sorted([nums[i],nums[j],nums[k],nums[l]])) # we should convert the list into sorted list and convert into tuple becaz set can store mutable data types like Ex : list 
                            result.add(quadraple)
        return [list( tpl) for tpl in result]                    
            

Easy rule to remember
List ([]) → Mutable → ❌ Cannot be added to a set or used as a dictionary key.
Tuple (()) → Immutable → ✅ Can be added to a set and used as a dictionary key.

This is why we write:

triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
result.add(triplet)

instead of:

triplet = sorted([nums[i], nums[j], nums[k]])  # This is a list
result.add(triplet)  # ❌ Error: unhashable type: 'list'            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->
            
-------------------------------------------------------------------------->

131. Count Inversions

Given an integer array nums. Return the number of inversions in the array.
Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
It indicates how close an array is to being sorted.
A sorted array has an inversion count of 0.
An array sorted in descending order has maximum inversion.


Example 1:
Input: nums = [2, 3, 7, 1, 3, 5]
Output: 5
Explanation:
The responsible indexes are:
nums[0], nums[3], values: 2 > 1 & indexes: 0 < 3
nums[1], nums[3], values: 3 > 1 & indexes: 1 < 3
nums[2], nums[3], values: 7 > 1 & indexes: 2 < 3
nums[2], nums[4], values: 7 > 3 & indexes: 2 < 4
nums[2], nums[5], values: 7 > 5 & indexes: 2 < 5


Example 2:
Input: nums = [-10, -5, 6, 11, 15, 17]
Output: 0
Explanation:
nums is sorted, hence no inversions present.


=> brute force solution : 
T.C ==> O(n^2)  :  two nested loops to check all pairs


Reverse Pairs — High-Level Workflow : 

1) Initialize count = 0 to store the number of reverse pairs.
2) Take each element nums[i] as the first element of the pair.
3) Compare it with every element after it using j = i + 1.
4) Check the reverse-pair condition:
   nums[i] > nums[j]
5) If the condition is true, increment count by 1.
6) Continue checking all possible pairs (i, j) where i < j.
7) Return count as the total number of reverse pairs.


class Solution:
    def numberOfInversions(self, nums):
        n = len(nums)
        count = 0 
        for i in range(0,n-1):
            for j in range(i+1,n):
                if nums[i] > nums[j]:
                    count +=1 
        return count             

        

=> optimal solution : 

High-Level Workflow — Revision  : 

Count Inversions Using Merge Sort

1) Divide the array into two halves recursively.
2) Find inversions in the left half using merge sort.
3) Find inversions in the right half using merge sort.
4) Merge the two sorted halves.
5) While merging, compare left and right elements.
6) If left <= right, add the left element normally.
7) If left > right, an inversion is found. Add mid - left + 1 (note we are given the sorted array as the input)
because all remaining elements in the left half are greater than the current right element.

8) Add remaining elements from both halves.
9) Copy the sorted elements back into the original array.
10) Return the total inversion count from left + right + merge.


Complexity : 
Time Complexity: O(n log n)
Space Complexity: O(n)

class Solution:
    def numberOfInversions(self, nums):
        
        def merge(arr, low, mid, high):
            temp = []
            left = low
            right = mid + 1
            count = 0

            while left <= mid and right <= high:
                
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                
                else:
                    # arr[left] > arr[right]
                    temp.append(arr[right])
                    
                    # All remaining elements in left half
                    # will form an inversion with arr[right]
                    count += (mid - left + 1)
                    
                    right += 1

            # Add remaining left elements
            while left <= mid:
                temp.append(arr[left])
                left += 1

            # Add remaining right elements
            while right <= high:
                temp.append(arr[right])
                right += 1

            # Copy sorted elements back
            for i in range(low, high + 1):
                arr[i] = temp[i - low]

            return count

        def merge_sort(arr, low, high):
            count = 0

            if low >= high:
                return count

            mid = (low + high) // 2

            # Count inversions in left half
            count += merge_sort(arr, low, mid)

            # Count inversions in right half
            count += merge_sort(arr, mid + 1, high)

            # Count cross inversions while merging
            count += merge(arr, low, mid, high)

            return count

        return merge_sort(nums, 0, len(nums) - 1)
        
        
TRACING THIS EXAMPLE INPUT ARRAY : [5, 3, 2, 4, 1] 
        
                                 [5, 3, 2, 4, 1]
                                  |
                    ┌─────────────┴─────────────┐
                    ↓                           ↓
                [5, 3, 2]                    [4, 1]
                    |                           |
              ┌─────┴─────┐                 ┌───┴───┐
              ↓           ↓                 ↓       ↓
            [5, 3]       [2]              [4]     [1]
              |
          ┌───┴───┐
          ↓       ↓
         [5]     [3]


==================== MERGE ====================

         [5] + [3]
              ↓
            [3,5]
              |
              | 5 > 3 → +1 inversion
              ↓
          [3,5] + [2]
              |
              | 3 > 2 → +2 inversions
              | 5 > 2
              ↓
           [2,3,5]


         [4] + [1]
              |
              | 4 > 1 → +1 inversion
              ↓
            [1,4]


================ FINAL MERGE ================

          [2,3,5] + [1,4]
                  |
                  |
          2 > 1 → +3 inversions
          3 > 1
          5 > 1
                  |
          5 > 4 → +1 inversion
                  ↓
            [1,2,3,4,5]


================ TOTAL =================

Left inversions   = 3
Right inversions  = 1
Cross inversions  = 4
                    ───
Total             = 8

===================================================================================>




493. Reverse Pairs : 

Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:

0 <= i < j < nums.length and nums[i] > 2 * nums[j].
 

Example 1:
Input: nums = [1,3,2,3,1]
Output: 2

Explanation: The reverse pairs are:
note : please make sure that (1,4 ) are the index numbers not the exact numbers  : 
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1


Example 2:
Input: nums = [2,4,3,5,1]
Output: 3

Explanation: The reverse pairs are:
note : please make sure that (1,4 ) are the index numbers not the exact numbers  : 
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1

=> BRUTE FORCE SOLUTION :
T.C ==> O(n^2)  :  two nested loops to check all pairs

Reverse Pairs — High-Level Workflow : 

1) Initialize count = 0 to store the number of reverse pairs.
2) Take each element nums[i] as the first element of the pair.
3) Compare it with every element after it using j = i + 1.
4) Check the reverse-pair condition:
   nums[i] > 2 * nums[j]
5) If the condition is true, increment count by 1.
6) Continue checking all possible pairs (i, j) where i < j.
7) Return count as the total number of reverse pairs.

class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0 
        for i in range(0,n-1):
            for j in range(i+1 , n):
                if nums[i] > 2*(nums[j]) :
                    count +=1 
        return count             

        
=> OPTIMAL FORCE SOLUTION :

T.C ==> O(n log n) :
The array is divided into halves recursively O(log n), 
and reverse pairs are counted + elements are merged in O(n) at each level.

S.C ==> O(n) :
merge() uses a temporary array temp to merge elements.

Workflow steps : 
1) Start with the entire array and call merge_sort(nums, 0, n-1).
2) If the range contains only one element (low >= high), return 0 because a single element cannot form a pair.
3) Find the middle index:
   mid = (low + high) // 2
4) Divide the array into two halves:
   Left half → low ... mid
   Right half → mid + 1 ... high
5) Recursively count reverse pairs inside the left half.
6) Recursively count reverse pairs inside the right half.
7) Count cross reverse pairs, where:
   first element comes from the left half
   second element comes from the right half
8) Check the reverse-pair condition:
arr[left] > 2 * arr[right]
9) Because both halves are already sorted, use the right pointer to efficiently count multiple valid pairs instead of checking every pair individually.

Add the cross-pair count to the total:
count += count_pairs(...)

10) Merge the two sorted halves using merge() so that the current range becomes sorted.
11) Return the total count from the current recursive call.
12) Finally, return the total number of reverse pairs:
return merge_sort(nums, 0, len(nums) - 1)


class Solution:
    def reversePairs(self, nums: list[int]) -> int:

        def merge(arr, low, mid, high):
            temp = []

            left = low
            right = mid + 1

            # Merge two sorted halves
            while left <= mid and right <= high:

                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1

                else:
                    temp.append(arr[right])
                    right += 1

            # Remaining elements from left half
            while left <= mid:
                temp.append(arr[left])
                left += 1

            # Remaining elements from right half
            while right <= high:
                temp.append(arr[right])
                right += 1

            # Copy sorted elements back
            for i in range(low, high + 1):
                arr[i] = temp[i - low]

        def count_pairs(arr, low, mid, high):
            right = mid + 1
            count = 0

            for left in range(low, mid + 1):

                while right <= high and arr[left] > 2 * arr[right]:
                    right += 1

                count += right - (mid + 1)

            return count

        def merge_sort(arr, low, high):

            if low >= high:
                return 0

            mid = (low + high) // 2

            count = 0

            # Count reverse pairs in left half
            count += merge_sort(arr, low, mid)

            # Count reverse pairs in right half
            count += merge_sort(arr, mid + 1, high)

            # Count cross reverse pairs
            count += count_pairs(arr, low, mid, high)

            # Merge both sorted halves
            merge(arr, low, mid, high)

            return count

        return merge_sort(nums, 0, len(nums) - 1)
------------------------->
flow chart based tracing of the above code for the input array : [40,25,19,12,9,6,2]

                              merge_sort(0,6)
                    Array = [40,25,19,12,9,6,2]
                                  |
                     mid = (0+6)//2 = 3
                                  |
                    ┌─────────────┴─────────────┐
                    ↓                           ↓
             merge_sort(0,3)              merge_sort(4,6)
             [40,25,19,12]                [9,6,2]
                    |                           |
              mid = 1                     mid = 5
                    |                           |
             ┌──────┴──────┐              ┌─────┴─────┐
             ↓             ↓              ↓           ↓
       merge_sort(0,1)  merge_sort(2,3) merge_sort(4,5) merge_sort(6,6)
       [40,25]          [19,12]         [9,6]          [2]
             |             |                |             |
        mid = 0         mid = 2        mid = 4          |
             |             |                |             |
          ┌──┴──┐       ┌─┴─┐           ┌─┴─┐           |
          ↓     ↓       ↓   ↓           ↓   ↓           |
       (0,0)  (1,1)   (2,2)(3,3)      (4,4)(5,5)      (6,6)
       [40]    [25]     [19] [12]       [9]  [6]       [2]
          |       |       |    |          |    |         |
          0       0       0    0          0    0         0
          |       |       |    |          |    |         |
          └──┬────┘       └─┬──┘          └─┬──┘         |
             ↓               ↓                ↓           |
       count_pairs          count_pairs     count_pairs   |
       (0,0,1)              (2,2,3)        (4,4,5)        |
       [40] vs [25]         [19] vs [12]   [9] vs [6]    |
             |                  |               |          |
           count=0            count=0         count=0       |
             |                  |               |          |
             ↓                  ↓               ↓          |
       merge(0,0,1)        merge(2,2,3)    merge(4,4,5)    |
             |                  |               |          |
             ↓                  ↓               ↓          |
          [25,40]           [12,19]          [6,9]         |
             |                  |               |          |
             └──────────┐       └───────┐       └──────┐  |
                        ↓               ↓              ↓  |
                  merge_sort(0,1)  merge_sort(2,3) merge_sort(4,5)
                  returns 0         returns 0       returns 0
                        |               |              |
                        └───────┬───────┘              |
                                ↓                      |
                         count_pairs(0,1,3)            |
                         [25,40] vs [12,19]            |
                                |                      |
                         reverse pairs = 3             |
                         (25,12)                       |
                         (40,12)                       |
                         (40,19)                       |
                                |                      |
                                ↓                      |
                         merge(0,1,3)                  |
                                |                      |
                                ↓                      |
                         [12,19,25,40]                |
                                |                      |
                         merge_sort(0,3)               |
                         returns 3                      |
                                                       |
                                                       ↓
                                              merge_sort(6,6)
                                              returns 0
                                                       |
                                                       ↓
                                              count_pairs(4,5,6)
                                              [6,9] vs [2]
                                                       |
                                              reverse pairs = 2
                                              (6,2)
                                              (9,2)
                                                       |
                                                       ↓
                                              merge(4,5,6)
                                                       |
                                                       ↓
                                                   [2,6,9]
                                                       |
                                                       ↓
                                              merge_sort(4,6)
                                              returns 2
                                                       |
                                                       |
                     ┌─────────────────────────────────┘
                     ↓
              BOTH HALVES ARE READY
                     |
                     ↓
       LEFT  = [12,19,25,40]
       RIGHT = [2,6,9]
                     |
                     ↓
             count_pairs(0,3,6)
                     |
        ┌────────────┼────────────┐
        ↓            ↓            ↓
      12 vs 2      19 vs ...    25/40 vs ...
        |            |            |
      count 1      count 3      count 3 + 3
        |            |            |
        └────────────┴────────────┘
                     |
                     ↓
              CROSS COUNT = 10
                     |
                     ↓
                merge(0,3,6)
                     |
                     ↓
          [2,6,9,12,19,25,40]
                     |
                     ↓
              FINAL COUNT
                3 + 2 + 10
                     |
                     ↓
                     15
===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>
===> 152. Maximum Product Subarray  : 
Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

===>  📦 Intuitive Analogy:
Think of max and min as twin warriors.
When they face a negative enemy, they swap powers.
Always keep the strongest twin (max_prod) noted after every battle (iteration)

===> T.C ==> O(n)  note: becaz we are finding max value out of 2 values only
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        if not nums : 
            return -1

        max_prod = nums[0]
        curr_max = curr_min = nums[0]
        
        for n in nums[1:]:
            if n < 0:
                curr_max, curr_min = curr_min, curr_max  # swap when negative
            
            curr_max = max(n, curr_max * n)
            curr_min = min(n, curr_min * n)
            
            max_prod = max(max_prod, curr_max)
        
        return max_prod     


best example to understand the above code  : 
Input: [-2, 3, -4]
Let's go step by step:
Start: curr_max = curr_min = -2, max_prod = -2

At n = 3:
curr_max = max(3, -2 * 3) = max(3, -6) = 3
Because starting from 3 is better than continuing

At n = -4:

Swap curr_max and curr_min → now curr_max = -6, curr_min = 3
curr_max = max(-4, -6 * -4) = max(-4, 24) = 24
Multiplying with a negative flipped things!
Answer: 24

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>

===================================================================================>