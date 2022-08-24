class Driver extends Account {
    
    public Driver(String name, String document) {
        super(name, document);
    }

    void printDataDriver(){
        System.out.println("Document: " + document + " Name: "+ name);
    }
}
