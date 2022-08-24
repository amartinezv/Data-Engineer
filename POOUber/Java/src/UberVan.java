import java.util.Map;
import java.util.ArrayList;;

class UberVan extends Car{
    
    Map<String, Map<String, String>> typeCarAccepted;
    ArrayList<String> seatsMaterial;
    private Integer passegenger;


    public UberVan(String license, Account driver, Map<String, Map<String, String>> typeCarAccepted, ArrayList<String> seatsMaterial){
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial = seatsMaterial;
    }

    @Override
    public void setPassegenger(Integer passegenger) {
        if (passegenger == 4){
            this.passegenger = passegenger;
        }else{
            System.out.println("Necesitas asignar 4 pasajeros");
        }

    }
}