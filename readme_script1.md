# Simulador de Partido de Tenis

Este programa simula un partido de tenis entre dos jugadores. Se hace seguimiento de los puntos, juegos y sets, siguiendo las reglas del tenis para determinar el ganador del partido.

## Cómo Usar

### Iniciando el Programa

1. Ejecuta `Script1.py` en tu entorno Python.
2. Cuando se solicite, introduce los nombres de los dos jugadores que competirán en el partido.

### Jugando el Partido

- El programa pedirá entrada para decidir quién gana cada punto.
- Debes ingresar `1` si el Jugador 1 gana el punto, o `2` si el Jugador 2 gana el punto.
- La puntuación será actualizada y mostrada después de cada punto, mostrando el estado actual de puntos, juegos y sets para ambos jugadores.

### Reglas a Seguir

- El partido sigue un formato al mejor de tres sets.
- Un juego es ganado por el primer jugador en alcanzar 4 puntos (0, 15, 30, 40) y tener al menos 2 puntos de ventaja.
- Si el juego alcanza un empate 40-40, pasa a "deuce". Desde el deuce, un jugador debe ganar dos puntos consecutivos para ganar el juego.
- Un set es ganado por el primer jugador en ganar 6 juegos y tener al menos 2 juegos de ventaja. Si el set alcanza un empate 6-6, el juego continúa hasta que un jugador tenga una ventaja de 2 juegos.
- El partido termina cuando un jugador gana 2 sets.

### Formato de Entrada

- Durante el juego, el programa indicará: `Elige quien gana el punto, digita 1 para [Jugador 1] y 2 es para [Jugador 2]:`
- Responde con `1` o `2` de acuerdo a quién gane el punto.

### Ejemplo

```
Bienvenido al juego de tenis!
Van a jugar 2 jugadores, ingresa sus nombres.

Nombre del jugador 1: Alicia
Nombre del jugador 2: Roberto

*** Se está jugando un partido de tenis en este momento, es el juego #1 ***
Alicia [puntos:0 juegos:0 sets:0]
Roberto [puntos:0 juegos:0 sets:0]

Elige quien gana el punto, digita 1 para Alicia y 2 es para Roberto: 1
```

Sigue las indicaciones hasta que el partido concluya y se declare un ganador.

---
