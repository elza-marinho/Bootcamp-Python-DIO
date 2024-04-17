total = 500
limite_saques = 3
quantidade_saques = 0
extrato = ""

while True:
    # Display menu options
    print("Menu:")
    print("1. Saques")
    print("2. Depósitos")
    print("3. Extratos")
    print("0. Sair")

    # Get user input
    opcao = input("Escolha uma opção: ")
    # Process user input
    if opcao == "1":

        if quantidade_saques >= limite_saques:
            print("Limite de saques atingido. Não é possível sacar mais.")


        else:
            valor = float(input("Digite o valor que deseja sacar: "))
        if valor >= total:
            print("Valor maior que o saldo, operação não pode ser realizada.")
        else:
            total -= valor
            quantidade_saques += 1
            print(f"seu saldo atual é R${total:.2f}")
    elif opcao == "2":

        valor = float(input("Digite o valor que deseja depositar: "))
        if valor > 0:
            total += valor
            print(f"seu saldo atual é R${total:.2f}")






    elif opcao == "3":
        print(f"Seu saldo é R$: {total:.2f}")




    elif opcao == "0":
        print("Sair")
        break  # Exit the loop if user chooses to quit
    else:
        print("Opção inválida. Por favor, escolha novamente.")

    # Process user input
