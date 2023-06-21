class Seguro:
    def __init__(self, num_apolice, proprietario):
        self._num_apolice = num_apolice
        self._proprietario = proprietario
    
class SeguroVida(Seguro):
    def __init__(self, num_apolice, proprietario, nome_beneficiario):
        super().__init__(num_apolice, proprietario)
        self._nome_beneficiario = nome_beneficiario
class SeguroAutomovel(Seguro):
    def __init__(self, num_apolice, proprietario, num_licenca, nome_modelo, ano, valor_auto):
        super().__init__(num_apolice, proprietario)
        self._num_licenca = num_licenca
        self._nome_modelo = nome_modelo
        self._ano = ano
        self._valo_auto = valor_auto
class Cliente:
    def __init__(self, cpf, nome, idade):
        self.__cpf = cpf
        self.__nome = nome
        self.__idade = idade

    @property
    def cpf(self):
        return self.__cpf
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    

