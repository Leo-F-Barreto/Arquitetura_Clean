import os
from typing import List, Optional
from domain.entities import Conta, Cliente
from domain.interfaces import IContaRepository

class ArquivoContaRepository(IContaRepository):
    def __init__(self, filepath="dados_contas.txt"):
        self.filepath = filepath
        if not os.path.exists(self.filepath):
            open(self.filepath, 'w').close()

    def _ler_todas(self) -> List[Conta]:
        contas = []
        with open(self.filepath, 'r', encoding='utf-8') as f:
            for linha in f:
                linha = linha.strip()
                if not linha: continue
                partes = linha.split('|')
                numero, nome, cpf, saldo_str, historico_str = partes
                cliente = Cliente(nome, cpf)
                conta = Conta(numero, cliente, float(saldo_str))
                conta.historico = historico_str.split(';') if historico_str else []
                contas.append(conta)
        return contas

    def _salvar_todas(self, contas: List[Conta]) -> None:
        with open(self.filepath, 'w', encoding='utf-8') as f:
            for c in contas:
                hist = ';'.join(c.historico)
                f.write(f"{c.numero}|{c.titular.nome}|{c.titular.cpf}|{c.saldo}|{hist}\n")

    def salvar(self, conta: Conta) -> None:
        contas = self._ler_todas()
        atualizada = False
        for i, c in enumerate(contas):
            if c.numero == conta.numero:
                contas[i] = conta
                atualizada = True
                break
        if not atualizada:
            contas.append(conta)
        self._salvar_todas(contas)

    def buscar_por_numero(self, numero: str) -> Optional[Conta]:
        contas = self._ler_todas()
        for c in contas:
            if c.numero == numero:
                return c
        return None

    def listar_todas(self) -> List[Conta]:
        return self._ler_todas()
