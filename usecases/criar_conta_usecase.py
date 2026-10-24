from domain.entities import Cliente, Conta
from domain.interfaces import IContaRepository

class CriarContaUseCase:
    def __init__(self, repo: IContaRepository):
        self.repo = repo

    def executar(self, nome: str, cpf: str, saldo_inicial: float):
        if not nome or not cpf:
            raise ValueError("Nome e CPF são obrigatórios.")
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        
        contas_existentes = self.repo.listar_todas()
        novo_numero = f"{len(contas_existentes) + 1:03d}"
        
        cliente = Cliente(nome, cpf)
        nova_conta = Conta(novo_numero, cliente, saldo_inicial)
        self.repo.salvar(nova_conta)
        return nova_conta
