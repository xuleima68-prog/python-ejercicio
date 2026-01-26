package objetos;

import java.util.Scanner;

public class fabruca_coches {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	Scanner leer = new Scanner (System.in);
		
		coches cochecito1 = new coches(); //genero el objero perrete1 a partir de la calse Perro
		cochecito1.marca="Audi";
		cochecito1.modelo= "C-HR";
		cochecito1.kilometros = 1251;
		cochecito1.pintaCoches();
		
		
		
		coches cochecito2= new coches();
		cochecito2.marca="Toyota";
		cochecito2.modelo= "A3";
		cochecito2.kilometros = 24850;
		cochecito2.pintaCoches();
		
		
		
		
	}

}
