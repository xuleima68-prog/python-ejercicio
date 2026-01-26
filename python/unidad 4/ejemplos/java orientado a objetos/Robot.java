package objetos;

public class Robot {
	String nombre;
	int fuerza;
	boolean encendido;
	int energia;
	
	//constructor
	Robot () {
		//Valores por defecto
		nombre = "no tiene";
		fuerza = (int) (Math.random() * 10);
	}
	
	public void saluda() {
		if (encendido) {
	System.out.println("Hola me llamo "+ nombre);
		}
		else {
			System.out.println("ERROR");
		}
	}
	public void encender() {
		if (!encendido) {
			encendido=true;
			System.out.println("esta encendido");
		}
	}
	
	public int pelea(Robot otro){
		int resultado = 0;
	
	if (encendido) {
		if (this.fuerza > otro.fuerza) {
			this.energia=this.energia+otro.energia;
			//otro.energia=otro.energia-this.energia; le quitaria la energia
			resultado = 1;
			}
		else if 
		(this.fuerza < otro.energia) {
			this.energia=this.energia+otro.energia;
			resultado =  -1;
		}
		else resultado = 0;
	}else {
		System.out.println("error");
		resultado = -5;
	}
	return resultado;
	}
		
	
	public void pintaRobot() {
		
			System.out.println("Robot con nombre "+ nombre +" con fuerza "+fuerza+ " energia "+ energia);
	}
	
	public int sumar(int num1, int num2) {
		return (num1+num2);
		
	}
	
	public int peleaEnergia(Robot otro) {
		if (this.fuerza > otro.fuerza) {
			return 1;
		}
		else if (this.fuerza < otro.fuerza) {
			return -1;
		}
		else  return 0;
	}
	
	
	}
	
	
	

