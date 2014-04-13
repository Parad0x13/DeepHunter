class BasePlayer(object):
	def setup(self, color, state):
		pass
	def next_move(self, state):
		raise NotImplementedError()