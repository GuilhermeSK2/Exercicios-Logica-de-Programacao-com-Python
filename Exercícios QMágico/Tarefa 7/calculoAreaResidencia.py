# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que permite calcular a área total de uma residência, solicitando as dimensões de cada cômodo e apresentando o resultado acumulado.

continuar = "SIM"
area_total = 0

while continuar == "SIM" or continuar == "sim":
    nome = input("Digite o nome do cômodo: ")
    largura = float(input("Digite a largura do cômodo em metros: "))
    comprimento = float(input("Digite o comprimento do cômodo em metros: "))
    
    area = largura * comprimento
    area_total += area
    
    print("Área do", nome, ":", area, "metros quadrados")
    continuar = input("Deseja calcular outro cômodo? (SIM/NAO): ")

print("Área total da residência:", area_total, "metros quadrados")