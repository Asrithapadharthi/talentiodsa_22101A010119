def sol(string):
    a=string.split()
    arr=[]
    for i in a:
        arr.append(i[::-1])
    return " ".join(arr)
string=input()
print(sol(string))