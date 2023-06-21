# João Augusto da Silva de Morais
# Matheus Henrique de Oliveira Rocha

class Aluno:
    def __init__(self, cpf, nome, dt_nasc, pont_enem, matricula_uni_publica=None, matricula_uni_priv=None):
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

    def solicitar_entrada(self,curso,universidade):
        if universidade.tipo == 'publica' and self.matricula_uni_publica != None:
            if self.pont_enem > curso.nota_corte:
                self.__matricula_uni_publica = True
                print(f'Solicitação Aceita!')
                return True
            else:
                print('Solicitação negada. Sua nota não é o suficiente para entrar no curso.')
        elif universidade.tipo == 'privada' and self.matricula_uni_priv != None:
            if self.pont_enem > curso.nota_corte:
                self.__matricula_uni_priv = True
                print(f'Solicitação Aceita!')
                return True
            else:
                print('Solicitação negada. Sua nota não é o suficiente para entrar no curso.')
        else:
            print(f'Você já foi aceito em uma universidade {universidade.tipo}.')

    def efetivar_matricula(self,curso,universidade):
        if self.solicitar_entrada(curso,universidade):
            curso.cadastrar_aluno(self)
            if curso.vagas > 0:
                curso.vagas -= 1
                print(f'Matricula efetivada!')
            else:
                print(f'O curso escolhido não possui mais vagas.')        
        
    def solicitar_transferencia(self,univ_ori,curso_ori,univ_dest):
        # Verifica se o aluno está realmente no curso e se esse curso existe na universidade de origem
        if self in curso_ori.alunos and curso_ori in univ_ori.cursos:
            # 
            if curso_ori in univ_dest.cursos:
                indice = univ_dest.cursos.index(curso_ori)
                curso = univ_dest.cursos[indice]
                if curso.vagas > 0:
                    curso_ori.alunos.remove(self)
                    # Adicionar aluno no curso da nova universidade.
                else:
                    print(f'O curso não possui mais vagas disponíveis.')
                pass
            else:
                print('Curso não encontrado.')
            pass
        else:
            print('Informações inválidas. Por favor, verifique se as informações que você inseriu estão corretas.')

    def __str__(self):
        pass
    
class Curso:
    def __init__(self, id_curso, nome, duracao, vagas, nota_corte, alunos):
        self.__id_curso = id_curso
        self.__nome = nome
        self.__duracao = duracao
        self.__vagas = vagas
        self.__nota_corte = nota_corte
        self.alunos = []
        
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
    def nota_corte(self):
        return self.__nota_corte
    @property
    def aluno(self):
        return self.__alunos

    def cadastrar_alunos(self,aluno):
        if aluno.matricula_uni_publica == True and aluno.matricula_uni_priv == False:
            self.alunos.append(aluno)
        elif aluno.matricula_uni_publica == False and aluno.matricula_uni_priv == True:
            self.alunos.append(aluno)
        else:
            print('cadastro não realizado por requisitos não atendidos!!') 
    def busca_aluno(self,aluno):
        pass

    def __str__(self):
        cab = f'curso:{self.__nome} - Relação de alunos'
        for i in self.__alunos:
            pass 
        
class Universidade:
    def __init__(self, sigla, nome, tipo):
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

    def cadastrar_curso(self, curso):
        if type(curso) == Curso:
            self.__cursos.append(curso)
            print(f'Curso cadastrado com sucesso!')
        else:
            print('Erro!')
    def buscar_curso(self,curso):
        for i in self.__alunos:
            if i.curso == curso:
                return i
        return None

class Sisu:
    __universidade = []
        
    def inclui_universidade(universidade):
        if type(universidade)==Universidade:
            Sisu.__universidades.append(universidade)


    def busca_universidade(nome):
        for i in Sisu.__universidades:
            if i.nome == nome:
                return i
        return None
     
