import csv
import os
import time
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from random import randint

OUTPUT_DIR = './output'
RESULT_FILE = './output/result.csv'


def fib(n: int):
    """Calculate a value in the Fibonacci sequence by ordinal number"""

    f0, f1 = 0, 1
    for _ in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


def create_file(ordinal: int, fibonacci_number: int):
    with open(f'{OUTPUT_DIR}/{ordinal}.txt', 'w') as opened_file:
        opened_file.write(str(fibonacci_number))


def func1(array: list):
    start = time.time()
    with ProcessPoolExecutor(mp_context=mp.get_context('fork')) as executor:
        fib_array = executor.map(fib, array)
    print("Time of Fibonacci numbers calculation:", time.time() - start)

    start = time.time()
    with ThreadPoolExecutor() as executor:
        executor.map(create_file, array, fib_array)
    print("Time of writing numbers to files:", time.time() - start)


def read_file(filename: str):
    with open(f'{OUTPUT_DIR}/{filename}') as opened_file:
        fibonacci_number = int(opened_file.read().strip())
    ordinal = int(filename[:-4])
    return ordinal, fibonacci_number


def func2(result_file: str):
    filenames = os.listdir(OUTPUT_DIR)
    start = time.time()
    with ThreadPoolExecutor() as executor:
        output_data = executor.map(read_file, filenames)
    print("Time of reading files:", time.time() - start)

    with open(result_file, 'w') as opened_file:
        writer = csv.writer(opened_file, delimiter=',')
        writer.writerows(output_data)


if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    i = 0
    for file in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, file)
        os.remove(path)
        i += 1
    print("Removed", i, "old files")

    func1(array=[randint(1000, 10000) for _ in range(1000)])
    func2(result_file=RESULT_FILE)
