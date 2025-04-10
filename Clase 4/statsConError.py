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
        median = (lst_sorted[middle] + lst_sorted[middle + 1]) / 2  # ❌ ERROR introducido
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
    # Casos previos
    stats([3, 1, 2, 5, 4])         # impar
    stats([1, 2, 2, 3, 3, 4])      # par
    stats([7, 7, 7, 7])            # todos iguales
    stats([10])                   # un solo elemento

    # ✅ Nuevo caso que detecta el error de median con +1
    stats([1, 2, 100, 101])  # La mediana debe ser (2 + 100) / 2 = 51.0, si imprime 100.5 está mal

test()
