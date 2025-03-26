from base import Base

class Definitions(Base):
	__definition: str = None

	def __init__(self, definition: str, source: str, url: str) -> None:
		self.__definition = definition if definition != "" else None
		super().__init__(source, url)

	@property
	def definition(self) -> str:
		return self.__definition