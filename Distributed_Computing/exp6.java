import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

public class exp6 {

    // Shared structures
    static Map<Integer, Integer> waiting = new ConcurrentHashMap<>();
    static Map<Integer, Integer> held = new ConcurrentHashMap<>();

    static Random rand = new Random();

    public static void main(String[] args) {

        Map<Integer, String> resources = new HashMap<>();
        resources.put(1, "R1");
        resources.put(2, "R2");
        resources.put(3, "R3");

        // Start processes
        List<Thread> processes = new ArrayList<>();

        for (int pid = 1; pid <= 4; pid++) {
            int id = pid;
            Thread t = new Thread(() -> processTask(id, resources));
            processes.add(t);
            t.start();
        }

        // Deadlock detector thread
        Thread detector = new Thread(() -> detectDeadlock());
        detector.setDaemon(true);
        detector.start();

        // Wait for processes
        for (Thread t : processes) {
            try {
                t.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        System.out.println("All processes completed.");
    }


    public static void processTask(int pid, Map<Integer, String> resources) {

        for (int i = 0; i < 2; i++) {

            int r = 1 + rand.nextInt(resources.size());

            System.out.println("Process " + pid + " requests Resource " + r);

            waiting.put(pid, r);

            // wait until resource is free
            while (held.containsKey(r) && held.get(r) != pid) {
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

            // acquire resource
            held.put(r, pid);
            waiting.remove(pid);

            System.out.println("Process " + pid + " acquired Resource " + r);

            try {
                Thread.sleep(500 + rand.nextInt(500));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            System.out.println("Process " + pid + " released Resource " + r);

            held.remove(r);

            try {
                Thread.sleep(100 + rand.nextInt(300));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    // ---------------- DEADLOCK DETECTOR ----------------
    public static void detectDeadlock() {

        while (true) {

            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            // Build wait-for graph
            Map<Integer, List<Integer>> graph = new HashMap<>();

            for (Map.Entry<Integer, Integer> entry : waiting.entrySet()) {

                int process = entry.getKey();
                int resource = entry.getValue();

                Integer holder = held.get(resource);

                if (holder != null) {
                    graph.computeIfAbsent(process, k -> new ArrayList<>()).add(holder);
                }
            }

            // Detect cycle using DFS
            Set<Integer> visited = new HashSet<>();
            Set<Integer> recStack = new HashSet<>();

            for (int node : graph.keySet()) {
                List<Integer> cycle = dfs(node, graph, visited, recStack, new ArrayList<>());

                if (cycle != null) {
                    System.out.println("⚠ Deadlock detected among processes: " + cycle);
                    return;
                }
            }
        }
    }

    // DFS cycle detection
    public static List<Integer> dfs(int node,
                                     Map<Integer, List<Integer>> graph,
                                     Set<Integer> visited,
                                     Set<Integer> recStack,
                                     List<Integer> path) {

        if (recStack.contains(node)) {
            path.add(node);
            return new ArrayList<>(path);
        }

        if (visited.contains(node)) {
            return null;
        }

        visited.add(node);
        recStack.add(node);
        path.add(node);

        for (int neighbor : graph.getOrDefault(node, new ArrayList<>())) {
            List<Integer> result = dfs(neighbor, graph, visited, recStack, new ArrayList<>(path));
            if (result != null) return result;
        }

        recStack.remove(node);
        return null;
    }
}