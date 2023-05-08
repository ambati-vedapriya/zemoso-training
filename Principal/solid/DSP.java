package Principal.solid;
 interface Feathers {
    String getColor();
}

 class DownFeathers implements Feathers {
    @Override
    public String getColor() {
        return "white";
    }
}

 class FlightFeathers implements Feathers {
    @Override
    public String getColor() {
        return "brown";
    }
}
 class BirdFeather {
    private Feathers feather;

    public BirdFeather(Feathers feather) {
        this.feather = feather;
    }

    public String getFeatherColor() {
        return feather.getColor();
    }
}

public class DSP {
    public static void main(String[] args) {
        DownFeathers downFeather = new DownFeathers();
        BirdFeather bird = new BirdFeather(downFeather);
        String featherColor = bird.getFeatherColor();
        System.out.println(featherColor);

        FlightFeathers flightFeather = new FlightFeathers();
        BirdFeather bird1 = new BirdFeather(flightFeather);
        featherColor = bird1.getFeatherColor();
        System.out.println(featherColor);

    }
}
   // the Bird class depends on the Feather interface, which is an abstraction,
// rather than a specific implementation of the Feather class.
// This allows us to easily swap out different feather implementations without modifying the Bird class.