# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que determina a soma e a média aritmética dos valores pares no intervalo de 50 a 70.

soma = 0
contador = 50
quantidade = 0

while contador <= 70:
    if contador % 2 == 0:
        soma += contador
        quantidade += 1
    contador += 1

media = soma / quantidade
print("Soma dos valores pares de 50 a 70:", soma)
print("Média aritmética dos valores pares:", round(media, 2))
