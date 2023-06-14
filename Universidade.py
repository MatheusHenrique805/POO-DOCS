class Aluno:
    def __init__(self, cpf, nome, dt_nasc, matricula_uni_publica, matricula_uni_priv, pont_enem):
        self.__cpf = cpf
        self.__nome = nome
        self.__dt_nasc = dt_nasc
        self.__matricula_uni_publica = matricula_uni_publica
        self.__matricula_uni_priv = matricula_uni_priv
        self.__pont_enem = pont_enem
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def dt_nasc(self):
        return self.__dt_nasc
    
    @property
    def matricula_uni_publica(self):
        return self.__matricula_uni_publica
    
    @property
    def matricula_uni_priv(self):
        return self.__matricula_uni_priv
    
    @property
    def pont_enem(self):
        return self.__pont_enem
    

class Curso:
    def __init__(self, id_curso, nome, duracao, vagas, nota_corte, alunos):
        self.__id_curso = id_curso
        self.__nome = nome
        self.__duracao = duracao
        self.__vagas = vagas
        self.__alunos = []
    @property
    def id_curso(self):
        return self.__id_curso
    @property
    def nome(self):
        return self.__nome
    @property
    def duracao(self):
        return self.__duracao
    @property
    def vagas(self):
        return self.__vagas
    @property
    def aluno(self):
        return self.__alunos
    
class Universidade:
    def __init__(self, sigla, nome, tipo, cursos):
        self.__sigla = sigla
        self.__nome = nome
        self.__tipo = tipo
        self.__cursos= []
    @property
    def sigla(self):
        return self.__sigla
    @property
    def nome(self):
        return self.__nome
    @property
    def tipo(self):
        return self.__tipo
    @property
    def cursos(self):
        return self.__cursos
        
class Sisu:
    __universidade = []
        
    @property
    def universidade(self):
        return self.__universidade
     
