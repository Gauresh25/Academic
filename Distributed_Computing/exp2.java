import java.util.*;

public class exp2 {

    // Group of processes (nodes)
    static List<String> groupMembers = Arrays.asList(
            "Node1", "Node2", "Node3", "Node4", "Node5"
    );

    public static void main(String[] args) {

        String sender = "Coordinator";

        // Message to be broadcast
        String message = "Hello Group! This is a broadcast message.";

        System.out.println(sender + " sending message to group...\n");

        broadcast(sender, message);

        System.out.println("\nAll nodes received the message.");
    }

    // Broadcast function (group communication)
    public static void broadcast(String sender, String message) {

        List<Thread> receivers = new ArrayList<>();

        for (String member : groupMembers) {

            Thread t = new Thread(() -> {
                receiveMessage(member, sender, message);
            });

            receivers.add(t);
            t.start();
        }

        // Wait for all nodes to receive message
        for (Thread t : receivers) {
            try {
                t.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    // Receiver function
    public static void receiveMessage(String receiver, String sender, String message) {

        System.out.println(receiver + " received message from " + sender);
        System.out.println("Message: " + message + "\n");

        try {
            Thread.sleep(500); // simulate processing delay
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}