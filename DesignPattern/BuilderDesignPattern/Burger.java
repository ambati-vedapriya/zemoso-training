public class Burger {

    private String size;
    private boolean egg;
    private boolean extraCheese;
    private boolean onions;
    private boolean mayonese;

    private Burger(BurgerBuilder burgerBuilder){
        this.size = burgerBuilder.size;
        this.egg = burgerBuilder.egg;
        this.extraCheese = burgerBuilder.extraCheese;
        this.onions = burgerBuilder.onions;
        this.mayonese = burgerBuilder.mayonese;
    }//constrouctor -intialize all fields

    public boolean isEgg() {
        return egg;
    }

    public String getSize() {
        return size;
    }

    public boolean isExtraCheese() {
        return extraCheese;
    }

    public boolean isOnions() {
        return onions;
    }

    public boolean isMayonese() {
        return mayonese;
    }

    @Override
    public String toString() {
        return this.size + " ; " + this.egg + " ; " + this.onions + " ; " + this.mayonese + " ; " + this.extraCheese;
    }
//Return same object everytime
    public static class BurgerBuilder{
        private String size;
        private boolean egg;
        private boolean extraCheese;
        private boolean onions;
        private boolean mayonese;

        public BurgerBuilder setSize(String size) {
            this.size = size;
            return this;
        }

        public BurgerBuilder setEgg(boolean egg) {
            this.egg = egg;
            return this;
        }

        public BurgerBuilder setExtraCheese(boolean extraCheese) {
            this.extraCheese = extraCheese;
            return this;
        }

        public BurgerBuilder setOnions(boolean onions) {
            this.onions = onions;
            return this;
        }

        public BurgerBuilder setMayonese(boolean mayonese) {
            this.mayonese = mayonese;
            return this;
        }

        public Burger build(){
            return new Burger(this);
        }

    }
}
