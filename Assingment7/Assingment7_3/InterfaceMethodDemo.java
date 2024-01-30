/*Create three interfaces, each with two methods.
Inherit a new interface that combines the three, adding a new method.
Create a class by implementing the new interface and also inheriting from a concrete class.
Now write four methods, each of which takes one of the four interfaces as an argument.
In main( ), create an object of your class and pass it to each of the methods.
 */

package com.Assingments.Assingment7.Assingment7_3;
public class InterfaceMethodDemo {

	public static void main(String[] args) {
		CombinedClass combinedClass=new CombinedClass();
		InterfaceMethods interfaceMethods=new InterfaceMethods();
		
		interfaceMethods.InterfaceMethod1(combinedClass);
		interfaceMethods.InterfaceMethod2(combinedClass);
		interfaceMethods.InterfaceMethod3(combinedClass);
		interfaceMethods.InterfaceMethod4(combinedClass);
		combinedClass.concreteMethod();
	}

}
