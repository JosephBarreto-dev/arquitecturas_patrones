package Prototype;

public class LogMensaje implements Cloneable {
    private String mensaje;
    private String nivel;

    public LogMensaje(String mensaje, String nivel) {
        this.mensaje = mensaje;
        this.nivel = nivel;
    }

    public void mostrar() {
        System.out.println("(" + nivel + ") " + mensaje);
    }
    public LogMensaje clonar() {
        try {
            return(LogMensaje) super.clone();
        }catch (CloneNotSupportedException e) {
            return null;
        }
    }
}
