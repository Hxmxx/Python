h, b, c, s = input().split()

h = int(h)
b = int(b)
c = int(c)
s = int(s)

total = h*b*c*s
byte = total / 8
kb = byte / 1024
mb = kb / 1024

print("%0.1f MB" %mb)