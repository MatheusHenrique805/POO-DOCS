class Cachorro():
    raça = None
    nome = None
    peso = None
    idade = None
    def __init__(self, peso, idade):
        self.peso = peso
        self.idade = idade
    def mudar_nome(self, nome):
        self.nome = nome
        
        
    def engordar(self, peso):
        self.peso += peso

        
    def envelhecer(self):
        self.idade += 1


meu_dog = Cachorro(1,0)
meu_dog.nome = 'faisca'
meu_dog.raça = 'vira-lata'
meu_dog.mudar_nome('coock')
for _ in range(15):
    meu_dog.engordar(2)
    meu_dog.envelhecer()
    print(f'O nome do meu cachorro é {meu_dog.nome}')
    print(f'A raça dele é {meu_dog.raça}')
    print(f'Ele pesa atualmente {meu_dog.peso}kg')
    print(f'Sua idade atual é de {meu_dog.idade} anos')
    print(f'--------------------------------------------')