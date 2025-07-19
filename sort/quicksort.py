import random

def randomized_quicksort(arr, low=0, high=None):
    """
    Sorts arr[low..high] in-place using Randomized Quicksort.
    :param arr: list of comparable elements
    :param low: start index
    :param high: end index (inclusive)
    :return: the same list, sorted in ascending order
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Partition around a randomly chosen pivot
        p = _randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, p - 1)
        randomized_quicksort(arr, p + 1, high)
    return arr


def _randomized_partition(arr, low, high):
    pivot_idx = random.randint(low, high)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    return _partition(arr, low, high)


def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def deterministic_quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        arr[low], arr[high] = arr[high], arr[low]
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        p = i + 1
        deterministic_quicksort(arr, low, p - 1)
        deterministic_quicksort(arr, p + 1, high)

