def calculadora(num1, num2, operacao):
#operações: (+, -, *, /)
  if operacao == '+':
    return num1 + num2
  elif operacao == '-':
    return num1 - num2
  elif operacao == '*':
    return num1 * num2
  elif operacao == '/':
    if num2 == 0:
      return "Erro: Divisão por zero!"
    else:
      return num1 / num2
  else:
    return "Erro: Operação inválida!"

# Usabilidade:
num1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))
resultado = calculadora(num1, num2, operacao)
print("Resultado:", resultado)
