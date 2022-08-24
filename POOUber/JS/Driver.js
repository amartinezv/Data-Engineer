class Driver extends Account{
    constructor(name, document){
        super(name, document)
    }

    printDataDriver(){
        console.log('name ${this.name}')
        console.log('document ${this.document}')
    }
}