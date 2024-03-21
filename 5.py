def hsh(st):
    alf = ''.join(sorted('ёйцукенгшщзхъфывапролджэячсмитьбю'))
    alf = alf.upper() + ' ' + alf
    sth = [alf.index(el) + 1 for el in st]
    p, m, s = 67, 10 ** 9 + 9, 0
    for i in range(len(sth)):
        s += sth[i] * (p ** i % m)
    return s

