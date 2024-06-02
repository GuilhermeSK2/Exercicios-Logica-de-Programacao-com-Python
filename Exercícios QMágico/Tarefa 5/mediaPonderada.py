# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que calcula a média final ponderada de um aluno.

nota1 = float(input("Digite a primeira nota (peso 2): "))
nota2 = float(input("Digite a segunda nota (peso 3): "))
nota3 = float(input("Digite a terceira nota (peso 5): "))

media_final = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

print("A média final do aluno é:", round(media_final,2))