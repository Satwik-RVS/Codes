# RVS

n = input().strip()

m = len(n)
x = int(n)
c = 0
for i in range(m):
    y = int(n[i])
    if y and x%y == 0:
        c += 1

print(c)
