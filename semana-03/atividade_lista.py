'''notas = [7.5, 8.0, 6.5, 9.0, 5.5]'''

"""Faça um programa que:

Mostre todas as notas.
Mostre a primeira nota.
Mostre a última nota.
Adicione uma nova nota 8.5.
Altere a nota 5.5 para 6.0.
Remova a nota 7.5.
Mostre quantas notas existem agora.
Mostre a lista final."""

notas = [7.5, 8.0, 6.5, 9.0, 5.5]
print (notas)
print (notas[0])
print (notas[4])
notas.append(8.5)
print (notas)
notas[notas.index(5.5)] = 6.0
print (notas)
notas.remove(7.5)
print (notas)
print (len(notas))
print (notas)

