class pessoa:
    def __init__(self, nome, peso, altura, sexo, estado='Vivo(a)', estado_civil='Solteiro(a)', conjugue=None):
        self.nome = nome
        self.__idade = idade
        self.__peso = peso            
        self.__altura = altura    
        self.__sexo = sexo
        self.estado = estado
        self.estado_civil = estado_civil
        self.conjuge = conjuge
    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, valor):
        print('Sem permissão')
    
    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, valor):
        print('Sem permissão')
    
    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, valor):
        print('Sem permissão')
        
    @property
    def sexo(self):
        return self.__sexo
    @sexo.setter
    def sexo(self, valor):
        print('Sem permissão')
        
    
    def envelhecer(self):
        if self.estado == 'Vivo':
            self.__idade += 1
            if self.__idade <= 21:
                self.__altura += 0.5
            else:
                print(f'{self.nome} não pode mais crescer, pois está com 21 anos ou mais.') 
        else:
            if self.sexo == 'M':
                print(f'{self.nome} está morto.')
            else:
                print(f'{self.nome} está morta.')

    def engordar(self, valor):
        if self.estado == 'Vivo':
            self.__peso += valor
        else:
            if self.sexo == 'M':
                print(f'Operação não realizada. {self.nome} está morto.')
            else:
                print(f'Operação não realizada. {self.nome} está morta.')
    
    def emagrecer(self, valor):
        if self.estado == 'Vivo':
            self.__peso -= valor
        else:
            if self.sexo == 'M':
                print(f'Operação não realizada. {self.nome} está morto.')
            else:
                print(f'Operação não realizada. {self.nome} está morta.')
    
    def crescer(self, valor):
        if self.estado == 'Vivo':
            if self.__idade <= 21:
                self.__altura += valor 
            else:
                print(f'{self.nome} não pode mais crescer pois está com 21 anos ou mais.')
        else:
            if self.sexo == 'M':
                print(f'Operação não realizada.{self.nome} está morto.')
            else:
                print(f'Operação não realizada.{self.nome} está morta.')

    def casar(self, conjuge)
        if self.estado == 'Vivo':
            if self.__idade >= 18:
                if self.estado_civil != 'Casado':
                    self.estado_civil = 'Casado'
                    self.conjugue = conjuge
                    conjuge.estado_civil = 'Casado'
                    conjuge.conjuge = self
                 else:
                    print(f'Casamento não realizado. {self.nome} é casado')
            else:
                print(f'Casamento não realizado.{self.nome} é de menor')
        else:
            if self.sexo == 'M':
                print(f'Casamento não pode ser realizado.{self.nome} está morto.')
            else:
                print(f'Casamento não pode ser realizado.{self.nome} está morto')
    
    def morrer(self, conjuge)
        if self.estado == 'Vivo':
            self.estado = 'Morto'
            print('{self.nome} morreu')
        else:
            if self.sexo == 'M':
                print(f'Operação não realizada. {self.nome} já está morto.')
            else:
                print(f'Operação não realizada. {self.nome} já está morta.')
def menu():
    print('1 - Listar pessoas')
    print('2 - Incluir nova pessoa')
    print('3 - Envelhecer')
    print('4 - Engordar')
    print('5 - Emagrecer')
    print('6 - Crescer')
    print('7 - Casar')
    print('8 - Morrer')
    print('9 - Alterar dados de uma pessoa')
def main():
    pessoas = [pessoa('Maria'), pessoa(),pessoa()]
