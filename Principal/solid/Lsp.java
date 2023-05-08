package Principal.solid;

class Birds{
    public void info(){
        System.out.println("i am bird");
    }
    /*public void fly(){
        System.out.println("i am flying");
    }*/
}
class FlyingBird extends Birds{
    public void fly(){
        System.out.println("i am flying");
    }

}
class Sparrow extends FlyingBird{
    public void name(){
        System.out.println("i am parrot");
    }

}
class Ostrich extends Birds{
    public void name(){
        System.out.println("i am Ostrich");
    }

}



public class Lsp {
    public static void main(String[] args){
        Ostrich o=new Ostrich();
        o.info();

    }
}
//Subclasses should be able to be used in place of their parent classes
// without affecting the correctness of the program.
