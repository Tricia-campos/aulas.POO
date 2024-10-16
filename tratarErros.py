try:
    print(x)
except NameError:
    print("O x não existe")

try:
    ok=int(input('digite:'))

except ValueError:
    print("digite numeros")

