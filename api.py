from fastapi import FastAPI
from supabase import create_client

app = FastAPI()

url = "https://ccytkddvqawcapcqrvvb.supabase.co"
key = "sb_publishable_8flZJ6jvoiAu5nLFUwsLHw_xB_JaIOL"

supabase = create_client(url, key)

@app.get("/consulta/{cpf}")
def consulta(cpf: str):

    resposta = supabase.table("clientes").select("*").eq("cpf", cpf).execute()

    if resposta.data:
        return resposta.data[0]
    else:
        return {"erro": "CPF não encontrado"}
