def problem(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
       # mid=left+(right-left)//2
        if arr[mid]==target:
            return mid
        elif target<arr[mid]:
            right=mid-1
        else:
            left=mid+1
    return -1
arr=list(map(int,input().split()))
target=int(input())
print(problem(arr,target))
        
