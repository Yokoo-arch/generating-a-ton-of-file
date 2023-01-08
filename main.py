import random
import timeit
import cProfile
import io
import pstats

def measure_perf(nb):
    def wrapper(func):
        def inner(*args, **kwargs):
            # Measure execution time with timeit
            time = timeit.timeit(lambda: func(), number=10000)
            print(f'test_function took {time:.6f} seconds to complete with timeit')

            # Measure execution time and other performance stats with cProfile
            pr = cProfile.Profile()
            pr.enable()
            result = func(*args, **kwargs)
            pr.disable()
            s = io.StringIO()
            ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
            ps.print_stats()
            profiler_result = s.getvalue()
            return result, profiler_result
        return inner
    return wrapper

@measure_perf(1000)
def generateCsvLine(n_list:list):
    #   Shuffling the list
    random.shuffle(n_list)
    #   Tranforming the int list into a str list
    n_list = [str(n) for n in n_list]
    return ','.join(n_list)

l = random.sample(range(1, 10), 9)
result, profiler_result = 