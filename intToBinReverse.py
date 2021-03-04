def intToReverseBin(n):
    return int(bin(n)[:1:-1],2)

print(intToReverseBin(8))