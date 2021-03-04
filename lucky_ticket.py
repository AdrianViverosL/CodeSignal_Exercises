def isLucky(n):
    num_str = str(n)
    size = len(num_str) // 2

    left_sum = sum([int(i) for i in list(num_str[:size])])
    right_sum = sum([int(i) for i in list(num_str[size:])])

    if(left_sum == right_sum):
        return True
    else:
        return False

print(isLucky(1230))
print(isLucky(239017))
#isLucky(1230)
