# n2_Algorithms

The following algorithms with **O(n²)** time complexity are implemented:
+ Selection Sort
+ Duplicate Detection (Double Loop)
+ All Possible Pairs

## Complexities Analysis

### Selection Sort
+ **Best Case (O(n²))**: Even if the array is sorted, it still compares each pair.
+ **Worst Case (O(n²))**: All elements must be compared with all others.
+ **Average Case (O(n²))**: Unsorted elements are selected in each pass and compared.

### Duplicate Detection (Double Loop)
+ **Best Case (O(1))**: Duplicate is found at the start of the iteration.
+ **Worst Case (O(n²))**: No duplicates; each element is compared with every other.
+ **Average Case (O(n²))**: Most elements must be compared at least once.

### All Possible Pairs
+ **Best/Worst/Average Case (O(n²))**: All pairs must be generated regardless of input order or value.

## Unit and Coverage Testing



Each function has associated unit tests covering:
- Typical inputs
- Edge cases
- Empty inputs
- Validity of returned results

## Test and Visualization

A script compares execution times across growing input sizes and generates a chart for visualization:


**Explanation:**
- The plot shows the typical quadratic time growth.
- Input sizes grow linearly, but execution time grows roughly by the square.
- This highlights the inefficiency of O(n²) algorithms for large inputs.



