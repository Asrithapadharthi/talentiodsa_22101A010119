def sol(arr):
    sums=0
    mid=len(arr)//2
    for i in arr:
        sums+=i
    avg=sums//2
    sorted_arr=sorted(arr)
    if len(arr)%2==0:
            median=(sorted_arr[mid]+sorted_arr[mid-1] )/2
    else:
       median=sorted_arr[mid]
    return f"sum={sums} average={avg} median={median}"
arr=list(map(int,input().strip().split()))
print(sol(arr))
