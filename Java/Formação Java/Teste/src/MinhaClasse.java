import java.util.Scanner;

public class MinhaClasse {

    public static void main(String[] args){
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Digite o primeiro número: ");
            int numero1 = scanner.nextInt();
            System.out.println("Digite o segundo número: ");
            int numero2 = scanner.nextInt();
            int soma = soma(numero1, numero2);
            System.out.println("A soma de "  + numero1 + " + " + numero2 + " é: " + soma);
        }
    }

    public static int soma(int numero1, int numero2){
        return numero1+numero2;
    }

}