# AA2_LP
Juego del Ahorcado en Python 
Esta es una versión mejorada desarrollada en Python que incluye un sistema de categorías, pistas visuales en arte ASCII y validación de entradas.

-Características
Sistema de Categorías: Las palabras se seleccionan de temas específicos (Hogar, Tecnología, Mascotas, Naturaleza) para dar una pista inicial al jugador.

Interfaz Visual ASCII: Gráficos que evolucionan conforme pierdes intentos.

Validación Inteligente: El programa reconoce si intentas repetir una letra o si ingresas caracteres no válidos.

Adivinanza Directa: Permite intentar adivinar la palabra completa en cualquier momento.

-Instrucciones de Juego
Al iniciar, verás la categoría de la palabra y el número de letras representadas por guiones bajos (_).

Tienes 6 intentos antes de perder el juego (representados por las partes del cuerpo del ahorcado).

En cada turno puedes:
Escribir una letra.

Escribir la palabra completa si crees saber cuál es.

Si la letra es correcta, se revelará su posición. Si es incorrecta, perderás una vida.

-Estructura del Código
palabras_categorias: Un diccionario que almacena el vocabulario del juego.

obtener_palabra(): Lógica para la selección aleatoria de temas y palabras.

mostrar_ahorcado(): Función que gestiona el arte ASCII según los fallos.

jugar(): El bucle principal que controla la lógica de victoria/derrota.

mostrar_ahorcado(): Función que gestiona el arte ASCII según los fallos.

jugar(): El bucle principal que controla la lógica de victoria/derrota.
