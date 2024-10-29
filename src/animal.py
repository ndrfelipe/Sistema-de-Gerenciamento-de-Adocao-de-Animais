import json
import os 
from time import sleep
 
arquivo = os.path.join(os.path.dirname (__file__), 'database', 'animal.json')

def carregar_dados_animais():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)
        return []

    with open(arquivo, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("Arquivo vazio.")
            return []

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
    animais = carregar_dados_animais()

    nome_animal  = str(input("  DIGITE O NOME DO ANIMAL: "))
    tipo_animal  = str(input("  QUAL O ANIMAL? "))
    raca_animal  = str(input("  QUAL A RAÇA DO ANIMAL? "))
    idade_animal = str(input("  QUAL A IDADE DO ANIMAL? "))
    sexo_animal  = str(input("  QUAL O SEXO DO ANIMAL? "))
    cor_animal   = str(input("  QUAL A COR DO ANIMAL? "))
    peso_animal  = str(input("  QUAL O PESO DO ANIMAL? "))

    print("""
        =========================
        | [1] PORTE MINI        |
        | [2] PEQUENO PORTE     |
        | [3] PORTE MÉDIO       |
        | [4] PORTE GRANDE      |
        | [5] PORTE GIGANTE     |
        | [6] VOLTAR            |
        =========================
        """)

    porte_animal = int(input(" SELECIONE O PORTE DO ANIMAL:"))
    
    match porte_animal:
        case 0:
            return
        case 1:
            porte_animal = "MINI"
        case 2:
            porte_animal = "PEQUENO"
        case 3:
            porte_animal = "MÉDIO"
        case 4:
            porte_animal = "GRANDE"
        case 5:
            porte_animal = "GIGANTE"
        case _:
            print(" DIGITE UM CÓDIGO VÁLIDO! ")
            return

    animais.append({
    'nome_animal':  nome_animal, 
    'tipo_animal':  tipo_animal, 
    'raca_animal':  raca_animal, 
    'idade_animal': idade_animal, 
    'sexo_animal':  sexo_animal, 
    'cor_animal':   cor_animal, 
    'peso_animal':  peso_animal, 
    'porte_animal': porte_animal})

    with open(arquivo, 'w') as f:
        json.dump(animais, f, indent=4, ensure_ascii=False)
    print("ANIMAL ADICIONADO COM SUCESSO! 🐶")
    voltar_menu_principal()

def listar_animais():
    animais = carregar_dados_animais()
    if animais:
        for animal in animais:
            print(f"NOME: {animal['nome_animal']}, TIPO:  {animal ['tipo_animal']}, RAÇA:  {animal ['raca_animal']}, IDADE: {animal ['idade_animal']}, SEXO:  {animal ['sexo_animal']}, COR:   {animal ['cor_animal']}, PESO:  {animal ['peso_animal']}, PORTE: {animal ['porte_animal']}")
    else:
        print("NENHUM ANIMAL CADASTRADO. 🐥")
    voltar_menu_principal()

def atualizar_animal(): #Ainda com problemas
    animais = carregar_dados_animais()
    nome_animal_antigo = input("NOME DO ANIMAL QUE DESEJA ATUALIZAR: ")
    for animal in animais:
        if  animal ['nome_animal'] == nome_animal_antigo:
            animal ['nome_animal']  = input("NOVO NOME: ")
            animal ['idade_animal'] = input("NOVA IDADE: ")
            animal ['peso_animal']  = input("NOVO PESO: ")
            animal ['porte_animal'] = input("NOVO PORTE: ")
            break
        else:
            print("ANIMAL NÃO ENCONTRADO.")
        
        with open(arquivo, 'w') as f:
            json.dump(animais, f, indent=4, ensure_ascii=False)
        print("ANIMAL ATUALIZADO COM SUCESSO! 🐱")
        voltar_menu_principal()

def excluir_animal(nome_animal):
    animais = carregar_dados_animais()

    for animal in animais:
        if animal['nome_animal'] == nome_animal:
            animais.remove(animal)
            break

    with open(arquivo, 'w') as f:
        json.dump(animais, f, indent=4, ensure_ascii=False)
    print("ANIMAL EXCLUÍDO COM SUCESSO! 🦝")
    voltar_menu_principal()

def listar_um_animal():
    nome_animal = input("DIGITE O NOME DO ANIMAL QUE DESEJA BUSCAR: ")
    animais = carregar_dados_animais()
    
    for animal in animais:
        if animal['nome_animal'].lower() == nome_animal.lower():
            print(f"NOME: {animal['nome_animal']}, TIPO: {animal['tipo_animal']}, RAÇA: {animal['raca_animal']}, IDADE: {animal['idade_animal']}, SEXO: {animal['sexo_animal']}, COR: {animal['cor_animal']}, PESO: {animal['peso_animal']}, PORTE: {animal['porte_animal']}")
            break
    else:
        print("ANIMAL NÃO ENCONTRADO.")

def voltar_menu_principal():
    input("APERTE ENTER PARA VOLTAR AO MENU.:")
    sleep(3)
    exibir_opcoes_animal()

def exibir_opcoes_animal():
    try:
        exibir_menu_animal()
        opcao_animal = int(input("INFORME UMA OPÇÃO: "))
        match opcao_animal:
            case 1:
                cadastrar_animal()
            case 2:
                print("ANIMAIS CADASTRADOS: ")
                listar_animais()
            case 3:
                atualizar_animal()
            case 4:
                nome_animal = input("NOME DO ANIMAL QUE DESEJA EXCLUÍR:")
                excluir_animal(nome_animal)
            case 5:
                exibir_menu_animal()
            case 6:
                print("VOLTANDO AO MENU INICIAL...")
                sleep(1)
                print('UM ELEFANTE')
                sleep(1)
                print('DOIS ELEFANTES')
                sleep(1)
                print('TRÊS ELEFANTES')
                sleep(1)
    except ValueError:
        print("OPÇÃO INVÁLIDA.")

