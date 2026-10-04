=========================================================================================================================================>
                                           DYNAMIC PROGRAMMING 
=========================================================================================================================================>
70. Climbing Stairs   : 

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
 
Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step  


High-level workflow
1) Handle base cases: If n < 3, return n.
2) Initialize: a = 3, b = 2 representing the previous two Fibonacci values.
3) Loop: From the 3rd step onward, calculate the next value using a = a + b.
4) Update: Move b to the previous a using b = a - b.
5) Return: a is the number of ways to climb n stairs.

Time & Space Complexity
Time: O(n) — the loop runs approximately n times.
Space: O(1) — only a, b, and i are used.

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3 : 
            return n 
        else : 
            a = 3 
            b= 2 
            # 1,2,3,5,8,13,21,............
            for i in range(n-3):
                a = a+b
                b= a - b  
            return a     


                                                    
=========================================================================================================================================>
198. House Robber  -1 : 

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

==> T.C ==> Time Complexity: O(n)  

workflow steps :

1) Handle edge cases: If there is 1 house, return its money; if there are 2 houses, return the maximum of the two.
2) Create a dp array to store the maximum money that can be robbed up to each house.
3) Initialize the first two values: dp[0] = nums[0] and dp[1] = nums[1].
4) For each house from index 2: calculate the maximum of:
   - Rob current house: dp[i-2] + nums[i]
   - Skip current house: dp[i-1]
Store the maximum value in dp[i].
Return dp[-1], which contains the maximum amount that can be robbed.


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1 : # if single 
             return  nums[0]
        if len(nums) ==2 : # if 2 elements are there just return max of them 
            return max(nums[0],nums[1])
        # memorize max loots at first 2 indexes  
        dp=[0]*len(nums)    
        dp[0] = nums[0]
        dp[1] = nums[1]
        # use them to fill the array(dp) 
        for i in range(2,len(nums)):
            # core logic 
            dp[i] = max((dp[i-2]+ nums[i]) , dp[i-1])
        # return last index value in dp array 
        return dp[-1]   

=========================================================================================================================================>
213. House Robber - II   : 

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob 
tonight without alerting the police.


Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

====> T.C ==> O(n) 

House Robber II — High-Level Workflow : 

1) Handle edge cases: If there is 1 house, return its money; if there are 2 houses, return the maximum of the two.
2) Because houses are circular, you cannot rob both the first and last house.
3) Create two cases:
   - skipLastHouse → include first house, exclude last house.
   - skipFirstHouse → exclude first house, include last house.
4) Apply normal House Robber DP separately to both arrays.
For each array, calculate maximum loot using:
max(rob current, skip current).
Compare both cases and return the larger loot.

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1 : 
            return nums[0]
        if len(nums) ==2 :
            return max(nums[0] , nums[1])
        def rob(nums):
            if len(nums) ==1 : 
                return nums[0]
            if len(nums) ==2 :
                return max(nums[0] , nums[1])  

            dp = [0]*len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0] , nums[1])

            for i in range(2, len(nums)): 
                dp[i] = max((dp[i-2]+nums[i]) , dp[i-1])
            return dp[-1]     
        # create 2 new arrays to include and excluede 1st and last elements in the arrays 
        skipLastHouse = [] # inclueds 1st element and excludes last element 
        skipFirstHouse =  [] # includes last element and excludes 1st element 
        for i in range(len(nums)-1):
            skipFirstHouse.append(nums[i])
            skipLastHouse.append(nums[i+1])
        # get the loots from both possibilities 
        lootFirstHouse = rob(skipFirstHouse)
        lootLastHouse = rob(skipLastHouse)
        # return the max of 2 loots 
        return max(lootFirstHouse , lootLastHouse)
