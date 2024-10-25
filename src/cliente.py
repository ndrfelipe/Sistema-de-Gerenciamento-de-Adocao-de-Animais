lista_de_clientes = []

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    idade = int(input("Digite a idade do cliente: "))
    
    lista_de_clientes.append({'nome': nome, 'idade': idade})
    
    
def listar_clientes():
    for cliente in lista_de_clientes:
        print(cliente)+
        
        