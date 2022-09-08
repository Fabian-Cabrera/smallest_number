                                                #N es un entero dentro de este rango [1 ... 100,000] (cantidad del arreglo)
def validateLeng(n):                            #funcion para validar la longitud de un arreglo
    if (len(n) >= 1 and len(n)<= 100000):
        return True
    return False
                                                #Cada elemento del Array A es un entero dentro de este rango [−1,000,000 ... 1,000,000].
def validateElement(m):                         #funcion para validar el rango del elemento
    if (m >= -1000000 and m <= 1000000):
        return True
    return False 
  
def smallest_number(arr):    
    number = 0                              #number nos determinara el menor numero a mostrar en la salida, empezamos como 0 para validar en caso de que no exista el 1 en el arreglo                      
    if (not validateLeng(arr)):             #validamos la longitud del arreglo (1<=N<=100.000)             
        return -1                           #entregamos un -1 para indicar el error de longitud     
    arr.sort(key=int)                       #ordenamos el arreglo de menor a mayor
    for i in range(len(arr)):               #recorremos el arreglo
        if(not validateElement(arr[i])):    #validamos el entero de la posicion [i], rango entre -1.000.000 hasta 1.000.000      
            return -2                       #devolvemos el -2 para identificar el error
        if ( arr[i] <= number):             #ignoramos todos los numeros menores e iguales a cero (0)
            pass
        else:                               #si el entero a validar es mayor a cero, ingresamos al else
            if (arr[i]-number == 1):        #si el entero evaluado es consecutivo al numero auxiliar
                number = arr[i]             #asignamos el entero a la variable numero
            else:                           #si los numeros no son consecutivos, rompemos el ciclo ya que encontramos el menor numero en el arreglo
                break     
    number += 1                             #aumentamos una unidad al entero que encontramos, ya que es el que no esta en el arreglo
    return number                           #devolvemos el numero   
