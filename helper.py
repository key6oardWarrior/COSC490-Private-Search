from sys import exit

from PyGUI import Window, WIN_CLOSED

WIN_NAME = "Private Search"
SETTINGS_FILE = "settings.conf"
WIDTH, HEIGHT = Window.get_screen_size()

def exit_app(event: str, window: Window, kill_app: bool=True) -> bool:
	if((event == "Exit") or (event == WIN_CLOSED)):
		window.close()

		if kill_app:
			exit(0)

		return True
	return False
