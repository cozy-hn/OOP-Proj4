class Die(Exception):
	looser = None
	def __init__(self, looser, args):
		super().__init__(args)
		self.looser = looser