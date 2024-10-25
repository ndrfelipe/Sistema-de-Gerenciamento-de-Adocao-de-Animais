import json
import os

arquivo = os.path.join(os.path.dirname(__file__), 'animal.json')

# Carregar lista de animais do arquivo, se existir
if os.path.exists(arquivo):
    with open(arquivo, 'r') as f:
        lista_animais = json.load(f)
else:
    lista_animais = []

def salvar_animais():
    with open(arquivo, 'w') as f:
        json.dump(lista_animais, f, indent=4)

def pagina_animal():
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
    op = int(input("   | Digite a opção desejada: "))

    match op:
        case 0:
            return  # Sai da função
        case 1:
            os.system('clear')
            adicionar_animal()
        case 2:
            os.system('clear')
            listar_animais()
        case 3:
            os.system('clear')
            atualizar_animal()
        case 4:
            os.system('clear')
            excluir_animal()
        case 5:
            os.system('clear')
            listar_um_animal()
        case _:
            print("   DIGITE UM CÓDIGO VÁLIDO!!!👺")
            pagina_animal()

def adicionar_animal():
    nome_animal = str(input("   Digite o nome do animal: "))
    animal = str(input("   Qual seu animal?: "))
    raca_animal = str(input("   Qual raça do seu animal?: "))
    idade_animal = int(input("   Insira a idade do seu animal: "))
    sexo_animal = str(input("   Insira o sexo do seu animal: "))
    cor_animal = str(input("   Insira a cor do seu animal: "))
    peso_animal = str(input("   Insira o peso do seu animal: "))

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
    porte_animal_op = int(input("Selecione o porte do animal: "))
    
    match porte_animal_op:
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

    lista_animais.append(animais_info)
    salvar_animais()

    op3 = str(input("Você deseja adicionar um novo animal? (S/N) "))
    if op3.lower() == "s":
        adicionar_animal()

def listar_animais():
    pass
def listar_animais():
    pass
def atualizar_animal():
    pass
def excluir_animal():
    pass
def listar_um_animal():
    pass

pagina_animal()