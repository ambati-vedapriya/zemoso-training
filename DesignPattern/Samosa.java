public class Samosa {

    private static Samosa samosa;
    //constructor
    private Samosa(){

    }

    //Lazy way of creating singleton object
   /* public static Samosa getSamosa(){
       if(samosa == null){
           samosa = new Samosa();
       }
        return samosa;
    }*/
    //method synchronization
    /*public synchronized static Samosa getSamosa(){
        if(samosa == null){
            samosa = new Samosa();
        }
        return samosa;
    }*/

    //block synchronization

    public static Samosa getSamosa(){
        if(samosa == null){
            synchronized (Samosa.class){
                if(samosa == null)
                samosa = new Samosa();
            }
        }
        return samosa;
    }

}
