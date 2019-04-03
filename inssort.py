import random,time
def insertion(L):
    N=len(L)
    for i in range(1,N):
        v=L[i]
        j=i-1
        while j>=0 and L[j]>v:
            L[j+1]=L[j]
            j-=1
        L[j+1]=v
    return L
print("Insertion sort:")
alist=[random.randint(0,2000) for i in range(2000)]
print(alist)
start=time.time()
insertion(alist)
end=time.time()
print(end-start,"Seconds")
print(alist)