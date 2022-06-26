from flask import Flask
# from flask_bootstrap import Bootstrap4

app = Flask(__name__,
	template_folder='../client', #index.html/login.html
	static_folder='../client/assets' #css/js
)


# bootstrap = Bootstrap4(app)

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




CATEGORIAS = {f"categoria{num+1}":desc 
	for num, desc in enumerate(keys_indicadores.items())
}

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

from app import api
from app import routes