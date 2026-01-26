package objetos;

import java.util.Scanner;

public class fabrica_perro {

	public static void main(String[] args) {
		
		Scanner leer = new Scanner (System.in);
		
		perro perrete1 = new perro(); //genero el objero perrete1 a partir de la calse Perro
		perrete1.raza="pitbull";
		perrete1.edad=4;
		perrete1.fuerza = 2;
		perrete1.pintaPerro();
		
		perrete1.ladrar();
		
		perro perrete2= new perro();
		perrete2.raza="chiwawa";
		perrete2.edad=2;
		perrete2.fuerza = 20;
		perrete2.pintaPerro();
		
		System.out.println(perrete1.pelea(perrete2));
	}
	
}
