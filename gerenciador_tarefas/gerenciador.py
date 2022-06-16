from fastapi import FastAPI

app = FastAPI()

# ...
TAREFAS = [
    {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "titulo": "titulo 1",
        "descricao": "descricao 1",
        "estado": "finalizado",
    }
]
# ...

@app.get("/tarefas")
def listar():
    return TAREFAS