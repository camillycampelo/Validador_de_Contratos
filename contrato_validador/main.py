import os
import pandas as pd
from utils import validar_cnpj, validar_assinatura

CNPJS_FILE = 'cnpjs.csv'
CONTRATOS_DIR = 'contratos'
APROVADOS_DIR = 'aprovados'

def carregar_cnpjs():
    df = pd.read_csv(CNPJS_FILE)
    return set(df['CNPJ'].astype(str))

def processar_contratos():
    cnpjs_validos = carregar_cnpjs()
    if not os.path.exists(APROVADOS_DIR):
        os.makedirs(APROVADOS_DIR)
    for nome_arquivo in os.listdir(CONTRATOS_DIR):
        caminho = os.path.join(CONTRATOS_DIR, nome_arquivo)
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        cnpj = validar_cnpj(conteudo, cnpjs_validos)
        assinatura = validar_assinatura(conteudo)
        if cnpj and assinatura:
            destino = os.path.join(APROVADOS_DIR, nome_arquivo)
            with open(destino, 'w', encoding='utf-8') as f:
                f.write(conteudo)
            print(f"{nome_arquivo} aprovado!")
        else:
            print(f"{nome_arquivo} rejeitado: {'CNPJ inválido' if not cnpj else 'Sem assinatura'}")

if __name__ == "__main__":
    processar_contratos()