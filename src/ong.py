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
    
    print("-" *41)
    print(f"ONG {nome} adicionada com sucesso! ✨ ")
    voltar_menu_principal()

    
def listar_ong():
    lista_de_ong = carregar_dados_ongs()
    if lista_de_ong:
        exibir_subtitulo("Lista das ONG's")
        print(f"{'Nome'.ljust(22)} | {'CNPJ'.ljust(20)} | {'Endereço'.ljust(35)} | {'Telefone'.ljust(20)}\n")
        
        for ong in lista_de_ong:
            nome = ong['nome']
            cnpj = ong['CNPJ']
            endereco = ong['endereço']
            numero = ong['numero']
            print(f'- {nome.ljust(20)} | {cnpj.ljust(20)} | {endereco.ljust(35)} | {numero.ljust(20)}\n')
    else:
        print("😒 NENHUM USUÁRIO CADASTRADO.")

    voltar_menu_principal()

def atualizar_ong():
    exibir_subtitulo("Atualização de ONG")
    lista_de_ong = carregar_dados_ongs()
    antigo_cadastro = input("Digite o CNPJ da ONG que deseja atualizar: ")
    for ong in lista_de_ong:
        if ong['CNPJ'] == antigo_cadastro:
            ong['nome'] = input("Digite o novo nome da ONG: ")
            ong['CNPJ'] = input("Digite o novo CNPJ da ONG: ")
            ong['endereço'] = input("Digite o novo endereço da ONG: ")
            ong['numero'] = input("Digite o novo número da ONG: ")
            salvar_dados_ongs(lista_de_ong)
            sleep(2)
            print("-" *43)
            print("Atualizando os dados...")
            sleep(2)
            print("Atualização feita com sucesso! ✨")
            voltar_menu_principal()
            break
    print("ONG não encontrada!")
    voltar_menu_principal()



def deletar_ong():
    lista_de_ong = carregar_dados_ongs()
    exibir_subtitulo("Deletar ONG")
    deletando_ong = input("Digite o CNPJ da ONG que deseja deletar: ")
    
    deletar = [
        ong for ong in lista_de_ong 
        if ong['CNPJ'].strip() == deletando_ong.strip()
    ]
    if deletar:
        print("ONG encontrada:")
        for ong in deletar:
            print(f"- Nome: {ong['nome']}\n- CNPJ: {ong['CNPJ']}\n- Endereço: {ong['endereço']}\n- Telefone: {ong['numero']} ")
            
            lista_de_ong.remove(ong)  
            
            print("-" *41)
            print("Excluindo ONG...")
            sleep(2)
            print("ONG deletada com sucesso. ✨")
            salvar_dados_ongs(lista_de_ong)
            voltar_menu_principal()
    else:
        print("😒 Nenhuma ONG encontrada com esse CNPJ.")
        voltar_menu_principal()

def buscar_ong():
    lista_de_ong = carregar_dados_ongs()
    exibir_subtitulo("Buscar ONG")
    buscando_ong = input("Digite o nome ou CNPJ da ONG: ")

    busca = [
        ong for ong in lista_de_ong 
        if ong['nome'].lower() == buscando_ong.lower() or ong['CNPJ'].strip() == buscando_ong.strip()
    ]

    if busca:
        print("ONG encontrada:")
        for ong in busca:
            print(f"- Nome: {ong['nome']}\n- CNPJ: {ong['CNPJ']}\n- Endereço: {ong['endereço']}\n- Número: {ong['numero']}\n")
    else:
        print("😒 Nenhuma ONG encontrada com esse nome ou CNPJ.")

    voltar_menu_principal()


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

