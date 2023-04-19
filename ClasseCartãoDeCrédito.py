class cartao:
    def __init__(self, numero, titular, validade, cod_seguranca,limite_compra=1000, senha=None, fatura_pagar=0,valor_min_pagar=0, status='bloqueado'):
        self.__numero = numero
        self.__titular = titular
        self.__validade = validade
        self.__cod_seguranca = cod_seguranca
        self.limite_compra = limite_compra
        self.__senha = senha
        self.__fatura_pagar = fatura_pagar
        self.__senha = senha
