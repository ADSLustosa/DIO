import java.util.InputMismatchException;
import java.util.Locale;
import java.util.Scanner;


public class AboutMe {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in).useLocale(Locale.US);

        try{
        System.out.println("Digite seu nome: ");
        String nome = sc.next();

        System.out.println("Digite seu sobrenome: ");
        String sobrenome = sc.next();

        System.out.println("Digite sua idade: ");
        String idade = sc.next();

        System.out.println("Digite sua altura: ");
        String altura = sc.next();


        System.out.println("Olá, me chamo " + nome.toUpperCase() + ".");
        System.out.println("Tenho " + idade + " anos. ");
        System.out.println("Minha altura é " + altura + " cm. ");
        sc.close();
        }
        catch (InputMismatchException e) {
            System.err.println("Os campos idade e altura precisam ser númericos.");
        }

    }
}
