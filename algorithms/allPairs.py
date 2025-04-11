def allPairs(array):
    """
    Generates all possible ordered pairs (i, j) from the list.

    :param array: List of elements.
    :return: List of tuples with all possible (element_i, element_j) combinations.
    """
    pairs = []
    for i in range(len(array)):
        for j in range(len(array)):
            pairs.append((array[i], array[j]))
    return pairs