# Prueba Técnica - RuufSolar  

Este repositorio contiene la solución a la prueba técnica para la postulación a **RuufSolar**. La prueba consiste en calcular la cantidad máxima de paneles solares que pueden colocarse en un techo, considerando las dimensiones de los paneles y del techo, y optimizando el uso del espacio disponible.  

## Descripción del Problema  

Dado un techo de dimensiones `X` e `Y` y paneles solares de dimensiones `A` y `B`, el objetivo es determinar cuántos paneles pueden colocarse en el techo, considerando:  
- La orientación original de los paneles.  
- La posibilidad de rotar los paneles en los espacios restantes.  

La solución debe manejar casos en los que el techo no pueda alojar ningún panel debido a restricciones de tamaño.  

## Solución Implementada  

El algoritmo sigue los siguientes pasos:  
1. Calcular cuántos paneles caben en la orientación original (`A x B`).  
2. Determinar el espacio restante en los ejes `X` e `Y` tras colocar los paneles.  
3. Evaluar si en los espacios restantes pueden colocarse paneles en orientación rotada (`B x A`).  
4. Sumar los paneles adicionales colocados en los espacios restantes al total

## Soluciones Descartadas  

Durante el desarrollo de esta prueba técnica, se consideraron otras aproximaciones al problema, pero fueron descartadas por los siguientes motivos:  

1. **Solución No Determinista**  
   - Se planteó utilizar un enfoque no determinista, probando diferentes configuraciones posibles de paneles de manera aleatoria o probabilística para aproximar el resultado.  
   - **Motivo de descarte**: Este enfoque no garantiza consistencia en los resultados ni asegura encontrar la solución óptima en todos los casos. Además, añade complejidad innecesaria al tratarse de una prueba técnica que busca claridad y precisión.  

2. **Optimización con Derivadas**  
   - Se consideró modelar el problema como una función continua que maximizara el área cubierta por los paneles, aplicando derivadas para encontrar los puntos críticos (máximos locales o globales).  
   - **Motivo de descarte**: Aunque teóricamente interesante, este enfoque no es adecuado para un problema discreto como este, donde las dimensiones del techo y los paneles son números enteros. Dado que es una prueba técnica, la solución buscaba simplicidad y practicidad para ser explicada.  

## Contacto

Email: Diego.Codina2201@alumnos.ubiobio.cl
Telefono: +56 9 6591 5091
LinkedIn: https://www.linkedin.com/in/diego-codina-pino/
