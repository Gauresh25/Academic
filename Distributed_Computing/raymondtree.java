import java.util.ArrayList;

public class raymondtree {
    static class Node {
    
        int id;
        int holder;
        boolean asked;
        ArrayList<Integer> queue;

        Node(int id,int holder){
            this.id = id;
            this.holder = holder;
            this.asked = false;
            this.queue = new ArrayList<Integer>();
        }
    }

    // ── Hardcoded tree: 0-1, 1-2, 1-3. Node 0 starts with token ───
    //
    //      0         holder[0] = 0  (has the token, points to self)
    //       \        holder[1] = 0  (points toward node 0)
    //        1       holder[2] = 1  (points toward node 1, which leads to 0)
    //       / \      holder[3] = 1  (same)
    //      2   3

    static Node[] nodes = {
        new Node(0,0),
        new Node(1,0),
        new Node(2,1),
        new Node(3,1),
    };

    public static void main(String[] args) {
        
        nodes[2].queue.add(2);
        process(nodes[2]);

        nodes[3].queue.add(3);
        process(nodes[3]);

        nodes[0].queue.add(0);
        process(nodes[0]);
    }

    static void process(Node curr){
        

        if(curr.id == curr.holder)
            {
            int nextID = curr.queue.remove(0);

            if (nextID == curr.id) {
                System.out.println("processing critical section " + curr.id);
                if (!curr.queue.isEmpty()) {
                process(curr);
                }
            }
            else{//serve
                Node next = nodes[nextID];

                curr.holder = next.id;
                curr.asked = false;

                next.holder = next.id;
                next.asked = false;
                process(next);
            }
        }
        else{
            curr.asked = true;
            Node upstream = nodes[curr.holder];
            upstream.queue.add(curr.id);
            System.out.println("sending request from "+ curr.id +" to "+ upstream.id);

            process(upstream);
        }//now has token
        
    }

}
