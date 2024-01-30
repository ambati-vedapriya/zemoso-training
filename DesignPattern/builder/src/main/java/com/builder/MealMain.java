package com.builder;

public class MealMain {
    public static void main(String[] args) {
        Meal meal = new MealDirector(new VegMealBuilder()).prepareMeal();

        System.out.println(meal);

        MealDirector mealDirector = new MealDirector(new NonVegMealBuilder());

        Meal nonVegMeal = mealDirector.prepareMeal();

        System.out.println(nonVegMeal.toString());
    }
}
