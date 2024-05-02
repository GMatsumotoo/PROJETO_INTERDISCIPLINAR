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
            print("Binário:", bin(decimal))
        elif opcao == "2":
            decimal = int(input("Digite o número decimal: "))
            print("Hexadecimal:", hex(decimal))
        elif opcao == "3":
            decimal = int(input("Digite o número decimal: "))
            print("Octal:", oct(decimal))
        elif opcao == "4":
            binario = input("Digite o número binário: ")
            print("Decimal:", int(binario, 2))
        elif opcao == "5":
            hexadecimal = input("Digite o número hexadecimal: ")
            print("Decimal:", int(hexadecimal, 16))
        elif opcao == "6":
            octal = input("Digite o número octal: ")
            print("Decimal:", int(octal, 8))
        else:
            print("Opção inválida. Por favor, digite novamente.")

if __name__ == "__main__":
    main()
