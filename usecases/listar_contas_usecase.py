from domain.interfaces import IContaRepository

class ListarContasUseCase:
    def __init__(self, repo: IContaRepository):
        self.repo = repo

    def executar(self):
        return self.repo.listar_todas()
