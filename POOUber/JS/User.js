class User extends Account{
    constructor(name, document){
        super(name, document)
    }

    printDataUser(){
        console.log(this.name)
        console.log(this.document)
    }
}