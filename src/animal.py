import json
import os

arquivo = os.path.join(os.path.dirname(__file__), 'database', 'animal.json')

lista_de_animais = []

def exibir_menu_animal():
    print("""
    ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
    ───█▒▒░░░░░░░░░▒▒█───
    ────█░░█░░░░░█░░█────
    ─▄▄──█░░░▀█▀░░░█──▄▄─
    █░░█─▀▄░░░░░░░▄▀─█░░█
    █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
    █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
    █░░║║║╠─║─║─║║║║║╠─░░█
    █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
    █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█""")
    print("   =========================")
    print("   | [1] ADICIONAR ANIMAL  |")
    print("   | [2] LISTAR ANIMAIS    |")
    print("   | [3] ATUALIZAR ANIMAL  |")
    print("   | [4] EXCLUIR ANIMAL    |")
    print("   | [5] LISTAR UM ANIMAL  |")
    print("   | [0] VOLTAR            |")
    print("   =========================")

def cadastrar_animal():
    pergunta = 's'
    while pergunta != "N":
        nome_animal = str(input("   Digite o nome do animal: "))
        animal = str(input("   Qual seu animal?: "))
        raca_animal = str(input("   Qual raça do seu animal?: "))
        idade_animal = int(input("   Insira a idade do seu animal: "))
        sexo_animal = str(input("   Insira o sexo do seu animal: "))
        cor_animal = str(input("   Insira a cor do seu animal: "))
        peso_animal = str(input("   Insira o peso do seu animal: "))
        lista_de_animais.append({'Nome:': nome_animal})

        print("""
=========================
| [1] PORTE MINI        |
| [2] PEQUENO PORTE     |
| [3] PORTE MÉDIO       |
| [4] PORTE GRANDE      |
| [5] PORTE GIGANTE     |
| [0] VOLTAR            |
=========================
""")
        op = int(input("Selecione o porte do animal: "))
    
        match op:
            case 0:
                return
            case 1:
                porte = "MINI"
            case 2:
                porte = "PEQUENO"
            case 3:
                porte = "MÉDIO"
            case 4:
                porte = "GRANDE"
            case 5:
                porte = "GIGANTE"
            case _:
                print("   DIGITE UM CÓDIGO VÁLIDO!!!👺")
                return

        animais_info = {
            "nome": nome_animal,
            "tipo": animal,
            "raca": raca_animal,
            "idade": idade_animal,
            "sexo": sexo_animal,
            "cor": cor_animal,
            "peso": peso_animal,
            "porte": porte
        }

def listar_animais():
    for animal in lista_de_animais:
        print(f"Nome do animal: {animal['nome_animal']} | Tipo: {animal['animal']} | Raça: {animal[raca_animal]} | Idade: {animal['idade']} | Sexo: {animal['sexo']} Cor: {animal['cor']} | Peso: {[peso_animal]} | Porte: {['porte']}")

def atualizar_animal():
    pass

def excluir_animal():
    pass

def listar_um_animal():
    pass 

def exibir_opcoes_animal():
    while True:
        exibir_menu_animal()
        opcao_animal = int(input("Informe uma opção: "))
    
        match(opcao_animal):
            case 1:
                cadastrar_animal()
            case 2:
                listar_animais()
            case 3:
                atualizar_animal()
            case 4:
                excluir_animal()
            case 5:
                def listar_um_animal():()
            case 6:
                print("Voltando ao menu inicial... ")
                break
            case _:
                print("Opção inválida. Tente novamente")
                