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
#Falta completar essa função
def faturamentoClinica(d):
    faturamento = 0
    mes = int(input('O relatorio de qual mês você quer ver? '))
    for cod, cons in d.items():
        data = cons[0].data
        data_consulta = datetime.strptime(data, '%d/%m/%Y').date() 
        if data_consulta.month == mes and cons[0].estado == True:
            print('_'*55)
            print(f'Consulta {cod}: \n{cons}\n')
            print('_'*55)
        else:
            pass


def relatorioConsultas(d):
    while True:
        try:
            cont = 0
            esc = int(input('Medico: \n1-Arnaldo \n2-Laura \n3-Jonas \n4-Carlos\n>>>'))
            if esc >= 1 and esc <= 4:
                medico, area = areas_med(esc)
                if cont == 0:
                    print('_'*55)
                    print(' '*19,f'{medico.upper()} ({area.upper()})')
                for cod, cons in d.items():
                    if cons[0].nome_medico == medico and cons[0].estado == True :
                        print('_'*55)
                        print(f'Consulta {cod}: \n{cons}\n')
                        print('_'*55)
                        cont += 1
                    else:
                        pass
                break 
            else:
                print('As escolhas vão de 1 até 4!!!')
                
            print(f'Número de consulas realizadas: {cont}') 
        except:
            print('Opção inválida!!! Tente novamente!')

def agendar_retorno(ret,d):
    while True:
        try:
            cod = int(input('Digite o código da consulta.\n'))
            for codigo, consult in d.items():
                if cod == codigo:
                    data_retorno = escolher_data()
                    data_con_passada = datetime.strptime(consult[0].data, '%d/%m/%Y').date()
                    preco = 0
                    if date.today() <= data_con_passada + timedelta(days=30):
                        retorno = consulta(data_retorno, consult[0].nome_paciente, consult[0].area_medica, consult[0].nome_medico, preco)
                        ret[data_retorno] = retorno
                        print('Seu retorno foi marcado.')
                        break
                    else:
                        print('O prazo para marcar o retorno acabou!Será necessario marcar uma nova consulta!!')
                        break
                else:
                    pass
            break
        except:
            print('Erro na digitação do código da consulta!!')
            
    return ret
                
                
def cancelar_consulta(d):
    while True:
        try:
            cod = int(input('Digite o código da consulta deseja.\n'))
            print('-'*20, 'CONSULTA','-'*20)
            for codigo, consulta in d.items():
                if cod == codigo:
                    print(consulta[0].nome_medico)
                    print('_'*55)
                    print(f'Consulta {codigo}: \n{consulta}\n')
                    print('_'*55)
                    esc = input('Deseja cancelar essa consulta?(S-Sim/N-Não)\n').upper()[0]
                    if esc == 'S':
                        del d[codigo]
                        print('Sua consulta foi cancelada.')
                        break
                    elif esc == 'N':
                        pass
                        break
                    else:
                        print('Opção inválida!!')
                else:
                    pass
            break
        except:
            print('Só números inteiros como respostas!!!')
            
    return d
             
#Efetua o pagamento das consultas não pagas e verifica as que ja foram pagas.
def pagamento(d):
    while True:
        try:        
            cod = int(input('Digite o código da Consulta.\n'))
            if cod in d.keys():
                cons = d[cod]
                if cons[0].estado == True:
                    print('A Consulta já está paga.')
                    break
                else:
                    print('O valor da Consulta é de R$ 300,00.')
                    while True:
                        try:  
                            sit = input('Deseja pagar a consulta agora [S - Sim/N - Não]?\n').upper()  
                            if sit == 'S':
                                cons[0].pagar_consulta()
                                sleep(1)
                                print('-'*20,'CONSULTA PAGA', '-'*20)
                                break
                            elif sit == 'N':
                                print('Lembre-se que para poder se consultar você tem que efetuar o pagamento!!')
                                sleep(1)
                                break
                            else:
                                print('Digite uma das opções disponíveis!')
                        except:
                            print('As opções disponíveis são "S" e "N"!!')
                break
            else:
                print('Código não encontrado', end=' ')
        except:
            print('Verifique se esse é realmente o código correto!!!')
#Dicionario com as áreas disponivel para consulta e seus medicos.
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
    
    return areamed, nomemedic
            
#Verfica se a data marcada pra consulta não está errada, como cair num dia que já passou ou em um fim de semana
def escolher_data():
    fds = [5, 6]
    while True:
        try:
            d = datetime.strptime(input("Data da consulta/Retorno:\n"),"%d/%m/%Y").date()
            if d <= date.today() or d.weekday() in fds:
                print("Data inserida menor que data atual ou corresponde a um dia de sábado ou domingo.")
            else:
                data = d.strftime("%d/%m/%Y")
                break
        except:
            print('Digite a data desse modo dd/mm/aa!!')
                
    return data
                        
#Cria o objeto nova_consulta, inseri ele dentro de uma lista que é implementada num dicionário.
def criar_consulta(dc):
    while True:
        try:
            #Preechimento dos dados da consulta.
            data = escolher_data()
            nome = input('Nome completo do paciente:\n').capitalize()
            if nome.isalpha() is True:
                print('_'*55)
                area = int(input('\nPara qual área é a consulta: \n1-Pediatria \n2-Cardiologia \n3-Dermatologia \n4-Urologia \n>>> '))
                if area <= 4 and area >= 1:
                    area_med, nome_med = areas_med(area) 
                    preco = 300
                    #Criação do objeto consulta e implementação num dicionario.
                    nova_consulta = consulta(data, nome, area_med, nome_med, preco)
                    nova_consulta_lista = [nova_consulta]  
                    print(nova_consulta)
                    dc[nova_consulta.codigo] = nova_consulta_lista
                    break
                else:
                    print('A escolha só pode ser de 1 até 4!!')
            else:
                print('Somente carecteres alfabéticos!!')
        except:
            print('Houve um erro. Por favor, preencha os campos novamente.')
    return dc

#Mostra ao cliente o menu do consultorio e recebe a ação que ele quer executar no sistema.
def menu():
    while True:
        try:
            print('_' *55)
            print('1 - Nova consulta \n2 - Pagar consulta \n3 - Cancelar consulta \n4 - Agendar retorno \n5 - Relatório de consultas realizadas no mês por médico \n6 - Relatório de faturamento da Clinica por mês\n0 - Encerrar programa')
            print('_' *55)
            #Verifica se ação do usuário está nas opções citadas a cima.
            resp = int(input('>>> '))
            if resp > 0 and resp < 7:
                break
        except:
            print('Açãoa não encontrada. Tente novamente.')
    return resp 

        
def main():
    retornos = {}
    dic_consultas = {}
    while True:
        r = menu()
        if r == 1:
            consultas = criar_consulta(dic_consultas)
        elif r == 2:
            pagamento(consultas)
        elif r == 3:
            consultas = cancelar_consulta(consultas)
        elif r == 4:
            retornos = agendar_retorno(retornos,consultas)
        elif r == 5:
            relatorioConsultas(dic_consultas)  
        elif r == 6:
            faturamentoClinica(dic_consultas)
        elif r == 0:
            print('Encerrando programa!!')
            sleep(1)
            break
        
                
if __name__ == '__main__':
    main()
