from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from datetime import date
from gerenciador import GerenciadorEncomendas
from algoritmos import ALGORITMOS
import random
from datetime import date, timedelta

# 1. Inicialização
app = FastAPI(title="Sistema de Logística - Ordenação")
g = GerenciadorEncomendas()
g.carregar_dados_iniciais("dados.json")

# Permite que o frontend (HTML) faça requisições para esta API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Modelo de Entrada (O que o Frontend envia)
class EncomendaIn(BaseModel):
    nome: str
    data_postagem: date
    peso: float
    quantidade: int
    prioridade: int

# 3. Rotas da API

@app.get("/")
def pagina_principal():
    # Isso faz o servidor ler o arquivo HTML e enviar para o navegador
    return FileResponse("index.html")

@app.get("/encomendas")
def listar_todas():
    return g.listar()

@app.post("/encomendas")
def criar_nova(enc: EncomendaIn):
    # Passamos os dados recebidos do front para o gerenciador
    nova = g.criar(enc.nome, enc.data_postagem, enc.peso, enc.quantidade, enc.prioridade)
    return {"mensagem": "Encomenda criada!", "id": nova.id}

@app.get("/ordenar/{atributo}/{algoritmo}")
def ordenar_encomendas(atributo: str, algoritmo: str):
    # Reutilizando as validações que já existem no gerenciador
    _ATRIBUTOS = ["nome", "id", "data_postagem", "peso", "quantidade", "prioridade"]
    
    if atributo not in _ATRIBUTOS or algoritmo not in ALGORITMOS:
        raise HTTPException(status_code=400, detail="Atributo ou Algoritmo inválido")
        
    resultado = g.ordenar(atributo, algoritmo)
    return resultado

@app.post("/gerar-teste/{quantidade}")
def gerar_massa_teste(quantidade: int):
    # Listas de palavras para gerar nomes de produtos realistas
    tipos = ["Notebook", "Monitor", "Cadeira", "Teclado", "Mouse", "Mesa", "Gabinete", "Placa", "Cabo"]
    marcas = ["Dell", "Razer", "Logitech", "Corsair", "Asus", "Acer", "LG", "Samsung"]
    
    data_base = date.today()

    for _ in range(quantidade):
        nome_aleatorio = f"{random.choice(tipos)} {random.choice(marcas)} {random.randint(100, 999)}"
        # Gera uma data aleatória nos últimos 365 dias
        data_aleatoria = data_base - timedelta(days=random.randint(0, 365))
        peso_aleatorio = round(random.uniform(0.1, 50.0), 2)
        qtd_aleatoria = random.randint(1, 100)
        prio_aleatoria = random.randint(1, 5)

        # Injeta direto no gerenciador
        g.criar(nome_aleatorio, data_aleatoria, peso_aleatorio, qtd_aleatoria, prio_aleatoria)

    return {"mensagem": f"{quantidade} encomendas geradas com sucesso!"}