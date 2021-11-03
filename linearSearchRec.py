def linearSearch(arr, n, key, pos):
    if pos >= n :
        return 0
    elif arr[pos] == key :
        return pos
    else :
        return linearSearch(arr, n, key, pos+1)

n = int(input("Enter the number of array elements"))
print("enter the array elements")
arr = []
for i in range(0,n):
    num = int(input())
    arr.append(num)

print("enter the search value")
key = int(input())

result = linearSearch(arr, n, key, 0)

if result != 0 :
    print("Element found at position : ", result + 1)
else : 
    print("Element not found")
        
