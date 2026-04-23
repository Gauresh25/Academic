import java.util.*;
import java.util.concurrent.*;

public class dummy {

    static final int N = 3;
    static Process[] processes = new Process[N];

    public static void main(String[] args) throws InterruptedException {
        for (int i = 0; i < N; i++) processes[i] = new Process(i);

        Thread[] threads = new Thread[N];
        for (int i = 0; i < N; i++) {
            final int id = i;
            threads[i] = new Thread(() -> processes[id].run());
            threads[i].start();
        }
        for (Thread t : threads) t.join();
    }

    static class Process {
        int id, burst, reqrep;
        boolean asked = false, critical = false;
        BlockingQueue<Integer> inbox = new LinkedBlockingQueue<>(); // replaces defq polling
        Queue<Integer> defq = new LinkedList<>();

        Process(int id) { this.id = id; }

        void run() {
            try {
                Thread.sleep(id * 200L); // stagger so not everyone requests at once
                reqCrit(3);
            } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
        }

        void reqCrit(int burst) throws InterruptedException {
            this.burst = burst;
            this.asked = true;
            this.reqrep = N - 1;

            // Broadcast request — push my id into their inboxes
            for (int i = 0; i < N; i++)
                if (i != id) processes[i].inbox.put(id);

            // ---- THIS IS YOUR turn() loop, but driven by blocking instead of ticks ----
            // Listen for replies/requests until reqrep hits 0
            while (reqrep > 0) {
                int from = inbox.take(); // BLOCKS until a message arrives (replaces your while loop tick)

                // Is 'from' a reply or a request?
                // Simple version: negative id = reply, positive = request
                if (from < 0) {
                    synchronized (this) { reqrep--; }
                } else {
                    // Someone else wants CS — defer or reply immediately
                    if (asked) {
                        defq.add(from); // defer — same as your simulated version
                    } else {
                        processes[from].inbox.put(-id); // reply immediately
                    }
                }
            }

            // Enter CS
            critical = true;
            System.out.println("P" + id + " enters CS");
            Thread.sleep(400); // simulate work
            System.out.println("P" + id + " exits CS");
            critical = false;
            asked = false;

            // Flush deferred — identical to your simulated version
            while (!defq.isEmpty()) {
                int recpt = defq.poll();
                processes[recpt].inbox.put(-id); // send reply
            }
        }
    }
}