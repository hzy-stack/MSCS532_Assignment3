import unittest
import random

from sort.quicksort import randomized_quicksort


class TestRandomizedQuicksort(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(randomized_quicksort([]), [])

    def test_single_element(self):
        self.assertEqual(randomized_quicksort([42]), [42])

    def test_already_sorted(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(randomized_quicksort(data.copy()), data)

    def test_reverse_sorted(self):
        data = [5, 4, 3, 2, 1]
        self.assertEqual(randomized_quicksort(data.copy()), sorted(data))

    def test_repeated_elements(self):
        data = [3, 1, 2, 3, 3, 0, 1, 2]
        self.assertEqual(randomized_quicksort(data.copy()), sorted(data))

    def test_random_arrays(self):
        for _ in range(20):
            size = random.randint(0, 50)
            arr = [random.randint(-100, 100) for _ in range(size)]
            expected = sorted(arr)
            self.assertEqual(randomized_quicksort(arr.copy()), expected)


if __name__ == "__main__":
    unittest.main()
