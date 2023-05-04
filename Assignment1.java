/*Create a java program to search through the home directory and look for files that match a regular expression.
The program should be able to take inputs repeatedly and should print out the full absolute path of the matching files found.

Provide appropriate documentation and comments on your code.*/

package com.Assingments;

import java.io.File;
import java.util.Scanner;
public class Assignment1 {

    public static void main(String[] args) {
        File directory = new File("C:\\Users");
        Scanner sc = new Scanner(System.in);
        String s;
        while(true)
        {
            boolean flag= false;
            System.out.println("Enter File Name");
            s =sc.nextLine();
            String[] files = directory.list();
            for (String file : files){
                if (s.equals(file)){
                    flag = true;
                    System.out.println("File found!");
                    System.out.println(file);
                    System.out.println("AbsoluteFilePath : "+ directory.getAbsolutePath());
                }
            }
            if(!flag)
            {
                System.out.println("File not found");
            }
        }

    }
}



