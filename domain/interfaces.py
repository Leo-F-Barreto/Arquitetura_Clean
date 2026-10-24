from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities import Conta

class IContaRepository(ABC):
    @abstractmethod
    def salvar(self, conta: Conta) -> None:
        pass

    @abstractmethod
    def buscar_por_numero(self, numero: str) -> Optional[Conta]:
        pass

    @abstractmethod
    def listar_todas(self) -> List[Conta]:
        pass
