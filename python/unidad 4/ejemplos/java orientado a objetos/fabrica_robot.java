package objetos;

public class fabrica_robot {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	
		
		
		
		Robot robot1= new Robot();
		robot1.pintaRobot();
		
		
		Robot robot2= new Robot();
		robot2.pintaRobot();
		
		
		System.out.println(robot1.pelea(robot2));//this es robot1 y el otro robot2 
		System.out.println(robot2.pelea(robot1));//this es robot2 y el otro robot1 
	}

}
