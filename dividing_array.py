def divide(arr,left,right):
    if left>right:
        return 
    #print(arr[left:right+1])
    if left==right:
        print(arr[left])
        return 
    for i in range(left,right+1):
        print(arr[i],end=" ")
    print()
    mid=(left+right)//2
    divide(arr,left,mid)
    divide(arr,mid+1,right)
arr=[10,79,30,22,45,77]
left=0
right=len(arr)-1
divide(arr,left,right)
