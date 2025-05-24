package Composite;

import java.util.ArrayList;
import java.util.List;

public class Panel implements Elemento {
    private List<Elemento> elementos = new ArrayList<>();

    public void agregar(Elemento e) {
        elementos.add(e);
    }

    public void mostrar() {
        System.out.println("Panel:");
        for (Elemento e : elementos) {
            e.mostrar();
        }
    }
}
