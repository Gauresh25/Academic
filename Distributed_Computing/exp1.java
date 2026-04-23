import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

public class exp1 {

    public static void main(String[] args) throws InterruptedException {
        BlockingQueue<String> queue = new LinkedBlockingQueue<>();

        Thread producer = new Thread(() -> {
            String[] messages = {
                "Hello",
                "This is IPC via Queue",
                "Java threading",
                "Goodbye"
            };

            try {
                for (String msg : messages) {
                    System.out.println("Producer sending: " + msg);
                    queue.put(msg);
                    Thread.sleep(500);
                }
                queue.put("exit");
            } catch (Exception e) {
                e.printStackTrace();
            }
        });

        Thread consumer = new Thread(() -> {
            System.out.println("Consumer started...");
            try {
                while (true) {
                    String msg = queue.take();
                    if (msg.equalsIgnoreCase("exit")) {
                        System.out.println("Consumer exiting...");
                        break;
                    }
                    System.out.println("Consumer received: " + msg);
                    Thread.sleep(200);
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        });

        consumer.start();
        producer.start();

        producer.join();
        consumer.join();

        System.out.println("Program terminated.");
    }
}