import java.net.*;

public class MulticastReceiver {

    static final String GROUP_ADDRESS = "230.0.0.0";
    static final int PORT = 5000;

    public static void main(String[] Args) throws Exception{

        InetAddress group = InetAddress.getByName(GROUP_ADDRESS);

        MulticastSocket sock =  new MulticastSocket(PORT);
        sock.joinGroup(group);

        while (true) {
            byte[] buffer = new byte[1024];
            DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
            sock.receive(packet);
            String message = new String(packet.getData(),0,packet.getLength());
            System.out.println(message);

            if (message.equals("end")) {
                break;
            }
        }

        sock.close();
    }
}