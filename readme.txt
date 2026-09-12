<h1 align="center">🤖 Búsqueda en Laberintos: Algoritmos PP y PA</h1>

<h3 align="center">Proyecto de Inteligencia Artificial I</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PyQt5-41CD52?style=for-the-badge&logo=qt&logoColor=white" alt="PyQt5">
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white" alt="Matplotlib">
</p>

> Este proyecto implementa una aplicación con interfaz gráfica para resolver problemas de búsqueda en un espacio de estados tipo laberinto (10x10 casillas). Para ello, utiliza y compara el rendimiento de los algoritmos de búsqueda no informada **Primero en Profundidad (PP)** y **Primero en Amplitud (PA)**.

---

## 🌟 Características Principales

- 🧩 **Generación Aleatoria:** Creación de laberintos aleatorios de 10x10 casillas para poner a prueba los algoritmos en diferentes escenarios.
- 🚀 **Algoritmo PP (Profundidad):** Encuentra una solución priorizando la exploración por ramas. Es ideal para ahorrar recursos computacionales y realizar menos iteraciones, aunque no garantiza encontrar el camino más corto.
- 🎯 **Algoritmo PA (Amplitud):** Garantiza encontrar el camino de solución óptimo (el más corto), explorando el espacio de estados por niveles, a un costo mayor de procesamiento y memoria.
- 📊 **Visualización Gráfica:** Interfaz interactiva que muestra la matriz del laberinto, renderiza el árbol de expansión (grafos) y detalla la evolución paso a paso de los nodos explorados (lista a explorar y lista de verificados).

---

## 🛠️ Tecnologías y Librerías Utilizadas

El núcleo del sistema está desarrollado en **Python**, apoyado por las siguientes librerías especializadas:

- **PyQt5:** Para la creación y gestión de la interfaz gráfica y ventanas.
- **Matplotlib:** Para la representación gráfica de listas en 2 dimensiones (el laberinto matricial).
- **NetworkX:** Para la construcción de los grafos (nodos y aristas) que representan los árboles de expansión.
- **Random:** Para la generación de números pseudo-aleatorios aplicados a la creación del laberinto.

---

## ⚙️ Instalación y Ejecución

Sigue estos pasos para probar la simulación de los algoritmos en tu entorno local:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/ChoniGomez/TPIA1.git](https://github.com/ChoniGomez/TPIA1.git)
   cd TPIA1
