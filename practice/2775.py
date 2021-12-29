t = int(input())
list = []
for i in range(t):
    k = int(input())
    n = int(input())
    for j in range(1,n):
        cnt = 1
        cnt += (k+1)*j
    list.append(cnt)

for i in list:
    print(i)