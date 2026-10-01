import json
from time import sleep

ARQUIVO = "solicitacoes.json"


def carregar_dados():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Erro: o arquivo JSON está com problema.")
        return []


def salvar_dados(lista):
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump(lista, arquivo, ensure_ascii=False, indent=4)

    except OSError:
        print("Erro ao salvar os dados.")


def exibir_menu():
    print("=" * 50)
    print("""
        BANCO RERISON - CENTRAL DE SOLICITAÇÕES

        [1] Cadastrar Solicitação
        [2] Consultar Solicitação
        [3] Listar Solicitações
        [4] Estatísticas
        [0] Sair
    """)

    try:
        escolha = int(input("O que deseja fazer: "))
        return escolha

    except ValueError:
        print("Entrada inválida. Digite um número.")
        return None


def pedir_campo(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor:
            return valor

        print("Este campo não pode ficar vazio.")


def cadastrar_solicitacao(lista):
    print("\n=== CADASTRAR SOLICITAÇÃO ===")

    protocolo = pedir_campo("Digite seu número de protocolo: ")


    for solicitacao in lista:
        if solicitacao["protocolo"] == protocolo:
            print("Esse protocolo já está cadastrado.")
            sleep(2)
            return

    nome = pedir_campo("Digite seu nome: ")
    setor = pedir_campo("Digite seu setor: ")

    categorias_validas = ["Suporte", "Acesso", "Sistema"]

    while True:
        categoria = pedir_campo(
            "Digite a categoria (Suporte/Acesso/Sistema): "
        ).capitalize()

        if categoria in categorias_validas:
            break

        print("Categoria inválida.")
        print("Escolha: Suporte, Acesso ou Sistema.")

    assunto = pedir_campo("Digite o assunto: ")
    descricao = pedir_campo("Informe uma breve descrição: ")

    prioridades_validas = ["Alta", "Média", "Baixa"]

    while True:
        prioridade = pedir_campo(
            "Qual a prioridade? (Alta/Média/Baixa): "
        ).capitalize()

        if prioridade in prioridades_validas:
            break

        print("Prioridade inválida.")
        print("Escolha: Alta, Média ou Baixa.")

    solicitacao = {
        "protocolo": protocolo,
        "nome": nome,
        "setor": setor,
        "categoria": categoria,
        "assunto": assunto,
        "descricao": descricao,
        "prioridade": prioridade
    }

    lista.append(solicitacao)
    salvar_dados(lista)

    print("=" * 50)
    print("Solicitação cadastrada com sucesso!")
    sleep(2)


def consultar_solicitacao(lista):
    protocolo = input(
        "\nDigite o protocolo para a busca: "
    ).strip()

    encontrado = False

    for s in lista:

        if s["protocolo"] == protocolo:

            encontrado = True

            print("\n--- SOLICITAÇÃO ENCONTRADA ---")
            print(f"Protocolo: {s['protocolo']}")
            print(f"Nome: {s['nome']}")
            print(f"Setor: {s['setor']}")
            print(f"Categoria: {s['categoria']}")
            print(f"Assunto: {s['assunto']}")
            print(f"Descrição: {s['descricao']}")
            print(f"Prioridade: {s['prioridade']}")
            print("-" * 30)

            break

    if not encontrado:
        print("\nProtocolo não encontrado.")

    sleep(2)


def listar_todas_solicitacoes(lista):

    if not lista:
        print("\nNenhuma solicitação cadastrada ainda.")

    else:
        print(
            f"\n--- LISTANDO {len(lista)} SOLICITAÇÃO(ÕES) ---"
        )

        for posicao, s in enumerate(lista, start=1):

            print(
                f"[{posicao}] "
                f"Protocolo: {s['protocolo']} | "
                f"Assunto: {s['assunto']} | "
                f"Nome: {s['nome']}"
            )

    sleep(2)


def mostrar_estatisticas(lista):

    print("\n=== ESTATÍSTICAS ===")

    total = len(lista)

    print(f"\nTotal de solicitações: {total}")

    if total == 0:
        print("Não existem dados para analisar.")
        sleep(2)
        return

  
    prioridades = {}

    for s in lista:
        prioridade = s["prioridade"]

        if prioridade in prioridades:
            prioridades[prioridade] += 1
        else:
            prioridades[prioridade] = 1

    print("\nPor prioridade:")

    for prioridade, quantidade in prioridades.items():
        print(f"{prioridade}: {quantidade}")


    categorias = {}

    for s in lista:
        categoria = s["categoria"]

        if categoria in categorias:
            categorias[categoria] += 1
        else:
            categorias[categoria] = 1

    print("\nPor categoria:")

    for categoria, quantidade in categorias.items():
        print(f"{categoria}: {quantidade}")

    sleep(3)