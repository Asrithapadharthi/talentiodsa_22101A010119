def problem(arr):
    a=[]
    b=[]
    for i in range(len(arr)):
        if arr[i]%2==0:
            a.append(arr[i])
        else:
          b.append(arr[i])
    return f"Even={len(a)} odd={len(b)}"
arr=[1,2,3,4,5,6]
print(problem(arr))