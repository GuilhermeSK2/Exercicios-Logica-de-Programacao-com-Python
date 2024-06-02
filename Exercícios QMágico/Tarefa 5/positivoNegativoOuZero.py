# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Recebe um número e verifica se é positivo, negativo ou zero.

numero = int(input("Digite um número para saber se é positivo ou negativo: "))

if numero > 0:
    print("O número", numero, "é positivo!")
elif numero < 0:
    print("o número", numero, "é negativo!")
else:
    print("O número é zero!")