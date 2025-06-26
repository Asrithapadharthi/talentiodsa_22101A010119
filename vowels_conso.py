#def sol(a):
    #vowel="AEIOUaeiou"
    #vowels=0
    #consonants=0
    #for i in a:
        #if i in vowel:
           # vowels+=1
        #else:
        # consonants+=1
   # return f"vowels={vowels} consonants={consonants}"
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowel= 0
    consonant= 0
    i = 0
    j = len(s) - 1

    while i <= j:
        
        if s[i].isalpha():
            if s[i] in vowels:
                vowel+= 1
            else:
                consonant+= 1
        
        
        if i != j and s[j].isalpha():
            if s[j] in vowels:
                vowel+= 1
            else:
                consonant+= 1
        
        i += 1
        j -= 1

    return vowel, consonant
print(count_vowels_consonants("hello"))
