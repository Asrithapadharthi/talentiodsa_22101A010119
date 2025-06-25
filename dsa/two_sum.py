def sol(arr,target):
    a=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                a.append(i)
                a.append(j)
    return a
arr=[2,7,5,8,9]
target=9
print(sol(arr,target))