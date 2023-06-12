package com.Assingments.Assingment8;

public class CustomExceptionDemo {


        public void CustomMethod() throws CustomException1, CustomException2, CustomException3 {
            int n = (int) (Math.random() * 3) + 1;
            if (n == 1) {
                throw new CustomException1("CustomException1");
            }
            else if (n == 2) {
                throw new CustomException2("CustomException2");
            }
            else {
                throw new CustomException3("CustomException3");
            }
        }
    }


