## **Evaluación 2: La raíz que se esconde**

### Integrante: Andy Rivera Olguin

---

### **Introducción**

En este trabajo se implementaron los métodos de Bisección, Falsa Posición, Punto Fijo, Secante, Newton-Raphson y Newton-Raphson Mejorado utilizando Python, NumPy y Matplotlib. El objetivo fue comparar su comportamiento en funciones polinómicas, logarítmicas, exponenciales, trigonométricas y mixtas, registrando iteraciones, aproximaciones de raíces y errores con una tolerancia de 1e-6.

---

## **1\. ¿Qué método convergió en menos iteraciones en cada función? ¿Por qué?**

En la función polinómica simple f(x)=x3−x−2f(x)=x^3-x-2, los métodos que convergieron en menos iteraciones fueron Newton-Raphson y Newton-Raphson Mejorado, ambos con aproximadamente 3 iteraciones según los datos obtenidos.

Los métodos cerrados, como Bisección y Falsa Posición, requirieron una mayor cantidad de iteraciones porque reducen progresivamente un intervalo de búsqueda. En cambio, Newton-Raphson y Newton-Raphson Mejorado utilizan información de la derivada para aproximarse rápidamente a la raíz.

Secante y Punto Fijo mostraron un comportamiento intermedio, requiriendo más iteraciones que Newton pero menos que los métodos cerrados.

Por lo tanto, el método más eficiente en términos de iteraciones fue Newton-Raphson, seguido muy de cerca por Newton-Raphson Mejorado.

---

## **2\. ¿Qué orden de convergencia tiene cada método y cómo se refleja en el gráfico |error| vs iteración?**

Según la teoría presentada en la guía:

* Bisección: convergencia lineal.  
* Falsa Posición: convergencia lineal.  
* Punto Fijo: convergencia lineal.  
* Secante: convergencia superlineal (≈1,618).  
* Newton-Raphson: convergencia cuadrática.  
* Newton-Raphson Mejorado: convergencia cuadrática.

Esto se aprecia claramente en el gráfico de convergencia:

* Bisección disminuye el error lentamente.  
* Falsa Posición mejora ligeramente respecto de Bisección.  
* Punto Fijo reduce el error más rápidamente.  
* Secante presenta una caída pronunciada del error.  
* Newton-Raphson y Newton-Raphson Mejorado muestran la caída más abrupta, llegando al error mínimo en muy pocas iteraciones.

El comportamiento observado coincide con los órdenes de convergencia descritos en la pauta.

---

## **3\. ¿Qué métodos requieren un intervalo con cambio de signo y cuáles no?**

Los métodos que requieren un intervalo donde exista cambio de signo son:

* Bisección.  
* Falsa Posición.

Ambos necesitan verificar que:

f(a)⋅f(b)\<0f(a)\\cdot f(b)\<0

antes de iniciar el procedimiento.

Los métodos que no requieren cambio de signo son:

* Punto Fijo.  
* Secante.  
* Newton-Raphson.  
* Newton-Raphson Mejorado.

Estos métodos abiertos trabajan a partir de una o más aproximaciones iniciales y no necesitan encerrar la raíz dentro de un intervalo.

---

## **4\. En la función que toca el eje x (raíz doble): ¿qué métodos fallan o no aplican y cuál se comporta mejor? ¿Por qué?**

La función:

f(x)=(x−2)2f(x)=(x-2)^2

posee una raíz doble en x=2x=2. En este caso la función toca el eje x pero no cambia de signo a ambos lados de la raíz.

Debido a ello:

* Bisección no puede aplicarse correctamente.  
* Falsa Posición tampoco puede utilizarse porque no existe cambio de signo.

Los métodos abiertos sí pueden aplicarse utilizando aproximaciones iniciales adecuadas.

Entre ellos, Newton-Raphson y Newton-Raphson Mejorado presentan el mejor comportamiento debido al uso de derivadas, permitiendo aproximarse a la raíz aun cuando no exista cambio de signo.

Este caso demuestra que tener una raíz no implica necesariamente que exista un cambio de signo.

---

## **5\. ¿Cómo influyen el intervalo inicial y la estimación inicial en la cantidad de iteraciones y en si el método converge?**

La elección de valores iniciales influye directamente en el desempeño de los métodos.

En los métodos cerrados:

* Un intervalo que encierre correctamente la raíz garantiza convergencia.  
* Un intervalo más amplio suele aumentar la cantidad de iteraciones.

En los métodos abiertos:

* Una estimación inicial cercana a la raíz reduce considerablemente el número de iteraciones.  
* Una estimación inadecuada puede provocar convergencia lenta o incluso divergencia.

Por este motivo, la selección adecuada de intervalos y estimaciones iniciales es fundamental para mejorar la eficiencia de los algoritmos.

---

## **6\. ¿Qué método recomiendan según el tipo de función, considerando el compromiso entre velocidad y robustez?**

Si se conoce poco acerca de la función y se dispone de un intervalo con cambio de signo, se recomienda utilizar Bisección porque es el método más robusto y confiable.

Si se desea mejorar la velocidad manteniendo la seguridad del intervalo, Falsa Posición es una buena alternativa.

Cuando se dispone de derivadas y de una estimación inicial razonable, Newton-Raphson es la mejor opción debido a su rápida convergencia.

Si la derivada no está disponible, Secante constituye una excelente alternativa porque ofrece una velocidad cercana a Newton-Raphson sin necesidad de calcular derivadas.

Por tanto:

* Máxima robustez → Bisección.  
* Mejor equilibrio → Secante.  
* Máxima velocidad → Newton-Raphson.

---

# **Conclusión**

El desarrollo de esta evaluación permitió comparar distintos métodos numéricos de búsqueda de raíces en funciones con características variadas. Los resultados mostraron que la elección del método depende tanto del tipo de función como de la información disponible sobre ella. Los métodos de intervalo, como Bisección y Falsa Posición, demostraron ser más robustos, ya que garantizan la convergencia cuando existe un cambio de signo en el intervalo inicial, aunque requieren una mayor cantidad de iteraciones. En contraste, Newton-Raphson y Newton-Raphson Mejorado fueron los más rápidos, alcanzando la solución en muy pocas iteraciones gracias al uso de derivadas, mientras que Secante ofreció un buen equilibrio entre velocidad y simplicidad al no necesitar el cálculo explícito de derivadas.

El análisis de la función con raíz doble permitió comprobar que una función puede tener una raíz sin necesariamente cambiar de signo. En este caso, los métodos basados en intervalos no resultan adecuados, mientras que los métodos abiertos continúan siendo capaces de aproximarse a la solución si se eligen apropiadamente las estimaciones iniciales. Esto evidencia que las condiciones de aplicación de cada algoritmo son tan importantes como la existencia de la raíz misma.

Finalmente, se observó que la selección del intervalo inicial o de la aproximación inicial influye directamente en la velocidad de convergencia e incluso en la posibilidad de encontrar una solución. Estimaciones más cercanas a la raíz reducen significativamente el número de iteraciones necesarias, mientras que valores iniciales poco adecuados pueden ralentizar el proceso o provocar que algunos métodos no converjan. En conclusión, Newton-Raphson y Newton-Raphson Mejorado fueron los métodos más eficientes en los experimentos realizados, Secante destacó como una excelente alternativa cuando no se dispone de derivadas, y Bisección se mantuvo como la opción más robusta y confiable cuando se conoce un intervalo con cambio de signo.

