# João Augusto da Silva de Morais
# Matheus Henrique de Oliveira Rocha

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
        return f'Nome do proprietário: {self._proprietario.nome}\nCPF: {self._proprietario.cpf}' 


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
            return self.valor_seguro
        elif benefic.idade >= 31 and benefic.idade <= 50:
            self._valor_seguro = 1300
            return self.valor_seguro
        else:
            self._valor_seguro = 1600
            return self.valor_seguro

                    
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
        return "------------INFORMAÇÃO DO SEGURO DE VIDA--------------\n" + super().__str__() + f' \nBeneficiário: {self._nome_benific}' + '\n-------------------------------------------------------'


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
        return self.valor_seguro
        
    def calcularPremio(self):
        self._valor_premio = self._valor_auto * 0.8
        return self.valor_premio
        
    def calcularFranquia(self):
        self._valor_franquia = (self._valor_auto * 0.03) * 0.4
        return self._valor_franquia
        
    def __str__(self):
        return "------------INFORMAÇÕES DO SEGURO AUTOMOTIVO--------------\n" + super().__str__() + f'\nNúmero da Licença: {self.num_lincenca}\nModelo: {self.nome_modelo}\nAno: {self.ano}'   +'\n-------------------------------------------------------'

class ControleDeSeguro:
    def __init__(self):
        self._seguros = []
    
    def cadastrarSeguroVida(self, seguro_vida):
        if type(seguro_vida) == SeguroVida:
            self._seguros.append(seguro_vida)
            print('Cadastro realizado com sucesso!')
        else:
            print('Por favor, verificar se a informação fornecida está correta.')

    def cadastrarSeguroAutomotivo(self, seguro_automovel):
        if type(seguro_automovel) == SeguroAutomovel:
            self._seguros.append(seguro_automovel)
            print('Cadastro realizado com sucesso!')
        else:
            print('Por favor, verificar se a informação fornecida está correta.')
        
    def exibirRelatorio(self):
        total_seguros_vida = 0
        total_seguros_automotivo = 0
        total_valores = 0.0
        
        print("RELATÓRIO DE SEGUROS")
        print("---------------------------------")
        for seguro in self._seguros:
            print("Número da apólice:", seguro._num_apolice)
            print("Nome do segurado:", seguro._proprietario.nome)
            print("Valor do seguro:", seguro._valor_seguro)
            print("Prêmio:", seguro._valor_premio)

            if isinstance(seguro, SeguroVida):
                total_seguros_vida += 1
            elif isinstance(seguro, SeguroAutomovel):
                total_seguros_automotivo += 1
        
            total_valores += seguro._valor_seguro

            print("---------------------------------")

        print("Total de seguros de vida:", total_seguros_vida)
        print("Total de seguros automotivos:", total_seguros_automotivo)
        print("Total dos valores:", total_valores)
        
