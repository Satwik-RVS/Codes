# RVS

n,m = map(int,input().split())
l = [ list(map(int,input().split())) for i in range(n) ]

for j in range(1,m):
    for i in range(n):
        if i == 0:
            l[i][j] += max(l[i][j-1],l[i+1][j-1])
        elif i == n-1:
            l[i][j] += max(l[i][j-1],l[i-1][j-1])
        else:
            l[i][j] += max(l[i][j-1],l[i-1][j-1],l[i+1][j-1])

rvs = [ i[-1] for i in l ]

print(max(rvs))
