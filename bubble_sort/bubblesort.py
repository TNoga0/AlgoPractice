from copy import deepcopy


test_set = [4, 2, 1, 5, 7]
test_set2 = [1, 7, 99, 2, 0, 12, 15]


def bubble_sort(x):
    """
    Performs the bubble sort operation
    :param x: a list with integers to be sorted
    """
    previous_step_list = []

    while x != previous_step_list:
        previous_step_list = deepcopy(x)
        for i in range(len(x) - 1):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
    return x


print(bubble_sort(test_set))
print(bubble_sort(test_set2))
