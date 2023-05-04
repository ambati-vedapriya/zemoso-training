/*Write a java function that checks if the input string contains all the letters of the alphabet a-z (case-insensitive).
 Write time and space complexity of your solution as comments in the source file.
 */

package com.Assingments;
import java.util.*;
public class Assingment2 {
    public static boolean containsAllLetters(String str) {
        boolean[] alphabet = new boolean[26]; // Space complexity: O(1)
        str = str.toLowerCase(); // Time complexity: O(n)
        for (int i = 0; i < str.length(); i++) { // Time complexity: O(n)
            char letter = str.charAt(i);
            if (letter >= 'a' && letter <= 'z') {
                alphabet[letter - 'a'] = true;
            }
        }
        for (boolean b : alphabet) { // Time complexity: O(1)
            if (!b) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println("Enter the para");
        Scanner sc=new Scanner(System.in);
        String para=sc.nextLine();


        System.out.println(containsAllLetters(para));


    }


}
