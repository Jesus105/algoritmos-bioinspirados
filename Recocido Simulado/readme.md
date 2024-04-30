### ¿Qué es el Recocido Simulado?

El recocido simulado (Simulated Annealing, SA) es un método probabilístico para la aproximación del óptimo global de una función dada. Inspirado en el proceso físico de calentamiento y enfriamiento de materiales para aumentar su tamaño de grano y reducir sus defectos, el algoritmo toma su nombre del recocido en metalurgia. Este método es especialmente útil para problemas donde el espacio de búsqueda es grande y los métodos tradicionales quedan atrapados en mínimos locales.

#### Principios Básicos del Recocido Simulado:

1. **Generación de una solución inicial**: Se empieza con una solución aleatoria.
2. **Ciclo de enfriamiento**: A medida que el algoritmo progresa, la "temperatura" del sistema se reduce gradualmente.
3. **Generación de nuevas soluciones**: En cada paso, se genera una nueva solución mediante una pequeña perturbación de la solución actual.
4. **Aceptación por probabilidad**: Las nuevas soluciones pueden ser aceptadas si mejoran la función objetivo, o con una cierta probabilidad si la empeoran, dependiendo de la temperatura actual.
5. **Criterio de terminación**: El algoritmo se detiene después de un número fijo de iteraciones o cuando la temperatura es suficientemente baja.

### Contenido del Archivo

1. **Función Michalewicz**: Se utiliza para probar el algoritmo en un contexto donde es desafiante encontrar el mínimo global debido a los múltiples mínimos locales.
2. **Visualización de resultados**: Mediante gráficos se puede observar cómo el algoritmo explora el espacio de soluciones y cómo evoluciona la búsqueda del óptimo a lo largo de las iteraciones.

### Uso del Archivo

**Requisitos:**
- Python 3.x
- Librerías: numpy, matplotlib, math, random

**Instrucciones de Uso:**
1. **Instalar las dependencias**: Asegúrate de que todas las librerías necesarias están instaladas.
2. **Ejecutar el notebook**: Puedes correr el notebook en un entorno de Jupyter para ver cómo el recocido simulado trabaja en la optimización de la función Michalewicz.

Este archivo proporciona un ejemplo práctico de cómo implementar y evaluar el recocido simulado en un problema de optimización complejo, demostrando la utilidad de esta técnica en contextos donde otras estrategias podrían fallar al encontrar soluciones óptimas.