# ISAIAS FELIPE
# SÁVYO GABRIEL

class Seguro:
    def __init__(self, num_apolice, proprietario, valor_seguro, valor_premio):
        self._num_apolice = num_apolice
        self._proprietario = proprietario
        self._valor_seguro = valor_seguro
        self._valor_premio = valor_premio

    def calcularValor(self):
        pass

    def calcularPremio(self):
        pass

    def __str__(self):
        return f"Número da Apólice: {self._num_apolice}\nProprietário: {self._proprietario.obterNome()}\nValor do Seguro: {self._valor_seguro}\nPrêmio: {self._valor_premio}"


class Cliente:
    def __init__(self, cpf, nome, idade):
        self._cpf = cpf
        self._nome = nome
        self._idade = idade

    def obterIdade(self):
        return self._idade

    def obterNome(self):
        return self._nome


class SeguroVida(Seguro):
    def __init__(self, num_apolice, proprietario, nome_beneficiario, idade):
        super().__init__(num_apolice, proprietario, 0, 0)
        self._nome_beneficiario = nome_beneficiario
        self._idade = idade

    def calcularValor(self):
        if self._idade <= 30:
            return 800.00
        elif 31 <= self._idade <= 50:
            return 1300.00
        else:
            return 1600.00

    def calcularPremio(self):
        if self._idade <= 30:
            return 50000
        elif 31 <= self._idade <= 50:
            return 30000
        else:
            return 20000

    def __str__(self):
        return f"Seguro de Vida\n{super().__str__()}\nNome do Beneficiário: {self._nome_beneficiario}"


class SeguroAutomovel(Seguro):
    def __init__(self, num_apolice, proprietario, numero_licenca, nome_modelo, ano, valor_automovel):
        super().__init__(num_apolice, proprietario, 0, 0)
        self._numero_licenca = numero_licenca
        self._nome_modelo = nome_modelo
        self._ano = ano
        self._valor_automovel = valor_automovel

    def calcularValor(self):
        return self._valor_automovel * 0.03

    def calcularPremio(self):
        return self._valor_automovel * 0.8

    def calcularFranquia(self):
        return self.calcularValor() * 0.4

    def __str__(self):
        return f"Seguro Automóvel\n{super().__str__()}\nNúmero da Licença: {self._numero_licenca}\nModelo: {self._nome_modelo}\nAno: {self._ano}\nValor do Automóvel: {self._valor_automovel}"


class ControleDeSeguros:
    def __init__(self):
        self.seguros = []

    def cadastrarSeguro(self, seguro):
        self.seguros.append(seguro)

    def relatorioSeguros(self):
        qtd_vida = 0
        qtd_automovel = 0
        total_valores = 0

        for seguro in self.seguros:
            print(seguro)
            total_valores += seguro._valor_seguro

            if isinstance(seguro, SeguroVida):
                qtd_vida += 1
            elif isinstance(seguro, SeguroAutomovel):
                qtd_automovel += 1

        print("\nQuantidade de seguros de vida:", qtd_vida)
        print("Quantidade de seguros de automóveis:", qtd_automovel)
        print("Total dos valores:", total_valores)

# Criação de clientes
cliente1 = Cliente("123456789", "João Silva", 35)
cliente2 = Cliente("987654321", "Carlos Santos", 45)

# Criação de seguros de vida
seguro_vida1 = SeguroVida("AP001", cliente1, "Maria Silva", cliente1.obterIdade())
seguro_vida2 = SeguroVida("AP002", cliente2, "Ana Santos", cliente2.obterIdade())

# Cálculo do valor e prêmio do seguro de vida
valor_seguro_vida1 = seguro_vida1.calcularValor()
premio_seguro_vida1 = seguro_vida1.calcularPremio()

valor_seguro_vida2 = seguro_vida2.calcularValor()
premio_seguro_vida2 = seguro_vida2.calcularPremio()

print("Valor do Seguro de Vida 1:", valor_seguro_vida1)
print("Prêmio do Seguro de Vida 1:", premio_seguro_vida1)

print("Valor do Seguro de Vida 2:", valor_seguro_vida2)
print("Prêmio do Seguro de Vida 2:", premio_seguro_vida2)

# Criação de seguros automotivos
seguro_auto1 = SeguroAutomovel("AP003", cliente1, "AB123456", "Fiat Palio", 2019, 25000.00)
seguro_auto2 = SeguroAutomovel("AP004", cliente2, "CD654321", "Chevrolet Onix", 2020, 30000.00)

# Cálculo do valor, prêmio e franquia do seguro automotivo
valor_seguro_auto1 = seguro_auto1.calcularValor()
premio_seguro_auto1 = seguro_auto1.calcularPremio()
franquia_seguro_auto1 = seguro_auto1.calcularFranquia()

valor_seguro_auto2 = seguro_auto2.calcularValor()
premio_seguro_auto2 = seguro_auto2.calcularPremio()
franquia_seguro_auto2 = seguro_auto2.calcularFranquia()

print("Valor do Seguro Automotivo 1:", valor_seguro_auto1)
print("Prêmio do Seguro Automotivo 1:", premio_seguro_auto1)
print("Franquia do Seguro Automotivo 1:", franquia_seguro_auto1)

print("Valor do Seguro Automotivo 2:", valor_seguro_auto2)
print("Prêmio do Seguro Automotivo 2:", premio_seguro_auto2)
print("Franquia do Seguro Automotivo 2:", franquia_seguro_auto2)

# Criação do controle de seguros
controle_seguros = ControleDeSeguros()

# Cadastro dos seguros no controle
controle_seguros.cadastrarSeguro(seguro_vida1)
controle_seguros.cadastrarSeguro(seguro_vida2)
controle_seguros.cadastrarSeguro(seguro_auto1)
controle_seguros.cadastrarSeguro(seguro_auto2)

# Geração do relatório de seguros
controle_seguros.relatorioSeguros()
