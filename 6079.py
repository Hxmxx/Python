a = int(input())

sum = 0
result = 0

for i in range(1, a) :
    sum += i
    result = i
    if sum >= a :
        print(result)
        break