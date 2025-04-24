from os import system, getcwd
from os.path import exists, join

from helper import SETTINGS_FILE

class AnonSystem:
	__is_secure = False
	__tor_location: str = None

	def __init__(self) -> None:
		self.__is_secure = True
		if exists(SETTINGS_FILE):
			file = open(join(getcwd(), SETTINGS_FILE), "r")
			self.__tor_location = file.read()
			file.close()
		system("sudo service tor start && sudo anonsurf start")

	@staticmethod
	def wipe_memory() -> None:
		system("sudo pandora bomb")

	def end_anonsurf(self) -> None:
		self.__is_secure = False
		system("sudo anonsuf stop && sudo service tor stop")

	def tor(self, link: str) -> None:
		if self.__tor_location:
			system(f"cd {self.__tor_location} && ./start-tor-browser.desktop --detach {link}")
		else:
			raise FileNotFoundError("Tor browser location not set")

	def proxychains(self, link: str) -> None:
		if self.__is_secure:
			system(f"proxychains firefox {link}")
		else:
			raise Exception("Cannot open link system not secure")
