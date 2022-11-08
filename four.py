# insertion sort

arr = [15,12,54,13,56,90]
print("Original List : " , arr)

for i in range(1 , len(arr)):
  key = arr[i]
  j = i-1

  while j >= 0 and key < arr[j]:
    arr[j+1] = arr[j]
    j -= 1
  
  arr[j+1] = key
  
print("List after sorting : " , arr)






