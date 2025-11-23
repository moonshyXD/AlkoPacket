import sys

n = int(sys.stdin.readline())
arr = [0] * 100

for _ in range(n):
    line = sys.stdin.readline()
    number = int(line.split()[0])
    arr[number] += 1

result = [0] * 100
result[0] = arr[0]
for i in range(1, 100):
    result[i] = result[i - 1] + arr[i]

print(*result)
