def isinteger(n):
    n = n.lstrip()
    n = n.rstrip()
    if len(n) >= 1 and n.isdigit():
        return True
    elif n[0] == "+" and n[1:].isdigit():
        return True
    elif n[0] == "-" and n[1:].isdigit():
        return True
    else:
        return False
    
def main():
    n = input("Digite uma string: ")
    if isinteger(n):
        print("Ela representa um número inteiro")
    else:
        print("Ela não representa um número inteiro")
if __name__ == "__main__":
    main()