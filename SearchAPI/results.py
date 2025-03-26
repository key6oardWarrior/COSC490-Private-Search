from quick_answers import QuickAnswer
from definitions import Definitions

class Results(QuickAnswer, Definitions):
	def __init__(self, response: dict) -> None:
		if response["AbstractText"] != "":
			QuickAnswer.__init__(self, response["AbstractText"], response["AbstractSource"], response["AbstractURL"])

		if response["Definition"] != "":
			Definitions.__init__(self, response["Definition"], response["DefinitionSource"], response["DefinitionURL"])