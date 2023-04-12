class pessoa:
    def __init__(self, nome, idade, peso, altura, sexo, estado='Vivo(a)', estado_civil='Solteiro(a)', conjuge=None):
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

    def casar(self, conjuge):
        if self.estado == 'Vivo' and conjuge.estado == 'Vivo':
            if self.__idade >= 18 and conjuge.__idade >= 18:
                if self.estado_civil != 'Casado' and conjuge.estado_civil != 'Casado':
                    self.estado_civil = 'Casado'
                    self.conjugue = conjuge
                    conjuge.estado_civil = 'Casado'
                    conjuge.conjuge = self
                else:
                    print(f'Casamento não realizado. {self.nome} ou {conjuge.nome} é casado')
            else:
                print(f'Casamento não realizado.{self.nome} ou {conjuge.nome} é de menor')
        else:
            if self.sexo == 'M':
                print(f'Casamento não pode ser realizado.{self.nome} ou {conjuge.nome} está morto.')
            else:
                print(f'Casamento não pode ser realizado.{self.nome} ou {self.nome} ou {conjuge.nome} está morto')
    
    def morrer(self, conjuge):
        if self.estado == 'Vivo':
            self.estado = 'Morto'
            if self.estado_civil == 'Casado':
                conjuge.estado_civil = 'Viúvo'
                conjuge.conjugue = None
                print(f'{self.nome} morreu')
            else:
               print(f'{self.nome} morreu')
        else:
            if self.sexo == 'M':
                print(f'Operação não realizada. {self.nome} já está morto.')
            else:
                print(f'Operação não realizada. {self.nome} já está morta.')

pessoas = [pessoa('Maria', 18, 63, 179,'F'), 
           pessoa('Bruna', 23, 44, 165, 'F'), 
           pessoa('Joâo', 18, 64, 178, 'M'),
           pessoa('Lucas', 17, 54, 168, 'M'),
           pessoa('Matheus', 22, 69, 171, 'M'),
           pessoa('Lara', 21, 61, 178, 'F'),
           pessoa('Andressa', 19, 52, 170, 'F'),
           pessoa('Pedro', 21, 64, 178, 'M')]


maria = pessoas[0]
matheus = pessoas[4]
joao = pessoas[2]
bruna = pessoas[1]
lucas = pessoas[3]
lara = pessoas[5]
andressa = pessoas[6]
pedro = pessoas[7]


