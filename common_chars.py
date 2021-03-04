def commonCharacterCount(s1,s2):
    lst_s1 = list(s1)
    lst_s2 = list(s2)
    print(lst_s1)
    print(lst_s2)
    counter = 0

    for char in lst_s1:
        if char in lst_s2:
            lst_s2.remove(char)
            counter +=1
    
    #print(lst_s1)
    print(lst_s2)
    print(counter)
    return counter

s1 = "aabcc"
s2 = "adcaa"

#print(commonCharacterCount(s1, s2))
commonCharacterCount(s1, s2)