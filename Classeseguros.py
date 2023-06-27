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

    def aumentar_idade(self):
        pass

    def nome_cliente(self):
        pass


class Seguro:
    def __init__(self, num_apolice, proprietario):
        self._num_apolice = num_apolice
        self._proprietario = Cliente
        
    def calcularValor(self):
        pass
    def calcularPremio(self):
        pass
        
    def __str__(self):
        dados = f'Nome do proprietário: {self._proprietario}'
        return dados


class SeguroVida(Seguro):
    def __init__(self, num_apolice, proprietario, nome_benfic):
        super().__init__(num_apolice, proprietario)
        self._nome_benific = nome_benefic
        
    def calcularValor(self):
        benefic = self._proprietario        
        if benefic.idade >= 1 and benecif.idade <= 30:
            valor = 800
        elif benefic.idade >=31 and benefic.idade <= 50:
            valor = 1.300
        elif benefic.idade < 50:
            valor = 1.600

        return valor
                    
    def calcularPremio(self):
        benefic = self._proprietario
        if  benefic.idade >= 1 and benefic.idade <= 30:
            premio = 50.000
        elif benefic.idade >=31 and benefic.idade <= 50:
            premio = 30.000
        elif benefic.idade < 50:
            premio = 20.000

        return premio
    def __str__(self):
        return super().__str__


class SeguroAutomovel(Seguro):
    def __init__(self, num_apolice, proprietario, num_licenca, nome_modelo, ano, valor_auto):
        super().__init__(num_apolice, proprietario)
        self._num_licenca = num_licenca
        self._nome_modelo = nome_modelo
        self._ano = ano
        self._valo_auto = valor_auto
        
    def calcularValor(self):
        valor = self._valor_auto * 0.03
        return valor
    def calcularPremio(self):
        premio = self._valor_auto * 0.8
        return premio
    def calcularFranquia(self):
        franquia = (self._valor_auto * 0.03) * 0.4 
        return franquia
        
    def __str__(self):
        return super().__str__

