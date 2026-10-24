import json
import os
from domain.models import Cliente, Conta
from application.interfaces import IContaRepository

class ArquivoContaRepository(IContaRepository):
    def __init__(self, caminho_arquivo: str = "banco_dados.txt"):
        self.caminho = caminho_arquivo

    def _ler_dados(self):
        if not os.path.exists(self.caminho):
            return {}
        with open(self.caminho, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}

    def _gravar_dados(self, dados):
        with open(self.caminho, "w") as f:
            json.dump(dados, f, indent=4)

    def salvar(self, conta: Conta):
        dados = self._ler_dados()
        dados[conta.numero] = {
            "numero": conta.numero,
            "titular_nome": conta.titular.nome,
            "titular_cpf": conta.titular.cpf,
            "saldo": conta.saldo,
            "historico": conta.historico
        }
        self._gravar_dados(dados)

    def buscar_por_numero(self, numero: str) -> Conta:
        dados = self._ler_dados()
        if numero in dados:
            d = dados[numero]
            cliente = Cliente(d["titular_nome"], d["titular_cpf"])
            conta = Conta(d["numero"], cliente, d["saldo"])
            conta.historico = d["historico"]
            return conta
        return None

    def listar_todas(self) -> list:
        dados = self._ler_dados()
        contas = []
        for d in dados.values():
            cliente = Cliente(d["titular_nome"], d["titular_cpf"])
            conta = Conta(d["numero"], cliente, d["saldo"])
            conta.historico = d["historico"]
            contas.append(conta)
        return contas
