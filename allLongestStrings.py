def allLongestStrings(inputArray):
    lng_strings = []
    lngths_lst = []
    for word in inputArray:
        lngths_lst.append(len(word))
    
    max_value = max(lngths_lst)

    for word in inputArray:
        if (len(word) == max_value):
            lng_strings.append(word)
    
    return(lng_strings)

inputArray = ["aba", "aa", "ad", "vcd", "aba"]

longest_words = allLongestStrings(inputArray)
print(longest_words)