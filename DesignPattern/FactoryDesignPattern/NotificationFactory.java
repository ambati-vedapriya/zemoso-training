public class NotificationFactory {
    public static Notification createNotification(String channel) throws IllegalAccessException {
        if(channel == null  || channel.isEmpty())
            throw new IllegalAccessException("unknown channel");
        switch (channel){
            case "SMS" :
                return new SMSNotification();
            case "EMAIL" :
                return new EmailNotification();
            case "PUSH NOTIFY" :
                return new PushNotification();
            default:
                throw new IllegalAccessException("Unknown channel " + channel);
        }
    }
}
