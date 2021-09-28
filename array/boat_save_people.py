from collections import defaultdict

people = [3,2,2,1]
limit = 5

# https://leetcode.com/problems/boats-to-save-people/

# d=defaultdict(lambda: 0)


people_sorted = sorted(people)

count = 0
l=0
r=len(people)-1

while l<=r:
    if l==r:
        count+=1
        break

    if (people_sorted[l]+ people_sorted[r])<=limit:
        count+=1
        l+=1
        r-=1
    else:
        count+=1
        r-=1


print(count)