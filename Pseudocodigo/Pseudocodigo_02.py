print("Bem-Vindo à Calculadora \n")

num1 = float(input("insira um número:\n"))

num2 = float(input("insira outro número:\n"))

op = input("Selecione uma operação (+, -, *, /): \n")

if op == "+":
    resultado = num1 + num2
    print("O resultado é: " , resultado)

elif op == "-":
    resultado = num1 - num2
    print("O resultado é: " , resultado)

elif op == "*":
    resultado = num1 * num2
    print("O resultado é:" , resultado) 

elif op == "/":
    resultado = num1 / num2
    print("O resultado é: " , resultado)  

else:
    print("Operação inválida.")         




