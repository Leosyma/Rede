# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 09:59:10 2024

@author: 2018459
"""

import os
import pandas as pd


# Diretório a ser mapeado
pastas = [r'']


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
df_rede.to_excel(r'',encoding = 'UTF-8', index=False) #Saida do arquivo
                
                

                
                
                