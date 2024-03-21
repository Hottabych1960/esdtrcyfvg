# сортировка выбором
data = [3, 4, 1, 2, 5]
for i in range(len(data) - 1):
    MIN = i
    for j in range(i + 1, len(data)):
        if data[j] < data[MIN]:
            MIN = j
    data[i], data[MIN] = data[MIN], data[i]
print(data)

# сортировка вставками
data = [3, 4, 1, 2, 5]
for i in range(1, len(data)):
    new_elem = data[i] # В new_elem сохранили значение data[i]
    j = i - 1 # Начиная с элемента data[i - 1]
    # все элементы, которые больше new_elem
    while j >= 0 and data[j] > new_elem:
        data[j + 1] = data[j] # сдвигаем вправо на 1
        j -= 1
    # На свободное место записываем new_elem
    data[j + 1] = new_elem
print(data)

# сортировка пузырьком
data = [3, 4, 1, 2, 5]
for j in range(len(data) - 1, 0, -1):
    for i in range(j):
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = data[i + 1], data[i]
print(data)


# быстрая сортировка
def q_sort(data):
    if len(data) <= 1:
        return data
    else:
        q = data[len(data)//2]
    data_mq = [x for x in data if x < q]
    data_eq = [q] * data.count(q)
    data_bq = [x for x in data if x > q]
    print(data_mq, data_eq, data_bq)
    return q_sort(data_mq) + data_eq + q_sort(data_bq)


print(q_sort(data))