from datetime import *
#Criação da classe consulta.
class consulta:
    cod_consultaAtual = 1#importante
    #Define o construtor, fazendo com que os atributos sejam 'preco' e 'consulta' recebam valores na criação do objeto. 
    def __init__(self, data, nome_paciente,  area_medica, nome_medico,  preco):
        self.codigo = consulta.cod_consultaAtual
        consulta.cod_consultaAtual +=1
        self.data = data#importante
        self.nome_paciente = nome_paciente#importante
        self.area_medica = area_medica#importante
        self.nome_medico = nome_medico#importante
        self.preco = preco#importante
        
        
    def __str__(self):
        return f'Consulta {self.codigo}: {self.nome_paciente} - {self.area_medica} ({self.nome_medico}) - {self.data}'
        
        
    def cod_consulta(self):
        self.codigo += 1 
    def nome_pacient(self, nome_paci):
        self.nome_paciente = nome_paci
    def nome_medi(self, nome_med):
        self.nome_medico = nome_med
    def area(self, area_med):
        self.area_medica = area_med
   
#Mostra ao cliente o menu do consultorio e recebe a ação que ele quer executar no sistema.
#Criar um arquivo .py para guardar o menu seria melhor, deixaria o principal mais limpo.
#FEITO
def menu():
    while True:
        try:
            print('_' *55)
            print('1 - Nova consulta \n2 - Pagar consulta \n3 - Cancelar consulta \n4 - Agendar retorno \n5 - Relatório de consultas realizadas no mês por médico \n6 - Relatório de faturamento da Clinica por mês')
            print('_' *55)
            #Verifica se ação do usuário está nas opções citadas a cima.
            resp = int(input('>>> '))
            if resp > 0 and resp < 7:
                break
        except:
            print('Ação não encontrada. Tente novamente.')
    return resp 

#Dicionario com as áreas disponivel para consulta e seus medicos.
#FEITO?
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
    d = datetime.strptime(input("Data da consulta: "),"%d/%m/%Y").date()
    if d <= date.today() or d.weekday() in fds:
            raise ValueError("Data de consulta menor que data atual.")
    else:
        data = d.strftime("%d/%m/%Y")
    return data
    
def criar_consulta(l, dc):
    while True:
        try:
            data = escolher_data()
            nome = input('Nome do paciente: ')
            area = int(input('Para qual área é a consulta: \n1-Pediatria \n2-Cardiologia \n3-Dermatologia \n4-Urologia \n>>> '))
            area_med, nome_med = areas_med(area) 
            preco = 300
            l.append(consulta(data, nome, area_med, nome_med, preco))
            consulta_atual = l[-1]
            dc[consulta.cod_consultaAtual] = l 
            print(consulta_atual)
            break
        except:
            print('Houve um erro. Por favor, preencha os campos novamente.')

def main():
    dic_colsutas = {}
    lista_consultas = []
    while True:
        try:
            r = menu()
            if r == 1:
                criar_consulta(lista_consultas, dic_colsutas)
            if r ==  2:
                for key in dic_colsutas:
                    print(key)
                    for item in key:
                        print(item)
                    
                
        except:
            print('Erro.')
            
        
if __name__ == '__main__':
        main()
