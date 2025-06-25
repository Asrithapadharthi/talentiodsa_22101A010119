def problem(arr):
   seen=set()
   a=[]
   for i in arr:
       if i in seen:
           a.append(i)
       seen.add(i)
   return a
arr=[1,2,4,3,2,4]
print(problem(arr))