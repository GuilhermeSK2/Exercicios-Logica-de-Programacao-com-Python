# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que lê a nota de um aluno e converte-a para conceito.

nota = float(input("Digite a nota: "))
if nota >= 9:
    print("Conceito A.")
elif nota >= 7:
    print("Conceito B.")
elif nota >= 5:
    print("Conceito C.")
elif nota >= 3:
    print("Conceito D.")
else:
    print("Conceito F.")
