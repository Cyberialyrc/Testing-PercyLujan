def stats(lst):
    min = None
    max = None
    freq = {}
    for i in lst:
        if min is None or i < min:
            min = i
        if max is None or i > max:
            max = i
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    lst_sorted = sorted(lst)
    if len(lst_sorted) % 2 == 0:
        middle = int(len(lst_sorted) / 2)
        median = (lst_sorted[middle] + lst_sorted[middle - 1]) / 2
    else:
        median = lst_sorted[int(len(lst_sorted) / 2)]
    mode_times = None
    for i in freq.values():
        if mode_times is None or i > mode_times:
            mode_times = i
    mode = []
    for (num, count) in freq.items():
        if count == mode_times:
            mode.append(num)
    print("list = " + str(lst))
    print("min = " + str(min))
    print("max = " + str(max))
    print("median = " + str(median))
    print("mode(s) = " + str(mode))

def test():
    # Caso impar (longitud 5), con un solo modo
    stats([3, 1, 2, 5, 4])

    # Caso par (longitud 6), con múltiple modo
    stats([1, 2, 2, 3, 3, 4])

    # Caso con todos los valores iguales
    stats([7, 7, 7, 7])

    # Caso con solo un elemento
    stats([10])

test()
