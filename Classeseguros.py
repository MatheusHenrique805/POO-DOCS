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


class Seguro:
    def __init__(self, num_apolice, proprietario):
        self._num_apolice = num_apolice
        self._proprietario = proprietario # É o objeto da classe Cliente
    
    @property
    def num_apolice(self):
        return self._num_apolice
    @property
    def num_apolice(self):
        return self._proprietario
    
    def calcularValor(self):
        pass
    def calcularPremio(self):
        pass
        
    def __str__(self):
        dados = f'Nome do proprietário: {self._proprietario.nome}'
        return dados


class SeguroVida(Seguro):
    def __init__(self, num_apolice, proprietario, nome_benefic, valor_seguro = None, valor_premio = None):
        super().__init__(num_apolice, proprietario)
        self._nome_benific = nome_benefic
        # Adicionei esses atributos pra ficar mais fácil mexer na classe ControleDeSeguro
        self._valor_seguro = valor_seguro
        self._valor_premio = valor_premio
    
    @property
    def valor_seguro(self):
        return self._nome_benific
    @property
    def valor_seguro(self):
        return self._valor_seguro
    @property
    def valor_premio(self):
        return self._valor_premio
          
    def calcularValor(self):
        benefic = self._proprietario        
        if benefic.idade >= 1 and benefic.idade <= 30:
            self._valor_seguro = 800
            return self._valor_seguro
        elif benefic.idade >= 31 and benefic.idade <= 50:
            self._valor_seguro = 1300
            return self._valor_seguro
        else:
            self._valor_seguro = 1600
            return self._valor_seguro

                    
    def calcularPremio(self):
        benefic = self._proprietario
        if  benefic.idade >= 1 and benefic.idade <= 30:
            self._valor_premio = 50000.00
            return self._valor_premio
        elif benefic.idade >= 31 and benefic.idade <= 50:
            self._valor_premio = 30000.00
            return self._valor_premio
        else:
            self._valor_premio = 20000.00
            return self._valor_premio

    def __str__(self):
        return super().__str__


class SeguroAutomovel(Seguro):
    def __init__(self, num_apolice, proprietario, num_licenca, nome_modelo, ano, valor_auto, valor_seguro = None, valor_premio = None, valor_franquia = None):
        super().__init__(num_apolice, proprietario)
        self._num_licenca = num_licenca
        self._nome_modelo = nome_modelo
        self._ano = ano
        self._valor_auto = valor_auto
        # Adicionei esses atributos pra ficar mais fácil mexer na classe ControleDeSeguro
        self._valor_seguro = valor_seguro
        self._valor_premio = valor_premio
        self._valor_franquia =  valor_franquia
    
    @property
    def num_lincenca(self):
        return self._num_licenca
    @property
    def nome_modelo(self):
        return self._nome_modelo
    @property
    def ano(self):
        return self._ano
    @property
    def valor_auto(self):
        return self._valor_auto
    @property
    def valor_seguro(self):
        return self._valor_seguro
    @property
    def valor_premio(self):
        return self._valor_premio
    @property
    def valor_premio(self):
        return self._valor_premio
        
    def calcularValor(self):
        self._valor_seguro = self._valor_auto * 0.03
        return self._valor_seguro
        
    def calcularPremio(self):
        self._valor_premio = self._valor_auto * 0.8
        return self._valor_premio
        
    def calcularFranquia(self):
        self._valor_franquia = (self._valor_auto * 0.03) * 0.4
        return self._valor_franquia
        
    def __str__(self):
        return super().__str__

class ControleDeSeguro:
    def __init__(self):
        self._seguros = []
    
    def cadastrarSeguroVida(self, seguro_vida):
        if type(seguro_vida) == SeguroVida:
            self._seguros.append(seguro_vida)
        else:
            print('Por favor, verificar se a informação fornecida está correta.')

    def cadastrarSeguroAutomotivo(self, seguro_automovel):
        if type(seguro_automovel) == SeguroAutomovel:
            self._seguros.append(seguro_automovel)
        else:
            print('Por favor, verificar se a informação fornecida está correta.')
        
    def exibirRelatorio(self):
        total_seguros_vida = 0
        total_seguros_automotivo = 0
        total_valores = 0.0
        
        print("RELATÓRIO DE SEGUROS")
        print("--------------------")
        for seguro in self._seguros:
            print("Número da apólice:", seguro._numero_apolice)
            print("Nome do segurado:", seguro._proprietario.nome)
            print("Valor do seguro:", seguro._valor_seguro)
            print("Prêmio:", seguro._valor_premio)

            if isinstance(seguro, SeguroVida):
                total_seguros_vida += 1
            elif isinstance(seguro, SeguroAutomovel):
                total_seguros_automotivo += 1
        
            total_valores += seguro._valor_seguro

            print("--------------------")

        print("Total de seguros de vida:", total_seguros_vida)
        print("Total de seguros automotivos:", total_seguros_automotivo)
        print("Total dos valores:", total_valores)
        
        
