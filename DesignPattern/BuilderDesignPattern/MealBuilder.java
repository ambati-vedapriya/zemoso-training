public abstract class MealBuilder {
    public abstract void addBriyani();
    public  abstract  void  addBread();
    public abstract void  addColdDrink();
    public abstract void addCurry();
    public abstract Meal build();

    @Override
    public String toString() {
        return "Meal Builder: " + this.getClass().getSimpleName();
    }
}
