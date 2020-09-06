var nome = JSON.parse(document.getElementById('nome').textContent);
var valor = JSON.parse(document.getElementById('valor').textContent);
var originalContents = document.body.innerHTML;

function printIt() {
    document.body.innerHTML = "nome do vinho: " + nome + " Valor: " + valor;
    window.print();
    document.body.innerHTML = originalContents
    window.location.replace("http://127.0.0.1:8000/");
  }