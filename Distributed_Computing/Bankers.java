import java.util.ArrayList;
public class Bankers {
    public static class Process {
        int[] max;
        int[] alloc;
        int[] need;
        boolean fin = false;

        Process(int[] alloc, int[] max, int resourceCount) {
            this.alloc = alloc;
            this.max   = max;
            this.need  = new int[resourceCount];
            for (int j = 0; j < resourceCount; j++)
                this.need[j] = max[j] - alloc[j]; // need computed right at construction
        }

        public boolean isSafe(int[] avail){

            for (int i =0;i<3;i++) {
                if(this.need[i]>avail[i])
                {
                    return false;
                }
            }
            return true;
        }
    }

    static int numResources =3;

    static Process[] processes = {
            new Process( new int[]{0,1,0}, new int[]{7,5,3}, numResources),
            new Process( new int[]{2,0,0}, new int[]{3,2,2}, numResources),
            new Process( new int[]{3,0,2}, new int[]{9,0,2}, numResources),
            new Process(new int[]{2,1,1}, new int[]{2,2,2}, numResources),
            new Process(new int[]{0,1,0}, new int[]{4,3,3}, numResources),
        };

    static int[] avail ={3,3,2};
    static ArrayList<Process> safeseq = new ArrayList<>();
    public static void main(String[] args) {

        for (int pass = 0; pass < 5; pass++) {

            for (Process p : processes) {
                if(!p.fin){
                    if (p.isSafe(avail)) {
                    p.fin = true;
                    for (int i = 0; i < 3; i++) {
                        avail[i] =  avail[i] + p.alloc[i];
                    }
                    safeseq.add(p);
                    }
            }
            }
            
        }
        for (Process p : safeseq) {
            System.out.println(p.alloc[0] + " " +p.alloc[1]);
        }
    }
}
