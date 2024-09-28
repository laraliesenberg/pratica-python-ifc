def permutação(a, b):
    #convertendo int para str
    a_str = str(a)
    b_str = str(b)

    #convertendo os números para uma lista de dígitos
    lista_a = list(a_str)
    lista_b = list(b_str)

    #ordenando a lista
    lista_a.sort()
    lista_b.sort()

    if  lista_a == lista_b:
        print("a é permutação de b")
    else:
        print("a não é permutação de b")
permutação(12334, 43213)