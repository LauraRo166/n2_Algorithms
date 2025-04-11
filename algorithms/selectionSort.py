def selectionSort(array):
    """
    Sorts a list in ascending order using the selection sort algorithm.

    :param array: List of comparable elements.
    :return: Sorted list.
    """
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array