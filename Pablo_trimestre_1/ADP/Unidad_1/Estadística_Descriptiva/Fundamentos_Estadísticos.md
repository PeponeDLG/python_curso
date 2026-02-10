# FUNDAMENTOS ESTADÍSTICOS
CONCEPTOS FUNDAMENTALES
---
- **Población**: Todos los elementos.
- **Indivíduo**: Cada uno de los elementos.
- **Variable**: Característica, comportamiento, etc.
- **Dato**: Valor de la variable.
- **Censo**: Recoger datos de toda la población.
- **Muestra**: Recoger datos de una **parte significativa** de la población.

## Tipos de variables
- **Cualitativas**: Reflejan cualidades no necesariamente numéricas. Pueden ser **nominales** (no ordenables) u **ordinales** (ordenables).
- **Cuantitativas**: Numéricas con significado aritmético. Pueden ser **discretas** (p.ej. número de hijos) o **contínuas** (p.ej. estatura). La limitación de precisión da discreción a las variables cuantitativas.

## Escalas de medida
- **Nominal**: En categorías sin orden. Ejemplo: Nacionalidad.
- **Ordinal**: Con orden. Ejemplo: Nivel de estudios.
- De **Intervalo**: Ejemplo: Temperatura.
- De **Razón**: Ejemplo: Total de ventas.

## Tipos de datos
- **Datos Transversales o de Sección Cruzada**: Varios individuos en un mismo momento. Ej: Número de ventas de varios productos en un día concreto.
- **Series Temporales**: Un individuo en varios momentos. Ej: Número de ventas de un producto concreto cada día de un mes.
- **Panel de Datos**: Transversalidad + temporalidad. Varios individuos en varios momentos. Ej: Número de ventas de varios productos cada día de un mes.

## Tipos de estadística
- **Univariante**: Una variable.
- **Multivariante**: Dos o más variables a la vez.

## Tabulación y Representación Gráfica de Datos Univariantes
- **Tabulación**: Ordenación y agrupamiento de datos para obtener distribuciones de frecuencias. Ej: Tamaño de la muestra (N).

## Tipos de Frecuencias
- **Frecuencia Absoluta**: Número de repeticiones de un valor. Ej: 10 indivíduos de 27 años.
- **Frecuencia Relativa**: Porcentaje de repeticiones de un valor. Ej: El 10% de los indivíduos tienen 27 años.
- **Frecuencia Absoluta Acumulada**: Número de repeticiones de todos los valores menores o iguales a uno concreto. Ej: 100 de los indivíduos tienen menos de 27 años.
- **Frecuencia Relativa Acumulada**: Porcentaje de repeticiones de todos los valores menores o iguales a uno concreto. Ej: El 20% de los indivíduos tienen 27 años o menos.

## Distribuciones de Frecuencias según el tipo de variable
- **Variables Cualitativas Nominales**: Sólo se calculan frecuencias absolutas y relativas. Como no tienen orden no se calculan frecuencias acumuladas.
- **Variables Ordinales y Discretas**: Se calculan todas las frecuencias (las 4)
- **Variables Contínuas Agrupadas**: Datos agrupados en intervalos. Ej: Clasificación de peso en categorías (peso pluma, welter etc). Si los intervalos no son iguales se calcula la **densidad de frecuencia** (Frecuencia Absoluta de cada intervalo / su amplitud).

## Representación Gráfica de Datos
### Variables Cualitativas:
- **Cartograma**: Representación geográfica de datos sobre mapas.
- **Pictograma**: Uso de símbolos o iconos para representar cantidades.
- **Diagrama de sectores**: Perfecto para variables cualitativas nominales.
- **Diagrama de barras**: Cada barra representa un **eje de abscisas** (modalidad de la variable) sin importar el orden de las barras. El tamaño de cada barra representa la **frecuencia** del dato que representa.
### Variables Discretas:
- Diagrama de barras para datos **no agrupados**: Cada barra representa un dato. Ej: Número de hijos.
### Variables Contínuas:
- **Histograma**: Barras contíguas cuya superficie es proporcional a la frecuencia del dato que representan. Perfectos para distribuciones agrupadas.
- **Polígono de frecuencias para datos agrupados**: Equivalente al histograma. Se obtiene uniendo los centros de las caras superiores de cada barra de un histograma. Perfectos para ver **distribuciones** y comparar diferentes conjuntos de datos.

## Medidas de posición
### Medidas de Tendencia Central:
Ubican el centro representativo de la distribución.
- **Media aritmética**: Promedio de todos los valores.
    - **Ponderada**: Tiene en cuenta el peso o importancia de cada valor.
    - **No ponderada**: Todos los valores se tratan con la misma importancia.
- **Mediana**: Valor que divide la distribución en dos partes iguales.
- **Moda**: Valor más frecuente.

### Medidas de Tendencia No Central:
Identifican otros puntos característicos.
- **Cuartiles**: Dividen los valores en 4 partes.
- **Deciles**: Dividen los valores en 10 partes.
- **Percentiles**: Dividen los valores en 100 partes.

## Medidas de Dispersión
Evalúan la variabilidad en un conjunto de datos, es decir **lo separados que están los datos** entre sí o respecto al valor central que los representa. Permiten evaluar lo representativa que puede ser una medida de posición. Cuanto más dispersos estén los datos, menos representativas son las medidas de dispersión.

