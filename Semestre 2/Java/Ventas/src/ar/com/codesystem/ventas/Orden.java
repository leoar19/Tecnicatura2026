package ar.com.codesystem.ventas;

public class Orden {
    private int idOrden;
    private Producto productos[]; // Declaramos el arreglo
    private static int contadorOrdenes;
    private int contadorProductos;
    private static final int MAX_PRODUCTOS = 10;
    
    // Constructor vacio
    public Orden(){
        this.idOrden = ++Orden.contadorOrdenes;
        this.productos = new Producto[Orden.MAX_PRODUCTOS];
    }
    
    // Comprobacion
    public void agregarProducto(Producto producto){ // Void porque no devuelve nada
        if(this.contadorProductos < Orden.MAX_PRODUCTOS){
            this.productos[this.contadorProductos++] = producto;
        }
        else{
            System.out.println("Se ha superado el maximo de productos: "+Orden.MAX_PRODUCTOS
            +". Para la orden "+this.idOrden);
        }
    }
    
    public double calcularTotal(){
        double total = 0;
        for (int i = 0; i < this.contadorProductos; i++) {
            //Producto producto = this.productos[i];
            //total += producto.getPrecio();
            total += this.productos[i].getPrecio(); // 2 lineas en una
        }
        return total;
    }
    
    public void mostrarOrden(){
        System.out.println("Id Orden: "+idOrden);
        double totalOrden = this.calcularTotal();
        System.out.println("El total de la orden es: $"+totalOrden);
        System.out.println("Productos de la orden: ");
        for (int i = 0; i < this.contadorProductos; i++) {
            System.out.println(this.productos[i]);
        }
    }
}
