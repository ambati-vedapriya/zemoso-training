package com.Assingments.Assingment7.Assingment7_4;
public class BicycleFactory implements CycleFactory {

	@Override
	public Cycle getCycle() {
		return new Bicycle();
	}

}
