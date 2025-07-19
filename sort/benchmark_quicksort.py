import random
import sys
import time

from sort.quicksort import randomized_quicksort, deterministic_quicksort

sys.setrecursionlimit(1000000)


def benchmark():
    sizes = [10 ** 3, 10 ** 4]
    distributions = {
        "Random": lambda n: [random.randint(0, n) for _ in range(n)],
        "Sorted": lambda n: list(range(n)),
        "Reverse": lambda n: list(range(n, 0, -1)),
        "Repeated": lambda n: [random.choice([1, 2, 3, 4, 5]) for _ in range(n)]
    }

    print("| Size | Distribution | Randomized QS (ms) | Deterministic QS (ms) |")

    for size in sizes:
        for name, gen in distributions.items():
            data = gen(size)

            arr1 = data.copy()
            start = time.perf_counter()
            randomized_quicksort(arr1)
            t_rand = (time.perf_counter() - start) * 1000

            arr2 = data.copy()
            start = time.perf_counter()
            deterministic_quicksort(arr2)
            t_det = (time.perf_counter() - start) * 1000

            print(f"| {size} | {name:^10s} | {t_rand:>18.3f} | {t_det:>22.3f} |")


if __name__ == "__main__":
    benchmark()
