def insert_search(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i-1
        while j>=0 and a[j]>key:
            a[j+1] = a[j]
            j-=1
        a[j+1] = key
    return a

list = [3,5,8,1,7]
print(list)

list =insert_search(list)
print(list)

