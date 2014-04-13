import chess

class InvalidMove(Exception):
	def __init__(self, *args, **kwargs):
		self.move = kwargs.pop('move')
		super(InvalidMove, self).__init__(*args, **kwargs)

class Game(object):
	def __init__(self, a, b):
		self.players = (a, b)

	def init(self):
		self.state = chess.Position()

		for color, player in zip(('W', 'B'), self.players):
			player.setup(color, self.state.fen)

	def run(self):
		self.init()

		while True:
			for player in self.players:
				move_text = player.next_move(self.state)
				try:
					move = chess.Move.from_uci(move_text)
				except ValueError:
					raise InvalidMove(move=move_text)

				if move not in self.state.get_legal_moves():
					raise InvalidMove(move=move_text)

				self.state.make_move(move)
				if self.state.is_game_over():
					return player