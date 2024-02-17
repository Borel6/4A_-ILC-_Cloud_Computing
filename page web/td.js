function addToScreen(value) {
    document.querySelector('.screen').innerText = value;
}

function clearScreen() {
    document.querySelector('.screen').innerText = '';
}

function calculate() {
    var expression = document.querySelector('.screen').innerText;
    var operator = expression.match(/[+\-*\/]/)[0]; // Récupère l'opérateur de l'expression
    var numbers = expression.split(operator); // Sépare les nombres à partir de l'opérateur
    var numA = parseFloat(numbers[0]); // Utilise parseFloat pour gérer les nombres décimaux
    var numB = parseFloat(numbers[1]);
    
    var url;
    switch (operator) {
        case '+':
            url = 'http://127.0.0.1:5000/api/add/' + numA + '/' + numB;
            break;
        case '-':
            url = 'http://127.0.0.1:5000/api/subs/' + numA + '/' + numB;
            break;
        case '*':
            url = 'http://127.0.0.1:5000/api/multi/' + numA + '/' + numB;
            break;
        case '/':
            url = 'http://127.0.0.1:5000/api/div/' + numA + '/' + numB;
            break;
    }

    fetch(url)
        .then(response => response.text())
        .then(result => {
            fetch('http://127.0.0.1:5000/result/' + result) // Récupère le résultat à partir de la route /result/
                .then(response => response.text())
                .then(finalResult => {
                    document.querySelector('.screen').innerText = finalResult; // Affiche le résultat dans le screen de la calculatrice
                });
        });
}
