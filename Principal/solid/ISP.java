package Principal.solid;
interface Flyable {
    void fly();
}

 interface Swimmable {
    void swim();
}

 class Parrot implements Flyable {
     @Override
     public void fly() {
         System.out.println("i can fly");

     }
     // ...
}

 class Penguin implements Swimmable {
     @Override
     public void swim() {
         System.out.println("i can swim");

     }

}


public class ISP {
    public static void main(String[] args){
        Parrot pr=new Parrot();
        pr.fly();
        Penguin pe =new Penguin();
        pe.swim();
    }
}
//Clients should only depend on the interfaces that they actually use.
// For example, the Bird class can implement a Flyable interface that defines methods for flight,
// while the Swimmable interface can define methods for swimming.