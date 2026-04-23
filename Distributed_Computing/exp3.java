import java.util.Random;

public class exp3 {

    static final int NUM_NODES = 5;

    public static void main(String[] args) {

        Random rand = new Random();
        double[] nodeClocks = new double[NUM_NODES];

        // Initialize random clocks
        System.out.println("Initial node clocks:");
        for (int i = 0; i < NUM_NODES; i++) {
            nodeClocks[i] = rand.nextInt(100);
            System.out.println("Node " + (i + 1) + ": " + nodeClocks[i]);
        }

        // Synchronize clocks
        double[] synchronizedClocks = synchronizeClocks(nodeClocks);

        // Print result
        System.out.println("\nSynchronized node clocks:");
        for (int i = 0; i < NUM_NODES; i++) {
            System.out.printf("Node %d: %.2f%n", (i + 1), synchronizedClocks[i]);
        }
    }

    public static double[] synchronizeClocks(double[] clocks) {

        double coordinatorTime = clocks[0];

        double[] offsets = new double[clocks.length];

        // Calculate offsets
        for (int i = 0; i < clocks.length; i++) {
            offsets[i] = clocks[i] - coordinatorTime;
        }

        // Calculate average offset
        double sum = 0;
        for (double offset : offsets) {
            sum += offset;
        }
        double avgOffset = sum / clocks.length;

        // Adjust clocks
        for (int i = 0; i < clocks.length; i++) {
            clocks[i] = clocks[i] - offsets[i] + avgOffset;
        }

        return clocks;
    }
}