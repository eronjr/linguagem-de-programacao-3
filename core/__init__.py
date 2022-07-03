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

class CategoriaDesc:
    def __init__(self, categoria_id, descricao, unnamed):
        self.categoria_id = categoria_id
        self.descricao = descricao
        self.unnamed = unnamed 

CATEGORIAS = {
    f"categoria{num+1}":CategoriaDesc(f"categoria{num+1}", desc[1], desc[0]) 
	for num, desc in enumerate(keys_indicadores.items())
}