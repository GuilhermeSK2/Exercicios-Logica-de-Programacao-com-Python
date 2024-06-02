# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que recebe os valores de saldo, do que será débitado e do que será créditado para calcular o saldo atual de uma conta.

numero_conta = input("Digite o número da conta do cliente: ")
saldo = float(input("Digite o saldo atual: "))
debito = float(input("Digite o débito: "))
credito = float(input("Digite o crédito: "))

saldo_atual = saldo - debito + credito

print("O saldo atual é:", round(saldo_atual,2))

if saldo_atual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")