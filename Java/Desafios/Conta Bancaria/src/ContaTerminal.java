import java.util.Scanner; // Importa a biblioteca Scanner para Entrada de valores.
import java.util.InputMismatchException; // Validação de Entrada. Caso a Entrada não seja do tipo esperado é aplicado a exceção "Entrada Inválida".
import java.text.DecimalFormat; // Importa a formatação de texto que adiciona vírgula às casas decimais.

public class ContaTerminal {

    //CONSTANTE- Mensagem de boas-vindas.
    private static final String MENSAGEM_BOAS_VINDAS = "Olá, %s! Obrigado por criar uma conta no Tiger Bank. O número da sua agência é %s, a sua conta é a %d e seu saldo disponível é de R$%s";

    public static void main(String [] args){

        // Scanner recebe a Entrada do Usuário.
        Scanner sc = new Scanner(System.in);

        // Exceção de validação de Entrada.
        try{
            int numero = solicitarNumeroConta(sc); // Solicita o número da Conta ao Usuário.
            String agencia = solicitarAgencia(sc); // Solicita o número da Agência ao Usuário.
            String nomeCliente = solicitarNomeCliente(sc); // Solicita o nome do Cliente ao Usuário.
            double saldo = solicitarSaldo(sc); // Solicita o saldo da conta ao Usuário.
            exibirMensagemBoasVindas(nomeCliente, agencia, numero, saldo); // Exibi a mensagem final com os dados formatados.
        }
        catch (InputMismatchException e){
            // Exibi a mensagem de invalidez da Entrada.
            System.out.println("Erro: Entrada inválida. Por favor, insira dos dados corretamente.");
        }
        finally {
            // Fecha o scanner para liberar recursos.
            sc.close();
        }
    }

    
    /**
     * Solicita o número da conta ao Usuário.
     * @param scanner Objeto Scanner para leitura da Entrada do usuário.
     * @return Número da conta fornecido pelo usuário.
    */
    private static int solicitarNumeroConta(Scanner scanner) {

        System.out.println("Por favor, digite o número da Conta: ");
        return scanner.nextInt();
    }


    /**
     * Solicita o número da agência ao usuário e formata com um hífen antes do último dígito.
     *
     * @param scanner Objeto Scanner para leitura da entrada do usuário.
     * @return Número da agência formatado.
     */
    private static String solicitarAgencia(Scanner scanner) {
        System.out.println("Por favor, digite o número da Agência: ");
        String agencia = scanner.next();
        int length = agencia.length();
        return agencia.substring(0, length - 1) + "-" + agencia.charAt(length - 1);
    }


    /**
     * Solicita o nome do cliente ao usuário.
     *
     * @param scanner Objeto Scanner para leitura da entrada do usuário.
     * @return Nome do cliente fornecido pelo usuário.
     */
    private static String solicitarNomeCliente(Scanner scanner) {
        scanner.nextLine();
        System.out.println("Por favor, digite o nome do Cliente: ");
        return scanner.nextLine();
    }


    /**
     * Solicita o saldo da conta ao usuário.
     * @param scanner Objeto Scanner para leitura da entrada do usuário.
     * @return Saldo da conta fornecido pelo usuário.
     */
    private static double solicitarSaldo(Scanner scanner) {
        System.out.println("Por favor, digite o saldo da conta: ");
        return scanner.nextDouble();
    }



    /**
     * Exibe a mensagem de boas-vindas ao usuário com os dados da conta formatados.
     * @param nomeCliente Nome do cliente.
     * @param agencia Número da agência formatado.
     * @param numero Número da conta.
     * @param saldo Saldo da conta.
     */

    private static void exibirMensagemBoasVindas(String nomeCliente, String agencia, int numero, double saldo) {

        // Cria um objeto DecimalFormat para formatar o saldo com separador de milhares e duas casas decimais.
        DecimalFormat decimalFormat = new DecimalFormat("#,##0.00");
        String saldoFormatado = decimalFormat.format(saldo);

        // Imprimir mensagem de boas-vindas com os dados do usuário.
        String mensagem = String.format(MENSAGEM_BOAS_VINDAS, nomeCliente, agencia, numero, saldoFormatado);
        System.out.println(mensagem);
    }
}