#######################################################################
# Criando os objetos da classe Cliente
joao = Cliente(20222110344, 'João Augusto', 18)
matheus = Cliente(20222110806, 'Matheus Henrique', 32)
flavio = Cliente(20222110254, 'Flávio Leão', 50)
adriano = Cliente(20222110866, 'Adriano Júnior', 21)
andressa = Cliente(20222110135, 'Andressa Felix', 30)
eduarda = Cliente(20222110531, 'Maria Eduarda', 55)
nikolas = Cliente(20222110825, 'Nikolas Felipe', 23)
#######################################################################
# Criando os objetos da classe SeguroVida
sv1 = SeguroVida(11, joao, joao.nome)
sv2 = SeguroVida(12,matheus,matheus.nome)
sv3 = SeguroVida(13, flavio, flavio.nome)
sv4 = SeguroVida(14, adriano, adriano.nome)
sv5 = SeguroVida(15, andressa, andressa.nome)
# Como to na dúvida do que botar no 'nome_benefic' farei esses exemplos separados
sv6 = SeguroVida(16, eduarda, 'Pedro Silva')
sv7 = SeguroVida(17, nikolas, 'Maria Santana')
print()
# Calculando o valor do seguro e o premio
print(f'Valor do Seguro R$:{sv1.calcularValor()}\nValor do Prémio R$: {sv1.calcularPremio()}\n')
print(f'Valor do Seguro R$:{sv2.calcularValor()}\nValor do Prémio R$: {sv2.calcularPremio()}\n')
print(f'Valor do Seguro R$:{sv3.calcularValor()}\nValor do Prémio R$: {sv3.calcularPremio()}\n')
print(f'Valor do Seguro R$:{sv4.calcularValor()}\nValor do Prémio R$: {sv4.calcularPremio()}\n')
print(f'Valor do Seguro R$:{sv5.calcularValor()}\nValor do Prémio R$: {sv5.calcularPremio()}\n')
print(f'Valor do Seguro R$:{sv6.calcularValor()}\nValor do Prémio R$: {sv6.calcularPremio()}\n')
print(f'Valor do Seguro R$:{sv7.calcularValor()}\nValor do Prémio R$: {sv7.calcularPremio()}\n')
print()
#Exibindo alguns seguros pra teste
print(sv1)
print(sv6)
print(sv3)
print(sv2)
print('\n\n\n\n')
#######################################################################
# Criando os objetos da classe SeguroAutomavel
sa1 = SeguroAutomovel(21, andressa, 1020,'Volkswagen Golf GTI', 2022, 150000.00) 
sa2 = SeguroAutomovel(22,joao, 2030, 'Ford Mustang', 2021, 300000.00) 
sa3 = SeguroAutomovel(23, matheus, 3040, 'Chevrolet Onix', 2023, 70000.00) 
sa4 = SeguroAutomovel(24, nikolas, 4050, 'Toyota Corolla', 2022, 120000.00) 
sa5 = SeguroAutomovel(25, adriano, 6070, 'Honda Civic', 2023, 111000.00) 
print()
# Calculando o valor do seguro, do premio e da franquia
print(f'Valor do Seguro R$:{sa1.calcularValor()}\nValor do Prémio R$: {sa1.calcularPremio()}\nValor da Franquia R$: {sa1.calcularFranquia()}\n')
print(f'Valor do Seguro R$:{sa2.calcularValor()}\nValor do Prémio R$: {sa2.calcularPremio()}\nValor da Franquia R$: {sa2.calcularFranquia()}\n')
print(f'Valor do Seguro R$:{sa3.calcularValor()}\nValor do Prémio R$: {sa3.calcularPremio()}\nValor da Franquia R$: {sa3.calcularFranquia()}\n')
print(f'Valor do Seguro R$:{sa4.calcularValor()}\nValor do Prémio R$: {sa4.calcularPremio()}\nValor da Franquia R$: {sa4.calcularFranquia()}\n')
print(f'Valor do Seguro R$:{sa5.calcularValor()}\nValor do Prémio R$: {sa5.calcularPremio()}\nValor da Franquia R$: {sa5.calcularFranquia()}\n')
print()
# Exibindo alguns seguros de automoveis para teste
print(sa2)
print(sa5)
print(sa1) 
print('\n\n\n\n')
#######################################################################
# Criando um objeto e executando os metodos da classe ControleDeSeguro
cont_seguro = ControleDeSeguro()
# Cadastrandos os objetos de SeguroVida na classe ControleDeSeguro
cont_seguro.cadastrarSeguroVida(sv1)
cont_seguro.cadastrarSeguroVida(sv2)
cont_seguro.cadastrarSeguroVida(sv3)
cont_seguro.cadastrarSeguroVida(sv4)
cont_seguro.cadastrarSeguroVida(sv5)
cont_seguro.cadastrarSeguroVida(sv6)
cont_seguro.cadastrarSeguroVida(sv7)
print()
# Cadastrandos os objetos de SeguroAutomovel na classe ControleDeSeguro
cont_seguro.cadastrarSeguroAutomotivo(sa1)
cont_seguro.cadastrarSeguroAutomotivo(sa2)
cont_seguro.cadastrarSeguroAutomotivo(sa3)
cont_seguro.cadastrarSeguroAutomotivo(sa4)
cont_seguro.cadastrarSeguroAutomotivo(sa5)
print('\n\n\n')
# Exibindo relatorio dos seguros
cont_seguro.exibirRelatorio()
#######################################################################
