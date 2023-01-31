insertion = []
N = int(input())
for i in range(N):
    insertion.append(int(input()))

for i in range(1,N):
    key = insertion[i]
    num = i-1
    while num>=0 and insertion[num] > key:
        insertion[num+1] = insertion[num]
        num = num-1
    insertion[num+1] = key
[print(v) for v in insertion]