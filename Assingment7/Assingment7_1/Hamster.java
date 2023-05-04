package com.Assingments.Assingment7.Assingment7_1;
public class Hamster extends Rodent {

	public Hamster() {
		System.out.println("I am Hamster Rodent");
		
	}

	@Override
	public void run() {
		System.out.println("Hamster is Started");
		
	}

	@Override
	public void close() {
		System.out.println("Hamster is Closed");
	}


}
