import java.util.ArrayList;
import java.util.Random;
import java.util.concurrent.locks.ReentrantLock;

public class exp5 {

    static ReentrantLock lock = new ReentrantLock(); // critical section lock
    static ArrayList<String> sharedResource = new ArrayList<>();

    public static void main(String[] args) {

        int NUM_PROCESSES = 5;
        ArrayList<Thread> processes = new ArrayList<>();

        for (int pid = 1; pid <= NUM_PROCESSES; pid++) {
            int id = pid;

            Thread t = new Thread(() -> processTask(id));
            processes.add(t);
            t.start();
        }

        // wait for all threads
        for (Thread t : processes) {
            try {
                t.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        System.out.println("\nShared Resource Log:");
        for (String entry : sharedResource) {
            System.out.println(entry);
        }
    }

    public static void processTask(int pid) {

        Random rand = new Random();

        for (int i = 0; i < 3; i++) {

            System.out.println("Process " + pid + " requests critical section.");

            // ENTRY SECTION (Mutual Exclusion)
            lock.lock();  // acquire lock

            try {
                // CRITICAL SECTION
                System.out.println("Process " + pid + " entering critical section.");

                sharedResource.add("Process " + pid + " was here");

                try {
                    Thread.sleep(500 + rand.nextInt(1000));
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

                System.out.println("Process " + pid + " leaving critical section.");

            } finally {
                lock.unlock(); // release lock
            }

            // REMAINDER SECTION
            try {
                Thread.sleep(100 + rand.nextInt(400));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}