import MenuClinica
from datetime import *

class Paciente:
    def __init__(self, id_pac, nome_pac, dt_nasc, contato):
        self.__id_paciente = id_pac
        self.nome_paciente = nome_pac
        self.__dt_nasc = dt_nasc
        self.__contato = contato

    @property
    def id_paciente(self):
        return self.__id_paciente
    
    def nome_paciente(self):
        return self.nome_paciente
    
    @property
    def dt_nasc(self):
        return self.__dt_nasc
    
    @property
    def contato(self):
        return self.__contato

class Medico:
    def __init__(self, id_medico, crm, nome_medico, esp):
        self.__id_medico = id_medico
        self.__crm = crm
        self.nome_medico = nome_medico
        self.especialidade = esp

    @property
    def id_medico(self):
        return self.__id_medico
    
    @property
    def crm(self):
        return self.__crm
    
    def nome_medico(self):
        return self.nome_medico

    def especialidade(self):
        return self.especialidade

class ConsultaMedica:
    dia_semana = {0:'segunda-feira',1:'terça-feira',2:'quarta-feira',3:'quinta-feira',4:'sexta-feira'}
    def __init__(self, id, medico, paciente, data, pago=False):
        self.__id = id
        if type(medico) == Medico:
            self.__medico = medico
        else:
            raise 'Error!'
        if type(paciente) == Paciente:
            self.__paciente = paciente
        else:
            raise 'Error!'
        self.__data = data
        self.__pago = pago
        self.__data_retorno = None
        fds = [5,6]

        d = datetime.strptime(data,"%d/%m/%Y").date()
        if (d <= date.today() or d.weekday() in fds):
            raise ValueError("data de consulta menor que data atual ou caiu em final de semana")
            print("Valor:", data)
        else:
            self.__data = datetime.strptime(data, '%d/%m/%Y').date()

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, valor):
        print('\nSem permissão!')
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, valor):
        print('\nSem permissão!')
    
    @property
    def pago(self):
        return self.__pago
    
    @pago.setter
    def pago(self, valor):
        print('\nSem permissão!')
    
    @property
    def data_retorno(self):
        return self.__data_retorno
    
    @data_retorno.setter
    def data_retorno(self, valor):
        print('\nSem permissão!')

    def __str__(self) -> str:
        return f'\nConsulta marcada para a data: {self.__data.strftime("%d/%m/%Y")}, {ConsultaMedica.dia_semana[self.__data.weekday()]}. \nPaciente: {self.__paciente.nome_paciente} \nMédico: {self.__medico.nome_medico}'
    
    def pagar_consulta(self):
        self.__pago = True
    
    def agendar_consulta(self, data):
        if self.__pago == True:
            self.__data_retorno = data
            #print(f'Retorno agendado para o dia: {dt_ret.strftime('%d/%m/%Y')}')
        else:
            print("Consulta não foi paga!")


def main():

    consultas = []
    pacientes = [Paciente(1, 'lorena', '22/03/2004', 86994920631)]
    medicos = [Medico(1, 1234, 'isaias', 'ortopedista')]

    while True:
        MenuClinica.menu()

        op = input('\nEscolha uma opção: ')
        
        if op == '1':
            id = int(input('ID paciente: '))
            nome = str(input('Nome do paciente: '))
            data = input('Data de nascimento (DD/MM/AAAA): ')
            contato = input('Contato: ')

            pasc = Paciente(id, nome, data, contato)

            pacientes.append(pasc)

            print('\nPaciente cadastrado!')
        elif op == '2':
            id = int(input('ID médico: '))
            crm = int(input('CRM: '))
            nome = str(input('Nome do médico: '))
            esp = str(input('Especialidade: '))

            med = Medico(id, crm, nome, esp)

            medicos.append(med)

            print('\nMédico cadatrado!')
        elif op == '3':
            id = int(input('ID consulta: '))
            nome_med = str(input('Nome do médico: '))
            nome_paciente = str(input('Nome do paciente: '))
            data_consul = input('Data da consulta: ')

            medico = None
            for med in medicos:
                if med.nome_medico == nome_med:
                    medico = med
            if not medico:
                print('\nMédico não encontrado!')
            
            paciente = None
            for pac in pacientes:
                if pac.nome_paciente == nome_paciente:
                    paciente = pac
            if not paciente:
                print('\nPaciente não encontrado!')
            
            consul = ConsultaMedica(id, medico, paciente, data_consul)

            consultas.append(consul)

            print(f'{consul}')
        elif op == '4':
            cont=0
            for i,j in enumerate(consultas):
                #seq+=1
                if not j.pago:
                    cont+=1
                print(i,j)
            if cont >0:
                op1 = int(input("escolha um indice correspondente a consulta:"))
                consultas[op1].pago = True
            else:
                print("Não existem consultas a serem pagas") 
        
if __name__ == '__main__':
    main()
