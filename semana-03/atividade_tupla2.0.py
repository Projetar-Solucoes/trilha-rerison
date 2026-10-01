'''personagem = ("Cococi", "Mago", 15, 100, 80)

A tupla representa:

(nome, classe, nível, vida, mana)

Faça um programa que:

Mostre o nome.
Mostre a classe.
Mostre o nível.
Mostre a vida.
Mostre a mana.
Mostre quantas informações existem na tupla.
Mostre todas as informações usando for.'''

personagem = ("Cococi", "Mago", 15, 100, 80)
print(f"O nome do personagem é: {personagem[0]}")
print(f"A classe do é: {personagem[1]}")
print(f"O nivel do usuario é: {personagem[2]}")
print(f"A vida é: {personagem[3]}")
print(f"A mana é: {personagem[4]}")
print(len(personagem))

for item in personagem:
    print(item)