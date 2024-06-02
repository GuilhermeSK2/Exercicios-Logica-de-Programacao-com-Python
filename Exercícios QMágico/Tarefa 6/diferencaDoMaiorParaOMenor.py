# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

valor1 = int(input("Digite um valor:"))
valor2 = int(input("Digite um segundo valor:"))

if valor1 > valor2:
    calculo = valor1 - valor2
    print("A diferença entre os dois valores é de:",calculo)
else:
    calculo = valor2 - valor1
    print("A diferença entre os dois valores é de:",calculo)