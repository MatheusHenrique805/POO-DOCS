from datetime import *
class Consultamedica:
    def __init__(self, id_consulta, medico, paciente, data, data_retorno=None , pago=False):
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
        self.__pago = pago
    
    def __str__(self):
        return f'Data da consulta:{self.__data}\nPaciente:{self.__paciente.nome}\nMédico:{self.__medico.nome}'
class Paciente:
    def __init__(self, id_paciente, nome, data_nasc, contato):
        self.__id_paciente = id_paciente
        self.__nome = nome
        self.__data_nasc = data_nasc
        self.__contato = contato
    
    
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


def cadastrar_medico():
    pass


def cadastrar_paciente():
    cpf = int(input('Informe o cpf.\n'))
    nome = input('Agora seu nome.\n')
    data_nascimento = datetime.strptime(input("Informe a data de nascimento:"),"%d/%m/%Y").date()
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
            # dar os inputs para os atributos
            # pegar o nome do paciente
            # buscar na lista de pacientes o objeto correspondente
            # pegar o nome do medico
            #buscar na lista de médicos o objeto correspondente
            #criar o objeto ConsultaMedica
            # inserir na lista de consultas médicas
        elif opc == 4:
            # pegar na lista de consultas (por data, por nome do paciente ou por nome do médico)
            # retornar o objeto correspondente ao critério da pesquisa
