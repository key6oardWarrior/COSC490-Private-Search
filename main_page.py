from os import getcwd
from os.path import join

from PyGUI import Window, Button, Text, Input, DropDown, FileBrowse

from helper import exit_app, WIN_NAME, SETTINGS_FILE
from query_page import query_page

def main_page() -> None:
	layout = [
		[Text("Query:"), Input(key="query")],
		[Button("Search Web", key="web"), Button("Search News", key="news")],
		[Text("Safe Search:"), DropDown(("On", "Moderate", "Off"), "Off", key="safe_search"), Button(button_color="white", image_source=join(getcwd(), join("Images", "settings_icon.png")), key="settings")]
	]

	search_page = Window(WIN_NAME, layout)

	while True:
		event, values = search_page.read()
		exit_app(event, search_page)

		if event == "settings":
			s_event, s_values = Window("Settings", [[Text("Tor browser file location"), FileBrowse("Browse", key="tor_file", file_types=(("Shell Files", "*.sh"),))]]).read()
			s_values: dict[str, str]

			if((s_values["tor_file"]) and (s_values["tor_file"].strip() != "")):
				file = open(SETTINGS_FILE, "w")
				file.write(s_values["tor_file"])
				file.close()

		if len(values["query"]) == 0:
			continue

		# trim trailing spaces from the query
		while values["query"][-1] == " ":
			values["query"] = values["query"][:-1]
			if len(values["query"]) == 0:
				break

		if len(values["query"]) == 0:
			continue

		if((event == "web") or (event == "news")):
			query_page(values["query"], event, values["safe_search"])

if __name__ == "__main__":
	main_page()