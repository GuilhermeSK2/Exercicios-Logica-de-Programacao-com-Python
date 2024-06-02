# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que realiza o somatório dos valores pares no intervalo de 1 a 500 e apresenta o total obtido.

total = 0
numero = 1

while numero <= 500:
    if numero % 2 == 0:
        total += numero
    numero += 1

print("Total do somatório dos valores pares de 1 a 500:", total)
