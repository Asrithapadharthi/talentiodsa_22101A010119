def problem(arr):
    a=sorted(arr)
    if arr==a:
        return True
    return False
arr=[1,5,3,9,2]
print(problem(arr))