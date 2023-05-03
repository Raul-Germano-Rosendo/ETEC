/*
 */
package exemploobjeto;

public class Exemploobjeto {

    public static void main(String[] args) {
        Pessoa x=new Pessoa("Raul","Caçapava","12992480557");
        System.out.println("Seu Nome: "+x.getNome());
        x.setNome("Maria");
        System.out.println("Seu Nome: "+x.getNome());
    }
    
}
