<?php
class User extends Account {
    public function __construct($name, $document, $email, $password){
        parent::__construct($name, $document, $email, $password);
    }

    public function PrintDataUser(){
        echo "User: ";
        echo "Name $this->name Document $this->document Email $this->email Password $this->password;
    }
}
?>