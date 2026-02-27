**Descripción del proyecto**  
    - Sistema de gestión de libros de una biblioteca.  

**Cómo ejecutarlo**  
    - Software:  
        Simplemente hay que situarse en el fichero main.py y ejecutar.  
        Desde la línea de comando, hay que situarse en la carpeta contenedora del proyecto y ejecutar:  
            *python3 main.py*  

    - BBDD:  
        Fichero inserts_libros.sql contiene tanto la CREACIÓN de la tabla libros como la inserción de los datos de esta.  
        Dentro de la base de datos hay que abrir un editor SQL.  
        Copiar el contenido del fichero inserts_libros.sql y ejecutar.  

**Decisiones de diseño**  
    - El ISBN no podrá ser duplicado ya que se usará como ID del libro.  
    - Se podrá duplicar tanto Título como Autor.

    