Algoritmo puntosAcumulados
	
	//Identificar y declarar variables
	Definir partidos_ganados, partidos_empatados, partidos_perdidos, puntos como real;
	// Ingresar la cantidad de partidos ganados, empatados y perdidos
	Escribir partidos_ganados ("Ingrese la cantidad de partidos ganados");
	leer partidos_ganados;
	
	Escribir partidos_empatados ("Ingrese la cantidad de partidos empatados");
	leer partidos_empatados;
	
	Escribir partidos_perdidos ("Ingrese la cantidad de partidos perdidos");
	leer partidos_perdidos;
	
	// Calcular los puntos
	puntos = (partidos_ganados * 3) + (partidos_empatados * 1) + (partidos_perdidos * 0);
	
	// Mostrar los puntos acumulados
	Escribir "La cantidad de puntos acumulados es: ", puntos;
	
FinAlgoritmo
