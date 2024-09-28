def encaixa(a, b):
    a = str(a)
    b = str(b)
    tamanho_a = len(a)
    tamanho_b = len(b)
    encaixa = True
    print("a\tb\t")
    for i in range(tamanho_b):
        if a[tamanho_a - 1 - i] != b[tamanho_b - 1 - i]:
            encaixa = False
            break
    if encaixa:
        print(f"{a}\t{b}\tEncaixa")
    else:
        print(f"{a}\t{b}\tNão encaixa")
        
a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))
encaixa(a, b)