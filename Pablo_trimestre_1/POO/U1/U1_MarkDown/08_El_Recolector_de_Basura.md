# ELIMINAR OBJETOS. EL RECOLECTOR DE BASURA (GARBAGE COLLECTOR)
https://educacionadistancia.juntadeandalucia.es/centros/cordoba/pluginfile.php/365653/mod_resource/content/6/8_eliminar_objetos_el_recolector_de_basura_garbage_collector.html
---
Un “recolector de basura” es un proceso que se utiliza para eliminar los objetos que no van a ser utilizados más. En Python, este recolector funciona de forma automática, liberando de ese trabajo al programador.

Cómo eliminar objetos.

La sentencia del permite eliminar objetos, elementos de listas y claves de diccionarios que no van a ser necesarios. Sería la operación contraria a la creación del objeto.

Escenarios donde puede ser conveniente usar “del”:
- Liberar memoria.
- Prevenir el uso de variables no existentes.
- Evitar conflictos de nombres.

La sintaxis de esta sentencia sería: “del referencia”. Dónde referencia puede ser un identificador (de variable, clase, función…), un índice o trozo (slice) de una secuencia mutable, una clave de diccionario o un miembro de una clase (atributo u objeto).

En el siguiente ejemplo puedes observar ejemplos del uso de esta sentencia.
```py
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = 10

# Eliminar un elemento de una lista
del a[2]   # elimina el tercer elemento (índice 2 → valor 3)
print("Lista después de borrar a[2]:", a)

# Eliminar una variable
del b

# Manejo seguro con try/except
try:
    print(b)   # intentamos acceder a 'b'
except NameError:
    print("La variable 'b' ya no existe (fue eliminada).")
```
- del a[2] elimina el elemento en la posición 2 de la lista a → desaparece el 3.
- del b elimina la variable b. Al intentar imprimirla después, Python lanza un NameError porque ya no existe en memoria.

## 8.1 Cómo funciona el recolector de basura (texto extraído íntegro de Stackoverflow)
Aunque el recolector de basura funciona automáticamente en Python y no debería ser algo de lo que te tengas que preocupar, conocer algunos detalles de cómo Python gestiona la memoria pueden serte útiles (aún sin usar nunca la interfaz gc).

- En python todos los datos son en realidad objetos y ocupan un espacio en memoria mayor de lo que cabría esperar en otros lenguajes, debido a que no sólo se guarda el dato en sí, sino también meta-información acerca del mismo (su tipo entre otras cosas).
- Por ejemplo, cuando usas un entero en tu programa como aquí, a = 10000, el intérprete necesita reservar un espacio en memoria donde poder guardar un objeto de tipo int que contiene el dato 10000. Lo que ocupe el objeto depende un poco de la implementación de Python con la que estés trabajando. En Python por ejemplo ocuparía 28 bytes. En otros lenguajes el entero es un dato de 32 bits (o de 64, según la arquitectura) por lo que ocuparía tan sólo 4 bytes (u 8, según la arquitectura).
- Una variable no es más que una referencia (un puntero si prefieres llamarlo así) a la dirección de memoria donde está realmente el dato.
- La memoria que se ha reservado para contener el entero 10000 permanecerá ocupada mientras haya alguna referencia que se refiera a ese dato. Internamente el intérprete mantiene un contador de referencias que va actualizando con cada asignación. Por ejemplo en este momento el contador de referencias sería 1, porque hemos asignado el dato a una variable a, y por tanto hay una referencia apuntando a él.
- Si seguidamente haces por ejemplo, b = a, Entonces el intérprete creará una variable b y copiará a ella la referencia que había en a, de modo que en este momento hay dos referencias al mismo objeto. Tanto a como b se están refiriendo al mismo objeto. Su contador de referencias vale 2.
- Si seguidamente haces por ejemplo, a = a + 1 entonces ocurren varias cosas:
    - Se crea un nuevo objeto de tipo int para contener el resultado de la operación (otros 28 bytes que son necesarios).
    - Se inicializa ese nuevo objeto int con el valor 10001 (qué es el resultado de la operación).
    - Se cambia la referencia que había en a (que apuntaba al entero 10000) para que ahora apunte al entero 10001.
    - Como consecuencia de esta asignación, el entero 10001 incrementa su contador de referencias que pasa a valer 1 (la referencia a apunta a él) y el entero 10000 decrementa su contador de referencias, ya que ha dejado de apuntar a él. El contador de referencias de 10000 vale 1 (porque b todavía apunta a él).
- Si finalmente haces algo como, b = "Hola", eso creará un nuevo objeto en memoria de tipo str, inicializado con la cadena "Hola", y hará que la referencia b cambie su valor para pasar a apuntar a este objeto.
    - Como consecuencia el objeto str tiene su contador de referencias a 1, y el contador de referencias de 10000 pasa a cero, pues b ha dejado de apuntar a él.
    - Entonces el intérprete ejecutará el recolector de basura para eliminar los objetos cuyo contador de referencias es 0.
    - En este caso se liberará el objeto int que valía 10000, liberándose así 28 bytes de memoria.
    
Moralejas de lo anterior:
- Las operaciones son más complicadas de lo que aparentaban en la superficie. Si vienes de un lenguaje como C, te habrá sorprendido el follón que se ha montado para un simple a=a+1. En C lo que ocurría simplemente es que la posición de memoria en que estaba guardado el 10000 se sobreescribe y pasa a contener un 10001. En Python no, pues los enteros son inmutables. Un 10000 siempre será un 10000 (mientras exista)
- La memoria no se va a liberar mientras tengas variables que se refieren a ese objeto. Por tanto una posible forma de liberar memoria cuando andes escaso de ella puede ser borrar la referencia. La instrucción “del a”, por ejemplo, elimina la referencia llamada a, decrementando así el contador de referencias del objeto al que apuntaba.

Considera este ejemplo:
```py
>>> a = 10000
>>> del a
>>> a Traceback (most recent call last): File "<stdin>", line 1, in <module> NameError: name 'a' is not defined
```
- La primera instrucción reservará 28 bytes para el entero 10000 y la referencia a apuntará a ese entero. Su contador de referencias será por tanto 1.
- La línea del a elimina la variable a (que pasa a ser no definida como se comprueba seguidamente). El entero al que “a” apuntaba pasará a tener un contador de referencias cero, y será por tanto liberado por el recolector de basura.
- Es necesario mencionar que el recolector de basura de Python no actúa inmediatamente, tras eliminar la última referencia de un objeto.
- El procedimiento usado es el de escanear la memoria de forma periódica buscando objetos no referenciados.
