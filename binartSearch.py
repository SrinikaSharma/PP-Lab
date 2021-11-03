def binarySearch(arr, n, key):
    high  = n - 1
    low = 0 
    while low <= high :
        mid = (low + high) // 2
        if arr[mid] == key :
            return mid
        elif arr[mid] < key : 
            low = mid  + 1
        else : 
            high = mid - 1
    return -1

n =  int(input("Enter the number of elements"))
arr = []
print("enter the elements")
for i in range(0,n) : 
    num = int(input())
    arr.append(num)

key = int(input("Enter the search value"))
arr.sort()
result = binarySearch(arr,n,key)
if result == -1 :
    print("Element not found")
else : 
    print("Element found at position  : ", result + 1)
