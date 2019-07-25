import java.util.*;

enum TYPE{
	buscar,
	cadastrar,
	remover,
	alugar,
	devolver
}


public class User {
	public static void main(String[] args) {
		try {
			Scanner s = new Scanner(System.in);
			Proxy proxy = new Proxy();
			
			String data = null;
			
			System.out.println("Manda:");
//			data = s.nextLine();
			
			data = "{\"nome\": \"Carlos\", \"cpf\": \"456456\", \"numero\": 1563}";
			String resp = proxy.doOperation(data);
			
			System.out.println(resp);
			

			s.close();
		} catch (Exception e) {
			System.out.println("User main: "+e.getMessage());
		}
		
	}
}
