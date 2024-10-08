nome = input('Digite seu nome completo: ')
print('Nome completo: ', nome)
while True: # enquanto não digitar um valor válido, pede que digite novamente
    try:
        ano_nascimento = int(input('Digite ano de Nascimento(entre 1922 e 2021):'))
        if 1922 <= ano_nascimento <= 2021:
            print(f"O usuário {nome} completou ou completará {2022 - ano_nascimento} em 2022: ")
            break # valor válido, sai do while
        # se não entrou no if acima, o valor é inválido
        print('Ano deve ser entre 1922 e 2021, formato: YYYY: ')
    except ValueError: # não foi digitado um número
        print('Digite um número válido')
