import java.util.ArrayList;
import java.util.Arrays;

import org.w3c.dom.Node;
public class DistGlobalAveraging {
    public static class node {
        int id;
        double value;
        double temp;
        ArrayList<Integer> neighbor;

        node(int id,int value, ArrayList<Integer> neighbor){
            this.id = id;
            this.value = value;
            this.temp = value;
            this.neighbor = neighbor;
        }
    }

    static node[] graph = {
        new node(0, 100, new ArrayList<>(Arrays.asList(1,3))),
        new node(1, 2000, new ArrayList<>(Arrays.asList(0,2))),
        new node(2, 300, new ArrayList<>(Arrays.asList(1,4))),
        new node(3, 40, new ArrayList<>(Arrays.asList(0,4))),
        new node(4, 50, new ArrayList<>(Arrays.asList(2,3))),
    };

    public static void main(String[] args) {
        for(int i = 0; i<10;i++)
        {
            for (node curr : graph) {
            double avg =curr.value;
            int count = 1;
            for (int id : curr.neighbor){
                avg = avg + graph[id].value;
                count++;
            }

            curr.temp = avg/count;
            System.out.println(curr.value);
                
        }for (node curr : graph) {
            curr.value = curr.temp;
        }
        
    }

}}
