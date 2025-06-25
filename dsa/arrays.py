
#reversing an array
def sol(arr):
   return arr[::-1]
arr=[1,2,3,4,5]
print(sol(arr))
#find the min and max
def sols(array):
   array.sort()
   return array[0] , array[-1]
array=[1,2,3,4,5]
print(sols(array))
#adding two arrays
def solution(a,b):
 sums=[]
 for i in range(len(a)):
   x=a[i]+b[i]
   sums.append(x)
 return sums
a=[1,2,3,4,5]
b=[6,7,8,9,5]
print(solution(a,b))