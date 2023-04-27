package Principal.solid;
interface Feather {
    String getColor();
}

 class DownFeather implements Feather {
    @Override
    public String getColor() {
        return "white";
    }
}

 class FlightFeather implements Feather {
    @Override
    public String getColor() {
        return "brown";
    }
}


public class OCP {
    public static void main(String[] args){
        DownFeather df=new DownFeather();
        System.out.println(df.getColor());
        FlightFeather ff=new FlightFeather();
        System.out.println(ff.getColor());

    }
}
//Classes should be open for extension but closed for modification.
// For example, we can create an Feather interface that can be implemented by different types of feathers.