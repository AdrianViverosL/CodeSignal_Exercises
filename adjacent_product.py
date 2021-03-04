def adjacentElementsProduct(inputArray):
    temp = 0
    for x in range(len(inputArray)-1):
        product = inputArray[x] * inputArray[x+1]
        if product > temp:
            temp = product 

    return temp

nums = [4, 6, -2, -5, 7, 3]

print(adjacentElementsProduct(nums))