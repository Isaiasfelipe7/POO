class Sisu(object):
  __universidades = []
  
  def inclui_universidade(universidade):
      if type(universidade)==Universidade:
         Sisu.__universidades.append(universidade)
      
  
  def busca_universidade(nome):
    for i in Sisu.__universidades:
      if i.nome == nome:
          return i
    return None
  

class Universidade:
  def __init__(self,sigla,nome,tipo):
    self.__sigla = sigla
    self.__nome = nome
    self.__tipo = tipo
    self.__cursos = []
  
  def inclui_curso(self,curso):
    if type(curso)==Curso:
       self.__cursos.append(curso)
       print(f'curso cadastrado com sucesso!')
    else:
       print("Erro!")
      
  
  def buscar_curso(self,curso):
    for i in self.__alunos:
      if i.curso == curso:
        return i
    return None
         

  def __str__(self):
    cab = f'{self.__sigla}- Relação de cursos\n'
    dados=''
    for i in self.__cursos:
      dados += f'Nome:{i.nome}  Nota de corte:{i.nota_corte}\n'
    return cab+dados

class Curso:
  
  def __init__(self,id,nome,duração,vagas,nota_corte):
     self.__id
     self.__nome
     self.__vagas
     self.__nota_corte
     self.alunos = []
  
  def inclui_alunos(self,aluno):
    pass
  
  def busca_aluno(self,aluno):
    pass
  
  def __str__(self):
    cab = f'curso:{self.__nome} - Relação de alunos'
    for i in self.__alunos:
      pass



maria = Aluno("11111111111111","Maria","01/02/1990")
josé = Aluno("22222222222","José","15/12/1998")
uespi = Universidade('UESPI','Universidade Estadual do Piauí','publico')
ufpi = Universidade('UFPI','Universidade Federal do Piauí','publico')
novafapi = Universidade('NovaFapi','NovaFapi', 'particular')

Sisu.inclui_universidade(uespi)
Sisu.inclui_universidade(ufpi)
Sisu.inclui_universidade(novafapi)

uespi.inclui_aluno(maria)
ufpi.inclui_aluno(maria)
ufpi.inclui_aluno(josé)
novafapi.inclui_aluno(Aluno('33333333333','Ana','14/06/2000'))
print(uespi)
print(ufpi)
print(novafapi)
print(maria.matricula_publica)
print(josé.matricula_publica)