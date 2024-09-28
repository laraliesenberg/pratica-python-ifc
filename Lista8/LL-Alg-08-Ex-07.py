def binário_iterativa(q):
    result = ""
    while q != 0:
        r = q % 2
        result = str(r) + result
        q = q // 2
    return result

q = 20
print(f'O número binário do número decimal {q} é {binário_iterativa(q)}')