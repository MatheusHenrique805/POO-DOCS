# João Augusto da Silva de Morais
# Matheus Henrique de Oliveira Rocha


class Aluno:
    def __init__(self, cpf, nome, dt_nasc, pont_enem, matricula_uni_publica=None, matricula_uni_priv=None,):
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
    def solicitar_entrada(self, curso, universidade):
        if universidade.tipo == "Pública" and self.matricula_uni_publica != True:
            if self.pont_enem >= curso.nota_corte:
                self.__matricula_uni_publica = True
                print(f"Solicitação Aceita!")
                return True
            else:
                print("Solicitação negada. Sua nota não é o suficiente para entrar no curso.")
        elif universidade.tipo == "Privada" and self.matricula_uni_priv != True:
            if self.pont_enem > curso.nota_corte:
                self.__matricula_uni_priv = True
                print(f"Solicitação Aceita!")
                return True
            else:
                print("Solicitação negada. Sua nota não é o suficiente para entrar no curso.")
        else:
            print(f"Você já foi aceito em uma universidade {universidade.tipo}.")

    def efetivar_matricula(self, curso, universidade):
        if self.solicitar_entrada(curso, universidade):
            if curso.vagas > 0:
                curso.cadastrar_aluno(self)
                curso.vagas -= 1
                print(f"Matricula efetivada!\n")
            else:
                print(f"O curso escolhido não possui mais vagas.")

    """- solicita_transferencia(self, univ_origem, curso_origem, univ_destino):
    O objetivo deste método é transferir o aluno para um mesmo curso em outra
    univerdade. Condição: Verificar se o aluno está matriculado no curso e respectiva
    universidade. A universidade destino tem que ter o curso e ter vaga. Não precisa checar a
    pontuação do enem"""

    def solicitar_transferencia(self, univ_ori, curso_ori, univ_dest):
        for i in univ_dest.cursos:
            if curso_ori.nome == i.nome:
                curso_dest = i
                # Verifica se o aluno está realmente no curso e se esse curso existe na universidade de origem
                if self in curso_ori.alunos and curso_ori in univ_ori.cursos:
                    # Verifica se o curso desejado existe na universidade
                    if curso_dest in univ_dest.cursos:
                        if i.vagas > 0:
                            curso_ori.alunos.remove(self)
                            i.cadastrar_aluno(self)
                            print(f"Transferência realizada com sucesso!")
                            break
                            # Adicionar aluno no curso da nova universidade.
                        else:
                            print(f"O curso não possui mais vagas disponíveis.")
                        pass
                    else:
                        print("Curso não encontrado.")
                    pass
                else:
                    print("Informações inválidas. Por favor, verifique se as informações que você inseriu estão corretas.")
            else:
                pass

    def __str__(self):
        return f"\nNome do Aluno: {self.nome} \nData de Nascimento: {self.dt_nasc} \nPontuação do Enem: {self.pont_enem}\n"


class Curso:
    def __init__(self, id_curso, nome, duracao, vagas, nota_corte):
        self.__id_curso = id_curso
        self.__nome = nome
        self.__duracao = duracao
        self.vagas = vagas
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
        return f"{self.__duracao} anos"

    @property
    def nota_corte(self):
        return self.__nota_corte

    @property
    def aluno(self):
        return self.__alunos

    # Esse metódo é chamado na classe Aluno nos metódos efetivar_matricula e solicitar_transferencia.
    def cadastrar_aluno(self, aluno):
        
        if aluno.matricula_uni_publica == True or aluno.matricula_uni_priv == True:
            self.alunos.append(aluno)
        else:
            print("cadastro não realizado por requisitos não atendidos!!")

    def buscar_aluno(self, aluno):
        for i in self.alunos:
            if i == aluno:
                print(i)
            else:
                pass
        print(f'Aluno não encontrado.')
            
    def __str__(self):
        cab = f"\ncurso:{self.__nome} - Relação de alunos:\n"
        for i in self.alunos:
            cab += f"\n{i}\n"
        return cab.strip("\n")


class Universidade:
    def __init__(self, sigla, nome, tipo):
        self.__sigla = sigla
        self.__nome = nome
        self.__tipo = tipo
        self.__cursos = []

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
            print(f"Curso cadastrado com sucesso!")
        else:
            print("Erro!")

    def buscar_curso(self, curso):
        for i in self.__curso:
            if i.curso == curso:
                return i
        print(f'Curso não encontrado.')

    def __str__(self):
        return f"\nSigla: {self.sigla}\nNome: {self.nome}\nTipo: {self.tipo}\n"


