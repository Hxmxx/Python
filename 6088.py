a, b, c = map(int, input().split())

sum = a

for i in range(1, c) :
    sum += b
    
print(sum)