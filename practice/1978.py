t = int(input())

list = []
for i in range(t):
    h, w, n = map(int, input().split())
    if n%h ==0:
        f = h
        r=n//h
    else:
        f = n%h
        r = n // h  + 1

    list.append(f*100+r)

for i in list:
    print(i)

