def sol(str1,str2):
    a=sorted(str1)
    b=sorted(str2)
    if a==b:
        return True
    return False
str1=input()
str2=input()
print(sol(str1,str2))