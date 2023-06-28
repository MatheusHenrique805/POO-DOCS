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
    # È chamado atráves do metódo efetivar_matricula
    def solicitar_entrada(self,curso,universidade):
        if universidade.tipo == 'publica' and self.matricula_uni_publica != True:
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
            if curso.vagas > 0:
                curso.cadastrar_aluno(self)
                curso.vagas -= 1
                print(f'Matricula efetivada!')
            else:
                print(f'O curso escolhido não possui mais vagas.')        

    '''- solicita_transferencia(self, univ_origem, curso_origem, univ_destino):
    O objetivo deste método é transferir o aluno para um mesmo curso em outra
    univerdade. Condição: Verificar se o aluno está matriculado no curso e respectiva
    universidade. A universidade destino tem que ter o curso e ter vaga. Não precisa checar a
    pontuação do enem'''
    
    def solicitar_transferencia(self,univ_ori,curso_ori,univ_dest):
        # Verifica se o aluno está realmente no curso e se esse curso existe na universidade de origem
        if self in curso_ori.alunos and curso_ori in univ_ori.cursos:
            # Verifica se o curso desejado existe na universidade
            if curso_ori in univ_dest.cursos:
                indice = univ_dest.cursos.index(curso_ori)
                curso = univ_dest.cursos[indice]
                # Verifica se existe vaga no curso
                if curso.vagas > 0:
                    curso_ori.alunos.remove(self)
                    curso.cadastrar_aluno(self)
                    print(f'Transferência realizada com sucesso!')
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
        return f'\nNome do Aluno: {self.nome} \nData de Nascimento: {self.dt_nasc} \nPontuação do Enem: {self.pont_enem}\n'
    
class Curso:
    def __init__(self, id_curso, nome, duracao, vagas, nota_corte):
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
        return f'{self.__duracao} anos'
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
        cab =f'\ncurso:{self.__nome} - Relação de alunos:\n'
        for i in self.alunos:
            cab += f'\n{i}\n'
        return cab.strip('\n')
        
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
        for i in self.__curso:
            if i.curso == curso:
                return i
        return None
    def __str__(self):
        return f'\nSigla: {self.sigla}\nNome: {self.nome}\nTipo: {self.tipo}\n'

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


#########################################################################
# Criando os objetos da classe Aluno
joao = Aluno(20222110344, 'João Augusto', '10/11/2004', 589)
flavio = Aluno(20222110760,'Flávio Leão','28/10/2001',625)
matheus = Aluno(20222110484, 'Matheus Henrique', '28/12/2000', 650)
print(joao, flavio, matheus)
########################################################################
# Criando os objetos da classe Universidade
uespi = Universidade('UESPI', 'Universidade Estadual do Piauí', 'Pública')
ufpi = Universidade('UFPI', 'Universidade Federal do Piauí', 'Pública')
unesa = Universidade('UNESA', 'Estácio', 'Privada')
print(uespi, ufpi, unesa)
######################################################################
# Criando os objetos da classe Curso
# -- UESPI --
medicina1 = Curso(5, 'Medicina', 8, 35, 850)
matematica1 = Curso(1, 'Matemática', 4, 40, 500)
portugues1 = Curso(2, 'Português', 4, 30, 620)
quimica = Curso(3, ' Química', 400, 40, 700 )
# --UFPI--
matematica2 = Curso(1, 'Matemática', 5, 30, 560)
portugues2 = Curso(2, 'Português', 4, 30, 650)
administracao1 = Curso(6, 'Administração', 550, 35, 700)
medicina2 = Curso(5, 'Medicina', 10, 25, 880)
# --UNESA--
matematica2 = Curso(1, 'Matemática', 5, 40, 560)
medicina2 = Curso(5, 'Medicina', 10, 40, 880)
ads = Curso(4, 'Análise e Desenvolvimento de Sistemas', 250, 50, 780)

quimica = Curso(3, ' Química', 400, 40, 700 )
ads = Curso(4, 'Análise e Desenvolvimento de Sistemas', 250, 50, 780)
medicina = Curso(5, 'Medicina', 600, 40, 850)
administracao = Curso(6, 'Administração', 550, 35, 700)
fisica = Curso(7, 'Física', 350, 30, 600)
print(matematica, portugues, quimica, ads, medicina, administracao)
######################################################################
#Cadastrando os cursos
uespi.cadastrar_curso(matematica)
uespi.cadastrar_curso(quimica)
uespi.cadastrar_curso(medicina)

ufpi.cadastrar_curso(matematica)
ufpi.cadastrar_curso(administracao)
ufpi.cadastrar_curso(portugues)

unesa.cadastrar_curso(matematica)
unesa.cadastrar_curso(ads)
unesa.cadastrar_curso(medicina)
#############################################
#
