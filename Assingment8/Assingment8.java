/*Error Handling

Create three new types of exceptions. Write a class with a method that throws all three.
 In main( ), call the method but only use a single catch clause that will catch all three types of exceptions.
 Add a finally clause and verify that your finally clause is executed, even if a NullPointerException is thrown.
 */


package com.Assingments.Assingment8;

public class Assingment8 {
        public static void main(String[] args) {
            CustomExceptionDemo obj=new CustomExceptionDemo();
            try {
                obj.CustomMethod();
            }
            catch (Exception e) {
                System.out.println(e.getMessage());
            }
            finally {
                System.out.println("Successfully Executed");
            }

        }

    }


