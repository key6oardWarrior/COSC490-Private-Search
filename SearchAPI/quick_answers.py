from base import Base

class QuickAnswer(Base):
	__answer: str = None

	def __init__(self, answer: str, source: str, url: str) -> None:
		self.__answer = answer if answer != "" else None
		super().__init__(self, source, url)

	@property
	def answer(self) -> str:
		return self.__answer