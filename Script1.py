class TennisMatch:
    def __init__(self, player1, player2):
        self.players = {player1: {'sets': 0, 'games': 0, 'points': 0},
                        player2: {'sets': 0, 'games': 0, 'points': 0}}
        self.current_server = player1  # Alternará después de cada juego.
        self.match_winner = None
        self.game_state = "0-0"  # Para control de puntos dentro de un juego.
        self.sets_to_win = 2  # Mejor de 3 sets.

    def score_point(self, player):
        # Implementar lógica para marcar puntos, considerando ventaja y juego.
        pass

    def check_game_winner(self):
        # Verificar si un jugador ha ganado el juego.
        pass

    def check_set_winner(self):
        # Verificar si un jugador ha ganado el set.
        pass

    def switch_server(self):
        # Cambiar el jugador que saca.
        pass

    def check_match_winner(self):
        # Verificar si un jugador ha ganado el partido.
        pass

    def update_court_side(self):
        # Cambiar de lado en la cancha si es necesario.
        pass

    def display_score(self):
        # Mostrar el marcador actual.
        pass

    def play(self):
        # Método principal para iniciar el juego y procesar la entrada del usuario.
        while not self.match_winner:
            try:
                # Obtener entrada del usuario y actualizar el marcador.
                input_str = input("Ingrese el jugador que gana el punto: ")
                self.score_point(input_str)
                self.display_score()
            except Exception as e:
                print(f"Error: {e}. Intente nuevamente.")

if __name__ == "__main__":
    player1 = input("Nombre del jugador 1: ")
    player2 = input("Nombre del jugador 2: ")
    match = TennisMatch(player1, player2)
    match.play()
