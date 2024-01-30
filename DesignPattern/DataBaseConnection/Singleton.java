package DataBaseConnection;

public class Singleton {
    private static Singleton singleton_instance = null;
    private Singleton(){
        connection();
    }

    public static Singleton getInstance(){
        if(singleton_instance == null){
            singleton_instance = new Singleton();
        }
        return singleton_instance;
    }

    public void connection(){
        System.out.println("connection to database");
    }

    public static void main(String[] args) {
        Singleton s1;
        s1 = Singleton.getInstance();
    }

}
