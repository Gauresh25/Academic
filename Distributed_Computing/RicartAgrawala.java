import java.util.ArrayList;

public class RicartAgrawala {
    public static class process {
        int id, burst, reqrep = 0;
        boolean asked = false, critical = false;
        ArrayList<Integer> defq = new ArrayList<>();

        process(int id) { this.id = id; }

        public void reqCrit(int burst,int ts) {
            this.burst = burst;
            this.asked = true;
            this.reqrep = 2;
            for (int i = 0; i < 3; i++)
                if (i != this.id) processes[i].defq.add(this.id);
            System.out.println("processs P"+this.id+" requesting cs at ts "+ts);
        }

        public void turn(int ts) {
            // Idle: reply to anyone waiting on me
            if (!this.asked && !this.critical) {
                while (!this.defq.isEmpty()) {
                    int recpt = this.defq.remove(0);
                    processes[recpt].reqrep--;
                    System.out.println("P" + this.id + " replies to P" + recpt);
                }
            }

            // Got all replies: enter CS
            if (this.asked && !this.critical && this.reqrep == 0) {
                this.critical = true;
                System.out.println("P" + this.id + " enters CS");
            }

            // Execute CS
            if (this.critical) {
                this.burst--;
                System.out.println("P" + this.id + " in CS, burst left: " + this.burst);
            }

            // Exit CS: flush deferred replies
            if (this.critical && this.burst == 0) {
                this.critical = false;
                this.asked = false;
                System.out.println("P" + this.id + " exits CS");
                while (!this.defq.isEmpty()) {
                    int recpt = this.defq.remove(0);
                    processes[recpt].reqrep--;
                    System.out.println("P" + this.id + " deferred reply to P" + recpt);
                }
            }
        }
    }

    static process[] processes = { new process(0), new process(1), new process(2) };

    public static void main(String[] args) {
        int clock = 0;
        processes[0].reqCrit(3,clock);
        
        while (clock < 2) {
            for (process p : processes) p.turn(clock);
            clock++;
        }
        processes[1].reqCrit(2,clock);
        while (clock < 15) {
            for (process p : processes) p.turn(clock);
            clock++;
        }
    }
}