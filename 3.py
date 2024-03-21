import csv

with open('students.csv', 'r', encoding='utf-8') as infile:
    data = [elem for elem in csv.reader(infile, delimiter=',')][1:]
    print(data)
    id = input()
    while id != 'СТОП':
        f = False
        for row in data:
            if id == row[2]:
                fio = row[1].split()
                name, surname = fio[1][0], fio[0]
                print(f'Проект № {id} делал: {name}.{surname} он(а) получил(а) оценку - {row[4]}.')
                f = True
        if not f:
            print('Ничего не найдено.')
        id = input()