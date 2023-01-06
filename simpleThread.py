import os
import random as rnd
import timeit
import math
import concurrent.futures as ccr

"""
Performance :
School Computer : 0.007235622000007424s per file
"""
# save data to a file
def saveFile(filepath, data):
    # open the file
    with open(filepath, 'w') as handle:
        # save the data
        handle.write(data)
        print(filepath)
 
# generate a line of mock data of 10 random data points
def generateLine():
    return ','.join([str(rnd.randint(1, 9)) for _ in range(10)])
 
# generate file data of 10K lines each with 10 data points
def generateFileData():
    # generate many lines of data
    lines = []
    for _ in range(1000):
        lines.append(generateLine())
    # convert to a single ascii doc with new lines
    return '\n'.join(lines)
 
def generateAllFiles(nb: int, path='tmp'):
    # create a local directory to save files
    os.makedirs(path, exist_ok=True)
    # create all files
    for i in range(nb):
        # generate data
        data = generateFileData()
        # create filenames
        filepath = os.path.join(path, f'data-{i:04d}.csv')
        # save data file
        saveFile(filepath, data)
        # report progress
        print(f'.created {filepath}')

def deleteFileFromDir(path: str):
    for file in os.listdir(path):
        f_path = os.path.join(path, file)
        os.remove(f_path)
        print(f'.removed {f_path}')

def test(nbOfFile = 500):
    #   timeit for calculating the time it takes
    tToCreate = timeit.timeit(
        lambda: generateAllFiles(nbOfFile, "D:/Code/Python/search_script/test_dir"), 
        number=1)
    tToRemove = timeit.timeit(
        lambda: deleteFileFromDir("D:/Code/Python/search_script/test_dir"), 
        number=1)
    #   Debug
    print(f".create take {tToCreate} s\n{tToRemove/nbOfFile}s/file in average\n")
    print(f".delete take {tToRemove} s\n{tToRemove/nbOfFile}s/file in average")

test(1000)