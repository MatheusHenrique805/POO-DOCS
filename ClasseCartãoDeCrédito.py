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
            return f'nº cartão: {self.numero} \ntitular: {self.titular}\n valor mínimo da fatura: {self.valor_min_pagar}\nValor da fatura: {self.fatura_pagar}' 
        
        def desbloquear(self):
            if self.__status == 'bloqueado':
                self.__status = 'desbloqueado'
                print('Cartão Desbloqueado.')
            else:
                print(f'Seu cartão ja está {self.__status}')
                
        def bloquear(self):
            if self.__status != 'bloqueado':
                self.__validade = 'desbloqueado'
                print('Cartão Bloqueado.')
            else:
                print(f'Seu cartão ja está {self.__status}')

        def mudar_senha(self, cod_seg, senha):
            if cod_seg == self.__cod_seg:
                self.__senha = senha
            else:
                print(f'codigo inválido')
                
        def comprar(self, valor, senha):
            if self.__status != 'bloqueado':
                if self.__limite_pagar > valor:
                    if senha == self.__senha:
                        self.__limite_compra -= valor
                        self.__fatura_pagar += valor
                        self.__valor_min_pagar = self._fatura_pagar * 0.3
                        print('Compra Realizada.')
                        
        def pagar_fatura(self, valor):
            if valor >= self.__valor_min_pagar and valor <= self.__fatura_pagar:
                self.__fatura_pagar -= valor
                self.__lim_compras += valor
                print('Fatura paga.')
            else:
                print('Valor não aceitável')
                
ct= [cartao(1111, 'João Augusto', '05/2023', 567, 3000, 1234),
    cartao(1112, 'Matheus Henrique', '06/2023', 550),
    cartao(1113, 'Maria Eduarda', '04/2023', 500, 4500, 1234),
    cartao(1114, 'Eizabeth Webber', '03/2023', 504),
    cartao(1115, 'Elizandra Scott', '10/2023', 405)]

print(ct[0].status)
ct[0].comprar(200, 1234)
