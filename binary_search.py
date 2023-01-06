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


arr = [2,3,4,6,9,10,85,100,500] 
x = 85

start = 0
end = len(arr) - 1
res = binary_search(arr,start,end ,x )


if res != -1:
    print("element is present in %d" % res)
else:
    print("element not")    
