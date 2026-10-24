from infrastructure.arquivo_conta_repository import ArquivoContaRepository
from usecases.criar_conta_usecase import CriarContaUseCase
from usecases.realizar_saque_usecase import RealizarSaqueUseCase
from usecases.realizar_deposito_usecase import RealizarDepositoUseCase
from usecases.obter_extrato_usecase import ObterExtratoUseCase
from usecases.listar_contas_usecase import ListarContasUseCase
from presentation.controllers import ContaController
from presentation.views import BancoView

if __name__ == "__main__":
    # 1. Configurar Infraestrutura (Resolução de Dependências)
    repository = ArquivoContaRepository("dados_contas.txt")
    
    # 2. Configurar Use Cases (Injetando a Interface do Repositório)
    criar_conta_uc = CriarContaUseCase(repository)
    sacar_uc = RealizarSaqueUseCase(repository)
    depositar_uc = RealizarDepositoUseCase(repository)
    extrato_uc = ObterExtratoUseCase(repository)
    listar_uc = ListarContasUseCase(repository)
    
    # 3. Configurar Apresentação (View e Controller)
    view = BancoView()
    controller = ContaController(
        view, criar_conta_uc, sacar_uc, depositar_uc, extrato_uc, listar_uc
    )
    view.controller = controller # Ligando o controller à view
    
    # 4. Iniciar a aplicação
    view.executar_interface()
