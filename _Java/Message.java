//
//class messageType{
//	public static int REQUEST = 0;
//	public static int REPLY = 1;
//}


public class Message {
	int type;
	int requestID;
	String objectReference;
	String methodName;
	String arguments;
	
	public Message(int _type, int _requestID, String _objectReference, String _methodName, String _arguments) {
		try {
			this.type = _type;
			this.requestID = _requestID;
			this.objectReference = _objectReference;
			this.methodName = _methodName;
			this.arguments = _arguments;
		}
		catch (Exception e) {
			System.out.println("Message contructor: "+e.getMessage());
		}
	}
	
	public Message() {
		
	}
}






/*
operação: 
	busca livro: nome, autor, editora
	busca cliente: nome, cpf
	cadastrar livro
	cadastrar cliente
	remover livro
	remover cliente
	alugar livro
	devolver livro
*/