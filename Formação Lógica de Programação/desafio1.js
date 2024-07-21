// DESAFIO 1- Classificador de Nível de Herói

const nomeDoHeroi = "MrCaranguejo";

let xp = 9500;
let nível = "";

switch(true) {
    case xp <= 1000:
    nível = " Ferro";
    break;
    
    case xp >= 1001 && xp <= 2000:
    nível = " Bronze";
        break;

    case xp >= 2001 && xp <= 5000:
    nível = " Prata";
    break;

    case xp >= 5001 && xp <= 7000:
    nível = " Ouro";
    break;

    case xp >= 7001 && xp <= 8000:
    nível = " Platina";
    break;

    case xp >= 8001 && xp <= 9000:
    nível = " Ascendente";
    break;
    
    case xp >= 9001 && xp <= 10000:
    nível = " Imortal";
    break;

    case xp >= 10001:
    nível = " Radiante";
    break;
}

console.log `O Herói de nome ${nomeDoHeroi} está no nível de ${nível}`