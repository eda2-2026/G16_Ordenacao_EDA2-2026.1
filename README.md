# Sistema de Encomendas

Trabalho 2 da disciplina de Estruturas de Dados 2 (EDA2 - 2026.1), ministrada pelo Prof. Maurício Serrano — UnB.

O projeto implementa um sistema de gerenciamento de encomendas com CRUD, ordenação por múltiplos algoritmos, modo CLI e uma API com interface web.

## Integrantes

| Nome | Matrícula | GitHub |
|------|-----------|--------|
| Caio Sabino | 231026302 | [@caiomsabino](https://github.com/caiomsabino) |
| João Victor Sapiência | 231026400 | [@JoaoSapiencia](https://github.com/JoaoSapiencia) |

## Estrutura do Projeto

```
.
├── api.py               # API FastAPI + rotas de ordenação
├── dados.json           # Massa de dados inicial (opcional)
├── encomenda.py         # Modelo de dados: classe Encomenda
├── gerenciador.py       # GerenciadorEncomendas: CRUD + ordenação
├── index.html           # Interface web (consome a API)
├── main.py              # Ponto de entrada e menu interativo (CLI)
├── requirements.txt     # Dependências da API
└── algoritmos/
    ├── __init__.py      # Expõe o dicionário ALGORITMOS
    ├── insertion.py     # Insertion Sort
    ├── selection.py     # Selection Sort
    ├── counting.py      # Counting Sort
    ├── quick.py         # Quick Sort
    ├── radix_lsd.py     # Radix Sort (LSD)
    └── radix_msd.py     # Radix Sort (MSD)
```

## Modelo de dados

Cada encomenda cadastrada possui os seguintes atributos:

| Atributo | Descrição |
|----------|-----------|
| `nome` | Nome do produto |
| `id` | Identificador único |
| `data_postagem` | Data de postagem |
| `peso` | Peso do pacote |
| `quantidade` | Quantidade de itens |
| `prioridade` | Nível de prioridade da entrega |

## Operações disponíveis

- **Criar** — cadastrar nova encomenda
- **Listar** — exibir todas as encomendas
- **Atualizar** — editar atributos de uma encomenda existente
- **Remover** — excluir uma encomenda pelo ID
- **Ordenar** — escolher atributo e algoritmo de ordenação

## Algoritmos de ordenação

As encomendas podem ser ordenadas por qualquer atributo usando os algoritmos abaixo:

| Algoritmo | Complexidade (médio) | Complexidade (pior caso) | Estável |
|-----------|----------------------|--------------------------|---------|
| Radix MSD | O(n · k) | O(n · k) | Sim |
| Selection Sort | O(n²) | O(n²) | Não |
| Radix LSD | O(n · k) | O(n · k) | Sim |
| Insertion Sort | O(n²) | O(n²) | Sim |
| Counting Sort | O(n + k) | O(n + k) | Sim |
| Quick Sort | O(n log n) | O(n²) | Não |

> `n` = número de encomendas, `k` = número de dígitos/chaves

## Requisitos

- Python 3.10 ou superior

## Como executar (CLI)

```bash
python main.py
```

## Como executar (API + Interface Web)

Instale as dependências:

```bash
pip install -r requirements.txt
```

Inicie o servidor:

```bash
uvicorn api:app --reload
```

Depois acesse:

- http://localhost:8000/ (interface web)

## Observações

- Se o arquivo `dados.json` existir, ele é carregado no início; caso contrário, o sistema começa vazio.
- A rota `/ordenar` retorna também o tempo de execução da ordenação em `tempo_ms`.
