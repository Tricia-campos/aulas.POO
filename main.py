from biblioteca import *

while True:
    opcoes=int(input(f"Digite a opção desejada:\n"
                     f"1- Gravar\n"
                     f"2- Ler\n"
                     f"3- Sair\n"))
    match opcoes:
        case 1:
            t = input("Digite um texto:")
            gravar(t)
        case 2:
            ler()
        case 3:
            break
        case 4:
            print("invalido")
