class Paciente:
    def __init__(self, id_pac, nom_pac, dt_nasc, contato):
        self.__id_paciente = id_pac
        self.nome_paciente = nom_pac
        self.__dt_nasc = dt_nasc
        self.__contato = contato

    pass

class Medico:
    def __init__(self, id_medico, crm, nome_medico, esp):
        self.__id_medico = id_medico
        self.__crm = crm
        self.nome_medico = nome_medico
        self.especialidade = esp

    pass

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

    def __str__(self):
        return f'Consulta marcada para a data: {self.__data} \nPaciente: {self.__paciente.nome_paciente} \nMédico: {self.__medico.nome_medico}'

