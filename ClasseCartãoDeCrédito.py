#João Augusto da Silva de Morais
#Matheus Henrique de Oliveira Rocha
class cartao:
    def __init__(self, numero, titular, validade, cod_seguranca,limite_compra=1000, senha=None, fatura_pagar=0, valor_min_pagar=0, status='bloqueado'):
        self.__numero = numero
        self.__titular = titular
        self.__validade = validade
        self.__cod_seguranca = cod_seguranca
        self.limite_compra = limite_compra
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
