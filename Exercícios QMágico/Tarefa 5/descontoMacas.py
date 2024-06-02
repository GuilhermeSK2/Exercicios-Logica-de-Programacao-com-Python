# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que recebe o número de maçãs compradas e retorna o valor total com ou sem desconto de acordo com o valor unitário e o da dúzia.

quantMacas = int(input("Digite a quantidade de maças compradas (Valor unitário = R$ 1,30 / Valor unitário dentro da dúzia = R$ 1,00)"))

valorQuantTotal = quantMacas * 1.30

valorTotalComDesc = quantMacas * 1.00

if quantMacas >= 12:
    print("O valor total da compra é de", valorTotalComDesc)
else:
    print("O valor total da compra é de", valorQuantTotal)