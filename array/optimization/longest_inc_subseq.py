# https://leetcode.com/problems/longest-increasing-subsequence

def lengthOfLIS(self, nums):
    sol = [1] * len(nums)
    for i in range(1, len(nums)):
        y = 1
        for j in range(i - 1, -1, -1):

            if nums[j] < nums[i]:
                y = max(y, sol[j] + 1)

        sol[i] = y

    return max(sol)

# https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/

arr = [1, 101, 2, 3, 100, 4, 5]
arr=[3, 4, 5, 10]
arr=[10, 5, 4, 3]
sol = arr.copy()

n = len(arr)

for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]:
            sol[i] = max(sol[i], arr[i] + sol[j])
print(max(sol))

a=[1,2,3,4]
aa=[i*i if i%2==0 else i*i*i for i in a]
print(aa)