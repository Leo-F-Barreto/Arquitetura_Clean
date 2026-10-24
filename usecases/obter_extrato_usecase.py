from domain.interfaces import IContaRepository

class ObterExtratoUseCase:
    def __init__(self, repo: IContaRepository):
        self.repo = repo

    def executar(self, numero_conta: str):
        conta = self.repo.buscar_por_numero(numero_conta)
        if not conta:
            raise LookupError("Conta não encontrada.")
        return conta
