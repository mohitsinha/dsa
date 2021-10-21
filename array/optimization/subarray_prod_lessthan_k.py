# https://leetcode.com/problems/subarray-product-less-than-k/submissions/
# https://www.geeksforgeeks.org/number-subarrays-product-less-k/
def numSubarrayProductLessThanK(self, nums, k: int) -> int:
    res = l = r = 0
    p = 1

    n = len(nums)

    while r < n:

        p *= nums[r]

        while p >= k and l < r:
            p /= nums[l]
            l += 1

        if p < k:
            res += (r - l + 1)

        r += 1

    return res


# Number of subarrays with given product
# https://www.geeksforgeeks.org/number-subarrays-given-product/

arr = [1, 2, 3, 4, 1]
k = 24

arr = [2, 1, 1, 1, 4, 5]
k = 4

arr = [2, 1, 1, 1, 3, 1, 1, 4 ]
k = 1

arr = [2, 1, 1, 1, 3, 1, 1, 1 ]
k = 3


l=r=0
res=0
p=1
n=len(arr)

while r<n:
    p*=arr[r]

    while p>k and l<r:
        p = p//arr[l]
        l+=1

    if p==k:
        c_one = 0

        while r<n-1 and arr[r+1]==1:
            c_one+=1
            r+=1

        res+= c_one + 1
        while arr[l]==1 and l<=r:
            res+=(c_one + 1)
            l+=1

    r+=1
print(res)