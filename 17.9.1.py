try:
    array = list(map(int, input("Введите список  чисел: ").split()))
except ValueError as e:
    print('Введите целые числа')
    array = list(map(int, input("Введите список целых чисел: ").split()))

try:
    element = int(input("Введите число для поиска: "))
except ValueError as e:
    print('Введите целое число')
    element = int(input("Введите целое число для поиска: "))

for i in range(len(array)):
    for j in range(len(array)-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]


def binary_search(array, element, left, right): #функция бинарного поиска индекса искомого элемента
    if left >= right:
        return False
    middle = (right + left) // 2
    if array[middle] < element <= array[middle + 1]:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

print(f'Список отсортирован по возростанию {array}')

if not binary_search(array, element, 0, len(array)):
    rI = min(array, key=lambda x: (abs(x - element), x))
    ind = array.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < element:
        print(f'''В списке нет введенного элемента 
Ближайший меньший элемент: {rI}, его индекс: {ind}
Ближайший больший элемент: {array[max_ind]} его индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {array.index(rI)}
В списке нет меньшего элемента''')
    elif rI > element:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {array.index(rI)}
Ближайший меньший элемент: {array[min_ind]} его индекс: {min_ind}''')
    elif array.index(rI) == 0:
        print(f'Индекс введенного элемента: {array.index(rI)}')
else:
    print(f'Индекс введенного элемента: {binary_search(array, element, 0, len(array))}')
