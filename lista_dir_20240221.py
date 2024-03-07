# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 09:59:10 2024

@author: 2018459
"""

import os
import pandas as pd


# Caminho INRA: \\pfl-cps-file\INRA
# Caminho Estratégia: \\pfl-cps-file\Estrategia Regulatoria
pastas = [r'\\pfl-cps-file\Estrategia Regulatoria\Conformidade',
          r'\\pfl-cps-file\Estrategia Regulatoria\GOVERNANÇA']


# Pasta para guardar os arquivos com mais de 250 caracteres
pasta_rede = []

# Função listar os arquivos
# r=root, d=directories, f = files
def lista_dir(pasta):
    for r, d, f in os.walk(pasta):
        for file in f:
            caminho = os.path.join(r,file)
            if len(fr'{caminho}') > 250:
                pasta_rede.append(os.path.join(r, file))
                print(os.path.join(r, file))
                

# Roda a função
for pasta in pastas:
    lista_dir(pasta)
                
# Exporta o arquivo
df_rede = pd.DataFrame(pasta_rede)
df_rede.to_excel(r'C:\Users\2018459\OneDrive - CPFL Energia S A\Documentos\Projetos\2023\Unificação da Rede\Dados\pasta_rede_conformidade.xlsx',encoding = 'UTF-8', index=False)
                
                

                
                
                