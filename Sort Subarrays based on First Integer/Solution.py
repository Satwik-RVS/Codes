# RVS

n = int(input())
l = list(map(int,input().split()))
k = int(input())

s = []
for i in range(0,n-k+1,k):
    s.append(l[i:i+k])

s = sorted(s, key = lambda x : x[0])

for i in s:
    print(*i, end = " ")
