# Desafío Teórico 
## Consigna 
### Procesos, hilos y corrutinas 
- Un caso en el que usarías procesos para resolver un problema y por qué:
Teniendo en cuenta que cada proceso reserva un espacio de memoria para código, archivos, datos y demás, se podría afirmar que es conveniente hacer uso de los procesos en los casos en los que nos interesa acceder a dichos recursos y mantenerlos guardados durante la ejecución de un programa.
- Un caso en el que usarías threads para resolver un problema y por qué:
Un caso en el cual sería optimo hacer uso de los hilos es por ejemplo cuando se cuenta con un sistema multiprocesador, ya que, al implementar los hilos, en este caso Kernel threads, el sistema operativo aprovecha sus distintos procesadores asignando hilos a cada uno, logrando así una respuesta más rápida.
- Un caso en el que usarías corrutinas para resolver un problema y por qué: 
Los casos en los cuales es preferible hacer uso de las corrutinas son aquellos en los que necesitamos manejar código asíncrono, por ejemplo, cuando requerimos esperar la respuesta de una instrucción o corrutina para poder ejecutar otra.
### Optimización de recursos del sistema operativo 
Si tuvieras 1.000.000 de elementos y tuvieras que consultar para cada uno de ellos información en una API HTTP. ¿Cómo lo harías? Explicar.
