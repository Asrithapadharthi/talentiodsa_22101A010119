#53,283,35,88
def pro(arr,k):
    i=0
    j=k
    max_array=0
    while j<len(arr):
        a=sum(arr[i:j])
        if a>max_array:
           max_array=a
        i+=1
        j+=1
    return max_array
arr=[2,1,5,1,3,2]
k=3
print(pro(arr,k))
           



