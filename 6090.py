a, m, d, n = map(int, input().split())

t = a

for i in range(1, n) :
    t = (t * m) + d

print(t)