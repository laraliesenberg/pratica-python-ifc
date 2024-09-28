def conta_digitos(n, d):
    n = str(n)
    d = str(d)
    contando_d = n.count(d)
    print(f'O dígito {d} aparece {contando_d} vezes em {n}')
conta_digitos(29032006, 0)