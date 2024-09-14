def nu_pares():
    while True:
        num = input("Digite um número par: ")
        
        try:
            # Converte para inteiro.
            numero = int(num)
        except ValueError:
            
            print("Você digitou um caractere inválido. Tente novamente.")
            continue
        
        # Verifica se o número é par
        if numero % 2 == 0:
            print(f"Você digitou o número par: {numero}")
            break
        else:
            print("Você digitou um valor ímpar. Tente novamente.")

# Chama a função para iniciar o programa
nu_pares()
