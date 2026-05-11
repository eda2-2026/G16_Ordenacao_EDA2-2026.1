from __future__ import annotations
from datetime import date
from encomenda import Encomenda
from algoritmos import ALGORITMOS
import json
import os

_ATRIBUTOS_VALIDOS = {"nome", "id", "data_postagem", "peso", "quantidade", "prioridade"}


class GerenciadorEncomendas:
    def __init__(self):
        self._encomendas: list[Encomenda] = []
        self._proximo_id: int = 1


    def criar(
        self,
        nome: str,
        data_postagem: date,
        peso: float,
        quantidade: int,
        prioridade: int,
    ) -> Encomenda:
        encomenda = Encomenda(
            id=self._proximo_id,
            nome=nome,
            data_postagem=data_postagem,
            peso=peso,
            quantidade=quantidade,
            prioridade=prioridade,
        )
        self._encomendas.append(encomenda)
        self._proximo_id += 1
        return encomenda


    def listar(self) -> list[Encomenda]:
        return list(self._encomendas)

    def buscar_por_id(self, id: int) -> Encomenda | None:
        for enc in self._encomendas:
            if enc.id == id:
                return enc
        return None


    def atualizar(
        self,
        id: int,
        nome: str | None = None,
        data_postagem: date | None = None,
        peso: float | None = None,
        quantidade: int | None = None,
        prioridade: int | None = None,
    ) -> Encomenda | None:
        enc = self.buscar_por_id(id)
        if enc is None:
            return None

        if nome is not None:
            enc.nome = nome
        if data_postagem is not None:
            enc.data_postagem = data_postagem
        if peso is not None:
            enc.peso = peso
        if quantidade is not None:
            enc.quantidade = quantidade
        if prioridade is not None:
            enc.prioridade = prioridade

        return enc


    def remover(self, id: int) -> bool:
        for i, enc in enumerate(self._encomendas):
            if enc.id == id:
                self._encomendas.pop(i)
                return True
        return False


    def ordenar(self, atributo: str, algoritmo: str) -> list[Encomenda]:
        if atributo not in _ATRIBUTOS_VALIDOS:
            raise ValueError(
                f"Atributo inválido: '{atributo}'. Escolha entre: {_ATRIBUTOS_VALIDOS}"
            )
        if algoritmo not in ALGORITMOS:
            raise ValueError(
                f"Algoritmo inválido: '{algoritmo}'. Escolha entre: {set(ALGORITMOS)}"
            )

        n = len(self._encomendas)
        if n == 0:
            return []

        chaves = [getattr(enc, atributo) for enc in self._encomendas]
        sorted_unique = sorted(set(chaves))
        rank = {k: r for r, k in enumerate(sorted_unique)}
        codificado = [rank[chaves[i]] * n + i for i in range(n)]

        ALGORITMOS[algoritmo](codificado)

        # Decodifica: posição original = valor % n
        return [self._encomendas[v % n] for v in codificado]
    
    def carregar_dados_iniciais(self, caminho_arquivo="dados.json"):
        # Verifica se o arquivo JSON existe antes de tentar abrir
        if not os.path.exists(caminho_arquivo):
            print("Arquivo de backup não encontrado. Iniciando vazio.")
            return

        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f) # Transforma o texto do JSON em uma lista do Python
            
            for item in dados:
                # O JSON salva a data como texto ("2026-05-10"), 
                # precisamos converter de volta para o tipo 'date' do Python
                data_convertida = date.fromisoformat(item["data_postagem"])
                
                # Usa a própria função criar que já existe para garantir que o ID seja gerado certo
                self.criar(
                    nome=item["nome"],
                    data_postagem=data_convertida,
                    peso=item["peso"],
                    quantidade=item["quantidade"],
                    prioridade=item["prioridade"]
                )
