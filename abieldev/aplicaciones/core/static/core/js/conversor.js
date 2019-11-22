//seleccion
function seleccion(x) {
	var moneda = document.getElementById(x);
	var elegir = document.getElementById('seleccion');
	moneda.addEventListener("click", function(){
	elegir.innerHTML = x;
	})	

}

function seleccion1(x) {
	var moneda = document.getElementById(x);
	var elegir = document.getElementById('seleccion1');
	moneda.addEventListener("click", function(){
	elegir.innerHTML = x;	
	})
}

//funcion para calcular el valor
function input1(precio) {
  	var valorM = document.getElementById('input1').value;
  	var valorF = parseInt(valorM) * parseInt(precio);
  	var salida = document.getElementById('salida');

  	if (valorF.value == NaN){
  		document.getElementById("salida").innerHTML = '';
  	}else{
  		salida.value = valorF;
  	}
  	console.log(valorF);
}

/*
function seleccion(x) {
	var moneda = document.getElementById(x);
	var elegir0 = document.getElementById('seleccion');
	var elegir1 = document.getElementById('seleccion1');
	if (elegir0.expanded == true){
		elegir0.addEventListener("click", 
			moneda.addEventListener("click", function(){
			elegir0.innerHTML = x;
		}))
	}
	else if (elegir1.expanded == true){
		elegir1.addEventListener("click", 
			moneda.addEventListener("click", function(){
			elegir1.innerHTML = x;
		}))		
	}
}
*/
