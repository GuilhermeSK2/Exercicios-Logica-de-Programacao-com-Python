# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que solicita a entrada de 10 valores numéricos, calcula o somatório e a média aritmética desses valores, exibindo os resultados.

soma = 0
contador = 1

while contador <= 10:
    valor = float(input("Digite o valor #", contador, ": "))
    soma += valor
    contador += 1

media = soma / 10
print("Total do somatório:", soma)
print("Média aritmética:", round(media, 2))