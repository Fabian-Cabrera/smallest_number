##API Smallest Number
	- Version python: 3.10

##Función
Recibe un Array A de N números enteros, devuelve el menor entero positivo que NO esté incluido en el Array, por ejemplo:

Para A = [1, 3, 6, 4, 1, 2], retorna 5.
Para A = [1, 2, 3], retorna 4.
Para A = [−1, −3], retorna 1.

Con las condiciones:
- Nuestro array no debe contener menos de 1 elemento ni mas de 100.000
- Cada elemento del array debe ser un entero entre -1.000.000 y 1.000.000
## Instrucciones
- Si deseas implementar solo la funcion, puedes encontrarla en el archivo **solution.py** , en este, encontraras los metodos para validar las condiciones y retornar la salida del programa.
##API REST
Puedes encontrar esta API hosteada en HEROKU, la url es la siguiente:
#### https://smallest-number.herokuapp.com/
###ENDPOINTS
1. https://smallest-number.herokuapp.com/smallest
		- Método: **POST**
		- Tipo de contenido: application/json 
	Para probar este endpoint podemos ingresar a https://reqbin.com/, este servicio nos permitira probar la API REST sin necesidad de instalar nada en nuesto equipo. 
	En la URL pondremos nuestro endpoint, modificaremos el método a POST, y en Content seleccionaremos JSON, a continuación podemos ingresar nuestro array con la siguiente estructura:
			{
			“array”: [1, 3, 6, 4, 1, 2]
			}
	Te dejo una imagen de referencia de como debemos ingresar los: datos
	![](https://i.ibb.co/Hr2M98K/test-fastapi-online-post.png)

	Al terminar de ingresar los datos, damos click en el boton "Send" y en la parte derecha de nuestra pantalla, nos indicará la respuesta de nuestra API:
	![](https://i.ibb.co/n0zBnFw/test-fastapi-online-post-result.png)

	"result" nos devuelve el menor entero positivo que NO esté incluido en nuestro Array .

2.  https://smallest-number.herokuapp.com/stats
		- Método: **GET**
		- Tipo de contenido: application/json 
	Nuestro endpoint "/stats" recibe un número entero y devuelve para cuantos Arrays ese ha sido el resultado esperado, el total de Arrays que se hayan verificado y la tasa de ocurrencia, todo esto en formato JSON.
	
	Usando de nuevo nuestro API Testing online, en la URL pondremos nuestro endpoint, modificaremos el método a GET, y en Content eliminaremos todo ya que el método GET no puede llevar un body.
	![](https://i.ibb.co/4JQfmst/test-fastapi-online-get.png)
	En nuestro parametro number, indicaremos el numero que queremos evaluar y daremos click en "Send"
	Nos entregara la informacion de la siguiente manera:
	
	![](https://i.ibb.co/rdRzD4f/test-fastapi-online-get-result.png)
	
	Donde "count" es la cantidad de Arrays para el cual nuestro numero ha sido el resultado, "total" es nuestra cantidad de Arrays evaluados sin repetirse y "ratio" nos indicará la tasa de ocurrencia de este numero con respecto al total de arrays evaluados.
	
	Estos arrays se guardaran en una base de datos SQLite, dentro del repositorio la puedes encontrar como database.bd
	Solo se guardará un registro por Array consultado.