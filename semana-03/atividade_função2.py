jogador = {
    "nome": "Cococi",
    "pontos": 80,
    "nivel": 3,
    "vidas": 2
}
def mostrar_jogador():
    print("=== JOGADOR ===\n")

    print(f'NOME: {jogador["nome"]}')
    print(f'PONTOS: {jogador["pontos"]}')
    print(f'NÍVEL: {jogador["nivel"]}')
    print(f'VIDAS: {jogador["vidas"]}\n')

def adicionar_pontos(quantidade):
    jogador["pontos"] += quantidade
    print(f"{jogador['nome']} ganhou {quantidade}. PARABÉNS !\n")
    print(f"Agora {jogador['nome']} você está com {jogador['pontos']}")


mostrar_jogador()
adicionar_pontos(50)