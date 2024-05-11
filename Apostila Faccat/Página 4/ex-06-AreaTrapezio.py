# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Algoritmo  para  ler  as  dimensões  de  um  trapézio  (base  e  altura),  calcular  e  escrever  a área do trapézio.

print("Vamos calcular a área do trapézio!")
baseMaior = int(input("Insira o valor da base maior:"))
baseMenor = int(input("Insira o valor da base menor:"))
altura = int(input("Insira o valor da altura:"))

area = ((baseMaior + baseMenor) * altura) / 2

print("A área do trapézio é de", area)