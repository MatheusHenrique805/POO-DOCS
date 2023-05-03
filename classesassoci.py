class Pacinte:
    def __init__(self, id_paciente, nome, data_nasc, contato):
        self.__id_paciente = id_paciente
        self.nome = nome
        self.data_nasc = data_nasc
        self.contato = contato
    
    def __str__(self):
        return f'{self.__id_paciente}{self.nome}{self.data_nasc}{self.contato}'
class Medico:
    def __init__(self, id_medico, crm, nome, especialidade):
        self.__id_medico = id_medico
        self.crm = crm
        self.nome = nome
        self.especialidade = especialidade
    def __str__(self):
        return f'{self.__id_medico}{self.crm}{self.nome}{self.especialidade}'

class Consultamedica:
    def __init__(self, id_consulta, medico, paciente, data, data_retorno , pago=False):
        self.__id_consulta = id_consulta
        self.medico = medico
        self.paciente = paciente
        self.data = data
        self.data_retorno = data_retorno
        self.pago = pago
    