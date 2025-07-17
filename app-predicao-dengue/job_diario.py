from supabase_config import supabase
import requests
import pandas as pd



CHAVE_API = {"X-UID-Key": "JaniceSilva:2794c643-6e30-47a1-9f06-cf844c617983"}

def atualizar_dados(municipio="rio-de-janeiro"):
    url = f"https://api.mosqlimate.org/api/datastore/infodengue/?city={municipio}"
    r = requests.get(url, headers=CHAVE_API)
    if r.status_code != 200:
        print("Erro:", r.text)
        return
    dados = r.json().get("results", [])
    registros = [{"municipio": municipio,
                  "data": x["data_iniSE"],
                  "casos": x["casos_est"]} for x in dados if x["casos_est"]]
    supabase.table("casos_diarios").upsert(registros).execute()
    print(f"✅ {len(registros)} registros atualizados para {municipio}")

if __name__ == "__main__":
    atualizar_dados()