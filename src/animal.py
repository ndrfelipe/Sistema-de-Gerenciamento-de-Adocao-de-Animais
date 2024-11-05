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

    nome_animal  = str(input("    DIGITE O NOME DO ANIMAL: "))
    tipo_animal  = str(input("    QUAL O ANIMAL? "))
    raca_animal  = str(input("    QUAL A RAÇA DO ANIMAL? "))
    idade_animal = str(input("    QUAL A IDADE DO ANIMAL? "))
    print("""
        =========================
        | [1] MASCULINO         |
        | [2] FEMININO          |
        | [0] VOLTAR            |
        =========================
        """)

    sexo_animal = int(input(" SELECIONE A OPCAO: "))
    match sexo_animal:
        case 0:
            return
        case 1:
            porte_animal = "MASCULINO"
        case 2:
            porte_animal = "FEMININO"
        case _:
            print(" DIGITE UM CÓDIGO VÁLIDO! ")
            return

    cor_animal   = str(input("    QUAL A COR DO ANIMAL? " ))
    peso_animal  = float(input("  QUAL O PESO DO ANIMAL? "))

    print("""
        =========================
        | [1] PORTE MINI        |
        | [2] PORTE PEQUENO     |
        | [3] PORTE MÉDIO       |
        | [4] PORTE GRANDE      |
        | [5] PORTE GIGANTE     |
        | [6] VOLTAR            |
        =========================
        """)

    porte_animal = int(input(" SELECIONE O PORTE DO ANIMAL: "))
    
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
    exibir_opcoes_animal()

def listar_animais():
    animais = carregar_dados_animais()
    if animais:
        for animal in animais:
            try:
                print(f"LISTA DE ANIMAIS \n")
                print(f"{'NOME'.ljust(10)} | {'TIPO'.ljust(10)} | {'RAÇA'.ljust(10)} | {'IDADE'.ljust(10)} | {'SEXO '.ljust(10)} | {'COR'.ljust(10)} | {'PESO'.ljust(10)} | {'PORTE '.ljust(10)}")
                
                print(f"{animal.get('nome_animal', '').ljust(10)} | {str(animal.get('tipo_animal', '')).ljust(10)} | {str(animal.get('raca_animal', '')).ljust(10)} | {animal.get('idade_animal', '').ljust(10)} | {str(animal.get('sexo_animal', '')).ljust(10)} | {str(animal.get('cor_animal', '')).ljust(10)} | {str(animal.get('peso_animal', '')).ljust(10)}| {str(animal.get('porte_animal')).ljust(10)}")

            except Exception as e:
                print(f"Erro ao processar animal: {e}")
                continue
    else:
        print("NENHUM ANIMAL ENCONTRADO. 🐥")
    exibir_opcoes_animal()

