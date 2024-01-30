package com.Assingments.Assingments5.Data;

public class Data {
    private int num;
        private char alpha;

        public void printVariables(){
            System.out.println("Integer:-" + num);
            System.out.println("Character:-" + alpha);

        }

        public void printLocalVariables(){
            int myInt;
            char myChar;
            //System.out.println("myInt " + myInt);   giving error because these are not initialized
           // System.out.println("myChar " + myChar);
        }


    public static void main(String[] args) {
        Data myData = new Data();
        myData.printVariables();
    }
}



