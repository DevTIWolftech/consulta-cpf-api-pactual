from fastapi import FastAPI
from supabase import create_client

app = FastAPI()

url = "postgresql://postgres:[YOUR-PASSWORD]@db.ccytkddvqawcapcqrvvb.supabase.co:5432/postgres"
key = "Q1NAFcD7R3g9vLiB"

supabase = create_client(url, key)

@app.get("/consulta/{cpf}")
def consulta(cpf: str):

    resposta = supabase.table("clientes").select("*").eq("cpf", cpf).execute()

    if resposta.data:
        return resposta.data[0]
    else:
        return {"erro": "CPF não encontrado"}
