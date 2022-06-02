

document.addEventListener('DOMContentLoaded', function () {

    fetch('http://api.weatherstack.com/current?access_key=c3663b02189e9c099a84554bc6d7fc50&query=New%20York')
        .then(response => {
            return response.json()
        })
        .then(weatherData => {
            console.log(weatherData);
            let apiData = 'O tempo em ' + weatherData.location.region + ' é de ' + weatherData.current.temperature; 
            document.getElementById('forecast').innerHTML=apiData;
        })


});



