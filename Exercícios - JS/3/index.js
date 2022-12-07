const carteira = [2, 10, 5, 10, 20, 2, 5, 100, 50, 50, 10, 50, 10, 5, 2, 10, 50, 2, 100, 200, 200, 10, 5, 2, 100, 5, 2, 20, 2, 10, 50, 100, 10, 5, 2, 20, 10, 5, 10, 50, 20, 200, 2, 10, 50, 5, 5, 5, 10, 10, 10, 2, 20, 50, 10, 100, 20, 2, 10, 5, 5, 10, 5, 10, 2, 10, 2, 10, 50, 10, 20, 50, 20, 2, 10, 5, 20, 10, 50, 10, 5, 2, 10, 20, 2, 10, 5, 50, 100, 50, 100, 2, 10, 20, 50, 2, 5,5, 10, 2]

//function soma() {
    //let soma = 0
    //for (let valor in carteira){
    //   soma += carteira[valor]
    //}
   // return soma
//}

//soma()
// console.log(soma(carteira))

// const media = soma() / carteira.length
// console.log(media)

qnt = 0
function notasDois(){
    for (let i = 0; i < carteira.length; i++){
        if (carteira[i] === 2){
            qnt += carteira[i]
        }
    } 
    console.log((qnt * 100 / 2628).toFixed(2) + "%")
}
notasDois()

qnt2 = 0
function notasDez(){
    for (let i = 0; i < carteira.length; i++){
        if (carteira[i] === 10){
            qnt2 += 1
        }
    } 
    console.log(((qnt2 / carteira.length)* 100).toFixed(0) + "%")
}
notasDez()

function removeDuzentos(){
    for (let i = 0; i < carteira.length; i++){
        if (carteira[i] === 200){
            carteira.splice(i, 1)
            return removeDuzentos(carteira)
        }
    }

    let soma = 0
    for (let valor in carteira){
       soma += carteira[valor]
    }
    console.log((soma / carteira.length).toFixed(2))
}
removeDuzentos()





//2628
//2028



