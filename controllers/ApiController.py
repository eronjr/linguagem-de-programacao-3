from flask import request 
from flask import send_file
from core.server import indices_criminais
from core.server.geraGraf import contagemCrimesMensal

from core import CATEGORIAS

def indicadores_anual():
	params = request.args.to_dict(flat=False)
	if 'anos' in params and 'categoria' in params:
		anos = list(map(str, params.get('anos')))
		indicador = params.get('categoria')[0]
		indicadores = indices_criminais.Indicadores()
		path_indice = indicadores.get_indicador(
					CATEGORIAS[indicador].unnamed, 
					anos=anos
		)
		return send_file(path_indice, mimetype='image/png')
		
	return {
			'message':'erro na passagem de parametros'
	}

def indicadores_mensal():
	params = request.args.to_dict(flat=False)
	if 'anos' in params and 'categoria' in params and 'mes' in params:
		anos = list(map(str, params.get('anos')))
		mes = list(map(str.lower, params.get('mes')))
		indicador = params.get('categoria')   
		indicadores = contagemCrimesMensal
		crimes = [CATEGORIAS[indicador[0]].descricao]
		path_indice = indicadores(
                    mes=mes[0],
                    listadeAnos=anos,
                    ListaCrimes=crimes, 
            )
		return send_file(path_indice, mimetype='image/png')
	
	return {
		'message':'erro na passagem de parametros'
    }
