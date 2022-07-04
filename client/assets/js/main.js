
function updateGraphic() {
    const dataDe = document.querySelector("#date-de").value
    const dataAte = document.querySelector("#date-ate").value
    const lista_categoria = document.querySelectorAll('.form-check-input')

    const anoDeInt = parseInt(dataDe.split("-")[0]);
    const anoAteInt = parseInt(dataAte.split("-")[0]);
    if (anoAteInt - anoDeInt < 1) {
        alert('O tempo mínimo não pode ser menor que um ano!')
    }
    else {
        let anos = `anos=${anoDeInt}&anos=${anoAteInt}`
        console.log(anos)
        let categorias = ''
    
        for (item of lista_categoria) {
            if (item.checked)
                categorias += item["attributes"][2]["nodeValue"] + "&"
        }
    
    
        let url = `https://indicadoresrs.herokuapp.com/api/indicadores_anual?${anos}&categoria=${categorias}`;
        console.log(url)
    
        fetch(url)
            .then(image => image.blob())
            .then(imageBlob => document.querySelector("#plot-graphic").src = URL.createObjectURL(imageBlob))
    }

    //document.querySelector("#plot-graphic").src = "http://127.0.0.1:5000/api/indicadores_anual?anos=2015&anos=2016&anos=2017&categoria=categoria2";
}

// setInterval(function() {
//     document.querySelector("#plot-graphic").src = "http://127.0.0.1:5000/api/indicadores_anual?anos=2015&anos=2016&anos=2017&categoria=categoria2";
// }, 5000)
