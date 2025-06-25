def sol(arr,k):
    a=[]
    for i in arr:
        if i!=k:
            a.append(i)
    return a
arr=[1,2,3,2,4,2,5]
k=2
print(sol(arr,k))
    