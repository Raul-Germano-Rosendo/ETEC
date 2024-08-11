/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exercicio2808;

/**
 *
 * @author Aluno
 */
public class Exercicio2808 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int [] numeros = {15,15,46,43,100,14,85,49,75,46};
        int [] numeros2 = new int[10];
        int soma = 0;
        int media= numeros.length;
        int maior=0;
        int menor=0;
        for(int i =0; i <numeros.length; i+=1){
            System.out.println(numeros[i]);
            soma = soma + numeros[i];
            
            
        }
        
        System.out.println("A SOMA É " + soma);
            
        media =soma / media;
        System.out.println("A MÉDIA É " + media);
        System.out.println("o maior É " +  );
        
    }
    
}
