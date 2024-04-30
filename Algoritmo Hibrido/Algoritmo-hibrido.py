"""
Nombre del programa: Algoritmo Hibrido (Algorimto génetico y Recocido simulado)
utores: -Jesús Méndez Chávez
Grupo: 5BM1
Descripción: Es un programa de optimización de funciones que utiliza algoritmos genéticos y el método de recocido simulado para encontrar los valores óptimos de funciones matemáticas.
Fecha: 23 de junio de 2023
"""

#Importando librerías de python
import matplotlib.pyplot as plt
import numpy as np
import math
import random


# Funciones Benchmark

def fun_ackley(x):
    """
    Esta función calcula el valor de la función de Ackley para un punto x en el espacio.
    La función de Ackley es una función de prueba utilizada en la optimización global.
    Recibe como parámetro un arreglo x de coordenadas.
    Devuelve el valor de la función de Ackley evaluada en el punto x.
    """
    n = len(x)
    sum_sq = sum(xi**2 for xi in x)
    sum_cos = sum(math.cos(2*math.pi*xi) for xi in x)
    return -20 * math.exp(-0.2 * math.sqrt(sum_sq / n)) - math.exp(sum_cos / n) + 20 + math.e

def fun_rosenbrock(x):
    """
    Esta función calcula el valor de la función de Rosenbrock para un punto x en el espacio.
    La función de Rosenbrock es una función de prueba utilizada en la optimización global.
    Recibe como parámetro un arreglo x de coordenadas.
    Devuelve el valor de la función de Rosenbrock evaluada en el punto x.
    """
    sum = 0
    n = 0
    while n < 4:
        sum = sum + 100*((x[n]**2)-x[n+1])**2 + (1-x[n])**2
        n = n + 1

    return sum

def grafica(funcion, name):
    """
    Esta función genera una gráfica 3D de una función dada.
    Recibe como parámetros la función a graficar y un nombre para la función.
    Muestra la gráfica en una ventana.
    """
    # Generar datos para el gráfico
    x = np.linspace(-0.5, 0.5, 1000)
    y = np.linspace(-0.5, 0.5, 1000)
    x, y = np.meshgrid(x, y)
    z = np.zeros_like(x)

    for i in range(len(x)):
        for j in range(len(y)):
            z[i, j] = funcion([x[i, j], y[i, j], 0, 0, 0])  # Puedes agregar más ceros si necesitas más dimensiones

    # Crear la figura 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Graficar la función
    ax.plot_surface(x, y, z, cmap='viridis')

    # Configurar etiquetas y título
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Función ' + name)

    # Mostrar el gráfico
    plt.show()

# Función de recocido simulado

def simulated_annealing(n, initial_solution, initial_temperature, cooling_rate, function, resolucion):
    """
    Esta función implementa el algoritmo de recocido simulado para la optimización global.
    Recibe como parámetros el número de dimensiones del problema, la solución inicial, la temperatura inicial,
    la tasa de enfriamiento, la función a optimizar y la resolución deseada.
    Devuelve la mejor solución encontrada, el valor de la función para esa solución y una lista con los valores de energía durante la búsqueda.
    """
    current_solution = initial_solution
    best_solution = current_solution
    current_temperature = initial_temperature
    energy_values = []  # Lista para almacenar los valores de energía durante la búsqueda

    while function(best_solution) > 1*(10**(-1*resolucion)):
        for _ in range(n):
            new_solution = current_solution.copy()
            index = random.randint(0, n-1)
            new_solution[index] += random.uniform(-1, 1)

            current_energy = function(current_solution)
            new_energy = function(new_solution)

            if new_energy < current_energy:
                current_solution = new_solution
                if new_energy < function(best_solution):
                    best_solution = new_solution
            else:
                probability = math.exp((current_energy - new_energy) / current_temperature)
                if random.random() < probability:
                    current_solution = new_solution

        current_temperature *= cooling_rate
        energy_values.append(function(best_solution))  # Agregar el valor de energía a la lista

    return best_solution, function(best_solution), energy_values

# Funciones del algoritmo genético:

def initialize_population(population_size, n_dimensions, lower_bound, upper_bound):
    """
    Esta función inicializa una población para el algoritmo genético.
    Recibe como parámetros el tamaño de la población, el número de dimensiones del problema,
    los límites inferiores y superiores para los valores de las variables.
    Devuelve una lista de individuos (arreglos) que representan a la población inicializada.
    """
    population = []
    for _ in range(population_size):
        individual = [random.uniform(lower_bound, upper_bound) for _ in range(n_dimensions)]
        population.append(individual)
    return population

def evaluate_population(population, function):
    """
    Esta función evalúa la población dada utilizando la función dada.
    Recibe como parámetros la población y la función a evaluar.
    Devuelve una lista de los valores de ajuste (fitness) de cada individuo en la población.
    """
    fitness_values = []
    for individual in population:
        fitness_values.append(function(individual))
    return fitness_values

def select_parents(population, fitness_values, num_parents):
    """
    Esta función selecciona los padres para la siguiente generación del algoritmo genético.
    Recibe como parámetros la población, los valores de ajuste de la población y el número de padres a seleccionar.
    Devuelve una lista de los padres seleccionados.
    """
    parents = []
    sorted_indices = sorted(range(len(fitness_values)), key=lambda k: fitness_values[k])
    for i in range(num_parents):
        parents.append(population[sorted_indices[i]])
    return parents

def crossover(parents, population_size):
    """
    Esta función realiza el operador de cruce para generar descendencia en el algoritmo genético.
    Recibe como parámetros los padres seleccionados y el tamaño de la población.
    Devuelve una lista de individuos (descendencia) generados mediante el cruce.
    """
    offspring = []
    for _ in range(population_size):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        child = []
        for i in range(len(parent1)):
            if random.random() < 0.5:
                child.append(parent1[i])
            else:
                child.append(parent2[i])
        offspring.append(child)
    return offspring

