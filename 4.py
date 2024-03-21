import csv
from random import *

with open('students.csv', 'r', encoding='utf-8') as infile:
    data = [elem for elem in csv.reader(infile, delimiter=',')]
    data0 = data.pop(0) + ['login', 'password']
    print(data)
    alf1 = 'qwertyuiopasdfghjklzxcvbnm'
    alf2 = '0123456789'
    alf = alf1 + alf1.upper() + alf2
    for row in data:
        f = False
        while not f:
            psw = ''.join(choices(alf, k=8))
            if all((any(el in alf1 for el in psw), any(el in alf2 for el in psw), any(el in alf1.upper() for el in psw))):
                f = True
        res = ''
        fio = row[1].split()
        name, surname, ot = fio[1][0], fio[0], fio[2][0]
        row += [psw, f'{surname}_{name}{ot}']

with open('student_password.csv', 'w', encoding='utf-8') as outfile:
    print(','.join(data0), file=outfile)
    for row in data:
        print(','.join(row), file=outfile)