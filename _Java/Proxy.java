import com.google.gson.*;

public class Proxy {
	private TCPClient client;
	
	public Proxy() {
		try {
			this.client = new TCPClient();
		} catch (Exception e) {
			System.out.println("Proxy contructor: "+e.getMessage());
		}
	}
	
	public String doOperation(String data) {
		String resp = null;
		String resp2 = null;
		try {
			Gson gson = new Gson();
			
			int request = 0;
			
			Message message = new Message(request, 1, "search", "book_id", "1");
			
			String requestStr = gson.toJson(message);
			
			String teste = "{\"type\":0,\"requestID\":1,\"objectReference\":\"lib\",\"methodName\":\"rented\",\"arguments\":1}";
			
//			teste = "{\"objectReference\":\"search\",\"methodName\":\"book_id\",\"arguments\":\"1\"}";
			
//			teste = "1234567";
			
			client.sendRequest(teste);
			
			
			resp = client.getResponse();
			if(resp.indexOf('}')==-1) {
				resp2 = client.getResponse();
				resp = resp + resp2;
//				resp = resp.replace("!", "");
			}
			
//			System.out.println(resp2);
		} catch (Exception e) {
			System.out.println("Proxy doOperation: "+e.getMessage());
		}
		
		return resp;
	}
}
