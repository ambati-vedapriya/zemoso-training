package com.Assingments.Assingment7.Assingment7_4;
public class UnicycleFactory implements CycleFactory {

	@Override
	public Cycle getCycle() {
		return new Unicycle();
	}

}
