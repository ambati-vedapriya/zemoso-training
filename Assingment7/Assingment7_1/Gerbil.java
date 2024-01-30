package com.Assingments.Assingment7.Assingment7_1;

public class Gerbil extends Rodent {

	public Gerbil() {
		System.out.println("I am Gerbil Rodent");
		
	}

	@Override
	public void run() {
		System.out.println("Gerbil is Started");
		
	}

	@Override
	public void close() {
		System.out.println("Gerbil is Closed");
	}


}
