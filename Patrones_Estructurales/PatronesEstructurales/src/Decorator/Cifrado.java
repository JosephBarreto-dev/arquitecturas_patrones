package Decorator;

public class Cifrado extends Decorador {
    public Cifrado(Mensaje mensaje){
        super(mensaje);
    }

    public String enviar(){
        return cifrar(mensaje.enviar());
    }
    private String cifrar(String mensaje){
        return "Mensaje cifrado: " + mensaje;
    }
}
