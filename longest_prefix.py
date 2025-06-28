def pro(strs):
    strs.sort()
    i=strs[0]
    j=strs[-1]
    a=""
    for num in range(min(len(i),len(j))):
        if i[num]==j[num]:
            a+=i[num]
        else:
            break
    return a
        
strs=["flower","flow","flight"]
print(pro(strs))

