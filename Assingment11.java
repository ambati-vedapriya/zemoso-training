/*Using TextFile and a Map<Character,Integer>,
create a program that takes the file name as a command line argument and counts the occurrence
of all the different characters. Save the results in a text file.
 */

package com.Assingments;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.*;
public class Assingment11 {

        public static void main(String[] args) throws IOException {
            if (args.length < 1)
            {
                System.out.println("No file is given as argument!!!!");
                System.exit(1);
            }

            Map<Character, Integer> dict = new HashMap<>();
            BufferedReader br=new BufferedReader(new FileReader(args[0]));
            int ch;
            while((ch=br.read())!=-1){
                char c=(char)ch;
                if(dict.containsKey(c)) {
                    int count = dict.get(c);
                    dict.put(c, count + 1);
                } else {
                    dict.put(c, 1);
                }
            }

            FileWriter writer = new FileWriter("new.txt");
            for (char c : dict.keySet()) {
                writer.write(c + " : " + dict.get(c) + "\n");
            }
            writer.close();
            br.close();
        }

    }


