import chess
import pytest

from chaz import BasePlayer, Game
from chaz.run import InvalidMove

class TestPlayer:
	class DummyPlayer(BasePlayer):
		def setup(self, color, state):
			self.color = color
			assert self.color in ('W', 'B')

			self.state = chess.Position(state)

			# Tests scholar's mate
			self.moves = {
				'W': [
					'e2e4',
					'd1f3',
					'f1c4',
					'f3f7',
				],
				'B': [
					'e7e5',
					'b8c6',
					'a8b8',
				]
			}[self.color]

			self.move_iter = iter(self.moves)

		def next_move(self, state):
			return next(self.move_iter)

	class InvalidMovePlayer(BasePlayer):
		def __init__(self, move):
			self.move = move

		def next_move(self, state):
			return self.move

	def test_scholars_mate(self):
		a = self.DummyPlayer()
		b = self.DummyPlayer()

		game = Game(a, b)

		assert game.run() == a

	def test_invalid_move(self):
		a = self.InvalidMovePlayer('f1f8')
		b = self.InvalidMovePlayer('f1f8')

		game = Game(a, b)

		with pytest.raises(InvalidMove):
			game.run()

	def test_bad_format_move(self):
		a = self.InvalidMovePlayer('this obviously isn\'t a move')
		b = self.InvalidMovePlayer('same with this')

		game = Game(a, b)

		with pytest.raises(InvalidMove):
			game.run()