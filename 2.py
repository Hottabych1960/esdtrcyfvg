import csv

with open('students.csv', 'r', encoding='utf-8') as infile:
    data = [elem for elem in csv.reader(infile, delimiter=',')][1:]
    print(data)
    for i in range(len(data)):
        j = i - 1
        key = data[i]
        while float(data[j][4] if data[j][4] != 'None' else 0) < float(key[4] if key[4] != 'None' else 0) and j >= 0:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

print('10 класс:')
k = 1
for row in data:
    if k < 4:
        if '10' in row[3]:
            fio = row[1].split()
            name, surname = fio[1][0], fio[0]
            print(f'{k} место: {name}.{surname}')
            k += 1
