// DESAFIO 2- Calculadora de Partidas Rankeadas

let vitorias = 1000;

function saldoVitorias() {
    let nivel;
    switch (true) {
        case (vitorias < 10):
            nivel = "Ferro";
            break;
        case (vitorias >= 11 && vitorias <= 20):
            nivel = "Bronze";
            break;
        case (vitorias >= 21 && vitorias <= 50):
            nivel = "Prata";
            break;
        case (vitorias >= 51 && vitorias <= 80):
            nivel = "Ouro";
            break;
        case (vitorias >= 81 && vitorias <= 90):
            nivel = "Diamante";
            break;
        case (vitorias >= 91 && vitorias <= 100):
            nivel = "Lendário";
            break;
        case (vitorias > 100):
            nivel = "Imortal";
            break;
        default:
            nivel = "Nível Desconhecido";
    }
    console.log(`O Herói tem de saldo de ${vitorias} está no nível de ${nivel}`);
}

saldoVitorias();
