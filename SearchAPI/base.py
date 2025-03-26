class Base:
	__source: str = None
	__url: str = None

	def __init__(self, source: str, url: str) -> None:
		self.__source = source
		self.__url = url

	@property
	def source(self) -> str:
		return self.__source

	@property
	def url(self) -> str:
		return self.__url