w, h, b = map(int, input().split())

total = w*h*b
byte = total / 8
kb = byte / 1024
mb = kb / 1024

print("%.2f MB" %mb)