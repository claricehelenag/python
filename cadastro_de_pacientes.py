# Clarice Helena, da turma de redes de computadores subsequente - IFRN. 27/08/2022
# Implementação de cadastro de pacientes baseada na lógica CRUD utilizando banco de dados shelve.

from ast import Break
from bdb import Breakpoint
from pickle import TRUE
import shelve

def menu():

    print('=' * 50)
    print(f'O QUE DESEJA?:')
    print(f' ') 
    print(f'DIGITE 1 PARA AGENDAR CONSULTA:')
    print(f'DIGITE 2 PARA REMARCAR CONSULTA:')
    print(f'DIGITE 3 PARA CANCELAR CONSULTA:')
    print(f'DIGITE 4 PARA VISUALIZAR PACIENTES:')
    print(f'DIGITE 0 PARA SAIR DO SISTEMA')
    print('=' * 50)

def agendar ():

    dados = shelve.open('dados.shelve')

    while novo_paciente := input('Nome do novo paciente: '):
        if novo_paciente not in dados:
            nome = novo_paciente
            break
        else:
            print(f'O nome: {novo_paciente} ja cadastrado.')
   # guardar_nomes()

    RG = input('RG do novo paciente: ')
    
    # guardar_documentos()
   
    data = input('Qual a data você deseja agendar?: ')
        
    celular = input('Qual o numero do celular do paciente?: ')

    dados[nome] = {'Nome': nome, 'RG': RG, 'Celular': celular, 'Data' : data}

    dados.close()

def reagendar ():

    dados = shelve.open('dados.shelve')

    while paciente := input('DIGITE O NOME DO PACIENTE CADASTRADO:  '):
        if paciente in dados:
            nova_data = input(f'QUAL DATA DESEJA REMARCAR PARA {paciente} ?   ')
            usuario  = dados[paciente]
            usuario['Data'] = {nova_data}
            dados[paciente] = usuario
            dados.close()
            break
        else:
            print(f'O PACIENTE EM QUESTÃO NÃO ESTÁ CADASTRADO!')
    
def cancelar ():

    dados = shelve.open('dados.shelve')

    while paciente := input('DIGITE O NOME DO PACIENTE CADASTRADO:  '):
        if paciente in dados:
            del dados[paciente]
            dados.close()
            break
        else:
            print(f'O PACIENTE EM QUESTÃO NÃO ESTÁ CADASTRADO!')

def visualizar ():

    print('Digite [1] para visualizar paciente específico:')
    print('Digite [2] para visualizar todos os pacientes:')
    x = int(input())
    
    if (x == 1):
        dados = shelve.open('dados.shelve')
        while paciente := input('DIGITE O NOME DO PACIENTE CADASTRADO:  '):
            if paciente in dados:
                print(dados[paciente])
                dados.close()
                break
            else:
                print(f'O PACIENTE EM QUESTÃO NÃO ESTÁ CADASTRADO!')
    if (x == 2):
        dados = shelve.open('dados.shelve')
        for key in dados:
            print(dados[key])
        dados.close()

def main ():
    bandeira = TRUE
    while bandeira:
        menu()
        entrada = int(input())
        while entrada > 4 or entrada < 0:
            print(f'ERRO')
            print(f'DIGITE UM VALOR VÁLIDO')
        if (entrada == 0):
            print(f'ENCERRANDO SESSÃO ...')
            bandeira = False
            Break
        if (entrada == 1):
            agendar()
            print(f'AGENDAMENTO CONCLUIDO!')
            Break
        if (entrada == 2):
            reagendar()
            print('AGENDAMENTO ATUALIZADO COM SUCESSO!')
            Break
        if (entrada == 3):
            cancelar()
            print('CANCELAMENTO REALIZADO COM SUCESSO!')
            Break
        if (entrada == 4):
            visualizar()
            print('VISUALIZAÇÃO FINALIZADA!')
            Break
if __name__ == '__main__':
  main()
