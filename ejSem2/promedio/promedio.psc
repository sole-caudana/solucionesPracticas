Algoritmo costoxmetro
	
	//Identificar y declarar variables
	
	definir lado, area, cxm, costo_total como real;
	
	// Ingresar las dimensiones del cuadrado
	
	Escribir "Ingrese el valor del lado: ";
	leer alto;
	
	// Calcular el área de la pared
	area = lado * lado;
	
	// Guardar los datos suministrados
	
	Escribir "Ingrese el valor por metro: "
	leer cxm;
	
	// Calcular el costo total de mano de obra
	costo_total = area * cxm;
	
	// Mostrar el costo total
	Escribir "El costo total de mano de obra es: ", costo_total;
FinAlgoritmo
