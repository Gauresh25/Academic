import java.net.*;

public class MulticastSender {

    // Hardcoded messages to broadcast to the group
    static final String[] MESSAGES = {
        "Hello Group! This is message 1",
        "Distributed Systems is fun!",
        "This is multicast via UDP sockets",
        "end"
    };

    static final String GROUP_ADDRESS = "230.0.0.0";
    static final int PORT = 5000;

    public static void main(String[] Args) throws Exception{

        InetAddress address = InetAddress.getByName(GROUP_ADDRESS);

        MulticastSocket sock =  new MulticastSocket(PORT);

        for(String msg:  MESSAGES){
            byte[] buffer = msg.getBytes();
            DatagramPacket packet = new DatagramPacket(buffer,buffer.length,address,PORT);
            sock.send(packet);
            Thread.sleep(1000);
        }

        sock.close();
    }
}