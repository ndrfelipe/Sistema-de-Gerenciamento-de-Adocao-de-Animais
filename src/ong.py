from time import sleep
import os

lista_de_ong = []
ponto = 0

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


def cadastrar_ong():
    nome = input("Digite o nome da ONG: ")
    cnpj = input("Digite o CNPJ da ONG: ")
    endereço = input("Digite o endereço da ONG: ")
    numero = input("Digite o número de telefone para contato: ")

    lista_de_ong.append({'nome': nome, 'CNPJ': cnpj, 'endereço':endereço, 'numero':numero})
    print(f"ONG {nome} adicionada com sucesso! ")
    voltar_ao_menu_principal()
    
    
def listar_ong():
    for ong in lista_de_ong:
        print(f"Nome da ong: {ong['nome']} | CNPJ: {ong['cnpj']}")

def atualizar_ong():
    atualizacao = input("Digite o CNPJ da ONG que deseja atualizar: ")
    novo_nome = input("Atualize o nome da ONG: ")
    novo_cnpj = input("Atualize o CNPJ da ONG: ")
    novo_endereço = input("Atualize o endereço da ONG: ")
    novo_numero = input("Atualize o número da ONG: ")
    sleep(2)
    print("Atualizando os dados...")
    sleep(2)
    print("Atualização feita com sucesso!")

    voltar_ao_menu_principal()

def deletar_ong():
    deletar = input("Digite o CNPJ da ONG que deseja deletar: ")
    sleep(2)
    print("Excluindo ONG...")
    sleep(2)
    print("ONG excluída com sucesso!")
    
    voltar_ao_menu_principal()

def buscar_ong():
    pass

def voltar_ao_menu_principal():
    input('\n--> Digite uma tecla para voltar ao menu: ')
    print('Voltando...')
    sleep(2)
    os.system('cls')
    exibir_opcoes_ong()

#essa função será colocada no arquivo tela_inicial, na opcao cadastro de cliente.
def exibir_opcoes_ong():
    while True:
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
                print("Opção inválida. Tente novamente")
                



    
   # █▀▀ ░▀░ █▀▀ ▀▀█▀▀ █▀▀ █▀▄▀█ █▀▀█ 　 █▀▀█ █▀▀▄ █▀▀▀ 
    #▀▀█ ▀█▀ ▀▀█ ░░█░░ █▀▀ █░▀░█ █▄▄█ 　 █░░█ █░░█ █░▀█ 
   # ▀▀▀ ▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀░░░▀ ▀░░▀ 　 ▀▀▀▀ ▀░░▀ ▀▀▀▀ 