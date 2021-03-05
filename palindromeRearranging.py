def palindromeRearranging(inputString):
    lst = []
    for char in inputString:
        if (any([char in list for list in lst])) == False:
            n = inputString.count(char)
            lst.append([char, n])
            
    odds = [i[1] for i in lst if i[1]%2 != 0]
    
    return ((len(inputString)%2 == 0 and len(odds)== 0) or (len(inputString)%2 != 0 and len(odds)<2))

print(palindromeRearranging("zaa")) #True 
print(palindromeRearranging("aabb"))    #True
print(palindromeRearranging("aabcaa"))  #False
