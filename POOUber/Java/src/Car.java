public class Car {
    private Integer id;
    private String license;
    private Account driver;
    private Integer passegenger;

    public Car(String lincense, Account driver){
        this.license = lincense;
        this.driver = driver;
    }
    
    void printDataCar(){
        System.out.println("License: "+ license + " Name Driver: "+ driver.name + " Passenger "+ passegenger);
    }

    public Integer getPassegenger(){
        return passegenger;
    }

    public void setPassegenger(Integer passegenger){
        if (passegenger == 4){
            this.passegenger = passegenger;
        }else{
            System.out.println("Necesitas asignar 4 pasajeros");
        }
        
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getLicense() {
        return license;
    }

    public void setLicense(String license) {
        this.license = license;
    }

    public Account getDriver() {
        return driver;
    }

    public void setDriver(Account driver) {
        this.driver = driver;
    }

    
}
