arr=[12,11,13,5,6] #array to be sorted
n=len(arr)   #length of array
for i in range(1,n): #loop for passes
    key=arr[i]  #current element to be inserted and take the copy of the current element
    j=i-1  #index of the previous element
    while j>=0 and key<arr[j]: #loop for each pass
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print(arr)