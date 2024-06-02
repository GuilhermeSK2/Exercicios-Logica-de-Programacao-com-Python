# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que recebe 4 notas de um aluno e retorna se foi aprovado ou não tendo em mente que para ser aprovado a média deve se maior ou igual a 5.

nota1 = float(input("Digite o valor da primeira nota: "))
nota2 = float(input("Digite o valor da segunda nota: "))
nota3 = float(input("Digite o valor da terceira nota: "))
nota4 = float(input("Digite o valor da quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 5:
    print("O aluno foi aprovado com a média", media)
else:
    print("O aluno foi reprovado com a média", media)