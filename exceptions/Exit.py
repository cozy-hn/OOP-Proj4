class Exit(Exception):
	def __init__(self, looser):
		self.looser = looser