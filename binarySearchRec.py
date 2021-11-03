def binarySearch(arr, n, key, low, high):
    if low <= high :
        mid = (low + high) // 2
        if arr[mid] == key :
            return mid
        elif arr[mid] > key :
            return binarySearch(arr,n,key,low,mid-1)
        elif arr[mid] < key :
            return binarySearch(arr,n,key,mid+1,high)
    return -1

n = int(input("enter the number of elements"))
arr = []
print("Enter the elements")
for i in range(0,n) :
    num = int(input())
    arr.append(num)
key = int(input("enter the value to be searched"))
arr.sort()
result = binarySearch(arr,n,key,0,n-1)
if result == -1 :
    print("Element not found")
else :
    print("Element found at postion", result + 1)

