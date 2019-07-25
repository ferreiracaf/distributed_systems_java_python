import java.net.*;
import java.io.*;

public class TCPClient {
	private Socket s;
	private int serverPort;
	private DataInputStream in;
	private DataOutputStream out;
	
	public TCPClient() {
		try {
			this.serverPort = 12000;
			this.s = new Socket("localhost", serverPort);
			this.in = new DataInputStream( s.getInputStream());
			this.out = new DataOutputStream( s.getOutputStream());
		} catch (Exception e) {
			System.out.println("TCPClient constructor: "+e.getMessage());
		}
	}
	
	public TCPClient(int port) {
		try {
			this.serverPort = port;
			this.s = new Socket("localhost", serverPort);
			this.in = new DataInputStream( s.getInputStream());
			this.out = new DataOutputStream( s.getOutputStream());
		} catch (Exception e) {
			System.out.println("TCPClient constructor: "+e.getMessage());
		}
	}
	
	public void sendRequest(String data) {
		try {
			out.writeUTF(data);
		} catch (Exception e) {
			System.out.println("TCPClient sendRequest: "+e.getMessage());
		}
	}
	
	public String getResponse(){
		String resp = null;
		try {
			resp = this.in.readUTF();
		} catch (Exception e) {
			System.out.println("TCPClient getResponse: "+e.getMessage());
		}
		return resp;
	}
	
}



