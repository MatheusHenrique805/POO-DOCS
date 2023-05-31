class Bateria:
    def __init__(self, codigo, capacidade, percentual_carga):
        self.__codigo = codigo
        self.__capacidade = capacidade
        self.__percentual_carga = percentual_carga

    @property
    def codigo(self):
        return self.__codigo

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def percentual_carga(self):
        return self.__percentual_carga

    def carregar(self, valor):
        if valor <= 100:
            if valor <= 100 - self.percentual_carga:
                self.__percentual_carga += valor
            
        pass
    def descarregar(self, valor):
        if valor <= 100 and valor > 0:
            if valor <= self.percentual_carga:
                self.__percentual_carga -= valor

class Celular:
    def __init__(self, mei, bateria, wifi='desligado', estado=False):
        self.__mei = mei
        self.__bateria = bateria
        self.__wifi = wifi
        self.__estado = False
        
    @property
    def mei(self):
        return self.__mei

    @property
    def bateria(self):
        return self.__bateria

    @property
    def wifi(self):
        return self.__bateria

    @property
    def estado(self):
        return self.__estado
# Nota_de_corte = sum(lista_com_notas_de todos os concorrentes) / len(lista_com_notas_de todos os concorrentes)

    def ligarDesligar(self):
        # 'is' = '=='
        # 'not' = '!='
        if self.__bateria != None:
            if self.bateria.percentual_carga > 0:
                if self.__estado == False:
                    self.__estado = True
                    
                    return f'{self.bateria.percentual_carga}%'
                else:
                    print('l')
                    self.__estado = False
            else:
                print('Celular sem carga suficiente, por favor ponha para carregar.')
        else:
            print('Celular sem bateria.')

            
    def colocarBateria(self, bateria):
        if self.__bateria == None:
            self.__bateria = bateria
        else:
            print('O celular já possui bateria.')
            
    def ligarDesligarWifi(self):
        pass
    def assistirVideo(self, tempo):
        pass
    def carregar(self, valor):
        pass
    def descarregar(self, valor):
        pass


b1 = Bateria(111, 1200, 50)
c1 = Celular(123, b1)
print(c1.ligarDesligar())
print(c1.ligarDesligar())
