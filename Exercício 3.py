from datetime import *
#Criação da classe consulta.
class consulta:
    #Define o construtor, fazendo com que os atributos sejam 'preco' e 'consulta' recebam valores na criação do objeto. 
    def _init_(self, data, codigo, nome_medico, nome_paciente, area_medica,  preco):
        self.data = data
        self.nome_medico = nome_medico
        self.nome_paciente = nome_paciente
        self.area_medica = area_medica
        self.preco = preco
        self.codigo = codigo 
    def str(self):
        pass
        
    def cod_consulta(self):
        self.cod_consulta += 1 
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
    dic_areamed['pediatria'] = 'Arnaldo'
    dic_areamed['cardiologia'] = 'Laura'
    dic_areamed['dermatologia'] = 'Jonas'
    dic_areamed['urologista'] = 'Carlos'
    cont = 1
    for key in dic_areamed:
            if esc == cont:
                areamed = key
                nomemedic = dic_areamed.get(key)
                break
            else:
                cont += 1
    
    return areamed, nomemedic


def escolher_data():
    fds = [5, 6]
    d = datetime.strptime(input("Data da consulta: "),"%d/%m/%Y").date()
    if d <= date.today() or d.weekday() in fds:
        raise ValueError("Data de consulta menor que data atual.")
    else:
         d = d.strftime('%d/%m/%Y')
    return d
    
def criar_consulta():
    while True:
        try:
            data = escolher_data()
            nome = input('Nome do paciente: ')
            area = int(input('Para qual área é a consulta: \n1-Pediatria \n2-Cardiologia \n3-Dermatologia \n4-Urologia \n>>> '))
            area_med, nome_med = areas_med(area) 
            print(f'\nPaciente: {nome} \nData da consulta: {data} \nPara a área de: {area_med} \nMedico(a): {nome_med}\n')
            break
        except:
            print('Houve um erro. Por favor, preencha os campos novamente.')

def main():
    
    lista_consultas = []
    while True:
        try:
            r = menu()
            if r == 1:
                criar_consulta()
        except:
            print('Erro.')
            
        
if __name__ == '__main__':
    main()