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

![image](https://github.com/user-attachments/assets/581620ad-1457-4613-9474-ee9556a82a46)


Each function has associated unit tests covering:
- Typical inputs
- Edge cases
- Empty inputs
- Validity of returned results

## Test and Visualization

A script compares execution times across growing input sizes and generates a chart for visualization:

![image](https://github.com/user-attachments/assets/f38de9cf-2c6a-4e10-bea8-60d3da146640)


**Specific Cases**
***Duplicates***

![image](https://github.com/user-attachments/assets/dc8a8388-9784-4b90-921f-da96a24f4c3f)

***Selection Sort***

![image](https://github.com/user-attachments/assets/285d7c76-7a05-46c9-8220-35f75b319516)

***Selection Sort vs Duplicates***

![image](https://github.com/user-attachments/assets/f9b52e0d-a350-4f54-8b5d-736608c2d884)




