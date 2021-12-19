
def bubble_sort(lst, ascending):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if ((lst[j] > lst[j + 1]) and ascending) or ((lst[j] < lst[j + 1]) and not ascending):
                yield True, j, j + 1
            else:
                yield False, j, j + 1
