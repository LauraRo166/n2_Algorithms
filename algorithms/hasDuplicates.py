def hasDuplicates(array):
    """
    Checks if a list contains any duplicate elements.

    :param array: List of hashable elements.
    :return: True if duplicates exist, False otherwise.
    """
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                return True
    return False