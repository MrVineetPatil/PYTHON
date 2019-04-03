import random,time
def selection(L):
    for i in range(len(L)-1):
        min=i
    for j in range(i+1,len(L)):
        if L[j]<L[min]:
            min=j
    L[i],L[min] = L[min],L[i]
    print("Selection sort: ")
alist=[random.randint(0,2000) for i in range(2000)]
print(alist)
start=time.time()
selection(alist)
end=time.time()
print(end-start,"Seconds")
print(alist)