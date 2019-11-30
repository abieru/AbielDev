//www.creativos3up.com
new Vue({
	el: "#conversor",
	data:{
		monedas: ["USD","VES", "LTC", "BTC", "DOGE", "XMR", "DASH", "ETH", "EOS"],
		cantidad: null,
		from: 'USD',
		to: 'VES',
		resultado: null
	},
	mounted(){

	},
	computed:{
		calcularResultado(){
		return (Number(this.cantidad) * this.resultado).toFixed();
		}
	},
	methods:{
		convertirmoneda(){
			const busqueda = `${this.from}&tsyms=${this.to}`;
			const result = `${this.to}`;
			axios.get(`https://min-api.cryptocompare.com/data/price?fsym=${busqueda}&api_key=dc1bab01a536aaec3593f72a057f8494701868e70a3a6ea6005e6a5e4b70b29e`)
			.then((response) =>{
				console.log(response);
				return this.resultado = response.data[result];
			});
		}
	},
	watch:{
		from(){
			this.cantidad = 0;
		},
		to(){
			this.resultado = 0;
		}
	}
});


/*
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
	
	//casillas de seleccion
	var elegir1 = document.getElementById('seleccion');
	var elegir2 = document.getElementById('seleccion1');



	//la multipliciacion del conversor
  	var valorM = document.getElementById('input1').value;
  	var valorF = parseInt(valorM) * parseInt(precio);
  	var salida = document.getElementById('salida');
  	
  	salida.value = valorF;
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
