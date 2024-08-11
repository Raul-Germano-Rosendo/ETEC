/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exercicio1_raul;

/**
 *
 * @author Aluno
 */
public class Pessoa {
    private String nome;
    private String Cidade_Natal;
    private int data_nasc;
    private int cpf;
    private int rg;

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCidade_Natal() {
        return Cidade_Natal;
    }

    public void setCidade_Natal(String Cidade_Natal) {
        this.Cidade_Natal = Cidade_Natal;
    }

    public int getData_nasc() {
        return data_nasc;
    }

    public void setData_nasc(int data_nasc) {
        this.data_nasc = data_nasc;
    }

    public int getCpf() {
        return cpf;
    }

    public void setCpf(int cpf) {
        this.cpf = cpf;
    }

    public int getRg() {
        return rg;
    }

    public void setRg(int rg) {
        this.rg = rg;
    }
    
}
