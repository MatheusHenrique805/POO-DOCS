#João Augusto da Silva de Morais
#Matheus Henrique de Oliveira Rocha


#data_atual = date.today()
#print(data_atual)       
#data_em_texto = '{}/{}'.format(data_atual.month,data_atual.year)
#print(data_em_texto)
#data_em_texto = data_atual.strftime('%m/%Y')
#print(data_em_texto)

class cartao:
    def __init__(self, numero, titular, validade, cod_seguranca,limite_compra=1000, senha=None, fatura_pagar=0, valor_min_pagar=0, status='bloqueado'):
        self.__numero = numero
        self.__titular = titular
        self.__validade = validade
        self.__cod_seguranca = cod_seguranca
        self.__limite_compra = limite_compra
        self.__senha = senha
        self.__fatura_pagar = fatura_pagar
        self.__valor_min_pagar = valor_min_pagar
        self.__status = status

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, valor):
        print('Sem permissão.')

    @property
    def validade(self):
        return self.__validade

    @property
    def cod_seguranca(self):
        return self.__cod_seguranca

    @property
    def limite_compra(self):
        return self.__limite_compra

    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self, valor):
        print('Sem permissão')

    @property
    def fatura_pagar(self):
        return self.__fatura_pagar

    @property
    def valor_min_pagar(self):
        return self.__valor_min_pagar

    @property
    def status(self):
        return self.__status

    def __str__(self):
        return f'nº cartão: {self.numero} \ntitular: {self.titular}\nvalor mínimo da fatura: {self.valor_min_pagar}\nValor da fatura: {self.fatura_pagar}\n' 

    def desbloquear(self):
        data_atual = (4, 2023)
        if self.__status == 'bloqueado': 
            if self.__validade[0] >= data_atual[0] and self.__validade[1] >= data_atual[1]:
                self.__status = 'desbloqueado'
                print('Cartão Desbloqueado.')
            else:
                print('Cartão fora da validade')
        else:
            print(f'Seu cartão ja está {self.__status}')

    def bloquear(self):
        data_atual = (4, 2023)if senha == self.__senha:
104
                    self.__limite_compra -= valor
105
                    self.__fatura_pagar += valor
106
                    self.__valor_min_pagar = self._fatura_pagar * 0.3
107
                    print('Compra Realizada.')
108
                else:
109
                    print('Senha inválida')
        if self.__status != 'bloqueado':
            if self.__validade[0] < data_atual[0] and self.__validade[1] >= data_atual[1]:
                self.__status = 'bloqueado'
                print('Cartão Bloqueado.')
            else:
                print('Cartão fora da validade')
        else:
            print(f'Seu cartão ja está {self.__status}')

    def mudar_senha(self, cod_seg, senha):
        if self.__status != 'bloqueado':
            if cod_seg == self.__cod_seg:
                self.__senha = senha
            else:
                print(f'codigo inválido')

    def comprar(self, valor, senha):
        data_atual = (4, 2023)
        if self.__status != 'bloqueado':
            if senha == self.__senha:
                if self.__limite_compra > valor:
                    if self.__validade[0] >= data_atual[0] and self.__validade[1] >= data_atual[1]:
                        self.__limite_compra -= valor
                        self.__fatura_pagar += valor
                        vlr_min = self.__fatura_pagar * 3/100
                        self.__valor_min_pagar = vlr_min
                        print('Compra Realizada.')
                    else:
                        print('Cartão está fora da validade.')
                else:
                    print('Valor da compra maior que o limite permitido.')
            else:
                print('Senha inválida.')
        else:
            print('O cartão está bloqueado.')

    def pagar_fatura(self, valor):
        data_atual = (4, 2023)
        if self.__validade[0] >= data_atual[0] and self.__validade[1] >= data_atual[1]:
            if valor >= self.__valor_min_pagar and valor <= self.__fatura_pagar:
                self.__fatura_pagar -= valor
                self.__lim_compras += valor
                print('Fatura paga.')
                if self.__statif senha == self.__senha:
104
                    self.__limite_compra -= valor
105
                    self.__fatura_pagar += valor
106
                    self.__valor_min_pagar = self._fatura_pagar * 0.3
107
                    print('Compra Realizada.')
108
                else:
109
                    print('Senha inválida')us == 'bloqueado':
                    self.desbloquear()
                else:
                    pass
            else:
                print('Valor não aceitável')
        else:
            print('Cartão está fora da validade.')
            
#def __init__(self, numero, titular, validade, cod_seguranca,limite_compra=1000, senha=None, fatura_pagar=0, valor_min_pagar=0, status='bloqueado'):                
ct= [cartao(1111, 'João Augusto', (7,2023), 567, 3000, 1234, status='desbloqueado'),
    cartao(1112, 'Matheus Henrique', (2, 2023), 550),
    cartao(1113, 'Maria Eduarda', (4,2023), 500, 4500, 1234),
    cartao(1114, 'Eizabeth Webber', (10, 2023), 504), 
    cartao(1115, 'Elizandra Scott', (5, 2023), 405)]

#O print do __str__
for i in range(5):
    print(ct[i])
   
#Método bloquear
print(ct[1].bloquear)
print(ct[1].status)

#Mudar senha
print(ct[4].mudar_senha(345, 1234))
print(ct[4].senha)

#Comprar
print(ct[3].comprar(1200,1234))
#Pagar fatura
print(ct[0].pagar_fatura(1050) 


