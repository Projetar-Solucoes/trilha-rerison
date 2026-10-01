'''Crie um dicionário representando um aluno:

python
aluno = {
    "nome": "Cococi",
    "idade": 17,
    "curso": "Informática",
    "nota": 8.5
}


Faça um programa que:

1. Mostre o nome do aluno.
2. Mostre a idade.
3. Mostre o curso.
4. Mostre a nota.
5. Altere a nota para 9.0.
6. Adicione uma nova informação chamada "cidade".
7. Mostre o dicionário completo.'''

aluno = {
    "nome": "Cococi",
    "idade": 17,
    "curso": "Informática",
    "nota": 8.5
}
print(aluno["nome"])
print(aluno["idade"])
print(aluno["curso"])
print(aluno["nota"])
aluno["nota"] = 9.0
aluno["cidade"] = "jaguaretama"
print(aluno)