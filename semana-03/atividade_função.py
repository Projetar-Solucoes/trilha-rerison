personagem = {
    "nome": "Cococi",
    "classe": "Mago",
    "nivel": 10,
    "vida": 100
    }
def mostrar_personagem(p):
    print("=== PERSONAGEM ===\n")

    print(f'NOME: {personagem["nome"]}')
    print(f'CLASSE: {personagem["classe"]}')
    print(f'NÍVEL: {personagem["nivel"]}')
    print(f'VIDA: {personagem["vida"]}\n')

def aumentar_nivel(p):
    p["nivel"] += 1
    print(f"Parabéns ! {p['nome']} subiu para o nível {p['nivel']} ! \n")

mostrar_personagem(personagem)
aumentar_nivel(personagem)
mostrar_personagem(personagem)

'''Depois, crie uma função chamada adicionar_pontos().

A função deverá:

* receber o jogador e uma quantidade de pontos;
* adicionar esses pontos ao jogador;
* retornar o jogador atualizado.

Exemplo:

python
jogador = adicionar_pontos(jogador, 50)


Resultado esperado:

text
Pontos: 130




Crie uma função chamada verificar_nivel().

Ela deverá verificar os pontos do jogador:

* 100 pontos ou mais → nível 4
* 200 pontos ou mais → nível 5
* abaixo de 100 → permanece no nível atual

Depois, mostre o jogador novamente.'''