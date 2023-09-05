try:
    num = int(input("Digite um número inteiro positivo: "))
    if num < 0:
        print("01 - Erro: Você deve digitar um número inteiro positivo")
        exit()
except ValueError:
    print("02 - Erro: Você deve digitar um número inteiro positivo válido")
    exit()

print('''Escolha uma das bases para conversão:
[1] Binario
[2] Octal
[3] Hexadecimal''')
option = int(input("Sua opção: "))


if option ==1:
    print(f"{num} convertido para Binário é igual a {bin (num)[2:]}")
elif option ==2:
    print(f"{num} convertido para Octal é igual a {oct(num)[2:]}")
elif option ==3: 
    hex_result = hex(num)[2:]
    print(f"{num} convertido para Hexadecimal é igual a {hex_result}")
else:
    print("opção invalida")
