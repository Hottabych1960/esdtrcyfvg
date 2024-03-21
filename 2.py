import csv

with open('students.csv', 'r', encoding='utf-8') as infile:
    data = [elem for elem in csv.reader(infile, delimiter=',')][1:]
    array = '[]'
    print(data)
    for i in range(len(data) - 1):
        MIN = i
        print(data[i])
        if 'None' not in data[i]:
            for j in range(i + 1, len(data)):
                if int(data[j][-1]) < int(data[MIN][-1]):
                    MIN = j
            data[i], data[MIN] = data[MIN], data[i]


print('10 класс:')
k = 1
for row in data:
    if k < 4:
        if '10' in row[3]:
            fio = row[1].split()
            name, surname = fio[1][0], fio[0]
            print(f'{k} место: {name}.{surname}')
            k += 1