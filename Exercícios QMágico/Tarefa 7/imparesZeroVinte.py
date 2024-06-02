# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que lista todos os valores numéricos inteiros ímpares na faixa de 0 a 20.

numero = 0

while numero <= 20:
    if numero % 2 != 0:
        print(numero)
    numero += 1