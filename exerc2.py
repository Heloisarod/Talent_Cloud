def calculadora_interativa():
    while True:
        print("Operações disponíveis:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        escolha = input("Digite o número para a operação desejada: ")

        if escolha == '0':
            print("Saindo da calculadora. Até a próxima!")
            break

        if escolha in {'1', '2', '3', '4'}:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = 0

                if escolha == '1':
                    resultado = num1 + num2
                elif escolha == '2':
                    resultado = num1 - num2
                elif escolha == '3':
                    resultado = num1 * num2
                elif escolha == '4' and num2 != 0:
                    resultado = num1 / num2
                else:
                    print("Erro: Divisão por zero.")
                    continue

                print(f"Resultado: {resultado}")

            except ValueError:
                print("Erro: Insira números válidos.")
        else:
            print("Essa opção não existe. Tente novamente.")

# Executar a calculadora
calculadora_interativa()
