# Sistema de Encomendas

Trabalho 2 da disciplina de Estruturas de Dados 2 (EDA2 - 2026.1), ministrada pelo Prof. Maurício Serrano — UnB.

O projeto implementa um sistema de gerenciamento de encomendas com operações de CRUD e ordenação por diferentes algoritmos.

## Integrantes

| Nome | Matrícula | GitHub |
|------|-----------|--------|
| Caio Sabino | 231026302 | [@caiomsabino](https://github.com/caiomsabino) |

## Estrutura do Projeto

```
.
├── main.py              # Ponto de entrada e menu principal
├── encomenda.py         # Modelo e lógica CRUD das encomendas
└── algoritmos/
    ├── insertion.py     # Insertion Sort
    ├── selection.py     # Selection Sort
    ├── counting.py      # Counting Sort
    ├── quick.py         # Quick Sort
    ├── radix_lsd.py     # Radix Sort (LSD)
    └── radix_msd.py     # Radix Sort (MSD)
```

## Funcionamento

Cada encomenda cadastrada possui os seguintes atributos:

| Atributo | Descrição |
|----------|-----------|
| `nome` | Nome do produto |
| `id` | Identificador único |
| `data_postagem` | Data de postagem |
| `peso` | Peso do pacote |
| `quantidade` | Quantidade de itens |
| `prioridade` | Nível de prioridade da entrega |

### Operações disponíveis

- **Criar** — cadastrar nova encomenda
- **Listar** — exibir todas as encomendas
- **Atualizar** — editar atributos de uma encomenda existente
- **Remover** — excluir uma encomenda pelo ID
- **Ordenar** - escolhe um dos atributos disponíveis e escolhe algum dos algoritmos possíveis

### Algoritmos de ordenação

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

## Como executar

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd G16_Ordenacao_EDA2-2026.1

# Execute o sistema
python main.py
```
