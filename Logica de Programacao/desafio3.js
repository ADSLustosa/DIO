// DESAFIO 3- Escrevendo as classes de um jogo

class Heroi {
    constructor(nome, idade, tipo) {
        this.nome = nome;
        this.idade = idade;
        this.tipo = tipo;
    }


atacar() {
    let ataque;
    switch (this.tipo) {
        case 'mago':
            ataque = 'usou magia';
            break;
        case 'guerreiro':
            ataque = 'usou espada';
            break;
        case 'monge':
            ataque = 'usou artes marciais';
            break;
        case 'ninja':
            ataque = 'usou shuriken';
            break;
        default:
            ataque = 'usou ataque básico';
    }
    console.log(`O ${this.tipo} ${this.nome} atacou usando ${ataque}`);
    }

}

const heroi1 =new Heroi('Kenshi', 30, 'guerreiro');
const heroi2 =new Heroi('Quan Chi', 70, 'mago');
const heroi3 =new Heroi('Retsu', 85, 'monge');
const heroi4 =new Heroi('Scorpion', 20, 'ninja');

heroi1.atacar();
heroi2.atacar();
heroi3.atacar();
heroi4.atacar();