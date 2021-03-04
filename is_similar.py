

def areSimilar(a, b):
    temp = [a!=b for a,b in zip(a,b)]
    print(list(temp))
    print(sum(temp))
    return sorted(a) == sorted(b) and sum([a!=b for a,b in zip(a,b)]) <= 2


a = [1, 2, 4]
b = [1, 2, 3]
print(areSimilar(a, b))