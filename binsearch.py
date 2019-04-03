import time, random
def bin_iter(l,key,low,high):
    while(low<=high):
        mid = (low+high)//2
        if key==l[mid]:
            return mid
        elif key<l[mid]:
            high=mid-1
        else:
            low=mid+1
    return None

def bin_rec(l,key,low,high):
    if(low<=high):
        mid = (low+high)//2
        if key==l[mid]:
            return mid
        elif key<l[mid]:
            return bin_rec(l,key,low,mid-1)
        else:
            return bin_rec(l,key,mid+1,high)
    return None

k = [random.randint(0,200) for i in range(200)]
k.sort()
print(k)
key=int(input())
low = 0
high = len(k)-1

print("Iterative binary: ")
start = time.time()
match = bin_iter(k,key,low,high)
time.sleep(1)
end = time.time()
if match==None:
    print("Unsuccessfull search")
else:
    print("Key Found at "+ str(match+1))
    print ("Time taken: " + str(end-start) + " seconds")

print("Recursive binary: ")
start = time.time()
match = bin_rec(k,key,low,high)
time.sleep(1)
end = time.time()
if match==None:
    print("Unsuccessfull search")
else:
    print("Key Found at "+ str(match+1))
    print ("Time taken: " + str(end-start) + " seconds")