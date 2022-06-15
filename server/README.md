Repositório referente aos programas que faz a leitura dos indicadores.xlsx, para que seja feito 
um breve levamento dos **Indices Criminais** demonstrando visualmente através de gráficos.

Arquivo
```indices_criminais.py```
Possui uma classe principal chamada **Indicadores**, onde possui os métodos responsáveis que realizam o levamento
de indices

- os métodos: 



  ```...get_indicador(coluna, anos=[])```
---

Parâmetros

--- 

**coluna** obrigatório, representa o indicador que queremos que seja feito o levamento através de todos os anos

---
**anos** opcional, representa uma lista de anos a serem passadas, quando informada no método,
será feito o levamento do indicador apenas pelos anos informados através da lista, EX: ```...get_indicador(..., anos=["2012","2015","2021"])```, 
por padrão é feito por todos os anos.

---

Após ser concluído a execução do método, vai ter uma pasta "indicadores_graficos" com arquivos no formato png 
que possui os gráficos referente a cada consulta de indices criminais.
