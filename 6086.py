n = int(input())
sum = 0

for i in range(1, n+1) :
    if sum >= n :
        break
    sum += i

print(sum)