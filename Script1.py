from typing import Dict, Any


class TennisMatch:
    def __init__(self):
        self.players = {
            player1: {'points': 0, 'games': 0, 'sets': 0},
            player2: {'points': 0, 'games': 0, 'sets': 0}
        }
        self.current_server = player1  # Alternará después de cada juego.
        self.match_winner = None
        self.sets_to_win = 2  # Mejor de 3 sets.
        self.games_played = 1
        self.gametime = True

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
                    f"Elige quien gana el punto, digita 1 para {player1} y 2 es para {player2}: "))
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
        # Determina el jugador que gana el punto y el oponente.
        if shot == 1:
            winner = self.players[player1] # winner es por quien votaron que ganara el punto
            opponent = self.players[player2] # opponent es a quien no votaron
        else:
            winner = self.players[player2]
            opponent = self.players[player1]

        # Diccionario para actualizar el puntaje de acuerdo al puntaje actual
        points_to_games = {0: 15, 15: 30, 30: 40}

        # Asigna el nuevo puntaje a quien ganó en un caso no especial (donde no hay empates).
        current_points = winner['points']

        # Casos donde se encuentra por ganar el juego estando en los 40 puntos y adv.
        if current_points == 40 and opponent['points'] != 40 and opponent['points'] != 'adv': # 1er caso donde no hay empates y gana por 2 tiros.
            winner['points'] = 'game'
        elif current_points == 40 and opponent['points'] == 40: # 2ndo caso, hay empate y se asigna adv.
            # Otorga la ventaja porque aqui no la tiene.
            winner['points'] = 'adv'
        elif current_points == 'adv' and opponent['points'] == 40: #3er caso, hay adv y gana por volver a tirar.
            winner['points'] = 'game'
        elif current_points == 40 and opponent['points'] == 'adv': #4to caso, se baja de adv al oponente a 40.
            opponent['points'] = 40
        # Asignacion de los puntajes menores a 40
        elif current_points in points_to_games:
            winner['points'] = points_to_games[current_points]

        # Mostramos en pantalla quien se lleva el punto
        if shot == 1:
            print(f"Punto para {player1}.")
        else:
            print(f"Punto para {player2}.")
        self.display_score(self.players)

        # Si ya algun jugador marca game se manda a llamar a la funcion que reinicia los puntos y agrega puntos a games.
        if self.players[player1]['points'] == 'game' or self.players[player2]['points'] == 'game':
            self.check_game_winner()

        # Si el valor en games es mayor o igual a 6 empezamos a hacer las evaluaciones de quien gana el set.
        if self.players[player1]['games'] >= 6 or self.players[player2]['games'] >= 6:
            self.check_set_winner()

        # Funcion para ganar el partido por mayoria de sets y terminar con el bucle while del juego.
        if self.players[player1]['sets'] == 2 or self.players[player2]['sets'] == 2:
            self.check_match_winner()

    def check_game_winner(self):
        """
        Gana un juego:
        Determina si un jugador ha ganado un juego dentro del set actual.
        Actualiza el conteo de juegos del ganador y resetea los puntos de ambos jugadores.
        """
        # Agregamos el conteo a games en base al jugador que haya ganado los puntos
        if self.players[player1]['points'] == 'game':
            self.players[player1]['games'] += 1
            # Decimos quien gano ese juego
            print(f'El juego #{self.games_played} lo ha ganado {player1}, ahora se resetean los puntos.')
        else:
            self.players[player2]['games'] += 1
            print(f'El juego #{self.games_played} lo ha ganado {player2}, ahora se resetean los puntos.')

        # Reiniciamos el conteo de puntos
        self.players[player1]['points'] = 0
        self.players[player2]['points'] = 0

        # Funcion para que cambie quien saca en cada tiro, esto es cambiar de servidor en cada juego.
        self.switch_server()

        # Funcion para verificar si es necesario cambiar de lado de la cancha basado en las reglas que se proponen.
        self.update_court_side()

        # Sumamos un juego jugado.
        self.games_played += 1

        # Mostramos el score actual
        self.display_score(self.players)

    def check_set_winner(self):
        """
        Gana un Set:
        Implementa la lógica para determinar si un jugador ha ganado un set (alcanzando 6 juegos con una diferencia de
        al menos 2 juegos). También debe manejar casos especiales como 7-5 o 8-6.
        :return:
        """
        # Agregamos el conteo a sets en base al jugador que haya ganado al menos 6 juegos y la diferencia de juegos con
        # el otro jugador sea >= 2

        games_player1 = self.players[player1]['games']
        games_player2 = self.players[player2]['games']

        if games_player1 > games_player2: # El set iria para player1 al tener mas juegos
            if abs(games_player1 - games_player2) >= 2:
                self.players[player1]['sets'] += 1
                print(f'El set lo ha ganado {player1}')
                # Reiniciamos el conteo de games
                self.players[player1]['games'] = 0
                self.players[player2]['games'] = 0
                # Mostramos el score actual
                self.display_score(self.players)
        else: # El set iria para player2 al tener mas juegos
            if abs(games_player1 - games_player2) >= 2:
                self.players[player2]['sets'] += 1
                print(f'El set lo ha ganado {player2}')
                # Reiniciamos el conteo de games
                self.players[player1]['games'] = 0
                self.players[player2]['games'] = 0
                # Mostramos el score actual
                self.display_score(self.players)

    def check_match_winner(self):
        """
        Gana ya totalmente el partido:
        Verificar si un jugador ha ganado el partido.
        Debe revisar si alguno de los jugadores ha alcanzado los 2 sets ganados necesarios en un partido al mejor de 3 sets.
        Actualiza self.match_winner con el nombre del ganador del partido cuando se determina un ganador.
        """
        if self.players[player1]['sets'] == self.sets_to_win:
            print(f"********** FELICIDADES {player1} HAZ GANADO EL PARTIDO **********")
            self.display_score(self.players)
            self.gametime = False
        elif self.players[player2]['sets'] == self.sets_to_win:
            print(f"********** FELICIDADES {player2} HAZ GANADO EL PARTIDO **********")
            self.display_score(self.players)
            self.gametime = False

    def switch_server(self):
        """
        Cambio de Saque
        Después de que se completa un juego, esta función cambia el servidor al otro jugador. Asegúrate de que el cambio
        se realice correctamente después de cada juego.
        :return:
        """
        if self.current_server == player1:
            self.current_server = player2
        else:
            self.current_server = player1
        print(f"El servidor ahora es {self.current_server}.")

    def update_court_side(self):
        """
        Cambio de Cancha:
        Esta función debe verificar si es necesario cambiar de lado basándose en el número total de juegos jugados.
        Debe ser llamada después de cada juego para determinar si se requiere un cambio de cancha.
        :return:
        """
        # Calcula el total de juegos jugados en el set actual.
        total_games_current_set = self.players[player1]['games'] + self.players[player2]['games']

        # Verifica si el total de juegos en el set actual es impar para cambiar de lado.
        if total_games_current_set % 2 == 1:
            print("Los jugadores cambian de lado de la cancha.")
        else:
            # Adicionalmente, puedes verificar aquí si se necesita cambiar de lado al inicio de un nuevo set.
            if total_games_current_set == 0 and self.games_played > 1:  # Nuevo set, después del primer set.
                print("Nuevo set: Los jugadores cambian de lado de la cancha.")

    def display_score(self, players: Dict[str, Dict[str, Any]]) -> None:
        """
        Utilizada para mostrar el marcador actual, incluidos los puntos, juegos y sets para cada jugador.
        Debe reflejar la lógica correcta del marcador y el estado actual del partido.
        :return: No regresa nada, solo imprime la cadena.
        """

        if players[player1]['sets'] == 2 or players[player2]['sets'] == 2: # Marcador si acabó el partido
            print('\n**********MARCADOR FINAL**********')
        else:
            print('\n**********MARCADOR ACTUAL**********') # Marcador si no ha acabado el partido

        for player, stats in players.items():
            print(f"{player} [puntos:{stats['points']} juegos:{stats['games']} sets:{stats['sets']}]")
        print()  # Salto de linea

    def main(self):
        """
        Método principal para ejecutar el bucle del juego, obtener entradas del usuario, llamar a las funciones
        correspondientes para marcar puntos y actualizar el estado del juego, y manejar errores de entrada con
        estructuras try-except.
        :return:
        """
        print(f"\n*** Se esta jugando un partido de tennis en este momento, es el juego #{self.games_played} ***")
        # Imprimimos el status del juego.
        self.display_score(self.players)
        # Ejecutamos el partido hasta que haya un ganador
        while self.gametime:
            tiro = self.shot_election(player1, player2)
            self.score_point(tiro)


if __name__ == "__main__":
    print("Bienvenido al juego de tennis! \nVan a jugar 2 jugadores, ingresa sus nombres.\n")
    player1 = input("Nombre del jugador 1: ")
    player2 = input("Nombre del jugador 2: ")
    match = TennisMatch()
    match.main()
