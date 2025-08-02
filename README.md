# Operaciones con Conjuntos y Funciones

## Descripción
Este proyecto implementa un programa en Python para realizar operaciones básicas con conjuntos (unión, intersección, diferencia, complemento y producto cartesiano) y verificar si una relación es una función. La documentación en LaTeX, que incluye la especificación, implementación y resultados, se creará por separado en un entorno en línea.

## Características
- **Operaciones con Conjuntos**: Realiza unión, intersección, diferencia, complemento y producto cartesiano sobre conjuntos definidos.
- **Verificación de Funciones**: Comprueba si una relación dada es una función de un conjunto a otro.
- **Resultados**: Muestra los conjuntos definidos y los resultados de las operaciones en la consola.

## Estructura del Repositorio
- `main.py`: Script en Python que implementa las operaciones con conjuntos y la verificación de funciones.

## Requisitos
- **Python**: Versión 3.x o superior.

## Instrucciones de Uso
1. **Ejecutar el programa Python**:
   - Asegúrate de tener Python instalado.
   - Ejecuta el script con el comando:
     ```bash
     python main.py
     ```
   - El programa mostrará los conjuntos definidos, los resultados de las operaciones solicitadas (`A \ B`, `fun(E)`, `D \ U`) y la verificación de si la relación `E` es una función.

2. **Documentación en LaTeX**:
   - La documentación se creará en un entorno en línea (por ejemplo, Overleaf).
   - Incluye los conjuntos, las operaciones realizadas, los resultados y una captura de pantalla de la salida del programa.
   - Asegúrate de tomar una captura de pantalla de la ejecución de `main.py` para incluirla en el documento LaTeX.

## Ejemplo de Salida
```
Conjuntos:
U = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', '1', '2', '3', '4', '5'}
A = {'a', '1', '3', 'd', 'g', 'h', '4', '5'}
B = {'2', '1', '4', 'e', 'f', 'g', 'k'}
C = {'b', 'd', 'f', 'h', 'k', '2', '4'}
D = set()
E = {(1, 'a'), (2, 'b'), (3, 'c')}

Operaciones:
A \ B = {'a', '3', 'd', 'h', '5'}
fun(E) = True
D \ U = set()
```

## Notas
- Este proyecto fue desarrollado como parte de un ejercicio académico sobre teoría de conjuntos y funciones.
- La documentación LaTeX debe crearse por separado en un entorno en línea, incluyendo una captura de pantalla de la salida del programa.
- Los archivos deben cargarse en Canvas según las instrucciones del curso.

## Grupo 1