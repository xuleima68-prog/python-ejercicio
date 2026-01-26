package objetos;

public class fabrica_cubo {
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	Cubo cubo1=new Cubo(2,1);
	cubo1.pintaCubo();
	cubo1.dibujaCubo();
	
	
	Cubo cubo2= new Cubo(3,0);
	cubo2.pintaCubo();
	cubo2.dibujaCubo();
	
	
	
	cubo1.volcar(cubo2);
	
	cubo1.pintaCubo();
	cubo1.dibujaCubo();
	cubo2.pintaCubo();
	cubo2.dibujaCubo();
	
	}
}
