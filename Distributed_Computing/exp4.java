import java.util.ArrayList;
import java.util.Random;

public class exp4 {

    static final int NUM_PROCESSES = 5;

    public static void main(String[] args) {

        ArrayList<Integer> processes = new ArrayList<>();

        // Create process IDs: 1 to 5
        for (int i = 1; i <= NUM_PROCESSES; i++) {
            processes.add(i);
        }

        // Randomly fail one process
        Random rand = new Random();
        int failedProcess = processes.get(rand.nextInt(processes.size()));

        System.out.println("Process " + failedProcess + " has failed.\n");

        Integer coordinator = bullyElection(processes, failedProcess);

        System.out.println("\nNew coordinator is Process " + coordinator);
    }

    public static Integer bullyElection(ArrayList<Integer> processes, int failed) {

        // Remove failed process
        ArrayList<Integer> aliveProcesses = new ArrayList<>();
        for (int p : processes) {
            if (p != failed) {
                aliveProcesses.add(p);
            }
        }

        System.out.println("Alive processes: " + aliveProcesses);

        // Election simulation
        for (int p : aliveProcesses) {

            System.out.println("\nProcess " + p + " initiates election...");

            ArrayList<Integer> higherProcesses = new ArrayList<>();

            for (int hp : aliveProcesses) {
                if (hp > p) {
                    higherProcesses.add(hp);
                }
            }

            if (!higherProcesses.isEmpty()) {
                System.out.println("Processes " + higherProcesses +
                        " respond to election message from " + p);
            } else {
                System.out.println("No higher process responds. Process " +
                        p + " becomes coordinator!");
                return p;
            }
        }

        return null; 
    }
}