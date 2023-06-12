/* Create a Cycle interface, with implementations Unicycle, Bicycle and Tricycle.
Create factories for each type of Cycle, and code that uses these factories.
 */

package com.Assingments.Assingment7.Assingment7_4;
public class CycleFactoryDemo {

	public static void main(String[] args) {
		Cycle cycle;
		CycleFactory cycleFactory;
		cycleFactory=new UnicycleFactory();
		cycle = cycleFactory.getCycle();
		cycle.display();
		
		cycleFactory=new BicycleFactory();
		cycle = cycleFactory.getCycle();
		cycle.display();
		
		cycleFactory=new TricycleFactory();
		cycle = cycleFactory.getCycle();
		cycle.display();
		
	}

}
