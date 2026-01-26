package objetos;

public class Cubo {

	private int capacidad;
	int contenido;
	
	
	//constructor sin parametros
	Cubo() {
		capacidad=4;
		contenido=0;
	}
	//constructor con 2 parametros
	Cubo (int ca, int co){
		this.capacidad=ca;
		if (co>ca) contenido=ca;
		else
		this.contenido=co;
	}
	//constructor con 1 parametros
	Cubo (int ca){
			this.capacidad=ca;
		}
	
	void vaciar() {
		contenido=0;
	}
	void llenar() {
		contenido=capacidad;
	}
	void volcar(Cubo otro) {
		int espacio=otro.capacidad-otro.contenido;
		if (this.contenido <= espacio) {
			otro.contenido=otro.contenido+this.contenido;
			this.contenido=this.contenido-otro.contenido;
		}
	}
	
	
	public void pintaCubo() {
		System.out.println("Cubo con "+capacidad+" de capacidad y "+contenido+" de contenido");
	}
	
	public void dibujaCubo() {
		for (int i=1; i<=capacidad-contenido; i++) {
		System.out.println(i+"/ /");
		}
		for (int i=1; i<=contenido; i++) {
			System.out.println(i+"/~/");
		}
	}
	
	
	
	
	
	
	
	
	
	
	
}
