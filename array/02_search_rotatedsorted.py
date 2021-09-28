
def findPivot(arr, beg, end):
    mid = (beg+end)//2

    if arr[mid] > arr[mid+1]:
        return mid+1
    if arr[mid] < arr[mid-1]:
        return mid

    if arr[mid]>arr[beg]:
        return findPivot(arr,beg, mid-1)
    elif arr[end] < arr[mid]:
        return findPivot(arr, mid+1, end)



def binSearch(arr, num,  low, high):
    mid = (low+high)//2
    if arr[mid]==num:
        return mid


    if low==high:
        return -1
    if num < arr[mid]:
        return binSearch(arr, num, low, mid-1)
    else:
        return binSearch(arr, num, mid+1, high)


def findNum(arr, num):
    pivot = findPivot(arr, 0, len(arr) - 1)
    if arr[0] < num:
        return binSearch(arr, num, 0, pivot-1)
    else:
        return binSearch(arr, num, pivot, len(arr)-1)



# arr=[3,4,5,1,2]
# num=1
# print('index', findNum(arr,num))
#
#
# # print(find(arr, 0, len(arr)-1, num))
#
# arr=[3,4,5,6,7,8,9,1,2]
# num=9
# print('index', findNum(arr,num))
#
#
# # print(find(arr, 0, len(arr)-1, num))
#
# arr=[8,9,1,2, 3,4,5,6,7]
# num=9
# print('index', findNum(arr,num))
#
# # print(find(arr, 0, len(arr)-1, num))
#
# arr=[4,5,1,2, 3]
# num=1
# print('index', findNum(arr,num))
#
# # print(find(arr, 0, len(arr)-1, num))
# arr=[7, 8,1,2, 3,4,5,6]
# num=8
# print('index', findNum(arr,num))
#
#
#
#


def find(arr, l,  r, num):
    mid = (l+r)//2

    if l>r:
        return -1

    if arr[mid]==num:
        return mid
    if arr[l]<=arr[mid]:
        if num>=arr[l] and num<=arr[mid]:
            return find(arr, l, mid-1, num)
        else:
            return find(arr, mid+1, r, num)
    if num>=arr[mid] and num<=arr[r]:
        return find(arr, mid+1, r, num)
    return find(arr, l, mid - 1, num)

    # if l>r:
    #     return -1
    #
    # if arr[mid]==num:
    #     return mid
    #
    # if arr[l]<=arr[mid]:
    #     if arr[l]<=num and num<=arr[mid]:
    #         return find(arr,l, mid-1, num)
    #     else:
    #         return find(arr, mid+1, r, num)
    #
    # if num>=arr[mid] and num<=arr[r]:
    #     return find(arr, mid+1, r, num)
    # return find(arr, l, mid - 1, num)

arr=[3,4,5,1,2]
num=1
print('index', find(arr,0, len(arr)-1, num))


# print(find(arr, 0, len(arr)-1, num))

arr=[3,4,5,6,7,8,9,1,2]
num=9
print('index', find(arr,0, len(arr)-1, num))


# print(find(arr, 0, len(arr)-1, num))

arr=[8,9,1,2, 3,4,5,6,7]
num=9
print('index', find(arr,0, len(arr)-1, num))

# print(find(arr, 0, len(arr)-1, num))

arr=[4,5,1,2, 3]
num=1
print('index', find(arr,0, len(arr)-1, num))

# print(find(arr, 0, len(arr)-1, num))
arr=[7, 8,1,2, 3,4,5,6]
num=12
print('index', find(arr,0, len(arr)-1, num))

