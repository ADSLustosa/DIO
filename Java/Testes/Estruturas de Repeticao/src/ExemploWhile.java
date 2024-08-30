import java.util.Random;

public class ExemploWhile {

    public static void main(String[] args) {
        
        double mesada = 50.0;

        while( mesada > 0) {
            Double valorDoce = valorAleatorio();
            
            if(valorDoce > mesada)
                valorDoce = mesada;
            
            mesada -= valorDoce;
            System.out.println("Doce do valor: " + valorDoce + "Adicionado no carrinho. Mesada restante: " + mesada);
            if (mesada == 0) {
                System.out.println("Joãozinho gastou toda a sua mesada em doces");
            }
    }
}

    public static double valorAleatorio(){
        Random random = new Random();
        return 1 + (random.nextDouble() *49);
    }
}
