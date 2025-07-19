# MSCS532_Assignment3
MSCS532 Assignment3


### Test randomized quicksort
In MSCS532_Assignment3 folder, run command below
```shell
# Run randomized quick sort test
python3 -m unittest test.randomized_quicksort_test
```

In MSCS532_Assignment3 folder, run command below
```shell
# Run quick sort benchmark comparison.
python3 -m sort.benchmark_quicksort
```

Benchmark Result
```text
| Size | Distribution | Randomized QS (ms) | Deterministic QS (ms) |
| 1000 |   Random   |              1.604 |                  1.002 |
| 1000 |   Sorted   |              1.326 |                 15.517 |
| 1000 |  Reverse   |              1.241 |                 27.627 |
| 1000 |  Repeated  |              9.296 |                  8.485 |
| 10000 |   Random   |             17.157 |                 12.101 |
| 10000 |   Sorted   |             16.236 |               1410.489 |
| 10000 |  Reverse   |             16.760 |               2724.399 |
| 10000 |  Repeated  |            827.723 |                820.851 |
```

### Test hash table
In MSCS532_Assignment3 folder, run command below
```shell
python3 -m unittest test.randomized_quicksort_test
```

