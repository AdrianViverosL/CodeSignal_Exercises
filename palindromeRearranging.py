def palindromeRearranging(inputString):
    part1 = [inputString[i] for i in range(len(inputString)) if i % 2 == 0]
    part2 = [inputString[i] for i in range(len(inputString)) if i % 2 != 0]
    return set(part1)==set(part2)

inputString = "zaa"
print(palindromeRearranging(inputString)) #True or False
