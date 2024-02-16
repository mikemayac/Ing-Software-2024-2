from typing import Dict, Any


class TennisMatch:
    def __init__(self, player1, player2):
        self.players = {
            player1: {'sets': 0, 'games': 0, 'points': 0},
            player2: {'sets': 0, 'games': 0, 'points': 0}
        }
        self.current_server = player1  # Alternará después de cada juego.
        self.match_winner = None
        # self.game_state = "0-0"  # Para control de puntos dentro de un juego.
        self.sets_to_win = 2  # Mejor de 3 sets.
        self.games_played = 1

    def shot_election(self, player1: str, player2: str) -> int:
        """
        Funcion que nos permite introducir por consola para quien es el tiro del jugador.
        :param player1: Jugador1 a sumar el punto.
        :param player2: Jugador2 a sumar el punto.
        :return: Retorna el tiro, 1 o 2, o sea el jugador que gana el punto.
        """
        # Maneja solo la correcta entrada de 1 y 2.
        while True:
            try:
                shot = int(input(
                    f"Elige quien anota el punto de los jugadores, digita 1 es para {player1} y 2 es para {player2}: "))
                if shot == 1 or shot == 2:
                    return shot  # Sale del bucle porque la entrada es valida.
                else:
                    # Lanza una excepción personalizada si la entrada no es 1 o 2.
                    raise ValueError("Número introducido no válido")
            except ValueError as e:
                print(f"Solo puedes introducir 1 o 2, prueba de nuevo! {e} \n")

    def score_point(self, shot):
        """
        Puntuación de los Juegos:
        Esta función se encarga de actualizar la puntuación de los juegos basándose en los puntos ganados por los
        jugadores.
        Debe manejar la secuencia de puntos de 0, 15, 30, 40 y luego convertir el siguiente punto en un juego ganado,
        reiniciando los puntos para el siguiente juego.

        Regla de Ventaja:
        Dentro de score_point, necesitas manejar el caso de "deuce" (40-40), donde un jugador debe obtener dos puntos
        consecutivos para ganar el juego. Esto implica gestionar la "ventaja" y volver a "deuce" si el jugador contrario
        gana el siguiente punto.
        :param shot:
        :param player:
        :return:
        """
        # Si el tiro es para jugador 1, le sumamos un punto y se imprime la puntuacion
        if shot == '1':
            self.players[player1]['points'] += 1
            print(f"Punto para {player1}.")
            print(
                f"El marcador es {player1}:{self.players[player1]['points']} {player2}:{self.players[player2]['points']}")
        # Si el tiro es para jugador 2, le sumamos un punto y se imprime la puntuacion
        else:  # Para player2, cubre del 11 al 15.
            self.players[player2]['points'] += 1
            print(f"Punto para {player2}.")
            print(
                f"El marcador es {player2}:{self.players[player1]['points']} {player2}:{self.players[player2]['points']}")

    def check_game_winner(self):
        """
        Gana un juego:
        Determina si un jugador ha ganado un juego dentro del set actual.
        Actualiza el conteo de juegos del ganador y resetea los puntos de ambos jugadores.
        También verifica condiciones de 'deuce' y 'ventaja'.
        """
        pass

    def check_set_winner(self):
        """
        Gana un Set:
        Implementa la lógica para determinar si un jugador ha ganado un set (alcanzando 6 juegos con una diferencia de
        al menos 2 juegos). También debe manejar casos especiales como 7-5 o 8-6.
        :return:
        """
        pass

    def check_match_winner(self):
        """
        Gana ya totalmente el partido:
        Verificar si un jugador ha ganado el partido.
        Debe revisar si alguno de los jugadores ha alcanzado los 2 sets ganados necesarios en un partido al mejor de 3 sets.
        Actualiza self.match_winner con el nombre del ganador del partido cuando se determina un ganador.
        """
        pass

    def switch_server(self):
        """
        Cambio de Saque
        Después de que se completa un juego, esta función cambia el servidor al otro jugador. Asegúrate de que el cambio
        se realice correctamente después de cada juego.
        :return:
        """
        pass

    def update_court_side(self):
        """
        Cambio de Cancha:
        Esta función debe verificar si es necesario cambiar de lado basándose en el número total de juegos jugados.
        Debe ser llamada después de cada juego para determinar si se requiere un cambio de cancha.
        :return:
        """
        pass

    def display_score(self, players: Dict[str, Dict[str, Any]]) -> None:
        """
        Utilizada para mostrar el marcador actual, incluidos los puntos, juegos y sets para cada jugador.
        Debe reflejar la lógica correcta del marcador y el estado actual del partido.
        :return: No regresa nada, solo imprime la cadena.
        """
        for player, stats in players.items():
            print(f"{player} tiene {stats['points']} puntos en este juego, ha ganado {stats['games']} juegos y ha "
                  f"sido el mejor en {stats['sets']} sets.")
        print()  # Salto de linea

    def main(self):
        """
        Método principal para ejecutar el bucle del juego, obtener entradas del usuario, llamar a las funciones
        correspondientes para marcar puntos y actualizar el estado del juego, y manejar errores de entrada con
        estructuras try-except.
        :return:
        """
        # while not self.match_winner:
        #     try:
        #         # # Obtener entrada del usuario y actualizar el marcador.
        #         # input_str = input("Ingrese el jugador que gana el punto: ")
        #
        #         self.playing(player1, player2)
        #         # self.score_point(input_str)
        #         self.display_score()
        #     except Exception as e:
        #         print(f"Error: {e}. Intente nuevamente.")
        print(f"\n*** Se esta jugando un partido de tennis en este momento, es el juego #{self.games_played} ***\n")
        # Imprimimos el status del juego.
        self.display_score(self.players)
        # Aumentamos el contador de juegos jugados en uno para el siguiente juego.
        self.games_played += 1
        self.shot_election(player1, player2)


if __name__ == "__main__":
    player1 = input("Nombre del jugador 1: ")
    player2 = input("Nombre del jugador 2: ")
    match = TennisMatch(player1, player2)
    match.main()