def atualizar_animal(): 
    nome_animal_antigo = input("NOME DO ANIMAL QUE DESEJA ATUALIZAR: ")
    animais = carregar_dados_animais()
    def salvar_dados():
        with open(arquivo, 'w') as f:
            json.dump(animais, f, indent=4, ensure_ascii=False)

    for animal in animais:
        if animal['nome_animal'].lower() == nome_animal_antigo.lower():
            print("    ANIMAL ENCONTRADO!!")
            print(f"   ANIMAL SENDO EDITADO: {animal['nome_animal']}")
            print("""
        ==========================
        | [1] NOME DO ANIMAL     |
        | [2] TIPO DO ANIMAL     |
        | [3] RAÇA DO ANIMAL     |
        | [4] IDADE DO ANIMAL    |
        | [5] SEXO DO ANIMAL     |
        | [6] COR DO ANIMAL      |
        | [7] PESO DO ANIMAL     |
        | [8] PORTE DO ANIMAL    |
        | [0] VOLTAR             |
        ==========================""")
            opcao_de_atualização = int(input("    DIGITE A OPCAO QUE CORRESPONDE COM O DADO: "))
            match opcao_de_atualização:
                case 0:
                    exibir_opcoes_animal()
                case 1:
                    print("    "+"="*15)
                    print(f"    ANIMAL SENDO EDITADO: {animal['nome_animal']}")
                    print("    "+"="*15)
                    novo_nome_animal  = str(input("    DIGITE O NOVO NOME DO ANIMAL (DIGITE 0 PARA CANCELAR): "))
                    if novo_nome_animal != '0':
                        animal['nome_animal'] = novo_nome_animal
                        print(f"    Nome alterado para: {animal['nome_animal']}")
                        salvar_dados()
                        voltar_atualizar_para_menu()
                    else:
                        atualizar_animal()
                case 2:
                    print("    "+"="*15)
                    print(f"    ANIMAL SENDO EDITADO: {animal['nome_animal']}")
                    print("    "+"="*15)
                    novo_tipo_animal  = str(input("    DIGITE O NOVO TIPO DO ANIMAL (DIGITE 0 PARA CANCELAR): "))
                    if novo_tipo_animal != '0':
                        animal['tipo_animal'] = novo_tipo_animal
                        print(f"    Tipo alterado para: {animal['tipo_animal']}")
                        salvar_dados()
                        voltar_atualizar_para_menu()
                    else:
                        atualizar_animal()
                case 3:
                    print("    "+"="*15)
                    print(f"    ANIMAL SENDO EDITADO: {animal['nome_animal']}")
                    print("    "+"="*15)
                    nova_raca_animal  = str(input("    DIGITE A NOVA RAÇA DO ANIMAL (DIGITE 0 PARA CANCELAR): "))
                    if nova_raca_animal != '0':
                        animal['raca_animal'] = nova_raca_animal
                        print(f"    Raça alterada para: {animal['raca_animal']}")
                        salvar_dados()
                        voltar_atualizar_para_menu()
                    else:
                        atualizar_animal()
                case 4:
                    print("    "+"="*15)
                    print(f"    ANIMAL SENDO EDITADO: {animal['nome_animal']}")
                    print("    "+"="*15)
                    nova_idade_animal = str(input("    DIGITE A NOVA IDADE DO ANIMAL (DIGITE 0 PARA CANCELAR): "))
                    if nova_idade_animal != '0':
                        animal['idade_animal'] = nova_idade_animal
                        print(f"    Idade alterada para: {animal['idade_animal']}")
                        salvar_dados()
                        voltar_atualizar_para_menu()
                    else:
                        atualizar_animal()
                case 5:
                    print("    "+"="*10)
                    print(f"    ANIMAL SENDO EDITADO: {animal['nome_animal']}")
                    print("""
        =========================
        | [1] MASCULINO         |
        | [2] FEMININO          |
        | [0] CANCELAR          |
        =========================""")
                    novo_sexo_animal = int(input(" SELECIONE A OPCAO: "))
                    match novo_sexo_animal:
                        case 0:
                            atualizar_animal()
                        case 1:
                            animal['sexo_animal'] = "MASCULINO"
                            salvar_dados()
                            voltar_atualizar_para_menu()
                        case 2:
                            animal['sexo_animal'] = "FEMININO"
                            salvar_dados()
                            voltar_atualizar_para_menu()
                        case _:
                            os.system('cls')
                            print(" DIGITE UM CÓDIGO VÁLIDO! ")
                            atualizar_animal()
                    print(f"Sexo alterado para: {animal['sexo_animal']}")
                case 6:
                    print("    "+"="*10)
                    print(f"    ANIMAL SENDO EDITADO: {animal['nome_animal']}")
                    print("    "+"="*10)
                    nova_cor_animal   = str(input("    DIGITE A NOVA COR DO ANIMAL (DIGITE 0 PARA CANCELAR): "))
                    if nova_cor_animal != '0':
                        animal['cor_animal'] = nova_cor_animal
                        print(f"    Cor alterada para: {animal['cor_animal']}")
                        salvar_dados()
                        voltar_atualizar_para_menu()
                    else:
                        atualizar_animal()
                case 7:
                    print("    "+"="*10)
                    print(f"    ANIMAL SENDO EDITADO: {animal['nome_animal']}")
                    print("    "+"="*10)
                    novo_peso_animal  = float(input("    DIGITE O NOVO PESO DO ANIMAL (DIGITE 0 PARA CANCELAR): "))
                    if novo_peso_animal != '0':
                        animal['peso_animal'] = novo_peso_animal
                        print(f"    Peso alterado para: {animal['peso_animal']}")
                        salvar_dados()
                        voltar_atualizar_para_menu()
                    else:
                        atualizar_animal()
                case 8:
                    print("    "+"="*10)
                    print(f"    ANIMAL SENDO EDITADO: {animal['nome_animal']}")
                    print("""
        =========================
        | [1] PORTE MINI        |
        | [2] PORTE PEQUENO     |
        | [3] PORTE MÉDIO       |
        | [4] PORTE GRANDE      |
        | [5] PORTE GIGANTE     |
        | [0] CANCELAR          |
        =========================
        """)

                    op_novo_porte_animal = int(input("    SELECIONE O PORTE DO ANIMAL: "))
                    
                    match op_novo_porte_animal:
                        case 0:
                            atualizar_animal()
                        case 1:
                            animal['porte_animal'] = "MINI"
                            salvar_dados()
                            voltar_atualizar_para_menu()
                        case 2:
                            animal['porte_animal'] = "PEQUENO"
                            salvar_dados()
                            voltar_atualizar_para_menu()
                        case 3:
                            animal['porte_animal'] = "MÉDIO"
                            salvar_dados()
                            voltar_atualizar_para_menu()
                        case 4:
                            animal['porte_animal'] = "GRANDE"
                            salvar_dados()
                            voltar_atualizar_para_menu()
                        case 5:
                            animal['porte_animal'] = "GIGANTE"
                            salvar_dados()
                            voltar_atualizar_para_menu()
                        case _:
                            print(" DIGITE UM CÓDIGO VÁLIDO! ")
                            atualizar_animal()
            break

    else:
        print("ANIMAL NÃO ENCONTRADO.")
        with open(arquivo, 'w') as f:
            json.dump(animais, f, indent=4, ensure_ascii=False)
            
    exibir_opcoes_animal()

