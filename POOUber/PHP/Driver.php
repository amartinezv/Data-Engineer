<?php
class Driver extends Account{
    public function __construct($name, $document, $email, $password){
        parent::__construct($name, $document, $email, $password);
    }

    public function PrintDataDriver(){
        echo "User: ";
        echo "Name $this->name Document $this->document Email $this->email Password $this->password;
    }
}
?>