class Sisu:
    __universidade = []

    def inclui_universidade(universidade):
        if type(universidade) == Universidade:
            Sisu.__universidades.append(universidade)

    def busca_universidade(nome):
        for i in Sisu.__universidades:
            if i.nome == nome:
                return i
        return None


#########################################################################
# Criando os objetos da classe Aluno
joao = Aluno(20222110344, "João Augusto", "10/11/2004", 640)
flavio = Aluno(20222110760, "Flávio Leão", "28/10/2001", 625)
matheus = Aluno(20222110484, "Matheus Henrique", "28/12/2000", 650)
eduarda = Aluno(20222110808, 'Maria Eduarda', '12/05/2002', 710)
adriano = Aluno(20222110450, 'Adriano Junior', '11/12/2002', 850)
print(joao, flavio, matheus)
#########################################################################
# Criando os objetos da classe Universidade
uespi = Universidade("UESPI", "Universidade Estadual do Piauí", "Pública")
ufpi = Universidade("UFPI", "Universidade Federal do Piauí", "Pública")
unesa = Universidade("UNESA", "Estácio", "Privada")
print(uespi, ufpi, unesa)
#########################################################################
# Criando os objetos da classe Curso
# -- UESPI --
# O curso de matemática da UESPI terá só uma vaga, para finalidade de teste envolvendo o limite de vagas
medicina_uespi = Curso(5, "Medicina", 8, 35, 850)
matematica_uespi = Curso(1, "Matemática", 4, 1, 500)
administracao_uespi = Curso(6, "Administração", 5, 35, 650)
portugues_uespi = Curso(2, "Português", 4, 30, 620)
quimica_uespi = Curso(3, " Química", 4, 40, 700)
# --UFPI--
matematica_ufpi = Curso(1, "Matemática", 5, 30, 560)
portugues_ufpi = Curso(2, "Português", 4, 30, 650)
administracao_ufpi = Curso(3, "Administração", 5, 35, 700)
medicina_ufpi = Curso(4, "Medicina", 10, 25, 880)
quimica_ufpi = Curso(5, " Química", 4, 40, 700)
fisica_ufpi = Curso(6, "Física", 5, 30, 650)
# --UNESA--
medicina_unesa = Curso(2, "Medicina", 10, 40, 700)
ads_unesa = Curso(3, "Análise e Desenvolvimento de Sistemas", 3, 50, 750)
quimica_unesa = Curso(4, " Química", 4, 40, 600)
#########################################################################
# Cadastrando os cursos
uespi.cadastrar_curso(matematica_uespi)
uespi.cadastrar_curso(quimica_uespi)
uespi.cadastrar_curso(portugues_uespi)
uespi.cadastrar_curso(medicina_uespi)
uespi.cadastrar_curso(administracao_uespi)

ufpi.cadastrar_curso(matematica_ufpi)
ufpi.cadastrar_curso(administracao_ufpi)
ufpi.cadastrar_curso(portugues_ufpi)
ufpi.cadastrar_curso(medicina_ufpi)
ufpi.cadastrar_curso(quimica_ufpi)
ufpi.cadastrar_curso(fisica_ufpi)

unesa.cadastrar_curso(ads_unesa)
unesa.cadastrar_curso(medicina_unesa)
unesa.cadastrar_curso(quimica_unesa)
print()
#########################################################################
# Efetivando Matricula
joao.efetivar_matricula(matematica_uespi, uespi)
eduarda.efetivar_matricula(administracao_ufpi, ufpi)
matheus.efetivar_matricula(quimica_unesa, unesa)
adriano.efetivar_matricula(medicina_uespi, uespi)
# Efetivando matricula com notas menores que as exigidas
flavio.efetivar_matricula(medicina_uespi, uespi)
flavio.efetivar_matricula(portugues_ufpi, ufpi)
print()
# Efetivando matricula em outra universidade pública já estando em uma
joao.efetivar_matricula(portugues_uespi, uespi)
eduarda.efetivar_matricula(quimica_ufpi, ufpi)
print()
# Efetivando matricula em um curso que já atingiu o limite de vagas
flavio.efetivar_matricula(matematica_uespi, uespi)
print()
#########################################################################
# Solicitando transferência
joao.solicitar_transferencia(uespi, matematica_uespi, ufpi)
eduarda.solicitar_transferencia(ufpi, administracao_ufpi, uespi)
#########################################################################
# Bucando aluno em um curso
matematica_ufpi.buscar_aluno(joao)
medicina_uespi.buscar_aluno(adriano)
# Buscando aluno que não pertence ao curso
matematica_ufpi.buscar_aluno(eduarda)

#########################################################################
