# Validador de Contratos

Este projeto realiza a validação de contratos, verificando se o CNPJ é válido e se o contrato possui assinatura. Os contratos aprovados são movidos pra pasta 'aprovados'.

## Estrutura

- 'contratos/': Contratos em texto para validação.
- 'aprovados/': Onde ficam os contratos validados.
- 'cnpjs.csv': Planilha Excel com uma coluna chamada **CNPJ**, contendo os CNPJs válidos.
- 'main.py': Código principal.
- 'utils.py': Funções auxiliares.
- 'requirements.txt': Dependências.
- 'README.md': Este arquivo.

## Como usar

1. Instale as dependências:
'''
pip install - r requirements.txt
'''

2. Coloque seus contratos de texto na pasta 'contratos/'.

3. Preencha a planilha 'cnpjs.csv' com os CNPJs válidos.

4. Rode:
'''
python main.py
'''

5. Contratos aprovados vão para 'aprovados/'.

## Exemplo de contrato ('contratos/contrato1.txt')
'''
Contrato de Prestação de Serviço
CPNJ: 01.234.567/0001-89
Assinatura: Fulano de Tal
'''

## Exemplo de cnpj.csv
'''
CNPJ
01.234.567/0001-89
98.765.432/0001-00
12.345.678/0001-99
'''

