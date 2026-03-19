import re

def validar_cnpj(conteudo: str, cnpjs_validos: set) -> bool:
    match = re.search(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', conteudo)
    if match:
        cnpj = match.group()
        return cnpj in cnpjs_validos
    return False

def validar_assinatura(conteudo: str) -> bool:
    return "Assinatura:" in conteudo