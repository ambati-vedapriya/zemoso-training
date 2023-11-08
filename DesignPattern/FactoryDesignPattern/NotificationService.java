public class NotificationService {
    public static void main(String[] args) throws IllegalAccessException {
        NotificationFactory notificationFactory = new NotificationFactory();
        Notification notification = notificationFactory.createNotification("EMAIL");
        notification.notifyUser();
    }
}
