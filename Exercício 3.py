from datetime import *
from time import sleep
#Criação da classe consulta.
class consulta:
    cod_consultaAtual = 1#importante
    estado = False#importante
    quantidade_consultas = 0
    faturamento = 0
    #Define o construtor, fazendo com que os atributos sejam 'preco' e 'consulta' recebam valores na criação do objeto. 
    def __init__(self, data, nome_paciente,  area_medica, nome_medico,  preco):
        self.codigo = consulta.cod_consultaAtual
        consulta.cod_consultaAtual += 1
        self.data = data#importante
        self.nome_paciente = nome_paciente#importante
        self.area_medica = area_medica#importante
        self.nome_medico = nome_medico#importante
        self.preco = preco#importante       
        
        
    def __str__(self):
        return f'\nCódigo da consulta: {self.codigo}\nData da consulta: {self.data}\nNome do paciente: {self.nome_paciente}\nÁrea: {self.area_medica}\nMedico(a){self.nome_medico}\nPreço da consulta: R$ {self.preco}'
    def __repr__(self) -> str:
        return f'Data da consulta:{self.data}\nNome do paciente: {self.nome_paciente}\nEsp.medica: {self.area_medica}({self.nome_medico})\nPreço da consulta: R$ {self.preco} \nSituação do pagamento: {self.estado}'
    
    #Metodos da classe.
    def pagar_consulta(self):
        if not self.estado:
            self.estado = True 
            consulta.quantidade_consultas += 1
            consulta.faturamento += 100.00
            return True
        else:
            return False
        
def mostrar_consultas(d):
    print('-'*20, 'CONSULTAS','-'*20)
    for codigo, consulta in d.items():
        print(consulta[0].nome_medico)
        print('_'*55)
        print(f'Consulta {codigo}: \n{consulta}\n')
        print('_'*55)
             
#Mostra ao cliente o menu do consultorio e recebe a ação que ele quer executar no sistema.
#Criar um arquivo .py para guardar o menu e as outras funções seria melhor, deixaria o principal mais limpo.
#FEITO
def menu():
    while True:
        try:
            print('_' *55)
            print('1 - Agendar consulta \n2 - Pagar consulta \n3 - Cancelar consulta \n4 - Agendar retorno \n5 - Relatório de consultas realizadas no mês por médico \n6 - Relatório de faturamento da Clinica por mês')
            print('_' *55)
            #Verifica se ação do usuário está nas opções citadas a cima.
            resp = int(input('>>> '))
            if resp > 0 and resp < 7:
                break
        except:
            print('Ação não encontrada. Tente novamente.')
    return resp 

#Dicionario com as áreas disponivel para consulta e seus medicos.
#FEITO
def areas_med(esc):
    dic_areamed = {}
    dic_areamed['Pediatria'] = 'Arnaldo'
    dic_areamed['Cardiologia'] = 'Laura'
    dic_areamed['Dermatologia'] = 'Jonas'
    dic_areamed['Urologia'] = 'Carlos'
    cont = 1
    for key in dic_areamed:
            if esc == cont:
                areamed = key
                nomemedic = dic_areamed.get(key)
                break
            else:
                cont += 1
    
    return nomemedic, areamed 

#Verfica se a data marcada pra consulta não está errada, como cair num dia que já passou ou em um fim de semana
def escolher_data():
    fds = [5, 6]
    d = datetime.strptime(input("Data da consulta: "),"%d/%m/%Y").date()
    if d <= date.today() or d.weekday() in fds:
        raise ValueError("Data de consulta menor que data atual.")
    else:
        data = d.strftime("%d/%m/%Y")
    return data

#Cria o objeto nova_consulta, inseri ele dentro de uma lista que é implementada num dicionário.
def criar_consulta(dc):
    while True:
        try:
            #Preechimento dos dados da consulta.
            data = escolher_data()
            nome = input('Nome do paciente: ')
            print('_'*55)
            area = int(input('\nPara qual área é a consulta: \n1-Pediatria \n2-Cardiologia \n3-Dermatologia \n4-Urologia \n>>> '))
            nome_med, area_med = areas_med(area) 
            preco = 300
            #Criação do objeto consulta e implementação num dicionario.
            nova_consulta = consulta(data, nome, area_med, nome_med, preco)
            nova_consulta_lista = [nova_consulta]  
            print(nova_consulta)
            dc[nova_consulta.codigo] = nova_consulta_lista
            break
        except:
            print('Houve um erro. Por favor, preencha os campos novamente.')

