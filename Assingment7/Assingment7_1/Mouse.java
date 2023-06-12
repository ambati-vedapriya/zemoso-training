package com.Assingments.Assingment7.Assingment7_1;
public class Mouse extends Rodent {

	public Mouse() {
		System.out.println("I am Mouse Rodent");
		
	}

	@Override
	public void run() {
		System.out.println("Mouse is Started");
		
	}

	@Override
	public void close() {
		System.out.println("Mouse is Closed");
	}

}
