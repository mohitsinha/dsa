# https://leetcode.com/problems/minimum-window-substring/submissions/

# tracking count of the length of string t.

from collections import defaultdict

s='KADOBECODEBANC'
t='ABC'

def minWindow(s,t):

    n = len(t)
    if n > len(s):
        return ''
    m = defaultdict(lambda: 0)

    res = ''
    for i in t:
        m[i] += 1

    l = 0
    r = 0

    cnt = 0
    while r < len(s):
        if s[r] in m:
            m[s[r]] -= 1

            if m[s[r]] >= 0:
                cnt += 1

        while cnt == n:

            if res == '':
                res = s[l:r + 1]
            else:
                res = s[l:r + 1] if (r + 1 - l) < len(res) else res

            if s[l] in m:
                m[s[l]] += 1

                if m[s[l]] > 0:
                    cnt -= 1

            l += 1

        r += 1



# tracking count of all alphabets in string t are complete, whether they are repeated or not

def minWindow1(s,t):

    if len(t)>len(s):
        return ''
    cnt=0
    m=defaultdict(lambda: 0)
    for i in t:
        m[i]+=1
        if m[i]==1:
            cnt+=1

    l=r=0
    start=0
    end=-1


    while r<len(s):
        if s[r] in m:
            m[s[r]]-=1

            if m[s[r]]==0:
                cnt-=1

        while cnt==0:
            if end==-1:
                end=r
                start=l
            else:
                if r-l<end-start:
                    start=l
                    end=r

            if s[l] in m:
                m[s[l]]+=1
                if m[s[l]]==1:
                    cnt+=1

            l+=1
        r+=1

    return s[start:end+1] if end!=-1 else ''

print(minWindow1('KADOBECODEBANC', 'ABC'))

