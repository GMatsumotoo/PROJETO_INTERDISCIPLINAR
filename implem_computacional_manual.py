def decimal_para_binario(decimal):
    binario = ""
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal //= 2
    return binario

def decimal_para_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        resto = decimal % 16
        if resto < 10:
            hexadecimal = str(resto) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + resto - 10) + hexadecimal
        decimal //= 16
    return hexadecimal

def decimal_para_octal(decimal):
    octal = ""
    while decimal > 0:
        resto = decimal % 8
        octal = str(resto) + octal
        decimal //= 8
    return octal

def binario_para_decimal(binario):
    decimal = 0
    for digito in binario:
        decimal = decimal * 2 + int(digito)
    return decimal

def hexadecimal_para_decimal(hexadecimal):
    decimal = 0
    for digito in hexadecimal:
        if digito.isdigit():
            decimal = decimal * 16 + int(digito)
        else:
            decimal = decimal * 16 + ord(digito) - ord('A') + 10
    return decimal

def octal_para_decimal(octal):
    decimal = 0
    for digito in octal:
        decimal = decimal * 8 + int(digito)
    return decimal

def exibir_menu():
    print("Escolha a operação desejada:")
    print("1. Decimal para Binário")
    print("2. Decimal para Hexadecimal")
    print("3. Decimal para Octal")
    print("4. Binário para Decimal")
    print("5. Hexadecimal para Decimal")
    print("6. Octal para Decimal")
    print("0. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Digite o número da operação desejada: ")

        if opcao == "0":
            print("Saindo...")
            break
        elif opcao == "1":
            decimal = int(input("Digite o número decimal: "))
            print("Binário:", decimal_para_binario(decimal))
        elif opcao == "2":
            decimal = int(input("Digite o número decimal: "))
            print("Hexadecimal:", decimal_para_hexadecimal(decimal))
        elif opcao == "3":
            decimal = int(input("Digite o número decimal: "))
            print("Octal:", decimal_para_octal(decimal))
        elif opcao == "4":
            binario = input("Digite o número binário: ")
            print("Decimal:", binario_para_decimal(binario))
        elif opcao == "5":
            hexadecimal = input("Digite o número hexadecimal: ")
            print("Decimal:", hexadecimal_para_decimal(hexadecimal))
        elif opcao == "6":
            octal = input("Digite o número octal: ")
            print("Decimal:", octal_para_decimal(octal))
        else:
            print("Opção inválida. Por favor, digite novamente.")

if __name__ == "__main__":
    main()
