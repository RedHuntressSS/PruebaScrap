# Desafío Teórico 
## Consigna 
### Procesos, hilos y corrutinas 
- **Un caso en el que usarías procesos para resolver un problema y por qué:**
Teniendo en cuenta que cada proceso reserva un espacio de memoria para código, archivos, datos y demás, se podría afirmar que es conveniente hacer uso de los procesos en los casos en los que nos interesa acceder a dichos recursos y mantenerlos guardados durante la ejecución de un programa.
- **Un caso en el que usarías threads para resolver un problema y por qué:**
El uso de los hilos puede optimizar un proceso cuando se cuenta con un sistema multiprocesador, ya que, al implementar los hilos, en este caso Kernel threads, el sistema operativo aprovecha sus distintos procesadores asignando hilos a cada uno, logrando así una respuesta más rápida; por ejemplo, si el procesador del hardware con el que estemos trabajando tiene dos o más núcleos. Un caso específico podría ser un programa en el que se ejecuten varias peticiones independientes al tiempo, tal como un sistema de pago, en el que puedan efectuarse varios pagos en simultaneo para conseguir un menor tiempo de ejecución.
- **Un caso en el que usarías corrutinas para resolver un problema y por qué:** 
Los casos en los cuales es preferible hacer uso de las corrutinas son aquellos en los que necesitamos manejar código asíncrono, por ejemplo, cuando requerimos esperar la respuesta de una instrucción o corrutina para poder ejecutar otra. Un caso más específico es cuando se requiere trabajar con las llamadas a base de datos, ya que se requiere del contenido de la respuesta de la base de datos para así ejecutar otra operación.
### Optimización de recursos del sistema operativo 
**Si tuvieras 1.000.000 de elementos y tuvieras que consultar para cada uno de ellos información en una API HTTP. ¿Cómo lo harías? Explicar.**
Teniendo en cuenta el volumen de los datos requeridos, y asumiendo que se sabe en concreto la información específica que se requiere de cada uno de los elementos, una de las opciones más viables es hacer uso de GraphQL, ya que este nos permite optimizar el rendimiento de las aplicaciones y el uso de los datos puesto que mediante esta herramienta podemos pedir a una API la información necesaria (con un formato especifico) y obtenerla sin traer información de más con la ventaja de que se realiza una sola instrucción request.
