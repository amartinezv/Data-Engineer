/**
 * User
 */
class User extends Account {
    public User(String name, String document) {
        super(name, document);
    }

    void printDataUser(){
        System.out.println("Document: " + document + " Name: "+ name);
    }
    
}