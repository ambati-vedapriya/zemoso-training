public class EmailNotification implements Notification{
    @Override
    public void notifyUser() {
        System.out.println("sending an e-mail notification");
    }
}
