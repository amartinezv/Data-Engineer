<?php

require_once('Car.php');
require_once('Account.php');
require_once('UberPool.php');
require_once('UberX.php');

$car = new Car("AW456", new Account("Andres Herrera", "AMS123"));
$car->printDataCar();
$UberX = new UberX("CVB123", new Account("Andres Herrera", "DNI2123"), "Chevrolet", "Spark");
$UberX->printDataCar();

$user = new User("Mario Villa", "DEW12334", "Mario@mario.com", "kkfks")
$user->PrintDataUser();

?>