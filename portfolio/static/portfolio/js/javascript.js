

document.addEventListener('DOMContentLoaded', function () {

    fetch('http://api.weatherstack.com/current?access_key=c3663b02189e9c099a84554bc6d7fc50&query=New%20York')
        .then(response => {
            return response.json()
        })
        .then(weatherData => {
            console.log(weatherData);
            let apiData = 'O tempo em ' + weatherData.location.region + ' é de ' + weatherData.current.temperature + '&#8451;.'; 
            document.getElementById('forecast').innerHTML=apiData;
        })


});

document.addEventListener('DOMContentLoaded', function () {

    const options = {
        method: 'GET',
        headers: {
            'X-RapidAPI-Host': 'random-words5.p.rapidapi.com',
            'X-RapidAPI-Key': 'ed1c1ef4b8msheec033fa498f060p18a1cfjsn00e4fc492429'
        }
    };

    fetch('https://random-words5.p.rapidapi.com/getMultipleRandom?count=5', options)
    .then(response => {
        return response.json()
    })
        .then(response => {
            console.log(response);
            var api = 'Carrega em F5 e várias palavras random irão aparecer a cada pedido &#128512; -> ' + response;
            document.getElementById('randomWords').innerHTML = api;
    })
    


});

document.addEventListener('DOMContentLoaded', function () {

const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Host': 'covid-19-tracking.p.rapidapi.com',
		'X-RapidAPI-Key': 'ed1c1ef4b8msheec033fa498f060p18a1cfjsn00e4fc492429'
	}
};

fetch('https://covid-19-tracking.p.rapidapi.com/v1/portugal', options)
	.then(response => {
        return response.json()
    })
        .then(response => {
            console.log(response);
            var covid = 'Ligação com a API do covid mostrando o País em questão: ' + response.Country_text;
            document.getElementById('covid').innerHTML = covid;
    })
    


});

document.addEventListener('DOMContentLoaded', function () {

    const options = {
        method: 'GET',
        headers: {
            'X-RapidAPI-Host': 'covid-193.p.rapidapi.com',
            'X-RapidAPI-Key': 'ed1c1ef4b8msheec033fa498f060p18a1cfjsn00e4fc492429'
        }
    };
    
    fetch('https://covid-193.p.rapidapi.com/countries', options)
        .then(response => {
            return response.json()
        })
            .then(response => {
                console.log(response);
                var covid1 = 'Ligação com a API do covid mostrando todos os países registados na base de dados da mesma até ao momento começados com a letra "Z": ' + response.response[233] + ' e ' + response.response[234] + '.';
                document.getElementById('covid_paises_registados').innerHTML = covid1;
        })
        
    
    
    });