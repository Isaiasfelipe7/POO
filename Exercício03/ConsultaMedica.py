import datetime

class ConsultaMedica:

    def __init__(self, nome_medico, nome_paciente, data_hora):
        self.nome_medico = nome_medico
        self.nome_paciente = nome_paciente
        self.data_hora  = data_hora
        self.status = False
        self.valor = 300

    def pagar_consulta(self):
        if self.status == False:
            self.status = True
            return True
        
        else:
            return False
    
def main():

    consultas = []

    while True:

        print('''\nMENU PRINCIPAL

1. Nova consulta
2. Pagar consulta
3. Cancelar consulta
4. Agendar retorno
5. Relatório de consultas realizadas no mês por médico
6. Relatório de faturamento da clínica por mês
0. Sair
        ''')

        opcao = str(input('\nEscolha uma das opções: '))

        if opcao == '1':

            data = str(input("Digite a data da consulta (DD/MM/AAAA): "))
            hora = str(input('Digite a hora da consulta (HH:MM): '))
            data_hora = datetime.datetime.strptime(f'{data} {hora}', '%d/%m/%Y %H:%M')
            if data_hora < datetime.datetime.today():
                print("Não é possível agendar uma consulta para uma data anterior à de hoje.")

            else:
                nome_medico = input("Nome do médico para a consulta: ")
                nome_paciente = input("Nome do paciente: ")
                consulta = ConsultaMedica(nome_medico, nome_paciente, data_hora)
                consultas.append(consulta)

                print("\nConsulta marcada com sucesso!")

        elif opcao == '2':
             
            for i, consulta in enumerate(consultas):
                print(f'ID - {i} : MÉDICO - {consulta.nome_medico}, PACIENTE - {consulta.nome_paciente}, DATA E HORA - {consulta.data_hora}, VALOR - R$ {consulta.valor}.')

            Id = int(input('Digite o ID para pagar: '))

            if consultas[Id].pagar_consulta():
                print('\nConsulta paga com sucesso!')
            else:
                print('\nEsta consulta já foi paga!')

        elif opcao == '3':

            for i, consulta in enumerate(consultas):
                print(f'ID - {i} : MÉDICO - {consulta.nome_medico}, PACIENTE - {consulta.nome_paciente}, DATA E HORA - {consulta.data_hora}, VALOR - R$ {consulta.valor}.')

            Id = int(input('Digite o ID da consulta que deseja cancelar: '))

            consultas.pop(Id)

            print('\nConsulta cancelada com sucesso!')

        elif opcao == '4':
            
            data = str(input('Digite a data da consulta (DD/MM/AAAA): '))
            hora = str(input('Digite a hora da consulta (HH/MM): '))
            data_hora = datetime.datetime.strptime(f'{data} {hora}', '%d/%m/%Y %H:%M')
            nome_medico = str(input('Nome do médico que realizou a consulta: '))
            nome_paciente= str(input('Nome do paciente: '))

            for consulta in consultas:
                if consulta.data_hora == data_hora and consulta.nome_medico == nome_medico and consulta.nome_paciente == nome_paciente:

                    consulta.data_hora += datetime.timedelta(days=30)

                    print('\nRetorno agendado com sucesso!')
                    break

                else:
                    print('\nConsulta não encontrada!')

        elif opcao == '5':
            
            nome_medico = str(input('Digite o nome do médico: '))
            mes = int(input('Digite o mês desejado (1-12): '))
            
            tot_consul = 0

            for consulta in consultas:
                if consulta.nome_medico == nome_medico and consulta.data_hora.month == mes:
                    tot_consul += 1

            valor_medico = tot_consul * 200

            print(f'\nTotal de consultas realizadas pelo médico {nome_medico} no mês {mes} - {tot_consul}')
            print(f'Total a ser pago ao médico {nome_medico}: R$ {valor_medico:.2f}.')

        elif opcao == '6':

            mes = int(input('Digite o mês desejado (1-12): '))
            tot_consul = 0
            tot_fatura = 0

            for consulta in consultas:
                if consulta.data_hora.month == mes:
                    tot_consul += 1
                    tot_fatura += consulta.valor

            tot_pagamen_medicos = tot_consul * 200
            lucro_clinica =  tot_fatura - tot_pagamen_medicos

            print(f'\nTotal de consultas realizadas no mês {mes} - {tot_consul}')
            print(f'Faturamento da clínica no mês {mes} - R$ {tot_fatura:.2f}')
            print(f'Lucro da clínica no mês {mes} - R$ {lucro_clinica:.2f}')

        elif opcao == '0':

            print('\nPrograma Encerrado!!!')
            break

        else:

            print('\nOpção Inválida. Tente Novamente.')

if __name__ == '__main__':
    main()