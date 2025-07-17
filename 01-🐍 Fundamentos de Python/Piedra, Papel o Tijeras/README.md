# 🪨 Piedra, Papel o Tijeras – Juego en Consola

Este es un juego simple de "Piedra, Papel o Tijeras" donde el jugador compite contra la computadora. Fue desarrollado como parte de mi aprendizaje en fundamentos de Python siguiendo el curso de [freeCodeCamp – Learn Python Full Course for Beginners](https://www.youtube.com/watch?v=rfscVS0vtbw).

---

## 🎮 ¿Cómo funciona?

- El jugador elige una opción: `piedra`, `papel` o `tijeras`.
- La computadora elige aleatoriamente una de las tres opciones.
- Se comparan ambas elecciones y se determina el ganador con base en las reglas clásicas:

| Jugador      | Computadora | Resultado     |
|--------------|-------------|----------------|
| piedra       | tijeras     | Gana jugador   |
| papel        | piedra      | Gana jugador   |
| tijeras      | papel       | Gana jugador   |
| ...          | ...         | Pierde jugador o empate |

---

## 🧠 Lógica implementada

- Entrada del usuario con validación (`input()`).
- Elección aleatoria con `random.choice()`.
- Diccionario para organizar las elecciones.
- Comparación condicional para decidir el resultado.
- Mensajes claros para cada posible resultado.

---

## ▶️ Cómo ejecutar

Asegúrate de tener Python instalado. Luego, en la terminal:

```bash
python piedra_papel_tijeras.py
