def arrayMaximalAdjacentDifference(inputArray):
    max_value = 0
    for i in range(0, len(inputArray)-1):
        diff = abs(inputArray[i+1] - inputArray[i])
        if diff > max_value:
            max_value = diff
    
    return max_value

print(arrayMaximalAdjacentDifference([2, 4, 1, 0]))