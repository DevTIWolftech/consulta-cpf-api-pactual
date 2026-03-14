from fastapi import FastAPI
from supabase import create_client

app = FastAPI()

url = "https://ccytkddvqawcapcqrvvb.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNjeXRrZGR2cWF3Y2FwY3FydnZiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM1MTUxNDgsImV4cCI6MjA4OTA5MTE0OH0.RmhxCWvav15uEu64-TaP7YH5lJquOWif2UdMjyQ9vsA"

supabase = create_client(url, key)

@app.get("/consulta/{cpf}")
def consulta(cpf: str):

    resposta = supabase.table("clientes").select("*").eq("cpf", cpf).execute()

    if resposta.data:
        return resposta.data[0]
    else:
        return {"erro": "CPF não encontrado"}
