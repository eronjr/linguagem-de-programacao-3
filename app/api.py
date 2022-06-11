from app import app
from flask import request 
from server import indices_criminais
from server import download_indicadores
from flask import send_file
from app import CATEGORIAS

# download_indicadores.ParserIndicadores().get_indicadores()
@app.route('/api')
def api():
    return "I'am Working"

@app.route('/api/indicadores_anual')
def api_get_indicadores():
    
    # {
    #     "anos":[2015, 2016, 2022],
    #     "categoria":'categoria1'
    # }

    if request.method == 'GET':
        params = request.args.to_dict(flat=False)
        print(params)
        if 'anos' in params and 'categoria' in params:
            anos = list(map(str, params.get('anos')))
            indicador = params.get('categoria')[0]
        
        indicadores = indices_criminais.Indicadores()
        path_indice = indicadores.get_indicador(
                CATEGORIAS[indicador][0], 
                anos=anos
        )
        
        return send_file(path_indice, mimetype='image/png')
    

@app.route('/api/indicadores_mensal')
def api_get_mensal():

    params = request.args.to_dict(flat=False)

    return {
        "message":"sendo implementado"
    }

@app.route("/api/documentation")
def doc():
    anos = "<br>".join(map(str, range(2012, 2023)))
    categorias = "<br>".join(CATEGORIAS.keys())
    categorias_desc = "<br>".join(map(lambda v: f"{v[0]} --> {v[1][1]}",CATEGORIAS.items()))
    ex = "{'anos':[2015,2016], 'categoria':'categoria1'}"
    
    return f"""<b>Como usar a API</b></br>
parametros: <b><pre>anos<pre></b> - representa o escopo de determinado indicador requerido.
valores para o parâmetro.<br>
{anos}

<b><pre>categoria</b>
- representa indicador que deseja-se obter, a descrição do indicador está no final da página.
valores para o parâmetro.<br>
{categorias}


exemplo de requisição<br>
curl http://127.0.0.1:5000/api/indicadores_anual?anos=2015&anos=2016&anos=2022&categoria=categoria1

import requests
r = requests.get('http://127.0.0.1:5000/api/indicadores_anual', params={ex})

é retornado uma imagem quando é feito <b>GET</b> com sucesso
descrição das categorias<br>
{categorias_desc}
"""
