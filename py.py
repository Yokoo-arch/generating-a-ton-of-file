import timeit
def tris(l:list):
    for i in enumerate(l):
        print(i)

def recherche(l:list, x):
    if x in l:
        return l.index(x)
    return -1

#tris([1, 9, 2, 8, 4, 3])
print(recherche([1, 2, 4, 6, 7], 4))

print("Time elapsed: {:2f}s.".format(timeit.timeit(lambda: recherche([1, 2, 4, 6, 7], 4), number=1_000_000)))