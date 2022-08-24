public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        
        Car car = new Car("AMQ344", new Account("Andres Hernandez", "1193039292") );
        //car.passegenger = 4;
        //System.out.println("Car License: "+car.license);
        car.printDataCar();

        UberX uberx = new UberX("MK1234", new Account("Maria Echeverri", "11224343"), "chevrolet", "Spark");
        uberx.setPassegenger(4);
        uberx.printDataCar();

    }
}
