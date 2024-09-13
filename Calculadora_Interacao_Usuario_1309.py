def calculadora():
    while True:
        # Mostrar o menu de opções
        print("\nEscolha uma operação:")
        print("\033[1m 1: Soma \033[0m")
        print("\033[1m 2: Subtração \033[0m")
        print("\033[1m 3: Multiplicação \033[0m")
        print("\033[1m 4: Divisão \033[0m")
        print("\033[1m 0: Sair \033[0m")
        
        # Ler a escolha do usuário
        opcao = input("Digite o número para a operação correspondente: ")
        
        # Verificar se o usuário deseja sair
        if opcao == '0':
            print("Saindo do programa...")
            break
        
        # Verificar se a opção é válida
        if opcao not in {'1', '2', '3', '4'}:
            print("Essa opção não existe. Tente novamente.")
            continue
        
        # Pedir os dois valores para a operação
        try:
            valor1 = float(input("Digite o primeiro valor: "))
            valor2 = float(input("Digite o segundo valor: "))
        except ValueError:
            print("Opção digitada inválida. Digite uma das opções válidas.")
            continue
        
        # Executar a operação selecionada
        if opcao == '1':
            resultado = valor1 + valor2
            operacao = "Soma"
        elif opcao == '2':
            resultado = valor1 - valor2
            operacao = "Subtração"
        elif opcao == '3':
            resultado = valor1 * valor2
            operacao = "Multiplicação"
        elif opcao == '4':
            # Tratar divisão por zero
            if valor2 == 0:
                print("Erro: Divisão por zero não é permitida.")
                continue
            resultado = valor1 / valor2
            operacao = "Divisão"
        
        # Mostrar o resultado
        print(f"Resultado da {operacao}: {resultado}")

# Rodar a calculadora
calculadora()
