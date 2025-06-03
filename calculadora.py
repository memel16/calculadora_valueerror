try:

    num1=int(input("Digite o numero 1 "))
    num2=int(input("Digite o numero 2"))



    print("Escolha uma operação:")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")

operacao = input("Digite o símbolo da operação (+, -, *, /): ")

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    resultado == num1 / num2

else:
    resultado = "Erro:"

    print("Resultado:", resultado)

    except ValueError:
print(f"ocorreu um erro durante a operação no {ValueError}")
