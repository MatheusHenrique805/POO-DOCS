class Paciente:
    def __init__(self, id_paciente, nome, data_nasc, contato):
        self.__id_paciente = id_paciente
        self.nome = nome
        self.data_nasc = data_nasc
        self.contato = contato
    
    def __str__(self):
        return f'ID:{self.__id_paciente}\nNome:{self.nome}\nData de nascimento:{self.data_nasc}\nTelefone:{self.contato}'
class Medico:
    def __init__(self, id_medico, crm, nome, especialidade):
        self.__id_medico = id_medico
        self.crm = crm
        self.nome = nome
        self.especialidade = especialidade
    def __str__(self):
        return f'ID:{self.__id_medico}\nCRM:{self.crm}\nNome:{self.nome}\nEspecialidade:{self.especialidade}'

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
        self.data = data
        self.data_retorno = data_retorno
        self.pago = pago
    
    def __str__(self):
        return f'Data da consulta:{self.data}\nPaciente:{self.__paciente.nome}\nMédico:{self.__medico.nome}'
        

