from Agenda import Agenda

menu = '''
                    Agenda

        Digite 1 para cadastrar um contato.
        Digite 2 para buscar contato.
        Digite 3 para listar todos os contatos.
        Digite 4 para modificar um contato.
        Digite 5 para excluir um contato.
        Digite outro número para sair da agenda.
'''
def validador_nome():
    nome = str(input('Digite o nome do contato: ')).title()
    return nome

def validador_telefone():
    while 1:
        try:
            telefone = input('Digite o número de telefone(11 digitos, somente números): ')
            if len(telefone) == 11:
                telefone = int(telefone)
                break
            else:
                print('\nO número deve conter 11 dígitos.')
                continue
        except ValueError:
            print('\nNúmero inválido.\n')
    
    return telefone

def validador_id():
    while 1:
        try:
            identificador = int(input('Digite o Id do contato: '))
            break
        except ValueError:
            print('Digite somente números.')
            continue
    return identificador

def cadastrar_contato():
    agenda = Agenda('agenda.db')
    nome = validador_nome()
    telefone = validador_telefone()
    agenda.inserir(nome, telefone)
    agenda.fechar()

def buscar_contato():
    agenda = Agenda('agenda.db')
    valor_busca = input('Digite um nome ou parte dele: ')
    resultado = agenda.buscar(valor_busca)
    print('\nRegistros encontrados\n')

    if len(resultado) == 0:
        print('Não foram encontrados registros correspondentes.\n')
    else:
        for busca in resultado:
            print(f'Nome: {busca[1]}\nTelefone: {busca[2]}\n')
    
    agenda.fechar()

def listar_contatos():
    agenda = Agenda('agenda.db')
    resultado = agenda.listar()
    print('\nContatos Registrados:\n')

    for busca in resultado:
        print(f'Id: {busca[0]}\nNome: {busca[1]}\nTelefone: {busca[2]}\n')
    agenda.fechar()

def modificar_contato():
    menu = '''
            Digite uma opção:

        Digite 1 para modificar o nome.
        Digite 2 para modificar o telefone.
        Digite 3 para modificar o nome e o telefone.
        Digite outro número para abortar.
    '''
    listar_contatos()
    agenda = Agenda('agenda.db')
    identificador = validador_id()
    opcao = int()
    while 1:
        try:
            print(menu)
            opcao = int(input('Digite uma opção: '))
            break
        except ValueError:
            print('Digite uma opção válida.')
            continue
    
    if opcao == 1:
        nome = validador_nome()
        agenda.editar(nome=nome, identificador=identificador)
    elif opcao == 2:
        telefone = validador_telefone()
        agenda.editar(identificador=identificador, telefone=telefone)
    elif opcao == 3:
        nome = validador_nome()
        telefone = validador_telefone()
        agenda.editar(identificador=identificador, nome=nome, telefone=telefone)
    else:
        agenda.fechar()
        return None
    
    listar_contatos()
    agenda.fechar()

def excluir_contato():
    aviso = '''
            \nAtenção !!!
        Esta operação não pode ser revertida!!!\n
    '''
    listar_contatos()
    agenda = Agenda('agenda.db')
    print(aviso)
    opcao = input('Deseja conitnuar?[S/N]: ').upper()
    if opcao == 'S':
        identificador = validador_id()
        agenda.excluir(identificador)
        return None
    else:
        return None
        
def main():
    while 1:
        try:
            print(menu)
            opcoes = int(input('Digite a opção: '))
            if opcoes == 1:
                cadastrar_contato()
            elif opcoes == 2:
                buscar_contato()
            elif opcoes == 3:
                listar_contatos()
            elif opcoes == 4:
                modificar_contato()
            elif opcoes == 5:
                excluir_contato()
            else:
                break
        except ValueError as erro:
            print(f'\nDigite um número válido. Código do erro: {erro}\n')

main()
