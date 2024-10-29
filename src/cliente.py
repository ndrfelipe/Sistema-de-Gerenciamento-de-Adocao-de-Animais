import json
import os
from time import sleep

arquivo = os.path.join(os.path.dirname(__file__), 'database', 'cliente.json')

def carregar_dados_clientes():
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as file:
            return json.load(file)
    else:
        return []

def salvar_dados_clientes(dados):
    os.makedirs(os.path.dirname(arquivo), exist_ok=True)
    with open(arquivo, 'w') as file:
        json.dump(dados, file, indent=4)


def exibir_menu_cliente():
    os.system('cls')
    print("Sistema Cliente: \n")
    print(" 1 - Cadastrar um novo cliente")
    print(" 2 - Listar clientes")
    print(" 3 - Atualizar cliente")
    print(" 4 - Excluir cliente")
    print(" 5 - Listar um cliente")
    print(" 6 - Voltar ao menu anterior")


def cadastrar_cliente():
    clientes = carregar_dados_clientes()

    nome = input("Digite o nome do cliente: ")
    idade = int(input("Digite a idade do cliente: "))
    cpf = input("Digite o seu cpf: ")
    email = input("Digite seu email: ")
    telefone = int(input("Digite seu número de telefone: "))
    endereço = input("Digite seu endereço: ")
    renda = int(input("Digite sua renda familiar: "))
    profissao = input("Digite sua profissão: ")
    clientes.append({'nome': nome, 'idade': idade, 'cpf':cpf, 'email':email, 'telefone':telefone, 'endereço':endereço, 'renda':renda, 'profissao':profissao })
    print(f"O usuário {nome} adicionado com sucesso. ")

    salvar_dados_clientes(clientes)
    voltar_menu_principal()
    
    
    
def listar_clientes():
    clientes = carregar_dados_clientes()
    print("Lista dos clientes: ",clientes)
    for cliente in clientes:
     print(f" nome: {cliente['nome']}, idade: {cliente['idade']}, cpf: {cliente['cpf']}, email: {cliente['email']}, telefone: {cliente['telefone']}, endereço: {cliente['endereço']}, renda: {cliente['renda']}, profissão: {cliente['profissão']}")

    voltar_menu_principal()

    
    #ainda precisa de ajuste na parte de opçao invalida

    

def atualizar_cliente():
    clientes = carregar_dados_clientes()
    cadastro_antigo = str(input("Digite o CPF da pessoa que deseja atualizar os dados: "))
    for cliente in clientes:
        if cliente['CPF']== cadastro_antigo:
            cliente['nome'] = input("Digite o novo nome: ")
            cliente['idade'] = str(input("Digite a nova idade: "))
            cliente['cpf'] = str(input("Digite o novo CPF: "))
            cliente['email'] = input("Digite o novo email: ")
            cliente['telefone'] = input("Digite o novo telefone: ")
            cliente['endereço'] = str(input("Digite o novo endereço: "))
            cliente['renda'] = str(input("Digite a nova renda: "))
            cliente['profissao'] = input("Digite a nova profissão: ")
            
            salvar_dados_clientes(clientes)
            print("\nCliente atualizado com sucesso!")
    else:
            print("Cliente não encontrado.")


    voltar_menu_principal()

def excluir_cliente():
    pass

def listar_um_cliente():
    pass

def voltar_menu_principal():
    input('Digite uma tecla para voltar ao menu: ')
    sleep(3)
    exibir_opcoes_cliente()

def opcao_invalida():
    
    print("Opção inválida. Tente novamente. ")
    voltar_menu_principal()


def exibir_opcoes_cliente():        
    try:
        exibir_menu_cliente()
        opcao_cliente = int(input("Informe uma opção: "))
        match(opcao_cliente):
            case 1:
                cadastrar_cliente()
            case 2:
                listar_clientes()
            case 3:
                atualizar_cliente()
            case 4:
                excluir_cliente()
            case 5:
                listar_um_cliente()
            case 6:
                print("Voltando ao menu inicial... ")
                sleep(1)
                print('.')
                sleep(1)
                print('.')
                sleep(1)
                print('.')
                sleep(1)
            case _:
                opcao_invalida()
    except:
        opcao_invalida()
