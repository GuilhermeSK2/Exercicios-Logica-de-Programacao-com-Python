# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que efetua a leitura de valores inteiros positivos até que um valor negativo seja inserido, mostrando o maior e o menor valor informados.

valor = int(input("Digite um valor positivo (digite um valor negativo para encerrar): "))
maior = valor
menor = valor

while valor >= 0:
    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
    valor = int(input("Digite um valor positivo (digite um valor negativo para encerrar): "))

print("Maior valor digitado:", maior)
print("Menor valor digitado:", menor)