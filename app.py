from infrastructure.repositories import ArquivoContaRepository
from application.use_cases import RealizarSaqueUseCase
from domain.models import Conta, Cliente

if __name__ == "__main__":
    repositorio = ArquivoContaRepository("banco_dados.txt")

    # Criação de conta inicial para teste automatizado
    if not repositorio.buscar_por_numero("001"):
        cliente = Cliente("Leonardo F. Barreto", "12345678900")
        conta = Conta("001", cliente, 100.0)
        repositorio.salvar(conta)
        print("Conta de teste criada com saldo de R$ 100.0")

    saque_use_case = RealizarSaqueUseCase(repositorio)

    try:
        conta_atualizada = saque_use_case.executar(numero_conta="001", valor=50.0)
        print(f"Saque com sucesso. Novo saldo: R$ {conta_atualizada.saldo}")
    except Exception as e:
        print(f"Erro: {e}")
