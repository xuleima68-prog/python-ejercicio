package objetos;

public class perro { //la calse perro es la plantilla
//atributos
	String raza;
	int edad;
	int fuerza;
	
	
	//metodos
	public void ladrar() { //no tiene parametro 
		System.out.println("Guau Guau");
	}
	
	public void comer(String comida) { //tiene un parametro de tipo string+
		
		//cuando la comida sea carne se lo come
		if (comida.equals("carne")){
			System.out.println("ñam ñam que rica la carne");
			
		}
		else System.out.println("no quiero comer eso");
	}
	
	//este metodo devuelve 1 si gano, -1 si pierdo y 0 si empato
		public int pelea(perro otro) {
		if (this.fuerza > otro.fuerza) {
			return 1; 
		}
		else if (this.fuerza < otro.fuerza) {
			return -1;
		}
		else return 0;
	}
		
	
		//cuando es otra cosa no lo quiere
		public void pintaPerro() {
			System.out.println("Perro con raza "+raza+" y edad "+edad+" años y fueza "+fuerza);
		}
		
	}