def mutate(offspring, mutation_rate, lower_bound, upper_bound):
    """
    Esta función realiza el operador de mutación para la descendencia en el algoritmo genético.
    Recibe como parámetros la descendencia generada, la tasa de mutación y los límites inferiores y superiores para los valores de las variables.
    Devuelve la descendencia con mutaciones aplicadas.
    """
    for i in range(len(offspring)):
        for j in range(len(offspring[i])):
            if random.random() < mutation_rate:
                offspring[i][j] = random.uniform(lower_bound, upper_bound)
    return offspring

def genetic_algorithm(population_size, n_dimensions, lower_bound, upper_bound, num_parents, mutation_rate, num_generations, function):
    """
    Esta función implementa el algoritmo genético para la optimización de funciones.
    Recibe como parámetros el tamaño de la población, el número de dimensiones del problema,
    los límites inferiores y superiores para los valores de las variables, el número de padres a seleccionar,
    la tasa de mutación, el número de generaciones y la función a optimizar.
    Devuelve el mejor individuo encontrado, el valor de ajuste correspondiente y una lista de los mejores valores de ajuste por generación.
    """
    population = initialize_population(population_size, n_dimensions, lower_bound, upper_bound)
    best_fitness_values = []  # Lista para almacenar los mejores valores de ajuste por generación

    for _ in range(num_generations):
        fitness_values = evaluate_population(population, function)
        best_fitness_values.append(min(fitness_values))  # Agregar el mejor valor de ajuste a la lista

        parents = select_parents(population, fitness_values, num_parents)
        offspring = crossover(parents, population_size)
        offspring = mutate(offspring, mutation_rate, lower_bound, upper_bound)

        population = offspring

    best_solution = population[fitness_values.index(min(fitness_values))]
    return best_solution, min(fitness_values), best_fitness_values


def run(dimensiones, function, resolucion, funName):
    """
    Esta función ejecuta el programa de optimización de funciones utilizando el algoritmo genético y el recocido simulado.
    Recibe como parámetros el número de dimensiones del problema, la función a optimizar, la resolución deseada,
    y el nombre de la función para mostrar en la gráfica.
    No devuelve ningún valor, pero muestra los resultados y las gráficas correspondientes.
    """
    # Configuración del problema:
    n_dimensions = dimensiones
    lower_bound = -32
    upper_bound = 32

    # Parametros genéticos
    num_parents = 10
    mutation_rate = 0.01
    num_generations = 20000
    population_size = 150

    # Parametros recocido simulado
    initial_temperature = 100
    cooling_rate = 0.85

    # Ejecución del algoritmo genético
    best_solution, min_value, best_fitness_values = genetic_algorithm(population_size, n_dimensions, lower_bound, upper_bound, num_parents, mutation_rate, num_generations, function)
    print("Algoritmo genético")
    print(f'El mejor valor encontrado por el algoritmo genético fue: {min_value}')

    # Ejecución del recocido simulado
    best_solution, min_value, energy_values, num_iter = simulated_annealing(n_dimensions, best_solution, initial_temperature, cooling_rate, function, resolucion)
    print("Recocido simulado")
    print(f'El mejor valor encontrado por el recocido simulado fue: {min_value} después de {num_iter}')

    # Gráfico de la función
    grafica(function, funName)

    # Gráfico de los mejores valores de ajuste por generación
    plt.plot(best_fitness_values)
    plt.xlabel('Generación')
    plt.ylabel('Mejor Valor de Ajuste')
    plt.title('Evolución del Mejor Valor de Ajuste')
    plt.show()

#Ejecución del programa principal
if __name__ == '__main__':
    # Variable para controlar el flujo del programa
    fun = 1
    
    print("Bienvenido al programa de optimización de funciones")
    while fun != 0:
        try:
            # Solicitar al usuario que seleccione la función a optimizar
            fun = int(input("Seleccione la función que desea optimizar\n[1] Función de Ackley\n[2] Función de Rosenbrock\n[0] Salir\n"))
            
            if fun == 1:
                # Optimización de la función de Ackley
                print("Optimización de la función de Ackley")
                try:
                    # Solicitar al usuario el número de dimensiones y la resolución deseada
                    dim = int(input("Ingrese en número de dimensiones para la función: "))
                    res = int(input("Ingrese la resolución que desea para la función (ej. 1.1E-06 input = 6): "))
                except:
                    print("Debe ingresar una opción válida")
                
                # Mostrar gráfico de la función de Ackley
                grafica(fun_ackley, "de Ackley")
                
                # Ejecutar el programa de optimización para la función de Ackley
                run(dim, fun_ackley, res, "Ackley")
                
            elif fun == 2:
                # Optimización de la función de Rosenbrock
                print("Optimización de la función de Rosenbrock")
                try:
                    # Solicitar al usuario el número de dimensiones y la resolución deseada
                    dim = int(input("Ingrese en número de dimensiones para la función: "))
                    res = int(input("Ingrese la resolución que desea para la función (ej. 1.1E-06 input = 6): "))
                except:
                    print("Debe ingresar una opción válida")
                
                # Mostrar gráfico de la función de Rosenbrock
                grafica(fun_rosenbrock, "de Rosenbrock")
                
                # Ejecutar el programa de optimización para la función de Rosenbrock
                run(dim, fun_ackley, res, "Rosenbrock")
                
            elif fun == 0:
                # Salir del programa
                print("Hasta pronto")
                
            else:
                # Opción inválida
                print("Ingrese una opción válida.")
                
        except:
            print("Debe ingresar un número")

   