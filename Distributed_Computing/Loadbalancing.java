import java.util.*;

public class Loadbalancing {

    // A Server knows its own ID and how much load it's currently carrying
    static class Server {
        int id;
        int load;           // total load assigned so far
        List<Integer> tasks; // which task numbers landed here (for display)

        Server(int id) {
            this.id = id;
            this.load = 0;
            this.tasks = new ArrayList<>();
        }
    }

    public static void main(String[] args) {

        int numServers = 4;
        int numTasks   = 12;
        Random rand    = new Random(42); // fixed seed so results are reproducible

        // Build our "cluster" — an array of servers, just like our graph of nodes
        Server[] servers = new Server[numServers];
        for (int i = 0; i < numServers; i++)
            servers[i] = new Server(i);

        System.out.println("=== Simple Load Balancing (Least Loaded) ===\n");

        // Simulate tasks arriving one by one
        for (int taskId = 1; taskId <= numTasks; taskId++) {

            int taskWeight = 10 + rand.nextInt(91); // random weight between 10-100

            // THE CORE ALGORITHM: scan all servers, pick the least loaded one
            // This is an O(n) scan — fine for small clusters, but in real systems
            // with thousands of servers you'd use a min-heap for O(log n) lookup
            Server target = servers[0];
            for (Server s : servers) {
                if (s.load < target.load) {
                    target = s;
                }
            }

            // Assign the task to the winner
            target.load += taskWeight;
            target.tasks.add(taskId);

            System.out.printf("Task %2d (weight=%3d) → assigned to Server %d (new load=%3d)%n",
                taskId, taskWeight, target.id, target.load);
        }

        // Print final state of the cluster
        System.out.println("\n--- Final Load Distribution ---");
        int totalLoad = 0;
        for (Server s : servers) {
            System.out.printf("Server %d | load=%4d | tasks=%s%n",
                s.id, s.load, s.tasks);
            totalLoad += s.load;
        }

        // How well balanced are we? Ideal = every server has exactly totalLoad/numServers
        double idealLoad = (double) totalLoad / numServers;
        System.out.printf("%nTotal load : %d%n", totalLoad);
        System.out.printf("Ideal load : %.2f per server%n", idealLoad);

        // Imbalance score: average deviation from ideal
        // A score of 0 means perfect balance — the lower the better
        double imbalance = 0;
        for (Server s : servers)
            imbalance += Math.abs(s.load - idealLoad);
        imbalance /= numServers;
        System.out.printf("Avg imbalance: %.2f%n", imbalance);
    }
}