function inicio(){
    document.querySelectorAll('main article section')[0].style.display = "block"
    document.querySelectorAll('main article section')[1].style.display = "none"
    document.querySelectorAll('main article section')[2].style.display = "none"
    document.getElementById('conectado').style.display = "none"
}

function home(){
    document.querySelectorAll('main article section')[0].style.display = "block"
    document.querySelectorAll('main article section')[1].style.display = "none"
    document.querySelectorAll('main article section')[2].style.display = "none"
}

function login(){
    document.querySelectorAll('main article section')[0].style.display = "none"
    document.querySelectorAll('main article section')[1].style.display = "block"
    document.querySelectorAll('main article section')[2].style.display = "none"
}

function cadastro(){
    document.querySelectorAll('main article section')[0].style.display = "none"
    document.querySelectorAll('main article section')[1].style.display = "none"
    document.querySelectorAll('main article section')[2].style.display = "block"
}

function entrar(){
    var login = document.getElementsByName('txtLogin')[0].value 
    var senha = document.getElementsByName('txtSenha')[0].value 
    document.querySelector('main #conectado span').innerText = login
    document.querySelector('main #conectado span').style.fontSize = "25px"
    document.querySelector('main #conectado span').style.color = "green"
    document.querySelectorAll('main article')[0].style.display = "none"
    document.getElementById('conectado').style.display = "block"
}

function cadastrar(){
    var email = document.getElementsByName('txtEmail')[0].value 
    document.querySelector('main #conectado span').innerText = email
    document.querySelector('main #conectado span').style.fontSize = "25px"
    document.querySelector('main #conectado span').style.color = "green"
    document.querySelectorAll('main article')[0].style.display = "none"
    document.getElementById('conectado').style.display = "block"
}