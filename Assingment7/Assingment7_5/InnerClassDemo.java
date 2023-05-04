/*Create a class with an inner class that has a non-default constructor (one that takes arguments).
Create a second class with an inner class that inherits from the first inner class.
 */

package com.Assingments.Assingment7.Assingment7_5;

public class InnerClassDemo {

	public static void main(String[] args) {
		SubClass subClass=new SubClass(5);
		SubClass.SubInnerClass subInnerClass=subClass.new SubInnerClass(10);
		System.out.println("OuterClass Value:"+subClass.x);
		System.out.println("InnerClass Value:"+subInnerClass.y);
	}

}
