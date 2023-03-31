class pessoa:
    def __init__(self, nome, peso, altura, sexo, estado='Vivo(a)', estado_civil='Solteiro(a)', conjugue=None):
        self.nome = nome
        self.peso = peso            
        self.altura = altura    
        self.sexo = sexo
        self.estado = estado
        self.estado_civil = estado_civil
        self.conjugue = conjugue
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