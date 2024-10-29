from time import sleep
import os
import json

arquivo = os.path.join(os.path.dirname(__file__), 'database', 'ong.json')

def carregar_dados_ongs():
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as file:
            return json.load(file)
    else:
        return []

def salvar_dados_ongs(dados):
    os.makedirs(os.path.dirname(arquivo), exist_ok=True)
    with open(arquivo, 'w') as file:
        json.dump(dados, file, indent=4)

def exibir_menu_ong():
    print('''
    
▒█▀▀▀█ ░▀░ █▀▀ ▀▀█▀▀ █▀▀ █▀▄▀█ █▀▀█ 　 █▀▀▄ █▀▀ 　 ▒█▀▀▀█ █▀▀▄ █▀▀▀ 
░▀▀▀▄▄ ▀█▀ ▀▀█ ░░█░░ █▀▀ █░▀░█ █▄▄█ 　 █░░█ █▀▀ 　 ▒█░░▒█ █░░█ █░▀█ 
▒█▄▄▄█ ▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀░░░▀ ▀░░▀ 　 ▀▀▀░ ▀▀▀ 　 ▒█▄▄▄█ ▀░░▀ ▀▀▀▀
    ''')
    print('''
        |  [1] Cadastro de ONG's parceiras |
        |  [2] Listar ONG's parceiras      |
        |  [3] Atualizar dados             |
        |  [4] Deletar registro de ONG     |
        |  [5] Buscar uma ONG              |
        |  [6] Voltar ao menu principal    |
    ''')

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '-'*(len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_ong():
    lista_de_ong = carregar_dados_ongs()
   
    exibir_subtitulo("Cadastro de ONG")
    nome = input("Digite o nome da ONG: ")
    cnpj = input("Digite o CNPJ da ONG: ")
    endereco = input("Digite o endereço da ONG: ")
    numero = input("Digite o número de telefone para contato: ")

    lista_de_ong.append({'nome': nome, 'CNPJ': cnpj, 'endereço':endereco, 'numero':numero})
    salvar_dados_ongs(lista_de_ong)
    
    print(f"ONG {nome} adicionada com sucesso! ")
    voltar_menu_principal()

    
    
def listar_ong():
    lista_de_ong = carregar_dados_ongs()
    
    if lista_de_ong:
        exibir_subtitulo("Lista das ONG's")
        for ong in lista_de_ong:
            print(f"nome: {ong['nome']}, cnpj: {ong['cnpj']}, endereço: {ong['endereco']}, número: {ong['numero']}")
    else:
        print("😒 NENHUM USUÁRIO CADASTRADO.")
        voltar_menu_principal()


def atualizar_ong():
    exibir_subtitulo("Atualização de ONG")
    atualizacao = input("Digite o CNPJ da ONG que deseja atualizar: ")
    novo_nome = input("Atualize o nome da ONG: ")
    novo_cnpj = input("Atualize o CNPJ da ONG: ")
    novo_endereço = input("Atualize o endereço da ONG: ")
    novo_numero = input("Atualize o número da ONG: ")
    sleep(2)
    print("Atualizando os dados...")
    sleep(2)
    print("Atualização feita com sucesso!")

    voltar_menu_principal()

def deletar_ong():
    exibir_subtitulo("Deletar ONG")
    deletar = input("Digite o CNPJ da ONG que deseja deletar: ")
    sleep(2)
    print("Excluindo ONG...")
    sleep(2)
    print("ONG excluída com sucesso!")
    
    voltar_menu_principal()

def buscar_ong():
    exibir_subtitulo("Buscar ONG")

def voltar_menu_principal():
    input("\n--> Digite uma tecla para voltar ao menu: ")
    print("Voltando...")
    sleep(2)
    os.system('cls')
    exibir_opcoes_ong()

def opcao_invalida():
    os.system('cls')
    print("Opção inválida! Voltando ao menu...")
    sleep(2)
    voltar_menu_principal()

#essa função será colocada no arquivo tela_inicial, na opcao cadastro de cliente.
def exibir_opcoes_ong():
    try:
        exibir_menu_ong()
        opcao_ong = int(input("Informe uma opção: "))
    
        match(opcao_ong):
            case 1:
                cadastrar_ong()
            case 2:
                listar_ong()
            case 3:
                atualizar_ong()
            case 4:
                deletar_ong()
            case 5:
                buscar_ong()
            case 6:
                print("Voltando ao menu inicial...")
                sleep(2)
            case _:
                opcao_invalida()
    except:
            opcao_invalida() 