def excluir_animal(nome_animal):
    animais = carregar_dados_animais()

    for animal in animais:
        if animal['nome_animal'].lower() == nome_animal.lower():
            animais.remove(animal)
            break

    with open(arquivo, 'w') as f:
        json.dump(animais, f, indent=4, ensure_ascii=False)
    print("ANIMAL EXCLUÍDO COM SUCESSO! 🦝")
    exibir_opcoes_animal()

def listar_um_animal():
    nome_animal = input("DIGITE O NOME DO ANIMAL QUE DESEJA BUSCAR: ")
    animais = carregar_dados_animais()
    
    for animal in animais:
        if animal['nome_animal'].lower() == nome_animal.lower():
            print(f"NOME: {animal['nome_animal']}, TIPO: {animal['tipo_animal']}, RAÇA: {animal['raca_animal']}, IDADE: {animal['idade_animal']}, SEXO: {animal['sexo_animal']}, COR: {animal['cor_animal']}, PESO: {animal['peso_animal']}, PORTE: {animal['porte_animal']}")
            break
    else:
        print("ANIMAL NÃO ENCONTRADO.")
    exibir_opcoes_animal()

def voltar_atualizar_para_menu():
    print("    ANIMAL ATUALIZADO COM SUCESSO!!")
    input("    APERTE ENTER PARA VOLTAR")
    os.system('cls')
    exibir_opcoes_animal()

def voltar_menu_principal():
    input("APERTE ENTER PARA VOLTAR AO MENU.")
    sleep(3)
    exibir_opcoes_animal()

def exibir_opcoes_animal():
    try:
        exibir_menu_animal()
        opcao_animal = int(input("   INFORME UMA OPÇÃO: "))
        match opcao_animal:
            case 1:
                os.system('cls')
                cadastrar_animal()
            case 2:
                os.system('cls')
                listar_animais()
            case 3:
                os.system('cls')
                atualizar_animal()
            case 4:
                os.system('cls')
                nome_animal = input("NOME DO ANIMAL QUE DESEJA EXCLUÍR:")
                excluir_animal(nome_animal)
            case 5:
                os.system('cls')
                listar_um_animal()
            case 6:
                os.system('cls')
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