import sys
a,b,v = map(int, sys.stdin.readline().split())

cnt = (v-b)/(a-b)
print(int(cnt) if cnt == int(cnt) else int(cnt)+1)

