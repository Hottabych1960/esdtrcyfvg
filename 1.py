import csv

with open('students.csv', 'r', encoding='utf-8') as infile:
    data = [elem for elem in csv.reader(infile, delimiter=',')]
    print(data)
    dic = {row[3]: [] for row in data[1:]}
    for row in data[1:]:
        if 'Хадаров Владимир' in row[1]:
            print(f'Ты получил: {row[-1]}, за проект - {row[2]}')
        if 'None' not in row:
            dic[row[3]].append(int(row[-1]))
        if 'None' in row:
            dic[row[3]].append(0)
    for row in data[1:]:
        if 'None' in row:
            row[-1] = round(sum(dic[row[3]]) / len(dic[row[3]]), 3)

with open('student_new.csv', 'w', encoding='utf-8') as outfile:
    for row in data:
        print(','.join(row), file=outfile)
