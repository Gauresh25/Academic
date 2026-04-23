import java.util.*;
import java.util.concurrent.*;

public class exp7 {

    public static void main(String[] args) throws InterruptedException {

        int numServers = 3;

        // Create tasks
        List<String> tasks = new ArrayList<>();
        for (int i = 1; i <= 10; i++) {
            tasks.add("T" + i);
        }

        // Task queues for each server
        List<Queue<String>> taskQueues = new ArrayList<>();

        for (int i = 0; i < numServers; i++) {
            taskQueues.add(new ConcurrentLinkedQueue<>());
        }

        // ROUND ROBIN DISTRIBUTION
        for (int i = 0; i < tasks.size(); i++) {
            taskQueues.get(i % numServers).add(tasks.get(i));
        }

        // Log shared structure
        List<String> log = new CopyOnWriteArrayList<>();

        // Create server threads
        List<Thread> servers = new ArrayList<>();

        for (int i = 0; i < numServers; i++) {
            int serverId = i + 1;
            Queue<String> queue = taskQueues.get(i);

            Thread t = new Thread(() -> serverTask(serverId, queue, log));
            servers.add(t);
            t.start();
        }

        // Wait for all servers
        for (Thread t : servers) {
            t.join();
        }

        // Print log
        System.out.println("\nTask Processing Log:");
        for (String entry : log) {
            System.out.println(entry);
        }
    }

    // Server processing function
    public static void serverTask(int serverId, Queue<String> taskQueue, List<String> log) {

        Random rand = new Random();

        while (!taskQueue.isEmpty()) {

            String task = taskQueue.poll();

            if (task != null) {
                System.out.println("Server " + serverId + " processing Task " + task);

                log.add("Server " + serverId + " processed Task " + task);

                try {
                    Thread.sleep(500 + rand.nextInt(500));
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}