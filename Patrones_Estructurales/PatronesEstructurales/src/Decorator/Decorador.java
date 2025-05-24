package Decorator;

public abstract class Decorador implements Mensaje {
    protected Mensaje mensaje;

    public Decorador(Mensaje mensaje) {
        this.mensaje = mensaje;
    }
}
