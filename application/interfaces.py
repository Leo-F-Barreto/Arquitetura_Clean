from abc import ABC, abstractmethod
from domain.models import Conta


class IContaRepository(ABC):
    @abstractmethod
    def salvar(self, conta: Conta):
        pass

    @abstractmethod
    def buscar_por_numero(self, numero: str) -> Conta:
        pass

    @abstractmethod
    def listar_todas(self) -> list:
        pass
