/*Create a class with two (overloaded) constructors. Using this, call the second constructor inside the first one.*/


package com.Assingments.Assingment6;
public class Assignment6_2 {
    private int x;
    private int y;

    // First constructor
    public Assignment6_2(int x) {
        this.x = x;
        this.y = 0;
        System.out.println("First constructor called");
    }

    // Second constructor
    public Assignment6_2(int x, int y) {
        this(x);
        this.y = y;
        System.out.println("Second constructor called");
    }

    // Getter methods
    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }


    public static void main(String[] args) {
        Assignment6_2 obj1 = new Assignment6_2(10);
        System.out.println("x = " + obj1.getX() + ", y = " + obj1.getY());

        Assignment6_2 obj2 = new Assignment6_2(20, 30);
        System.out.println("x = " + obj2.getX() + ", y = " + obj2.getY());
    }
}


