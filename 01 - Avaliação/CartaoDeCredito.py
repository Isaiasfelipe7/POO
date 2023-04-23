import datetime

class CartaoDeCredito:
    def __init__(self, numero, titular, validade, cod_seguranca, senha, limite_de_compras=1000, fatura_a_pagar=0, status='bloqueado'):
        self.__numero = numero
        self.titular = titular
        self.__validade = datetime.datetime.strptime(validade, '%d/%m/%Y').date()
        self.__cod_seguranca = cod_seguranca
        self.senha = senha
        self.__limite_de_compras = limite_de_compras
        self.__fatura_a_pagar = fatura_a_pagar
        self.__status = status
        self.__valor_minimo_a_pagar = 0.3
    
    @property
    def numero(self):
        return self.__numero

    def titular(self):
        return self.titular

    @property
    def validade(self):
        return self.__validade

    @property
    def cod_seguranca(self):
        return self.__cod_seguranca

    @property
    def limite_de_compras(self):
        return self.__limite_de_compras

    @property
    def fatura_a_pagar(self):
        return self.__fatura_a_pagar

    @property
    def status(self):
        return self.__status

    @property
    def valor_minimo_a_pagar(self):
        return self.__valor_minimo_a_pagar
    
    def __str__(self):
        return f'\nNome do titular: {self.titular} \nValor da fatura: R${self.__fatura_a_pagar} \nValor minimo a pagar: R${self.__valor_minimo_a_pagar:.2f}'
    
    def desbloquear(self, add):
        add = int(input('Digite uma senha para o cartão: '))
        self.__status = 'liberado'
        self.senha = add
        print('\nSeu cartão está liberado!')

    def bloquear(self):
        self.__status = 'bloqueado'
        print('\nSeu cartão agora está bloqueado!')

    def mudar_senha(self, nome, cod):
        if cod != self.__cod_seguranca and nome != self.titular:
            print('\nO código de segurança ou nome do titular está incorreto!')
        elif cod == self.__cod_seguranca and nome == self.titular:
            nova_senha = int(input('Insira uma nova senha: '))
            self.senha = nova_senha
            print('\nSenha do cartão alterada!')

    def comprar(self, valor, senha, validade):
        hoje = datetime.date.today()
        if valor <= self.__limite_de_compras and self.__status == 'liberado' and self.senha == senha and validade > hoje and valor >= self.__valor_minimo_a_pagar:
            self.__limite_de_compras -= valor
            self.__fatura_a_pagar += valor
            self.__valor_minimo_a_pagar = 0.3 * self.__fatura_a_pagar

            print('\nCompra realizada com sucesso!')

        elif valor > self.__limite_de_compras:
            print('\nCompra negada. você não tem limite suficiente!')
        elif self.senha != senha:
            print('\nA senha do cartão está incorreta!')
        elif self.__status != 'liberado':
            print('\nO seu cartão está bloqueado!')
        elif validade < hoje:
            print('\nO cartão está vencido!')
        
    def pagar_fatura(self, valor):
        if valor <= self.__fatura_a_pagar:
            self.__fatura_a_pagar -= valor
            self.__limite_de_compras += valor
            self.__valor_minimo_a_pagar -= 0.3 * valor
            print(f'\nVocê pagou um valor de R${valor} da sua fatura!')
        elif valor > self.__valor_minimo_a_pagar:
            print('\nVocê informou um valor acima do valor da sua fatura atual!')
        elif valor < self.__valor_minimo_a_pagar:
            print(f'\nO valor minimo de para pagar a fatura é R${self.__valor_minimo_a_pagar}')

    def informacoes_pessoais(self):
        if self.__status == 'liberado':
            print(f'\nNome do Titular: {self.titular} \nVálidade: {self.__validade} \nLimite de crédito disponível: R${self.__limite_de_compras} \nCódigo de segurança do cartão: {self.__cod_seguranca} \nSenha: {self.senha} \nStatus: {self.__status}')
        else:
            print('\nVocê deve desbloquear seu cartão primeiro!')
         
def main():
 
    cartoes = CartaoDeCredito(12345678, 'Isaias', '22/03/2030', 789, None)

    while True:
        print('\n=== = Menu = ===')
        print('\n1 - Desbloquear cartão')
        print('2 - Bloquear cartão')
        print('3 - Mudar senha')
        print('4 - Realizar compra')
        print('5 - Pagar fatura')
        print('6 - Informações do cartão')
        print('7 - Mostrar informações pessoais')
        print('0 - Sair')

        op = input('\nEscolha uma opção: ')

        if op == '1':
            cartoes.desbloquear(None)

        elif op == '2':
            cartoes.bloquear()

        elif op == '3':
            titular = str(input('Nome do titular: '))
            cod = int(input('Código de seguranção: '))
            cartoes.mudar_senha(titular, cod)

        elif op == '4':
            valor = float(input('Digite o valor da compra: '))
            senha = int(input('Digite a senha do cartão: '))
            validade = cartoes.validade
            cartoes.comprar(valor, senha, validade)

        elif op == '5':
            valor = float(input('Digite o valor que deseja pagar: '))
            cartoes.pagar_fatura(valor)

        elif op == '6':
            print(cartoes)

        elif op == '7':
            cartoes.informacoes_pessoais()
    
        elif op == '0':
            print('Você saiu do programa...')
            break

        else:
            print('Opção Inválida. Tente Novamente!')

if __name__ == '__main__':
    main()
