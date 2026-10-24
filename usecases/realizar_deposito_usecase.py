from domain.interfaces import IContaRepository

class RealizarDepositoUseCase:
    def __init__(self, repo: IContaRepository):
        self.repo = repo

    def executar(self, numero_conta: str, valor: float):
        conta = self.repo.buscar_por_numero(numero_conta)
        if not conta:
            raise LookupError("Conta não encontrada.")
        if valor <= 0:
            raise ValueError("Valor deve ser maior que zero.")
        
        conta.saldo += valor
        conta.historico.append(f"Depósito realizado: +R$ {valor:.2f}")
        self.repo.salvar(conta)
        return conta
