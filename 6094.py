n = int(input())
k = input().split()

for i in range(n) :
    k[i] = int(k[i])

a = k[0]

for i in range(n) :
    if a>=k[i] :
        a = k[i]
print(a)