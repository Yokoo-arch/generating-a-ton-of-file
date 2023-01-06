import random
import timeit

def generateCsvLine():
    for _ in range(10):
        n_list = [str(n) for n in random.sample(range(1, 10), 9)]
        print(n_list)
    return ','.join(n_list)

elapsed_time = timeit.timeit(lambda: generateCsvLine(), number=1000)
print("Elapsed time1: {:.2f} seconds.".format(elapsed_time))