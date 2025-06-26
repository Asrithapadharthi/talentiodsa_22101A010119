def sol(arr):
    a=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[a]=arr[i]
            a+=1
    for i in range(a,len(arr)):
        arr[i]=0
arr=[0,1,0,3,12]
sol(arr)
print(arr)
def sol(arr):
    i = 0
    j = 0
    while j < len(arr):
        if arr[j] != 0:
            arr[i] = arr[j]
            i += 1
        j += 1
    while i < len(arr):
        arr[i] = 0
        i += 1
    return arr

print(sol([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]
