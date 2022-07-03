import pandas as pd
import numpy as np
import os
import re
import urllib.parse

DIR_ATUAL = os.getcwd()

# import download_indicadores

# ParserIndicadores().get_indicadores()

indicadores = [f'server/indicadores/{caminho.strip()}'
               for caminho in os.popen(f"ls server/indicadores/").readlines()
]


try:
    os.mkdir(f"{DIR_ATUAL}/server/indicadores_graficos")
    print("Diretório indicadores_graficos criado")
except FileExistsError:
    pass

REGEX_ANO = '[ano|municipios]-([0-9]+)'

indicadores = sorted(indicadores, 
    key=lambda c:int(re.findall(REGEX_ANO,c)[0])
)

indicadores_anos  = [re.findall(REGEX_ANO,ano)[0] 
                                      for ano in indicadores]

indicadores = dict(zip(indicadores_anos,indicadores))


keys_indicadores = {
    'Unnamed: 2': 'Homicídio Doloso', 
    'Unnamed: 3': 'Total de vítimas de Homicídio Doloso', 
    'Unnamed: 4': 'Latrocínio', 
    'Unnamed: 5': 'Furto', 
    'Unnamed: 6': 'Abigeato*', 
    'Unnamed: 7': 'Furto de Veículo', 
    'Unnamed: 8': 'Roubos', 
    'Unnamed: 9': 'Roubo de Veículo', 
    'Unnamed: 10': 'Estelionato', 
    'Unnamed: 11': 'Delitos Relacionados à Armas e Munições', 
    'Unnamed: 12': 'Entorpecentes - Posse', 
    'Unnamed: 13': 'Entorpecentes - Tráfico', 
    'Unnamed: 14': 'Vítimas de Latrocínio', 
    'Unnamed: 15': 'Vítimas de Lesão Corp. Seg. Morte'
}

"""
dict_keys(['GERAL', '201*', 'JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ'])

"""


def read_excel(caminho:str, sheet_name=None, header=None)->[list, list]:
    indice = pd.read_excel(caminho.strip(),
                           sheet_name=sheet_name, 
                           header=header
    )
    
    return indice

def indice_geral(data, key):    
    indice = data["GERAL"]
    data = indice[key][4:16]
    return data

class Indicadores:
    
    def __init__(self):
        self.indicadores = indicadores
    
    def get_indicadores_geral(self):
        self.colunas = [f'Unnamed: {ind}' for ind in range(2,15)]
        
        for coluna in self.colunas:
            self.get_indicador(coluna)
            
    def get_indicador(self, coluna, anos=None): 
        lista_indices_criminais = []
        if anos and isinstance(anos, list):
            self.indicadores = {
                ano:indicadores[ano] for ano in anos
            }
            anos.sort()
        
        for caminho in self.indicadores.values():
            #caminho = 'indicadores/13192731-site-geral-e-municipios-2013-publicacao.xlsx'
            indices = read_excel(caminho, header=1)
            indices_criminais = indice_geral(indices, coluna)

            
            indices_criminais.fillna(value = 0,  
                      inplace = True
            )

            lista_indices_criminais.append(np.array(indices_criminais))

        td = len(lista_indices_criminais)
        dados = np.array(lista_indices_criminais)
        
        dados = dados.reshape(12, td)
        dados_df = pd.DataFrame(dados)
        
        
        anos = '-'.join(map(str, anos))

        plot = dados_df.plot(
            title=f"{keys_indicadores[coluna]} no RS durante os anos de {anos}"
        )

        fig = plot.get_figure()
        path_indice = f"server/indicadores_graficos/indices_anos_{anos}_geral_{'-'.join(keys_indicadores[coluna].split())}.png"        
        fig.savefig(path_indice)
        # return send_file(path_indice, mimetype='image/png')
        return  f"{DIR_ATUAL}/{path_indice}"

