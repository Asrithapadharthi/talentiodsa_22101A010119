#the first number is 64
def divide(n):
    #this statement prints the number 64
    print(int(n))
    #here the n[which is 64]!=1 so we skip the bas case [which is return "n"or "1"]
    if n==1:
        return n#1
    #since we skipped the base case now we call the function itself
    #divide(n//2)means divide(64//2)[32]
    #which then becomes divide(32)
    #now the above process repeats
    #when n becomes 1 we stop the recursion
    divide(n//2)
divide(64)
