# quick sort using recursion
def quickSort(list1):
    print("True List is: ", list1)
    if len(list1) <= 1:
        return list1
    else:
        pivot = list1[0]
        print("Pivot is: ", pivot)
        less = [i for i in list1[1:] if i <= pivot]
        print("Less ", less)
        greater = [i for i in list1[1:] if i > pivot]
        print("Greater ", greater)
        return quickSort(less) + [pivot] + quickSort(greater)


if "__main__" == __name__:
    list1 = [5, 2, 4, 6, 1, 3]
    print(quickSort(list1))
