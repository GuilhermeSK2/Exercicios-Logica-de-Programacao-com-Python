# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que apresenta como resultado o valor do fatorial dos valores ímpares situados na faixa numérica de 1 a 10.

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

for i in range(1, 11):
    if i % 2 != 0:
        print("O fatorial de" ,i, "é", fatorial(i))