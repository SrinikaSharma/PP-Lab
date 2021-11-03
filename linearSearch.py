def linearSearch(arr, n, key):
    for i in range(0,n):
        if arr[i] == key :
            return i
    return -1

n = int(input("enter the number of array elements"))
print("Enter the elements")
arr = []
for i in range(0,n):
    value = int(input( ))
    arr.append(value)

print("Enter the search value")
key = int(input())

result = linearSearch(arr,n,key)
if result == -1 :
    print("Element not found")
else :
    print("Element found at position: ",result + 1)


        
    

