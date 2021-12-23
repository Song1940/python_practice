"""
1: 1
2: 1 1
3: 1 1 1
4: 1 2 1
5: 1 2 1 1
6: 1 2 2 1
7: 1 2 2 1 1
8: 1 2 2 2 1
9: 1 2 3 2 1
10:1 2 3 2 1 1
11:1 2 3 2 2 1
12:1 2 3 3 2 1
13:1 2 3 3 2 1 1
14:1 2 3 3 2 2 1
15:1 2 3 3 3 2 1
16:1 2 3 4 3 2 1


"""

r = int(input())
list = []

for i in range(r):
    x,y = map(int, input().split())
    list.append(y-x)

for i in list:
    cnt =1
    while 1:
        if i<cnt**2:
            cnt-=1
            break
        cnt+=1
    if i == cnt**2:
        print(cnt*2-1)
    elif (cnt+1)**2 - i > i-cnt**2:
        print(cnt*2)
    elif (cnt+1)**2-i <i - cnt**2:
        print(cnt*2+1)



