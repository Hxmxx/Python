import sys

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
d = list(map(int, input().split()))

st = sorted(d)
index_map = {value: idx for idx, value in enumerate(st)}

print(' '.join(map(str, (index_map[i] for i in d))))