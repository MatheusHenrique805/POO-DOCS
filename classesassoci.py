from datetime import *
class Consultamedica:
    def __init__(self, id_consulta, medico, paciente, data, data_retorno=None , pagamento=False):
        self.__id_consulta = id_consulta
        if type(medico) == Medico:
            self.__medico = medico
        else:
            raise 'Error!'
        if type(paciente) == Paciente:
            self.__paciente = paciente
        else:
            raise 'Error!'
        self.__data = data
        self.__data_retorno = data_retorno
        self.__pagamento = pagamento
        
    @property
    def id_consulta(self):
        return self.__id_consulta
    @property
    def medico(self):
        return self.__medico
    @property
    def paciente(self):
        return self.__paciente
    @property
    def pago(self):
        return self.__pago
    @property
    def data_retorno(self):
        return self.__data_retorno
    
    def __str__(self):
        return f'Data da consulta:{self.__data}\nPaciente:{self.__paciente.nome}\nMédico:{self.__medico.nome}'
class Paciente:
    def __init__(self, id_paciente, nome, data_nasc, contato):
        self.__id_paciente = id_paciente
        self.__nome = nome
        self.__data_nasc = data_nasc
        self.__contato = contato
        
    @property
    def id_paciente(self):
        return self.__id_paciente
    @property
    def data_nasc(self):
        return self.__dt_nasc
    @property
    def contato(self):
        return self.__contato
    
    def __str__(self):
        return f'ID:{self.__id_paciente}\nNome:{self.__nome}\nData de nascimento:{self.__data_nasc}\nTelefone:{self.__contato}'
class Medico:
    def __init__(self, id_medico, crm, nome, especialidade):
        self.__id_medico = id_medico
        self.__crm = crm
        self.nome = nome
        self.especialidade = especialidade
    def __str__(self):
        return f'ID:{self.__id_medico}\nCRM:{self.__crm}\nNome:{self.nome}\nEspecialidade:{self.especialidade}'

    @property
    def id_medico(self):
        return self.__id_medico
    @property
    def crm(self):
        return self.__crm


def escolher_data():
    fds = [5, 6]
    while True:
        try:
            d = datetime.strptime(input("Informe a data da consulta(dd/mm/aaaa).\n"),"%d/%m/%Y").date()
            if d <= date.today() or d.weekday() in fds:
                print("Data inserida não corresponde a um útil.")
            else:
                data = d.strftime("%d/%m/%Y")
                break
        except:
            print('Digite a data desse modo dd/mm/aa!!')
                
    return data


def confirmar_objetos(nome, lista):
    for i in lista:
        if nome == i.nome:
            return i.nome
        else:
            continue
    
    return None


def cadastrar_medico():
   
    cpf = int(input('Informe seu CPF(SEM PONTUAÇÃO GRÁFICA!!!).\n'))
    nome = input('Informe seu nome.\n')
    crm = int(input('Informe seu crm(SEM PONTUAÇÃO GRÁFICA!!!).\n'))
    espec_medica = input('Informe a sua especialidade médica.\n')
    
    return Medico(cpf, crm, nome, espec_medica)
            

def cadastrar_paciente():
    cpf = int(input('Informe o CPF(SEM PONTUAÇÃO GRÁFICA!!!).\n'))
    nome = input('Agora seu nome.\n')
    data_nascimento = datetime.strptime(input("Informe a data de nascimento(dd/mm/aaaa):"),"%d/%m/%Y").date()
    contato = int(input('Telefone para contato.\n'))

    return Paciente(cpf, nome, data_nascimento, contato)


def menu():
    print('1 - Cadastrar Paciente')
    print('2 - Cadastrar Médico')
    print('3 - Marcar Consulta')
    print('4 - Pagar Consulta')
    print('5 - Cancelar Consulta')
    print('6 - Marcar Retorno')
    print('7 - Sair')

    opc = int(input('Informe a opção desejada.\n'))
    if opc > 0 and opc <= 7:
        return opc
    else:
        print('Opção inválida!!!')
        menu()


def main():
    consultas = []
    pacientes = []
    medicos = []

    while True:
        opc = menu()
        
        if opc == 1:
            p1 = cadastrar_paciente()
            pacientes.append(p1)
        elif opc == 2:
            m1 = cadastrar_medico()
            medicos.append(m1)
        elif opc == 3:
            nome_paciente = input('Informe o nome do paciente.\n')
            pac = confirmar_objetos(nome_paciente, pacientes)
            cod_consulta = pacientes.index(pac)
            nome_medico = input('Informe nome do médico.\n')
            medi = confirmar_objetos(nome_medico, medicos)
            data_consulta = escolher_data()
            consultas.append(Consultamedica(cod_consulta, medi, pac, data_consulta))
        elif opc == 4:
            pass
