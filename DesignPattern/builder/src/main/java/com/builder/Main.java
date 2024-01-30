package com.builder;

public class Main {
    public static void main(String[] args) {
        Burger burger = new Burger.BurgerBuilder()
                .setSize("Large")
                .setEgg(true)
                .setExtraCheese(true)
                .setOnions(false)
                .setMayonese(true)
                .build();
        System.out.println(burger.toString());

    }
}


