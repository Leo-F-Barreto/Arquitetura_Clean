from usecases.criar_conta_usecase import CriarContaUseCase
from usecases.realizar_saque_usecase import RealizarSaqueUseCase
from usecases.realizar_deposito_usecase import RealizarDepositoUseCase
from usecases.obter_extrato_usecase import ObterExtratoUseCase
from usecases.listar_contas_usecase import ListarContasUseCase

class ContaController:
    def __init__(self, view, criar_conta_uc, sacar_uc, depositar_uc, extrato_uc, listar_uc):
        self.view = view
        self.criar_conta_uc = criar_conta_uc
        self.sacar_uc = sacar_uc
        self.depositar_uc = depositar_uc
        self.extrato_uc = extrato_uc
        self.listar_uc = listar_uc

    def cadastrar_nova_conta(self):
        nome, cpf, saldo_inicial = self.view.obter_dados_cliente()
        try:
            nova_conta = self.criar_conta_uc.executar(nome, cpf, saldo_inicial)
            self.view.exibir_conta_criada(nova_conta)
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}")

    def depositar(self):
        numero = self.view.pedir_numero_conta()
        valor = self.view.pedir_valor_operacao("Depósito")
        try:
            conta = self.depositar_uc.executar(numero, valor)
            self.view.exibir_mensagem(f"Sucesso! Novo Saldo: R$ {conta.saldo:.2f}")
        except (ValueError, LookupError) as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}")

    def sacar(self):
        numero = self.view.pedir_numero_conta()
        valor = self.view.pedir_valor_operacao("Saque")
        try:
            conta = self.sacar_uc.executar(numero, valor)
            self.view.exibir_mensagem(f"Sucesso! Novo Saldo: R$ {conta.saldo:.2f}")
        except (ValueError, LookupError) as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}")

    def exibir_extrato_completo(self):
        numero = self.view.pedir_numero_conta()
        try:
            conta = self.extrato_uc.executar(numero)
            self.view.exibir_historico_tela(conta)
        except LookupError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}")

    def listar_contas(self):
        contas = self.listar_uc.executar()
        if not contas:
            self.view.exibir_mensagem("Nenhuma conta cadastrada.")
        else:
            self.view.exibir_lista_contas(contas)
