from multiprocessing import Process

from main_page import main_page
from AnonSystem import AnonSystem

process = Process(target=main_page)
process.start()

while process.is_alive():
	pass

AnonSystem.wipe_memory()