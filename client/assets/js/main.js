function updateGraphic() {
    document.querySelector("#plot-graphic").src = "http://127.0.0.1:5000/api/indicadores_anual?anos=2015&anos=2016&anos=2017&categoria=categoria2";
}

// setInterval(function() {
//     document.querySelector("#plot-graphic").src = "http://127.0.0.1:5000/api/indicadores_anual?anos=2015&anos=2016&anos=2017&categoria=categoria2";
// }, 5000)