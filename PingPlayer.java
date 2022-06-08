
package py4j;
import py4j.GatewayServer;
public class PingPlayer 
{

    public String firstping(PongPlayer player)
     {
        return player.firstPong(this);
     }

    public String secondping(PongPlayer player) {
        return player.secondPong();
     }
     public static void main(String[] args) {
        PingPlayer y=new PingPlayer();
        GatewayServer gatewayServer = new GatewayServer(y);
        gatewayServer.start();
        System.out.println("Gateway Server Started");
    }

}
