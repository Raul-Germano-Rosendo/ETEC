/*Editor de Dados Pessoais
 */
package datainsert;
import java.util.Scanner;

public class DataInsert {

    public static void main(String[] args) {
        String Cpf;
        String Birth;
        String Name;
        String State;
        String City;
        String Country;
        String Gender;
        
        
        Scanner data=new Scanner(System.in);
        
        
        System.out.println("Qual Informação deseja alterar?");
        System.out.println("Seu CPF; DIGITE 1");
        System.out.println("Sua Data de Nascimento; DIGITE 2");
        System.out.println("Seu Nome; DIGITE 3");
        System.out.println("Seu Gênero; DIGITE 4");
        System.out.println("Seu País; DIGITE 5");
        System.out.println("Seu Estado; DIGITE 6");
        System.out.println("Sua Cidade; DIGITE 7");
        System.out.println("Caso deseje ver suas Informações; DIGITE 8");
        
        int Resp;
        System.out.println("Digite o Número");
        Resp=data.nextInt();
                if (Resp==1){
                System.out.println("Digite o CPF; ");
                Cpf=data.next();
                }
                else if (Resp==2){
                    System.out.println("Digite sua Data de Nascimento; ");
                    Birth=data.next();
                }
                else if (Resp==3){
                    System.out.println("Digite seu Nome; ");
                    Name=data.next();
                }
                else if (Resp==4){
                    System.out.println("Digite seu Gênero; ");
                    Gender=data.next();
                }
                else if (Resp==5){
                    System.out.println("Digite seu País residente; ");
                    Country=data.next();
                }
                else if (Resp==6){
                    System.out.println("Digite seu Estado residente; ");
                    State=data.next();
                }
                else if (Resp==7){
                    System.out.println("Digite Sua Cidade residente; ");
                    City=data.next();
                }
                else {
                    System.out.println(Cpf, Birth, Name, Gender, Country, State, City);
                }
         
        
    }
    
}
