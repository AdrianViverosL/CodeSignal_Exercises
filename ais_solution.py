def almostIncreasingSequence(sequence):
    last = prev = min(sequence) - 1
    warn = False
    for item in sequence:
        if item <= last:
            if warn:
                return False
            else:
                warn = True
            if item >= prev:
                prev = last = item
            else:
                prev = last
        else:
            prev, last = last, item
    return True


print(almostIncreasingSequence([1, 2, 1, 2]))