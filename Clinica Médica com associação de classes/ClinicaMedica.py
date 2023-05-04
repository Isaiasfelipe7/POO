import MenuClinica
from datetime import *

class Paciente:
    def __init__(self, id_pac, nom_pac, dt_nasc, contato):
        self.__id_paciente = id_pac
        self.nome_paciente = nom_pac
        self.__dt_nasc = dt_nasc
        self.__contato = contato

    @property
    def id_paciente(self):
        return self.__id_paciente
    
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

class ConsultaMedica:
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
        self.__data_retorno = True
        fds = [5,6]

        d = datetime.strptime(data,"%d/%m/%Y").date()
        if (d <= date.today() or d.weekday() in fds):
            raise ValueError("data de consulta menor que data atual ou caiu em final de semana")
            print("Valor:", data)
        else:
            self.__data = datetime.strftime(data, '%d/%m/%Y').date()

    @property
    def id(self):
        return self.__id
    
    @property
    def data(self):
        return self.__data
    
    @property
    def pago(self):
        return self.__pago
    
    @property
    def data_retorno(self):
        return self.__data_retorno
    
    def __str__(self):
        return f'Consulta marcada para a data: {self.__data} \nPaciente: {self.__paciente.nome_paciente} \nMédico: {self.__medico.nome_medico}'
    
    def pagar_consulta(self):
        self.__pago = True
    
    def agendar_consulta(self, data):
        if self.__pago == True:
            self.__data_retorno = data
            print(f'Retorno agendado para o dia: {dt_ret.strftime('%d/%m/%Y')}')


def main():

    consultas = []
    pacientes = []
    medicos = []

    while True:
        MenuClinica.menu()

        op = input('\nEscolha uma opção: ')

        isa = Paciente(16983573374, 'Isaias', '22/03/2004', 86994920631)
        bru = Medico(78201234167, 40029, 'Bruno', 'Dentista')
        conn = ConsultaMedica(1, bru, isa, '05/07/2030')

        print(f'\n{conn}')
        #print(f'{conn.} vai se consultar com o Dr.{conn.medico.nome_medico}')


if __name__ == '__main__':
    main()