#Efetua o pagamento das consultas não pagas e verifica as que ja foram pagas.
def pagamento(d):
    while True:        
        cod = int(input('Digite o código da Consulta: '))
        if cod in d.keys():
            cons = d[cod]
            if cons[0].estado == True:
                print('A Consulta já está paga.')
                break
            else:
                print('O valor da Consulta é de R$ 300,00.')
                while True:  
                    sit = input('Deseja pagar a consulta agora [S - Sim/N - Não]? ').upper()  
                    if sit == 'S':
                        # "cons[0]" é o objeto referente ao codigo.
                        cons[0].pagar_consulta()
                        sleep(1)
                        print('-'*20,'CONSULTA PAGA', '-'*20)
                        break
                    elif sit == 'N':
                        print('Lembre-se que para poder se consultar você tem que efetuar o pagamento')
                        sleep(1)
                        break
                    else:
                        print('Resposta inválida. Por favor, digite uma das opções oferecidas.')
            break
        else:
            print('Código inválido. Tente novamente.', end=' ')   

def cancelar_consulta(d):
    while True:
        try:
            codigo = int(input('Digite o Código da consulta que deseja cancelar: '))
            if codigo in d.keys():
                consulta = d[codigo]
                print('-'*20, 'CONSULTA','-'*20)
                print('_'*55)
                print(f'Consulta {codigo}: \n{consulta}\n')
                print('_'*55)
                while True:
                    r = input('Deseja cancelar essa consulta[S - Sim/N - Não]? ').upper()
                    if r == 'S':
                        r2 = input('A consulta será cancelada. Deseja continuar[S - Sim/N - Não]? ').upper()
                        if r2 == 'S':
                            del d[codigo]
                            sleep(1)
                            print('-'*20, 'CONSULTA CANCELADA','-'*20)
                            print('Caso queira marcar uma nova consulta, vá na opção "Agendar consulta".')
                            break
                        elif r2 == 'N':
                            break
                    elif r ==  'N':
                        break
                    else:
                        print('Resposta inválida. Por favor, digite uma das opções oferecidas.', end=' ')
                    
                break
            else:
                print('Código da consulta não encontrado. Tente novamente.', end=' ') 
        except ValueError:
            print('Por favor, digite um valor númerico.', end=' ')
            
def agendar_retorno(ret,d):
    while True:
        try:
            cod = int(input('Digite o código da consulta.\n'))
            for codigo, consult in d.items():
                if cod == codigo:
                    data_retorno = escolher_data()
                    data_con_passada = datetime.strptime(consult[0].data, '%d/%m/%Y').date()
                    consult[0].data = data_retorno
                    preco = 0
                    if date.today() <= data_con_passada + timedelta(days=30):
                        retorno = consulta(consult[0].data, consult[0].nome_paciente, consult[0].area_medica, consult[0].nome_medico, preco)
                        ret[data_retorno] = retorno
                        print('Seu retorno foi marcado')
                        break
                    else:
                        print('O prazo para marcar o retorno acabou!Será necessario marcar uma nova consulta')
                        break
                else:
                    pass
            break
        except:
            print('Erro na digitação do código da consulta!!')   
                     
def relatorioConsultas(d):
    cont = 0
    esc = int(input('Medico: \n1-Arnaldo \n2-Laura \n3-Jonas \n4-Carlos\n>>>'))
    medico, area = areas_med(esc)
    for cod, cons in d.items():
        if cont == 0:
            print('_'*55)
            print(' '*19,f'{medico} ({area})')
        if cons[0].nome_medico == medico:
            print('_'*55)
            print(f'Consulta {cod}: \n{cons}\n')
            print('_'*55)
            cont += 1
    print(f'Número de consulas realidas: {cont}') 

def main():
    dic_consultas = {}
    dic_retorno = {}
    while True:
        r = menu()
        #Criação da nova consulta(FEITO).
        if r == 1:
            criar_consulta(dic_consultas)
        #Efetua o pagamento da consulta e verifica se a consulta foi feita(FEITA).
        if r == 2:
            pagamento(dic_consultas)
        #Cancela a consulta desejada, usando o codigo dela.
        if r == 3:
            cancelar_consulta(dic_consultas)
        #Agendar o retorno.        
        if r == 4:
            agendar_retorno(dic_consultas,dic_consultas)
            pass
        #Relatório de consultas realizadas no mes por médico
        if r == 5:
            relatorioConsultas(dic_consultas)
            pass
        if r == 6:
            mostrar_consultas(dic_consultas)
            pass            
                  
        
if __name__ == '__main__':
    main()
