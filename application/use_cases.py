from application.interfaces import IContaRepository


class RealizarSaqueUseCase:
    def __init__(self, repository: IContaRepository):
        self.repository = repository

    def executar(self, numero_conta: str, valor: float):
        conta = self.repository.buscar_por_numero(numero_conta)
        if not conta:
            raise LookupError("Conta não encontrada.")
        if valor <= 0:
            raise ValueError("Valor deve ser maior que zero.")
        if valor > conta.saldo:
            raise ValueError("Saldo insuficiente.")

        conta.saldo -= valor
        conta.historico.append(f"Saque realizado: -R$ {valor:.2f}")

        self.repository.salvar(conta)
        return conta
