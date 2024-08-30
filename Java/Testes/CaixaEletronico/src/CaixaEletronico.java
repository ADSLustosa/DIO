public class CaixaEletronico {
    public static void main(String[] args) throws Exception {

        // Exemplo Condicional Simples.
        double saldo = 25.0;
        double valorSolicitado = 26.0;

        if(valorSolicitado < saldo)
        saldo = saldo - valorSolicitado;

        System.out.println(saldo);
    }

}
