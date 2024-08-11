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
public class Aluno {
    private String nome;
    private int semestre;
    private String materia;
    private int presenca_Porcentagem;
    private int nota;

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getSemestre() {
        return semestre;
    }

    public void setSemestre(int semestre) {
        this.semestre = semestre;
    }

    public String getMateria() {
        return materia;
    }

    public void setMateria(String materia) {
        this.materia = materia;
    }

    public int getPresenca_Porcentagem() {
        return presenca_Porcentagem;
    }

    public void setPresenca_Porcentagem(int presenca_Porcentagem) {
        this.presenca_Porcentagem = presenca_Porcentagem;
    }

    public int getNota() {
        return nota;
    }

    public void setNota(int nota) {
        this.nota = nota;
    }
    
}

