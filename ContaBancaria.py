class ContaBancaria:
    def __init__(self, numero, saldo, nome, tipo, limite, status = False):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.status = status
        self.limite = limite

    def ativarconta(self):
        if self.status == False:
            self.status = True
            print('A conta foi ativada')
        else:
            print('Conta já está ativada')

    def depositar(self, valor_deposito):
        if valor_deposito > 0:
            self.saldo += valor_deposito
            self.verificarsaldo()
        else:
            print('Não é possivel depositar um valor negativo!')
    def sacar(self, valor_saque):
        if valor_saque <= self.limite:
            self.saldo -= valor_saque
            self.verificarsaldo()
        else:
            print(f'Seu saque de {valor_saque} supera o seu limite de {self.limite}')
    def verificarsaldo(self):
        print(f'O seu saldo é: R${self.saldo}')


conta = ContaBancaria(123,123,"V","Corrente",5000)

deposito = int(input('Digite o valor do deposito: '))
conta.depositar(deposito)

saque = int(input('Digite o valor do saque: '))
conta.sacar(saque)