### Medidas de Dispersión Absolutas:
Tienen las **mismas unidades** que la cantidad que se mide. Por ejemplo si la medida es en metros, también lo será la medida de dispersión.
#### Sin referencia central:
- **Recorrido muestral**: Diferencia entre el valor máximo y mínimo. Muy afectado por los datos muy dispersos.
    *Recorrido muestral = Valor máximo - Valor mínimo*
- **Recorrido intercuartílico**: Comprende el 50% de los datos, que corresponden a los que están entre el primer y tercer cuartil. Menos sensible a datos atípicos.
    *Recorrido intercuartílico = Cuartil 3 - Cuartil 1*
#### Con referencia central:
- **Varianza**: Mide la variabilidad de un conjunto de datos respecto de la media aritmética. Si todos los valores fueran iguales, al no variar, la varianza sería 0. Cuanto más proxima sea a 0, mayor representatividad tiene la media. Tiene el inconveniente de que se expresa en unidades cuadráticas para poder eliminar el signo si el resultado es negativo.
- **Desviación típica o estándar**: Es la raíz cuadrada de la varianza. Resuelve el inconveniente de la varianza facilitando su interpretación.

### Medidas de Dispersión Relativas:
Son **adimensionales** permitiendo comparar datos que tienen diferentes unidades de medida. Calculan lo dispersos que están los datos en relación con su tamaño o posición.
- **Recorrido relativo**: Compara la diferencia entre el valor más alto y el más bajo, en proporción con el valor máximo.
    *Recorrido relativo = (Valor máximo - Valor mínimo) / Valor máximo*
- **Recorrido semi-intercuartílico**: Mide la dispersión del recorrido intercuartílico (50% central de los datos) comparando los cuartiles 1 y 3.
    *Recorrido semi-intercuartílico = (Cuartil 3 - Cuartil 1) / (Cuartil 3 + Cuartil 1)*
- **Coeficiente de Variación de Pearson**: Medida adimensional relativa a la varianza. Es fundamental para comparar distribuciones. Si es menor que 0.2, la dispersión relativa es baja y la media es representativa. No usar si la media aritmética es 0 (daría infinito).
    *Coeficiente de Variación de Pearson = Desviación Típica / Media Aritmética*

## Tipificación de Variables
Consiste en transformar los datos para que todos estén en la **misma escala sin importar sus unidades**. Se hace restando a cada dato la media aritmética y dividiendo por la desviación típica. Hacemos que la media sea 0 y la desviación típica 1.
Sirve para:
- Comparar datos distintos en una misma escala.
- Detectar valores atípicos (muy alejados del resto de valores).
- Trabajar con variables muy diferentes sin que las unidades influyan.

## Medidas de Forma
Nos ayudan a entender **cómo se distribuyen los datos** más allá de si están más o menos dispersos. Permiten ver si los datos están **equilibrados o desviados respecto a la posición central (Asimetría de Fisher)** y si están **muy concentrados o muy repartidos (curtosis).**
- **Coeficiente de Asimetría de Fisher**: Si es **menor que 0** los datos son **asimétricos a la izquierda**. Forman una **campana de Gauss**. Si es **mayor que 0** son **asimétricos a la derecha**. Si es **0** son **simétricos**.
- Medida de **Curtosis** o Apuntamiento o Deformación: Si es **menor que cero** los datos son **platicúrticos** (achatados). Si es **mayor que 0** son **leptocúrticos** (puntiagudos). Si es **0** son **mesocúrticos** (intermedios, ni más platicúrticos que leptocúrticos ni más leptocúrticos que platicúrticos).

## Resumen de las medidas para variables cuantitativas, su significado y cómo influye la dispersión en cada una:
- Medidas de Tendencia Central:
    - Media aritmética:
        Promedio de todos los valores.
        Muy sensible a valores extremos. A más dispersión, menos representatividad.
    - Media ponderada:
        Promedio que considera el peso o frecuencia de cada valor.
        Si los pesos son muy dispersos puede sesgar el resultado hacia los valores más frecuentes.
    - Mediana:
        Valor central de la distribución ordenada.
        Poco afectada por la dispersión. Representativa incluso con datos muy dispersos.
    - Moda:
        Valor que más se repite.
        Puede no existir o haber varias. A más dispersión, menos representatividad.
- Medidas de Dispersión:
    - Desviación media
    - Varianza muestral:
        Cuadrado de la desviación estándar.
        Mide la dispersión total. A mayor varianza menos representativa es la media.
    - Desviación estándar:
        Promedio de las diferencias respecto a la media.
        Cuanto mayor sea más dispersos están los datos. Reduce la fiabilidad de la media como resumen de la distribución.
    - Coeficiente de variación:
        Relación entre la desviación estándar y la media.
        Permite comparar dispersiones entre variables con distintas unidades.
    - Rango:
        Diferencia entre el valor máximo y mínimo.
        Muy sensible a valores extremos. No refleja bien la dispersión interna.
    - Rango intercuartílico:
        Diferencia entre el tercer y primer cuartil.
        Mide la dispersión del 50% central. Menos sensible a valores extremos.
    - Error estándar de la media (esta no la hemos visto):
        Estima la precisión de la media como representante de la población.
        Cuanto mayor sea, más fiable es la media.
- Medidas de Forma:
    - Coeficientes de asimetría o sesgo:
        - Coeficiente de asimetría de Fisher:
            Relación entre la desviación de los datos a ambos lados de la posición central.
        - Coeficiente de asimetría de Pearson:
            Versión adimensional de la varianza.
            Mide la falta de simetría en una distribución de datos.
    - Curtosis:
        Mide lo concentrados o repartidos que están los datos respecto a la posición central.
- Medidas de Posición (cuantiles)

        































