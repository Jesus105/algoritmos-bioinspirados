### ¿Qué es la Optimización por Enjambre de Partículas (PSO)?

PSO es un método computacional de optimización que simula el comportamiento social de un enjambre, como el de los pájaros o los peces. En PSO, cada "partícula" representa una solución potencial al problema de optimización. Las partículas "vuelan" a través del espacio de soluciones siguiendo las partículas vecinas más exitosas, ajustando sus posiciones en base a sus experiencias propias y las de sus vecinos para encontrar óptimos globales.

#### Principios Básicos del PSO:

1. **Inicialización**: Generar una población inicial de partículas con posiciones y velocidades aleatorias.
2. **Evaluación**: Cada partícula evalúa su posición actual usando una función de aptitud.
3. **Actualización de velocidades y posiciones**: Las partículas actualizan sus velocidades y, por ende, sus posiciones basadas en sus mejores posiciones personales y las mejores posiciones globales conocidas.
4. **Iteración**: El proceso se repite hasta que se cumpla un criterio de terminación, como un número máximo de iteraciones o una suficiente mejora en la aptitud.

### Contenido del Archivo

1. **Función Ackley**: Utilizada como función de prueba para demostrar cómo el PSO puede manejar funciones con múltiples mínimos locales.
2. **Implementación del PSO**: Se incluye probablemente una implementación detallada del PSO, mostrando cómo las partículas interactúan y evolucionan hacia el óptimo.
3. **Visualización del proceso**: Diagramas y gráficos para visualizar el progreso de las partículas a través del espacio de soluciones, mostrando la dinámica del enjambre.

### Uso del Archivo

**Requisitos:**
- Python 3.x
- Librerías: numpy, matplotlib, math, random

**Instrucciones de Uso:**
1. **Instalar las dependencias**: Asegurarse de que todas las librerías requeridas están instaladas.
2. **Ejecutar el notebook**: El notebook puede ser ejecutado en un entorno de Jupyter para observar cómo el algoritmo PSO optimiza la función Ackley.

Este notebook proporciona una excelente oportunidad para entender y visualizar cómo el PSO funciona en práctica, ofreciendo intuiciones sobre la adaptación y el rendimiento del algoritmo en problemas de optimización complejos.