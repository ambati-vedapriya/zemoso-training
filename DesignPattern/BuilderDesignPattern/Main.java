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

        Meal meal = new MealDirector(new VegMealBuilder()).prepareMeal();

        System.out.println(meal);

        MealDirector mealDirector = new MealDirector(new NonVegMealBuilder());

        Meal nonVegMeal = mealDirector.prepareMeal();

        System.out.println(nonVegMeal.toString());
    }
    }


