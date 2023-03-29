import datetime

class CarteiraDeHabilitação:
    def __init__(self, nome='Sem nome', cpf='Não Informado', categoria='Sem Categoria', pontos='Sem Pontuação', validade='Sem validade'):
        self.nome = nome
        self.cpf = cpf
        self.categoria = categoria
        self.pontos = pontos
        self.validade = validade

    def adicionar_nome(self, nome):
        self.nome = nome

    def adicionar_cpf(self, cpf):
        self.cpf = cpf

    def adicionar_categoria(self, categoria):
        self.categoria = categoria

    def adicionar_pontuação(self, pontos):
        self.pontos = pontos

    def pegar_validade(self):
        return self.validade.strftime("%d/%m/%Y")
    
    def renovar_validade(self, anos):
        self.validade += datetime.timedelta(days=anos*365)


def main():

    carteira = CarteiraDeHabilitação(nome='Marcelo Vinicius', cpf='190.876.523-40', categoria='A', pontos='20', validade=datetime.date.today())

    carteira.renovar_validade(5)

    print(f'Nome: {carteira.nome}')
    print(f'CPF: {carteira.cpf}')
    print(f'Categoria: {carteira.categoria}')
    print(f'Pontos: {carteira.pontos}')
    print(f'Validade: {carteira.pegar_validade()}')


if __name__ == '__main__':
    main()
