<?php
class Car {
	public $color;
	public $model;
	public function __construct($color, $model) {
		$this->color = $color;
		$this->model = $model;
	}
	public function message() {
		return "Meu carro é um " . $this -> color . " " .$this-> model . "!";
	}
}
$myCar = new Car ("Palio", "Branco");
echo $myCar -> message();
echo "<br>";
$myCar = new Car ("Gol", "prata");
echo $myCar -> message();
?>