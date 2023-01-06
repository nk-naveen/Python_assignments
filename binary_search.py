
def binary_search(arr, start, end, x):

   
    if(end >= start):

        mid = start + (end-start)//2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x :
            return binary_search(arr, start, mid-1, x)
        else:
            return binary_search(arr, mid+1, end , x)

    else:
        return -1

arr = []
print("Enter 10 Numbers in ascending order:")
for i in range(10):
    arr.insert(i, int(input()))
print("Enter a num to find:")
x = int(input())

start = 0
end = len(arr)-1

res =  binary_search(arr, start, end, x)
if res != -1:
    print("element is present at %d" % res)
else:
    print("element not")    
