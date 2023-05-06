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
    
    def __str__(self) -> str:
        return f'Nome do Paciente: {self.nome} \t Data.Nasc.:{self.__dt_nasc}'

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
    
    def __str__(self) -> str:
        return f'Nome do médico:{self.nome_medico} \n CRM:{self.__crm} \n Especialidade:{self.especialidade}'

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
            self.__data = datetime.strptime(data, "%d/%m/%Y").date()

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, valor):
        print('\nSem permissão!')
    
    @property
    def medico(self):
        return self.__medico
    
    @medico.setter
    def medico(self, valor):
        print('\nSem permissão!')
    
    @property
    def paciente(self):
        return self.__paciente
    
    @paciente.setter
    def paciente(self, valor):
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
        return f'\nConsulta {self.__id} marcada para a data: {self.__data.strftime("%d/%m/%Y")}, {ConsultaMedica.dia_semana[self.__data.weekday()]}, Paciente: {self.__paciente.nome_paciente}, Médico: {self.__medico.nome_medico}'
    
    def pagar_consulta(self):
        self.__pago = True
        print(f'\nConsulta paga!')
    
    def agendar_retorno(self, data):
        if self.__pago == True:
            self.__data_retorno = data
            print(f'\nRetorno agendado para o dia: {data.strftime("%d/%m/%Y")}')
        else:
            print('\nConsulta não foi paga!')
def menu():

    print('\n   Clinica Médica    ')
    print('\n1 - Cadastrar Paciente')
    print('2 - Cadastrar Médico')
    print('3 - Marcar Consulta')
    print('4 - Pagar Consulta')
    print('5 - Cancelar Consulta')
    print('6 - Marcar Retorno')
    print('7 - Sair')

def main():

    consultas = []
    pacientes = [Paciente(12345678901, 'mateus', '22/03/2004', 86994289101), Paciente(20987634265, 'maria', '14/06/2005', 86995672129), Paciente(98732465161, 'adrian', '11/12/1997', 86994523211)]
    medicos = [Medico(98765432182, 1234, 'pedro', 'ortopedista'), Medico(16725162187, 5678, 'orlando', 'dermatologista'), Medico(98076212309, 4567, 'marcio', 'neurocirurgia')]

    while True:
        menu()

        op = input('\nEscolha uma opção: ')
        
        if op == '1':
            cpf = int(input('CPF do paciente: '))
            nome = str(input('Nome do paciente: '))
            data = input('Data de nascimento (DD/MM/AAAA): ')
            contato = input('Contato: ')

            pasc = Paciente(cpf, nome, data, contato)

            pacientes.append(pasc)

            print(f'\nPaciente {nome} cadastrado!')
        elif op == '2':
            id = int(input('ID médico: '))
            crm = int(input('CRM: '))
            nome = str(input('Nome do médico: '))
            esp = str(input('Especialidade: '))

            med = Medico(id, crm, nome, esp)

            medicos.append(med)

            print(f'\nMédico {nome} cadatrado!')
        elif op == '3':
            id = int(input('Id consulta: '))
            nome_med = str(input('Nome do médico: '))
            nome_paciente = str(input('Nome do paciente: '))
            data_consul = input('Data da consulta (DD/MM/AAA): ')

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
            cont = 0
            for i,j in enumerate(consultas):
                if not j.pago:
                    cont+=1
                print(f'Indíce {i}: {j}')
            if cont > 0:
                op1 = int(input('Escolha um indice correspondente a consulta: '))
                ConsultaMedica.pagar_consulta(consultas[op1])
            else:
                print('\nNão existem consultas a serem pagas')
        elif op == '5':
            if not consultas:
                print('\nNão há consultas marcadas para cancelar!')
            else:
                for i, con in enumerate(consultas):
                    print(f'Indice {i}: {con}')
                    cancel = int(input('Indice da consulta para cancelar: '))
                    del consultas[cancel]
                    print(f'\nA consulta com o indice {i} cancelada!')
        elif op == '6':
            pac = str(input('Nome do paciente: '))
            c = 0

            for i, b in enumerate(consultas):
                if b._ConsultaMedica__paciente.nome_paciente == pac:
                    c += 1
                    print(f'Indíce {i}: {b}')
            if c > 0:
                id = int(input('Indice da consulta: '))
                dat_ret_max = consultas[id].data+timedelta(days=30)
                print(f'Data máxima de retorno: {dat_ret_max.strftime("%d/%m/%Y")}')
                dat_retor = input('Data de retorno: ')
                dat_retor = datetime.strptime(dat_retor, "%d/%m/%Y").date()
                if dat_retor > dat_ret_max:
                    print('\nData de retorno inválida!')
                else:
                    consultas[id].agendar_retorno(dat_retor)
            else:
                print('\nNão há consultas marcadas para este paciente.')

        elif op == '7':
            print('\nVocê saiu. . .')
            break
        else:
            print('\nOpção Inválida. Tente Novamente!')
        
if __name__ == '__main__':
    main()
