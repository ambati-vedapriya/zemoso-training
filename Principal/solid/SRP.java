package Principal.solid;

 class Bird {
    private String name;
    private String color;

    public void setName(String name) {
        this.name = name;
        System.out.println("my name is :"+name);

    }

    public void setColor(String color) {
        this.color = color;
        System.out.println("my color is:"+color);
    }
}

 class Flight {
    public void fly(Bird bird) {
       System.out.println("i am flying bird");
    }
}


public class SRP {
     public static void main(String[] args){
         Bird obj= new Bird();
        obj.setName("parrot");
        obj.setColor("green");

     }
}
//Each class should have only one responsibility.
// For example, the Bird class should only be responsible for managing a bird's basic attributes,
// such as its name and color,
// while the Flight class should only be responsible for managing a bird's flight behavior.