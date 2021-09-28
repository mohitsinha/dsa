# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/


def searchRange(self, nums, target):
    first = last = -1

    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            if mid == 0 or nums[mid - 1] != target:
                first = mid
                break
            r = mid - 1

        elif target < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1

    if first == -1:
        return [-1, -1]

    l, r = first, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            if mid == len(nums) - 1 or nums[mid + 1] != target:
                last = mid
                break
            l = mid + 1
        if target < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1

    return [first, last]


# https://leetcode.com/problems/first-bad-version/submissions/


def isBadVersion(mid):
    pass


def firstBadVersion(self, n):
    l, r = 0, n
    f = -1
    while l <= r:
        mid = (l + r) // 2

        if isBadVersion(mid):
            if not isBadVersion(mid - 1):
                return mid
            f = mid
            r = mid - 1
        else:
            l = mid + 1
    return f

