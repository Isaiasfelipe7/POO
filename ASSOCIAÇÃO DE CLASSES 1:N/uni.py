class Sisu:
    __universidades = []

    @staticmethod
    def inclui_universidade(universidade):
        if isinstance(universidade, Universidade):
            Sisu.__universidades.append(universidade)
            print("Universidade incluída com sucesso!")
        else:
            print("Erro!")

    @staticmethod
    def busca_universidade(nome):
        for universidade in Sisu.__universidades:
            if universidade.nome == nome:
                return universidade
        return None

class Aluno:
    def __init__(self, cpf, nome, dt_nasc):
        self.cpf = cpf
        self.nome = nome
        self.dt_nasc = dt_nasc
        self.matriculado = False
        self.pontuacao_enem = 0

    def solicita_entrada(self, curso):
        return self.pontuacao_enem >= curso.nota_corte

    def efetivar_matricula(self, curso):
        if not self.matriculado and curso.vagas_disponiveis() > 0:
            if self.solicita_entrada(curso):
                curso.cadastrar_aluno(self)
                self.matriculado = True
                print("Matrícula efetivada com sucesso!")
            else:
                print("Não é possível efetivar a matrícula.")
        else:
            print("Não é possível efetivar a matrícula.")

    def solicita_transferencia(self, univ_origem, curso_origem, univ_destino):
        if (
            self.matriculado
            and univ_origem.busca_curso(curso_origem.nome)
            and univ_destino.busca_curso(curso_origem.nome)
            and univ_destino.busca_curso(curso_origem.nome).vagas_disponiveis() > 0
        ):
            aluno = univ_origem.busca_curso(curso_origem.nome).remove_aluno(self.cpf)
            if aluno:
                univ_destino.busca_curso(curso_origem.nome).cadastrar_aluno(aluno)
                print(
                    f"Transferência efetuada do curso {curso_origem.nome} da universidade {univ_origem.nome} para o curso {curso_origem.nome} da universidade {univ_destino.nome}."
                )
            else:
                print("Não é possível efetuar a transferência.")
        else:
            print("Não é possível efetuar a transferência.")

    def calcular_pontuacao(self):
        return self.pontuacao_enem

    def __str__(self):
        return f"Nome: {self.nome}  CPF: {self.cpf}"


class Curso:
    def __init__(self, id, nome, duracao, vagas, nota_corte):
        self.__id = id
        self.nome = nome
        self.__duracao = duracao
        self.__vagas = vagas
        self.nota_corte = nota_corte
        self.__alunos = []

    def cadastrar_aluno(self, aluno):
        if isinstance(aluno, Aluno):
            self.__alunos.append(aluno)
            print("Aluno incluído com sucesso!")
        else:
            print("Erro!")

    def remove_aluno(self, cpf):
        for aluno in self.__alunos:
            if aluno.cpf == cpf:
                self.__alunos.remove(aluno)
                return aluno
        return None

    def vagas_disponiveis(self):
        return self.__vagas - len(self.__alunos)

    def __str__(self):
        cabecalho = f"Curso: {self.nome} - Relação de alunos\n"
        dados = ""
        for aluno in self.__alunos:
            dados += f"Nome: {aluno.nome}  CPF: {aluno.cpf}\n"
        return cabecalho + dados


class Universidade:
    def __init__(self, sigla, nome, tipo):
        self.__sigla = sigla
        self.nome = nome
        self.__tipo = tipo
        self.__cursos = []

    def cadastrar_curso(self, curso):
        if isinstance(curso, Curso):
            self.__cursos.append(curso)
            print("Curso cadastrado com sucesso!")
        else:
            print("Erro!")

    def busca_curso(self, nome):
        for curso in self.__cursos:
            if curso.nome == nome:
                return curso
        return None

    def __str__(self):
        cabecalho = f"Universidade: {self.nome} - Relação de cursos\n"
        dados = ""
        for curso in self.__cursos:
            dados += f"Curso: {curso.nome}  Vagas disponíveis: {curso.vagas_disponiveis()}\n"
        return cabecalho + dados


# EXECUÇÃO

# Criando instâncias de alunos
aluno1 = Aluno("111.111.111-11", "João", "01/01/2000")
aluno1.pontuacao_enem = 800

aluno2 = Aluno("222.222.222-22", "Maria", "02/02/2001")
aluno2.pontuacao_enem = 900

aluno3 = Aluno("333.333.333-33", "Pedro", "03/03/2002")
aluno3.pontuacao_enem = 750

# Criando instâncias de cursos
curso1 = Curso(1, "Engenharia Civil", 5, 10, 700)
curso2 = Curso(2, "Medicina", 6, 5, 800)

# Criando instâncias de universidades
universidade1 = Universidade("UFSC", "Universidade Federal de Santa Catarina", "Pública")
universidade2 = Universidade("USP", "Universidade de São Paulo", "Pública")

# Associando cursos às universidades
universidade1.cadastrar_curso(curso1)
universidade2.cadastrar_curso(curso2)

# Testando os métodos
aluno1.efetivar_matricula(curso1)  # Matrícula efetivada com sucesso!
aluno2.efetivar_matricula(curso1)  # Matrícula efetivada com sucesso!
aluno3.efetivar_matricula(curso1)  # Não é possível efetivar a matrícula.

print(curso1)  # Curso: Engenharia Civil - Relação de alunos
# Nome: João  CPF: 111.111.111-11
# Nome: Maria  CPF: 222.222.222-22

curso1.cadastrar_aluno(aluno3)  # Aluno incluído com sucesso!

aluno3.solicita_transferencia(
    universidade1, curso1, universidade2
)  # Transferência efetuada do curso Engenharia Civil da universidade UFSC para o curso Engenharia Civil da universidade USP.

print(universidade1)  # Universidade: Universidade Federal de Santa Catarina - Relação de cursos
# Curso: Engenharia Civil  Vagas disponíveis: 8

print(universidade2)  # Universidade: Universidade de São Paulo - Relação de cursos
# Curso: Engenharia Civil  Vagas disponíveis: 7

