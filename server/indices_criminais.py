import pandas as pd
import numpy as np
import os
import re

indicadores = [f'indicadores/{caminho.strip()}'
               for caminho in os.popen("ls indicadores").readlines()
]

try:
    os.mkdir("indicadores_graficos")
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
        lista_homicidio_doloso = []
        if anos and isinstance(anos, list):
          self.indicadores = {ano:indicadores[ano] for ano in anos}
        
        for caminho in self.indicadores.values():
            print(caminho)
            #caminho = 'indicadores/13192731-site-geral-e-municipios-2013-publicacao.xlsx'
            indices = read_excel(caminho, header=1)
            homicidio_doloso = indice_geral(indices, coluna)

            
            homicidio_doloso.fillna(value = 0,  
                      inplace = True
            )

            lista_homicidio_doloso.append(np.array(homicidio_doloso))

        td = len(lista_homicidio_doloso)
        dados = np.array(lista_homicidio_doloso)
        
        dados = dados.reshape(12, td)
        dados_df = pd.DataFrame(dados)
        
        
        
        plot = dados_df.plot(
            title=f"{keys_indicadores[coluna]} no RS durante os anos de 2012 e 2022"
        )

        fig = plot.get_figure()
        fig.savefig(f"indicadores_graficos/indices_geral_{keys_indicadores[coluna]}.png")
