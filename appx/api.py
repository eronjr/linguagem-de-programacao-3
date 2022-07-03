from app import app
from flask import request 
from server import indices_criminais
from server import download_indicadores
from flask import send_file
from app import CATEGORIAS

from server.geraGraf import contagemCrimesMensal

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

@app.route('/api/indicadores_mensal')
def api_get_mensal():

    if request.method == 'GET':
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

@app.route("/api/documentation")
def doc():
    anos = ",".join(map(str, range(2012, 2023)))
    categorias = ",".join(CATEGORIAS.keys())
    categorias_desc = "<br>".join(map(lambda v: f"{v.categoria_id} --> {v.descricao}",CATEGORIAS.values()))
    ex_ano = "{'anos':[2015,2016], 'categoria':'categoria1'}"
    ex_mes = "{'anos':[2016,2020], 'categoria':'categoria4', 'mes':'maio'}"
    style = """<style>
code {
  font-family: Consolas,"courier new";
  color: crimson;
  background-color: #f1f1f1;
  padding: 2px;
  font-size: 105%;
}
</style>""" 

    return f"""{style}
    <h1>Como usar a API</h1>

parametros: 

<b><pre>anos</pre></b> 
- representa o escopo de determinado indicador requerido.<br>valores para o parâmetro.<br>
{anos}

<b><pre>categoria</pre></b>
- representa indicador que deseja-se obter, a descrição do indicador está no final da página.<br>
valores para o parâmetro.<br>

{categorias}

<h2>Pegando os dados anuais</h2>

exemplo de requisição<br>

<br>usando curl<br>
<code>curl http://127.0.0.1:5000/api/indicadores_anual?anos=2015&anos=2016&anos=2022&categoria=categoria1</code>

<br>usando python<br>
<code>
import requests<br>
r = requests.get('http://127.0.0.1:5000/api/indicadores_anual', params={ex_ano})
</code>

<h2>Pegando os dados anuais a um mês pré fixado</h2>

exemplo de requisição<br>
<br>usando curl<br>
<code>curl http://127.0.0.1:5000/api/indicadores_mensal?anos=2016&anos=2020&categoria=categoria4&mes=maio</code>

<br>usando python<br>
<code>
import requests<br>
r = requests.get('http://127.0.0.1:5000/api/indicadores_mensal', params={ex_mes})
</code>
<br>
é retornado uma imagem quando é feito <b>GET</b> com sucesso
descrição das categorias<br>
<h2>Descrição de Categoria</h2>
{categorias_desc}
"""