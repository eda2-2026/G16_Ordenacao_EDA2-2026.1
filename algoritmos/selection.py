def selectionSort(v: list[int]) -> int:
    temp = 0
    size = len(v)
    for i in range(0, size-1):
        index_min = i
        for j in range(1, size-1):
            if v[index_min] > v[j]:
                index_min = j
        if index_min != i:
            temp = v[index_min]
            v[index_min] = v[i]
            v[i] = temp
    return v
