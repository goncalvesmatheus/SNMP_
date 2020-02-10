from easysnmp import *
from tabulate import tabulate
import time

# OID's que queremos monitorar. Variáveis global
oid_inf = '.1.3.6.1.2.1.25.4.2.1.2'
oid_mem = '.1.3.6.1.2.1.25.5.1.1.2'
oid_cpu = '.1.3.6.1.2.1.25.5.1.1.1'
# Captura o horário que está correndo na máquina local e armazena em duas variáveis, separando hora e minuto.
hora = str(time.localtime().tm_hour)
minuto = str(time.localtime().tm_min)
# oid_time = '.1.3.6.1.4.1.2021.100.4'
# oid_time = '.1.3.6.1.2.1.25.1.2.0'
# Lista que recebe os processos listados dentro da função lista_proc
scan = []
# Variáveis que recebem o IP/Nome do host e porta que utilizamos para monitorar
host = ''
porta = ''
# Sessão iniciada com as informações passadas pelo utilizador.
session = Session(hostname=host, community='public',
                  version=2, remote_port=porta)


# Função listar processos.
def lista_proc(session, scan):
    # Realiza o walk
    snmp = session.walk([oid_inf, oid_mem, oid_cpu])
    i = 0
    for item in snmp:
        # A cada terceira posição na lista, ele adiciona a informação oid_index na lista scan.
        if i % 3 == 0:
            scan.append('{oid_index}'.format(
                oid_index=item.oid_index))
        scan.append('{value}'.format(value=item.value))
        i += 1
    # Vai dividir a lista a cada 4 posições. (contando 0, 1, 2, 3)
    scan = [scan[x:x+4] for x in range(0, len(scan), 4)]
    print('\n')
    # Imprime a lista de forma tabulada
    print(tabulate(scan, headers=["PID", "Name",
                                  "Memory", "CPU"], tablefmt="orgtbl"))
    print('')
    print('Horário da máquina local: '+hora+' horas e '+minuto+' minutos.')
    print('Horário da máquina remota: EM DESENVOLVIMENTO')

# Função monitorar processo especificado pelo utilizador.


def oidget(session, oidbulk):
    # Variáveis para realizar o get
    oid_inf_get = '.1.3.6.1.2.1.25.4.2.1.2.'+str(oidbulk)
    oid_mem_get = '.1.3.6.1.2.1.25.5.1.1.2.'+str(oidbulk)
    oid_cpu_get = '.1.3.6.1.2.1.25.5.1.1.1.'+str(oidbulk)
    my_time = int(input('Por quantos segundos quer monitorar? '))
    i = 0
    lista_get = []
    listaget = session.get([oid_inf_get, oid_mem_get, oid_cpu_get])
    while my_time:
        for item in listaget:
            if i % 3 == 0:
                lista_get.append('{oid_index}'.format(
                    oid_index=item.oid_index))
            lista_get.append('{value}'.format(value=item.value))
            i += 1
        lista_get.append(my_time)
        lista_get = [lista_get[x:x+5] for x in range(0, len(lista_get), 5)]
        print(tabulate(lista_get, headers=["PID", "Name",
                                           "Memory", "CPU", "Seconds"], tablefmt="psql"))
        time.sleep(1)
        my_time = my_time - 1
        # Limpa a lista
        lista_get = []
    print('\n Monitoramento finalizado as '+hora +
          ' horas e '+minuto+' minutos. Horário local.')

# Função utilizada como teste no menu


def teste():
    print('Função de teste.')


# Inicio interação com o utilizador.
# Função menu com algumas validações.
def menu():
    # Variável utilizada para sair do menu.
    # Só sai do menu no momento que ela receber True, escolhendo a opção 0
    valida = False
    while valida == False:
        escolha = input("""
        *************MENU***************
        1: Listar os processos
        2: Monitorar processo específico
        3: Teste
        0: Sair

        Selecione uma opção: """)
        try:
            # Valida a informação passada, se ela é inteiro ou não.
            escolha = int(escolha)
            # Condição da variável ser maior que zero. (não aceitando números negativos.)
            if escolha >= 0:
                if escolha == 1 or escolha == '01':
                    host = input('Informe o IP: ')
                    porta = input('Informe a Porta: ')
                    realiza_scan = lista_proc(session, scan)
                elif escolha == 2 or escolha == '02':
                    oidbulk = input('Digite o PID que necessita monitorar: ')
                    oidget(session, oidbulk)
                elif escolha == 3 or escolha == '03':
                    teste()
                elif escolha == 0 or escolha == '00':
                    print('\nSaindo do programa. \nObrigado por utilizar!\n')
                    valida = True
                else:
                    print('\nOpção inválida. Escolha uma das opções apresentada!\n')
            else:
                print('\nOpção inválida. Escolha uma das opções apresentada!\n')
        except:
            print('\nErro! Verifique as informações inseridas\n')


menu()
