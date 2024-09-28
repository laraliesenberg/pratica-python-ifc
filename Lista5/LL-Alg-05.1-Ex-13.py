def segmento(a, b):
    a_str = str(a)
    b_str = str(b)
    if a_str in b_str or b_str in a_str:
        if a < b:
            print("a é segmento de b")
        else:
            print("b é segmento de a")
    else:
        print("Um não é elemento do outro")
segmento(123456, 234)
