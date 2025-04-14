from os import system
from os.path import exists

from helper import SETTINGS_FILE

class AnonSystem:
	__is_secure = False
	__tor_location: str = None

	def __init__(self) -> None:
		system("sudo service tor start && sudo anonsurf start")
		self.__is_secure = True
		
		if exists(SETTINGS_FILE):
			file = open(SETTINGS_FILE, "r")
			self.__tor_location = file.read()
			file.close()

	@staticmethod
	def wipe_memory() -> None:
		system("sudo pandora bomb")

	def end_anonsurf(self) -> None:
		self.__is_secure = False
		system("sudo anonsuf stop && sudo service tor stop")

	def tor(self, link: str) -> None:
		if self.__tor_location:
			system(f"./{self.__tor_location}/Browser/start-tor-browser --detach {link}")
		else:
			raise FileNotFoundError("Tor browser location not set")

	def proxychains(self, link: str) -> None:
		if self.__is_secure:
			system(f"proxychains firefox {link}")

		raise Exception("Cannot open link system not secure")